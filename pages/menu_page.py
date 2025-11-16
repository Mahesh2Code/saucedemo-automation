from selenium.webdriver.common.by import By

from saucelabs.pages.base_page import BasePage

class MenuPage(BasePage):
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def logout(self):
        self.click(self.MENU_BTN)
        # self.driver.refresh()
        self.click(self.LOGOUT_LINK)

