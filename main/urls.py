from django.urls import path

from main.views import UserCreateView, SignInView

urlpatterns = [
    path("sign_in/", SignInView.as_view(), name="sign-in"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
]
