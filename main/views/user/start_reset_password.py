from django.contrib.auth.views import PasswordResetView

from main.forms.user import UserStartResetPasswordForm


class UserStartResetPasswordView(PasswordResetView):
    email_template_name = "main/user/reset_password_email.html"
    form_class = UserStartResetPasswordForm
    success_url = "/user/sign_in/"
    template_name = "main/user/start_reset_password.html"
