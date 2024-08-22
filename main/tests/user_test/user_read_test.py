from main.tests.login_required_mixin import LoginRequiredMixin
from main.tests.test_case import TestCase


class UserReadTest(LoginRequiredMixin, TestCase):
    def test_success(self):
        self.web_driver.get(f"{self.live_server_url}/user/")
        self.login()

        self.assertEqual(len(self.find_elements("Email: email@email.com")), 1)
        self.assertEqual(len(self.find_elements("Email verified: True")), 1)
        self.assertEqual(len(self.find_elements("Name: name")), 1)
