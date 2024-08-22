from main.tests.login_required_mixin import LoginRequiredMixin
from main.tests.test_case import TestCase


class SignInTest(LoginRequiredMixin, TestCase):
    def test_success(self):
        self.login()

        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
