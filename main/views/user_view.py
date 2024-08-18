from django.views.generic import CreateView

from main.forms import UserCreateForm
from main.models import User


class UserCreateView(CreateView):
    form_class = UserCreateForm
    model = User
    success_url = "/"
