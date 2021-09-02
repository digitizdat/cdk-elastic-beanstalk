# AWS CDK / Python / Elastic Beanstalk hosting Java app

Start by sourcing the virtual env
```
source .venv/bin/activate
```

Once the virtualenv is activated, you can update the required dependencies.

```
pip install -r requirements.txt
```

Export the CDK_DEFAULT_ACCOUNT and CDK_DEFAULT_REGION variables to your shell
environment, unless you'd prefer to hard code them into the Python code.

```
export CDK_DEFAULT_ACCOUNT=ACCOUNT
export CDK_DEFAULT_REGION=REGION
```

At this point you can now synthesize the CloudFormation template for this code.

```
cdk synth --context jarpath=PATH_TO_JAR \
    --context tls_cert_arn=ACM_CERTIFICATE_ARN \
    --context appname=APPNAME
```

If this is the first time you've deployed CDK assets to this account, the toolkit stack must be deployed to the environment.

```
cdk bootstrap --context jarpath=PATH_TO_JAR \
    --context tls_cert_arn=ACM_CERTIFICATE_ARN \
    --context appname=APPNAME
```

Finally, you are ready to deploy.

```
cdk deploy --context jarpath=PATH_TO_JAR \
    --context tls_cert_arn=ACM_CERTIFICATE_ARN \
    --context appname=APPNAME
```
## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
