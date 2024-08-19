from django.forms import Form, CharField, HiddenInput


class UserVerifyEmailForm(Form):
    code = CharField(widget=HiddenInput)
