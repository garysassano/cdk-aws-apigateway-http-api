import os
import aws_cdk as cdk
from stacks.apigateway_http_api_stack import ApiGatewayHttpApiStack

app = cdk.App()

ApiGatewayHttpApiStack(
    app,
    "dev",
    stack_name="ApiGatewayHttpApiStack-dev",
    env=cdk.Environment(
        account=os.environ.get("CDK_DEFAULT_ACCOUNT"),
        region=os.environ.get("CDK_DEFAULT_REGION"),
    ),
)

app.synth()
