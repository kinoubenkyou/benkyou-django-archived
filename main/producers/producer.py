from json import dumps

from confluent_kafka import Producer as ConfluentProducer
from django.conf import settings


class Producer:
    def __init__(self):
        self.confluent_producer = ConfluentProducer(
            {
                "bootstrap.servers": settings.KAFKA_BOOTSTRAP_SERVER,
            }
        )

    def produce(self, key, value):
        self.confluent_producer.produce(self.TOPIC, key=key, value=dumps(value))
        self.confluent_producer.flush()
