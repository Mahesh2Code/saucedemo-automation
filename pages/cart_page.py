from selenium.webdriver.common.by import By

from saucelabs.pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    REMOVE_BTN = (By.XPATH, "//*[text()='Remove']")
    CHECKOUT_BTN = (By.ID, "checkout")

    def get_cart_items(self):
        items = [item.text for item in self.find_elements(self.CART_ITEM_NAME)]
        return items

    def remove_product(self, product_name):
        items = self.find_elements(self.CART_ITEM_NAME)
        for item in items:
            if item.text == product_name:
                parent = item.find_element(By.XPATH, "../../..")
                btn = parent.find_element(By.TAG_NAME, "button")
                btn.click()
                break

    def click_shopping_cart(self):
        self.click(self.SHOPPING_CART)

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)


