from django.urls import path

from main.views import (
    UserCreateView,
    SignInView,
    UserReadView,
    UserVerifyEmailView,
    ExpiredEmailVerificationView,
)

urlpatterns = [
    path("expired_email_verification/", ExpiredEmailVerificationView.as_view()),
    path("sign_in/", SignInView.as_view()),
    path("user/", UserReadView.as_view()),
    path("users/create/", UserCreateView.as_view()),
    path("user/verify_email/", UserVerifyEmailView.as_view()),
]
