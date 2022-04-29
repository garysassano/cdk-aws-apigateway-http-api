from projen.awscdk import AwsCdkPythonApp
from projen.python import PoetryPyprojectOptions

project = AwsCdkPythonApp(
    author_email="10464497+garysassano@users.noreply.github.com",
    author_name="Gary Sassano",
    cdk_version="2.130.0",
    module_name="cdk-aws-apigateway-http-api",
    name="cdk-aws-apigateway-http-api",
    poetry=True,
    version="0.1.0",
)

project.add_dependency

# Set Poetry local configuration for this project
poetry_toml = project.try_find_file("poetry.toml")
poetry_toml.add_override("virtualenvs.create", "true")
poetry_toml.add_override("virtualenvs.in-project", "true")

project.synth()
