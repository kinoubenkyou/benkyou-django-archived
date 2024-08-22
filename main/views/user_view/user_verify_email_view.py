from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import BadRequest
from django.shortcuts import render
from django.views.generic import FormView

from main.forms import UserVerifyEmailForm


class UserVerifyEmailView(LoginRequiredMixin, FormView):
    form_class = UserVerifyEmailForm
    success_url = "/user/"
    template_name = "main/user_verify_email.html"

    def form_valid(self, form):
        sentinel = object()
        code = cache.get(self.request.user.id, sentinel)
        if code is sentinel:
            return render(self.request, "main/expired_email_verification.html")
        elif code != form.cleaned_data["code"]:
            raise BadRequest
        user = self.request.user
        user.email_verified = True
        user.save()
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial["code"] = self.request.GET.get("code")
        return initial
