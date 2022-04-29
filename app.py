import os
from aws_cdk import App, Environment
from cdk_aws_apigateway_http_api.stacks.my_stack import MyStack

# for development, use account/region from cdk cli
dev_env = Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
)

app = App()

MyStack(app, "cdk-aws-apigateway-http-api-dev", env=dev_env)

app.synth()
