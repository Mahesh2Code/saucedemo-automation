from selenium.webdriver.common.by import By

from saucelabs.pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CANCEL_BTN = (By.ID, "cancel")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CONFIRMATION_MSG = (By.CLASS_NAME, "complete-header")

    def fill_checkout_info(self, first_name, last_name, post_code):
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.POSTAL_CODE, post_code)
        self.click(self.CONTINUE_BTN)

    def click_finish(self):
        self.click(self.FINISH_BTN)

    def is_confirmation_displayed(self):
        return self.is_displayed(self.CONFIRMATION_MSG)

    def click_cancel(self):
        self.click(self.CANCEL_BTN)
