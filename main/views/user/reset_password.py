from django.contrib.auth.views import PasswordResetConfirmView


class UserResetPasswordView(PasswordResetConfirmView):
    success_url = "/user/sign_in/"
    template_name = "main/user/reset_password.html"
