from hashlib import sha256
from secrets import token_hex, token_urlsafe
from urllib.parse import urlunparse

from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail
from django.utils.http import urlencode

from main.models import User


@shared_task
def start_reset_password(netloc, scheme, user_email):
    token = token_urlsafe()
    salt = token_hex()
    cache.set(
        f"reset_password.{User.objects.get(email=user_email).id}",
        f"{salt}{sha256(token.encode()).hexdigest()}",
    )
    send_mail(
        "Verify Email",
        urlunparse(
            [
                scheme,
                netloc,
                "/user/reset_password",
                None,
                urlencode({"token": token}),
                None,
            ],
        ),
        None,
        [user_email],
    )
