from django.views.generic import TemplateView


class ExpiredEmailVerificationView(TemplateView):
    template_name = "main/email/expired_email_verification.html"
