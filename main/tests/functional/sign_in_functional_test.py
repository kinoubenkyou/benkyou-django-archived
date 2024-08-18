from django.urls import reverse

from main.tests.functional import FunctionalTestCase, LoginRequiredMixin


class SignInFunctionalTest(LoginRequiredMixin, FunctionalTestCase):
    def test_success(self):
        self.web_driver.get(f"{self.live_server_url}{reverse("sign-in")}")
        self.login()

        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
