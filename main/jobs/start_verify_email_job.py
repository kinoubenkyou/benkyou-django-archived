from secrets import token_urlsafe

from django.core.cache import cache
from django.core.mail import send_mail
from django.utils.http import urlencode

from main.models import User


class StartVerifyEmailJob:
    @classmethod
    def consume(cls, value):
        cls.run(value["user_id"])

    @staticmethod
    def run(user_id):
        token = token_urlsafe()
        cache.set(f"verify_email.{user_id}", token)
        send_mail(
            from_email=None,
            message=f"http://localhost:8000/user/verify_email/?{urlencode({"token": token})}",
            recipient_list=[User.objects.get(id=user_id).email],
            subject="Verify Email",
        )
