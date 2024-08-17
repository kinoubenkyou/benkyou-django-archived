from django.urls import reverse
from selenium.webdriver.common.by import By

from main.tests.functional import FunctionalTestCase


class UserCreateFunctionalTest(FunctionalTestCase):
    def test_success(self):
        password = "dr0wss@p"

        self.web_driver.get(f"{self.live_server_url}{reverse("user-create")}")
        self.web_driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(
            "email@email.com"
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(
            "name"
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password1"]').send_keys(
            password
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password2"]').send_keys(
            password
        )
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/")
