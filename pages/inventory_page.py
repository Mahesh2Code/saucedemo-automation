from selenium.webdriver.common.by import By

from saucelabs.pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BTN = (By.XPATH, "//button[text()='Add to cart']")
    REMOVE_BTN = (By.XPATH, "//button[text()='Remove']")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")


    def get_product_names(self):
        products = [item.text for item in self.find_elements(self.INVENTORY_ITEM)]
        return products

    def add_product_to_cart(self, product_name):
        items = self.find_elements(self.INVENTORY_ITEM)
        for item in items:
            if item.text == product_name:
                parent = item.find_element(By.XPATH, "../../..")
                # print(dir(parent))
                # print(parent.get_attribute("outerHTML"))
                btn = parent.find_element(By.TAG_NAME, "button")
                btn.click()
                break

    def remove_product_from_cart(self, product_name):
        items = self.find_elements(self.INVENTORY_ITEM)
        for item in items:
            if item.text == product_name:
                parent = item.find_element(By.XPATH, "../../..")
                btn = parent.find_element(By.TAG_NAME, "button")
                btn.click()
                break

    def go_to_cart(self):
        self.click(self.CART_LINK)

