from django.contrib.auth.forms import PasswordResetForm

from main.models import User


class UserStartResetPasswordForm(PasswordResetForm):
    def get_users(self, email):
        return (user for user in User.objects.filter(email__iexact=email))
