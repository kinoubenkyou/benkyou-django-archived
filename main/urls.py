from django.urls import path

from main.views import UserCreateView

urlpatterns = [
    path("users/create/", UserCreateView.as_view(), name="user-create"),
]
