from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class UserReadView(LoginRequiredMixin, TemplateView):
    template_name = "main/user_read.html"
