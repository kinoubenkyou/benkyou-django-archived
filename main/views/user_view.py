from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import BadRequest
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, FormView

from main.forms import UserCreateForm, UserVerifyEmailForm
from main.models import User


class UserCreateView(CreateView):
    form_class = UserCreateForm
    model = User
    success_url = "/"


class UserReadView(LoginRequiredMixin, TemplateView):
    template_name = "main/user_read.html"


class UserVerifyEmailView(LoginRequiredMixin, FormView):
    form_class = UserVerifyEmailForm
    success_url = "/user/"
    template_name = "main/user_verify_email.html"

    def form_valid(self, form):
        sentinel = object()
        code = cache.get(self.request.user.id, sentinel)
        if code != form.cleaned_data["code"]:
            raise BadRequest
        elif code is sentinel:
            return redirect("/expired_email_verification/")
        user = self.request.user
        user.email_verified = True
        user.save()
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial["code"] = self.request.GET.get("code")
        return initial
