from django.urls import path

from main.views import UserCreateView, SignInView, UserReadView

urlpatterns = [
    path("sign_in/", SignInView.as_view(), name="sign-in"),
    path("user/", UserReadView.as_view(), name="user-read"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
]
