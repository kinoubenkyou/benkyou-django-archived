from selenium.webdriver.common.by import By

from main.tests.login_required_mixin import LoginRequiredMixin
from main.tests.test_case import TestCase


class UserReadTest(LoginRequiredMixin, TestCase):
    def test_success(self):
        self.web_driver.get(f"{self.live_server_url}/user/")
        self.login()

        self.web_driver.find_element(
            By.XPATH, '//*[contains(text(), "email@email.com")]'
        )
        self.web_driver.find_element(By.XPATH, '//*[contains(text(), "name")]')
