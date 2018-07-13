import boto3

from eventcore import Producer


class SQSProducer(Producer):
    """
    Produce to a Kafka queue.
    :param servers: list of brokers to consume from.
    """

    def __init__(self):
        pass

    def produce(self, topic, event, subject, data):
        pass
