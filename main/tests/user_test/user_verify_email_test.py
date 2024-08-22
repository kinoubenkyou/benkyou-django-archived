from django.core.cache import cache
from selenium.webdriver.common.by import By

from main.tests.login_required_mixin import LoginRequiredMixin
from main.tests.test_case import TestCase


class UserVerifyEmailTest(LoginRequiredMixin, TestCase):
    fixtures = ["user_verify_email"]

    def test_success(self):
        code = "code"
        cache.set(1, code)

        self.login()
        self.web_driver.get(f"{self.live_server_url}/user/verify_email/?code={code}")
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(len(self.find_elements("Email verified: True")), 1)

    def test_expired_email_verification(self):
        self.login()
        self.web_driver.get(f"{self.live_server_url}/user/verify_email/?code=code")
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(len(self.find_elements("Email verification expired.")), 1)

    def test_not_matched_code(self):
        cache.set(1, "-code")

        self.login()
        self.web_driver.get(f"{self.live_server_url}/user/verify_email/?code=code")
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(len(self.find_elements("Bad Request (400)")), 1)
