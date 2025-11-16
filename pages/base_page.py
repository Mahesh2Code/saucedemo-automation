from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_all_elements_located(locator))
        except:
            return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False