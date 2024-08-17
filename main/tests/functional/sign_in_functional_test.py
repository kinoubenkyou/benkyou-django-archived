from django.urls import reverse
from selenium.webdriver.common.by import By

from main.tests.functional import FunctionalTestCase


class SignInFunctionalTest(FunctionalTestCase):
    fixtures = ["sign_in"]

    def test_success(self):
        self.web_driver.get(f"{self.live_server_url}{reverse("sign-in")}")
        self.web_driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(
            "email@email.com"
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(
            "dr0wss@p"
        )
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/you/")
