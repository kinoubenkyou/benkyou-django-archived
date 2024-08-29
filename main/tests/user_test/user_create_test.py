from unittest.mock import patch

from django.core import mail
from selenium.webdriver.common.by import By

from main.jobs import StartVerifyEmailJob
from main.tests.test_case import TestCase


class UserCreateTest(TestCase):
    @patch("main.producers.producer.Producer.produce")
    def test_success(self, produce_mock):
        email = "email@email.com"
        password = "dr0wss@p"

        self.web_driver.get(f"{self.live_server_url}/users/create/")
        self.web_driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(
            email
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
        StartVerifyEmailJob.consume(produce_mock.call_args.args[1])

        self.assertEqual(len(self.find_elements("Created user.")), 1)
        self.assertIn(
            "http://localhost:8000/user/verify_email/?token=", mail.outbox[0].body
        )
        self.assertEqual(mail.outbox[0].subject, "Verify Email")
        self.assertIn(email, mail.outbox[0].to)
