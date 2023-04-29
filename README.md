# cdk-aws-apigateway-http-api

CDK app that deploys an Amazon API Gateway with HTTP API along with an AWS Lambda to handle GET requests on base path.

## Prerequisites

For this project you need an AWS account with the [CDK bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) process completed. You also need Docker to be installed on your system since the Lambda layer gets built inside a container.

## Installation

Install CDK:

```sh
npm install -g aws-cdk
```

Install Poetry + dotenv plugin:

```sh
curl -sSL https://install.python-poetry.org | python3 -
poetry self add poetry-plugin-dotenv
```

Configure Poetry to create the virtualenv inside the project's root directory:

```sh
poetry config virtualenvs.in-project true
```

Create the virtualenv and install all the dependencies inside it:

```sh
poetry install
```

## Configuration

In order to deploy to AWS, you need to [set AWS CLI environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-set).

To do that, rename `.env.example` to `.env` and add your variables like in the following example:

```dotenv
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_DEFAULT_REGION=eu-west-1
```

## Deployment

Synthesize the CloudFormation stack and deploy it:

```sh
cdk deploy
```

## Cleanup

Destroy the CloudFormation stack:

```sh
cdk destroy
```
