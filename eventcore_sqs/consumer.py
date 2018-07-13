import boto3
import json

from eventcore import Consumer


class SQSConsumer(Consumer):
    """
    Produce to a SQS queue.
    """

    def __init__(self):
        pass

    def consume(self):
        pass
