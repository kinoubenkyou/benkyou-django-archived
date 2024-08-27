from signal import signal, SIGTERM

from django.core.management import BaseCommand

from main.consumers import Consumer
from main.jobs import StartVerifyEmailJob
from main.producers import UserCreateProducer


class Command(BaseCommand):
    JOB_MAP = {UserCreateProducer.TOPIC: StartVerifyEmailJob}

    help = "Run a Kafka consumer"

    def handle(self, *args, **options):
        consumer = Consumer()
        signal(SIGTERM, lambda _signum, _frame: consumer.stop())
        consumer.consume()
