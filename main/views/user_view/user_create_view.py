from django.views.generic import CreateView

from main.forms import UserCreateForm
from main.models import User
from main.producers import UserCreateProducer


class UserCreateView(CreateView):
    form_class = UserCreateForm
    model = User
    success_url = "/users/create_done/"
    template_name = "main/user_create.html"

    def form_valid(self, form):
        result = super().form_valid(form)
        UserCreateProducer().send(self.object.pk)
        return result
