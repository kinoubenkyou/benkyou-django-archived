from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class UserFunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        cls.web_driver = WebDriver(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.web_driver.quit()
        super().tearDownClass()

    def test_user_create(self):
        email = "email@email.com"
        name = "name"
        password = "dr0wss@p"

        self.web_driver.get(f"{self.live_server_url}{reverse("user-create")}")
        self.web_driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(
            email
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(name)
        self.web_driver.find_element(By.XPATH, '//input[@name="password1"]').send_keys(
            password
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password2"]').send_keys(
            password
        )
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/")
