# AWS CDK / Python / Elastic Beanstalk hosting Java app

Start by sourcing the virtual env
```
source .venv/bin/activate
```

Once the virtualenv is activated, you can update the required dependencies.

```
pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
cdk synth --context jarpath=PATH_TO_JAR \
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
