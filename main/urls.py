from django.urls import path

from main.views import UserCreateView, SignInView, UserReadView

urlpatterns = [
    path("sign_in/", SignInView.as_view()),
    path("user/", UserReadView.as_view()),
    path("users/create/", UserCreateView.as_view()),
]
