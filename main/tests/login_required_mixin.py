from selenium.webdriver.common.by import By


class LoginRequiredMixin:
    fixtures = ["login_required_mixin"]

    def login(self):
        self.web_driver.get(f"{self.live_server_url}/sign_in/")
        self.web_driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(
            "email@email.com"
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(
            "dr0wss@p"
        )
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
