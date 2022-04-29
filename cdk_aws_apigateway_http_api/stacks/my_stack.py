from pathlib import Path
from aws_cdk import (
    CfnOutput,
    Stack,
)
from aws_cdk.aws_lambda import Code, Function, Runtime
from aws_cdk.aws_apigatewayv2 import (
    HttpApi,
    HttpMethod,
)
from aws_cdk.aws_apigatewayv2_integrations import HttpLambdaIntegration
from constructs import Construct


class MyStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        http_lambda = Function(
            self,
            "HttpLambda",
            function_name="http-lambda",
            code=Code.from_asset(
                str(Path(__file__).parent / ".." / "functions" / "http")
            ),
            handler="index.handler",
            runtime=Runtime.PYTHON_3_12,
        )

        http_api = HttpApi(
            self,
            "HttpApi",
            api_name="http-api",
        )

        http_api.add_routes(
            path="/",
            methods=[HttpMethod.GET],
            integration=HttpLambdaIntegration(
                "HttpApiLambdaProxy",
                handler=http_lambda,
            ),
        )

        CfnOutput(
            self,
            "HTTP API Endpoint",
            value=http_api.api_endpoint,
        )
