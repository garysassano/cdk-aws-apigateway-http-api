from aws_cdk import (
    CfnOutput,
    Duration,
    Stack,
    aws_apigatewayv2_alpha as apigwv2,
    aws_apigatewayv2_integrations_alpha as apigwv2_integrations,
    aws_lambda as _lambda,
)
from constructs import Construct


class ApiGatewayHttpApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create lambda function
        test_lambda = _lambda.Function(
            self,
            "LambdaFunction_test-lambda",
            function_name="test-lambda",
            code=_lambda.Code.from_asset("lambda/functions/test-lambda"),
            handler="lambda_function.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_10,
        )

        # Create HTTP API with CORS
        test_http_api = apigwv2.HttpApi(
            self,
            "HttpApiGateway_test-http-api",
            api_name="test-http-api",
            cors_preflight=apigwv2.CorsPreflightOptions(
                allow_methods=[apigwv2.CorsHttpMethod.GET],
                allow_origins=["*"],
                max_age=Duration.days(10),
            ),
        )

        # Add route to HTTP API
        test_http_api.add_routes(
            path="/",
            methods=[apigwv2.HttpMethod.GET],
            integration=apigwv2_integrations.HttpLambdaIntegration(
                "HttpLambdaProxyIntegration",
                handler=test_lambda,
            ),
        )

        # Print HTTP API endpoint
        CfnOutput(
            self,
            "HTTP API Endpoint",
            value=test_http_api.api_endpoint,
        )
