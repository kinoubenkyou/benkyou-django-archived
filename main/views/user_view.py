from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView

from main.forms import UserCreateForm
from main.models import User


class UserCreateView(CreateView):
    form_class = UserCreateForm
    model = User
    success_url = "/"


class UserReadView(LoginRequiredMixin, TemplateView):
    template_name = "main/user_read.html"
