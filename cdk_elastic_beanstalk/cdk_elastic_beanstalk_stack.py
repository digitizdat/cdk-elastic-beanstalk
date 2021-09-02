from glob import glob
from os.path import abspath, exists

import cdk_elastic_beanstalk_config as config
from aws_cdk import aws_elasticbeanstalk as eb
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3_assets as assets
from aws_cdk import core as cdk


class CdkElasticBeanstalkStack(cdk.Stack):
    def __init__(
        self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Get the path to the JAR file from context
        jarpath = self.node.try_get_context("jarpath")
        if not jarpath or not exists(abspath(jarpath)):
            raise RuntimeError(
                "Set value for jarpath with 'cdk synth --context jarpath=PATH'"
            )

        # Construct an S3 asset from the highest-versioned JAR available in the
        # ../target dir.
        jarfile = assets.Asset(self, "app.jar", path=jarpath)

        # Get the ARN for the TLS certificate from context
        tls_cert_arn = self.node.try_get_context("tls_cert_arn")
        if not tls_cert_arn:
            raise RuntimeError(
                "Set value for tls_cert_arn with 'cdk synth --context tls_cert_arn=ARN'"
            )

        # Get the app name from context and construct the env name from that.
        appname = self.node.try_get_context("appname")
        if not appname:
            raise RuntimeError(
                "Set value for appname with 'cdk synth --context appname=NAME'"
            )
        envname = f"{appname}-env"

        app = eb.CfnApplication(self, "Application", application_name=appname)

        self.eb_service_role = iam.CfnServiceLinkedRole(
            self,
            "ServiceLinkedRole",
            aws_service_name="elasticbeanstalk.amazonaws.com",
        )
        instance_profile = eb.CfnEnvironment.OptionSettingProperty(
            namespace="aws:autoscaling:launchconfiguration",
            option_name="IamInstanceProfile",
            value=self.eb_service_role.get_att("arn").to_string(),
        )
        certificate = eb.CfnEnvironment.OptionSettingProperty(
            namespace="aws:elbv2:listener:443",
            option_name="SSLCertificateArns",
            value=tls_cert_arn,
        )

        settings = config.create_eb_config()
        settings += [instance_profile, certificate]

        # Create an app version from the S3 asset defined above
        # The S3 "putObject" will occur first before CF generates the template
        appversion = eb.CfnApplicationVersion(
            self,
            "AppVersion",
            application_name=appname,
            source_bundle=eb.CfnApplicationVersion.SourceBundleProperty(
                s3_bucket=jarfile.s3_bucket_name, s3_key=jarfile.s3_object_key
            ),
        )

        ebenv = eb.CfnEnvironment(
            self,
            "Environment",
            application_name=appname,
            environment_name=envname,
            solution_stack_name=config.config["SolutionStackName"],
            platform_arn=config.config["PlatformArn"],
            option_settings=settings,
            # This line is critical - reference the label created in this same stack
            version_label=appversion.ref,
        )

        # Also very important - make sure that `app` exists before creating an app version
        appversion.add_depends_on(app)
