from django.urls import path

from main.views import (
    UserCreateDoneView,
    UserCreateView,
    SignInView,
    UserReadView,
    UserVerifyEmailView,
)

urlpatterns = [
    path("sign_in/", SignInView.as_view()),
    path("user/", UserReadView.as_view()),
    path("users/create/", UserCreateView.as_view()),
    path("users/create_done/", UserCreateDoneView.as_view()),
    path("user/verify_email/", UserVerifyEmailView.as_view()),
]
