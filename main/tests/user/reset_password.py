from secrets import token_hex

from django.core import mail
from selenium.webdriver.common.by import By

from main.tests.mixin import SignInMixin
from main.tests.test_case import TestCase


class UserResetPasswordTestCase(SignInMixin, TestCase):
    def test(self):
        password = token_hex()

        self.web_driver.get(f"{self.live_server_url}/user/start_reset_password/")
        self.web_driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(
            "email1@email.com",
        )
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.web_driver.get(mail.outbox[0].body)
        self.web_driver.find_element(
            By.XPATH,
            '//input[@name="new_password1"]',
        ).send_keys(password)
        self.web_driver.find_element(
            By.XPATH,
            '//input[@name="new_password2"]',
        ).send_keys(password)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.web_driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(
            "email1@email.com",
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(
            password,
        )
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
