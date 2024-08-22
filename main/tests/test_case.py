from django.core.cache import cache
from django.test import LiveServerTestCase
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestCase(LiveServerTestCase):
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

    def tearDown(self):
        cache.clear()

    def find_elements(self, text):
        return [
            element
            for element in self.web_driver.find_elements(
                By.XPATH, f'//*[normalize-space(text())="{text}"]'
            )
            if element.is_displayed()
        ]
