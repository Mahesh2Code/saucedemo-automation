from selenium.webdriver.common.by import By

from saucelabs.pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def is_error_displayed(self):
        return self.is_displayed(self.ERROR_MSG)

    def get_error(self):
        return self.get_text(self.ERROR_MSG)


