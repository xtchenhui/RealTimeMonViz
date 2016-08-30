#!/usr/local/python2.7

from pykafka import KafkaClient
from pykafka.common import OffsetType


class KafkaMsg:
    def __init__(self):
        self.client = KafkaClient(hosts = "127.0.0.1:9092")

    def getLatestData(self,tname):
        topic = self.client.topics[tname]
        consumer = topic.get_simple_consumer(auto_offset_reset=OffsetType.LATEST)
        message = consumer.consume()
        return message.value
