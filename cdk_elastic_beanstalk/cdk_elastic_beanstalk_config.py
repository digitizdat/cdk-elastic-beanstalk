import json

from aws_cdk import aws_elasticbeanstalk as eb

# This list can be auto-generated using the AWS CLI if you already built a
# prototype EB environment by hand.
#
# aws elasticbeanstalk describe-configuration-settings \
#        --application-name APPNAME --environment-name ENVNAME > settings.js
#
# You do need to do some massaging of the output:
# 1) Convert the JSON to Python using json.loads(open('settings.js').read())
# 2) replace Namespace -> namespace
# 3) replace OptionName -> option_name
# 4) replace ResourceName -> resource_name
# 5) replace Value -> value
# 6) Remove the top-level, "ConfigurationSettings"
# 7) Keep only the settings that you need to customize. Let Elastic Beanstalk fill in the rest.
#
config = {
    "SolutionStackName": "64bit Amazon Linux 2 v3.2.4 running Corretto 11",
    "PlatformArn": "arn:aws:elasticbeanstalk:us-east-2::platform/Corretto 11 running on 64bit Amazon Linux 2/3.2.4",
    "OptionSettings": [
        {
            "resource_name": "AWSEBAutoScalingGroup",
            "namespace": "aws:autoscaling:asg",
            "option_name": "Availability Zones",
            "value": "Any",
        },
        {
            "namespace": "aws:autoscaling:launchconfiguration",
            "option_name": "InstanceType",
            "value": "t3.small",
        },
        {
            "resource_name": "AWSEBAutoScalingGroup",
            "namespace": "aws:autoscaling:asg",
            "option_name": "Cooldown",
            "value": "120",
        },
        {
            "resource_name": "AWSEBAutoScalingGroup",
            "namespace": "aws:autoscaling:asg",
            "option_name": "EnableCapacityRebalancing",
            "value": "true",
        },
        {
            "resource_name": "AWSEBAutoScalingGroup",
            "namespace": "aws:autoscaling:asg",
            "option_name": "MaxSize",
            "value": "8",
        },
        {
            "resource_name": "AWSEBAutoScalingGroup",
            "namespace": "aws:autoscaling:asg",
            "option_name": "MinSize",
            "value": "4",
        },
        {
            "namespace": "aws:autoscaling:launchconfiguration",
            "option_name": "SSHSourceRestriction",
            "value": "tcp,22,22,10.1.2.3/32",
        },
        {
            "namespace": "aws:ec2:instances",
            "option_name": "EnableSpot",
            "value": "true",
        },
        {
            "namespace": "aws:elasticbeanstalk:application",
            "option_name": "Application Healthcheck URL",
            "value": "/health",
        },
        {
            "namespace": "aws:elasticbeanstalk:application:environment",
            "option_name": "SERVER_PORT",
            "value": "5000",
        },
        {
            "namespace": "aws:elasticbeanstalk:cloudwatch:logs",
            "option_name": "StreamLogs",
            "value": "true",
        },
        {
            "namespace": "aws:elasticbeanstalk:cloudwatch:logs:health",
            "option_name": "HealthStreamingEnabled",
            "value": "true",
        },
        {
            "namespace": "aws:elasticbeanstalk:cloudwatch:logs",
            "option_name": "RetentionInDays",
            "value": "7",
        },
        {
            "namespace": "aws:elasticbeanstalk:cloudwatch:logs:health",
            "option_name": "RetentionInDays",
            "value": "7",
        },
        {
            "namespace": "aws:elasticbeanstalk:command",
            "option_name": "DeploymentPolicy",
            "value": "TrafficSplitting",
        },
        {
            "resource_name": "AWSEBV2LoadBalancerTargetGroup",
            "namespace": "aws:elasticbeanstalk:environment:process:default",
            "option_name": "HealthCheckPath",
            "value": "/health",
        },
        {
            "namespace": "aws:elasticbeanstalk:healthreporting:system",
            "option_name": "SystemType",
            "value": "enhanced",
        },
        {
            "namespace": "aws:elasticbeanstalk:trafficsplitting",
            "option_name": "EvaluationTime",
            "value": "10",
        },
        {
            "namespace": "aws:elasticbeanstalk:trafficsplitting",
            "option_name": "NewVersionPercent",
            "value": "10",
        },
        {
            "namespace": "aws:elasticbeanstalk:xray",
            "option_name": "XRayEnabled",
            "value": "false",
        },
        {
            "resource_name": "AWSEBV2LoadBalancerListener443",
            "namespace": "aws:elbv2:listener:443",
            "option_name": "DefaultProcess",
            "value": "default",
        },
        {
            "resource_name": "AWSEBV2LoadBalancerListener443",
            "namespace": "aws:elbv2:listener:443",
            "option_name": "ListenerEnabled",
            "value": "true",
        },
        {
            "resource_name": "AWSEBV2LoadBalancerListener443",
            "namespace": "aws:elbv2:listener:443",
            "option_name": "Protocol",
            "value": "HTTPS",
        },
        {
            "resource_name": "AWSEBV2LoadBalancerListener443",
            "namespace": "aws:elbv2:listener:443",
            "option_name": "Rules",
        },
        {
            "resource_name": "AWSEBV2LoadBalancerListener443",
            "namespace": "aws:elbv2:listener:443",
            "option_name": "SSLPolicy",
            "value": "ELBSecurityPolicy-TLS-1-2-2017-01",
        },
        {
            "resource_name": ":default",
            "namespace": "aws:elbv2:listener:default",
            "option_name": "ListenerEnabled",
            "value": "false",
        },
    ],
}


def create_eb_config(c=config):
    options = []
    for setting in c["OptionSettings"]:
        options += [eb.CfnEnvironment.OptionSettingProperty(**setting)]

    return options
