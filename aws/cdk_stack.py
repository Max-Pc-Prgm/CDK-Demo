from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_lambda_event_sources as lambda_event_sources,
    aws_lambda as lambda_

)


class AwsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "AwsCdkQueue",
            visibility_timeout=Duration.seconds(300),
        )
        lambda_test =  lambda_.Function(
        self,
        "labmda_cdk",
        handler='lambda_handler.handler',
        runtime = lambda_.Runtime.PYTHON_3_11,
        code = lambda_.Code.from_asset('lambda')
        )

        #create event source
        event_source=lambda_event_sources.SqsEventSource(queue)

        #bind event source
        lambda_test.add_event_source(event_source)


      