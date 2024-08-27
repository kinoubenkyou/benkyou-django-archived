import logging
from json import loads

from confluent_kafka import Consumer as ConfluentConsumer
from confluent_kafka.admin import AdminClient
from confluent_kafka.cimpl import NewTopic, KafkaException
from django.conf import settings

from main.jobs import StartVerifyEmailJob
from main.producers import UserCreateProducer


logger = logging.getLogger("django.server")


class Consumer:
    JOB_MAP = {UserCreateProducer.TOPIC: StartVerifyEmailJob}

    def __init__(self):
        self.confluent_admin_client = AdminClient(
            {
                "bootstrap.servers": settings.KAFKA_BOOTSTRAP_SERVER,
            }
        )
        self.confluent_consumer = ConfluentConsumer(
            {
                "auto.offset.reset": "earliest",
                "bootstrap.servers": settings.KAFKA_BOOTSTRAP_SERVER,
                "enable.auto.commit": False,
                "group.id": "group",
            }
        )
        self.running = True

    def consume(self):
        topics = list(self.JOB_MAP.keys())
        self.confluent_admin_client.create_topics([NewTopic(topic) for topic in topics])
        try:
            self.confluent_consumer.subscribe(topics)
            logger.info("Start consuming...")
            while self.running:
                message = self.confluent_consumer.poll(5)
                if not message:
                    continue
                error = message.error()
                if error:
                    raise KafkaException(error)
                value = loads(message.value())
                self.JOB_MAP[message.topic()].consume(value)
                logger.info(
                    "%s %d %d %s %s"
                    % (
                        message.topic(),
                        message.partition(),
                        message.offset(),
                        message.key(),
                        value,
                    )
                )
                self.confluent_consumer.commit()
        finally:
            logger.info("Stop consuming...")
            self.confluent_consumer.close()

    def stop(self):
        self.running = False
