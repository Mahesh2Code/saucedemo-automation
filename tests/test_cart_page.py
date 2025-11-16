import pytest

from saucelabs.pages.login_page import LoginPage
from saucelabs.pages.inventory_page import InventoryPage
from saucelabs.pages.cart_page import CartPage


def login_and_navigate_to_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.add_product_to_cart("Sauce Labs Backpack")
    cart = CartPage(driver)
    cart.click_shopping_cart()
    return cart

@pytest.mark.cart_page
def test_cart_items_display(driver):
    cart = login_and_navigate_to_cart(driver)
    items = cart.get_cart_items()
    assert "Sauce Labs Backpack" in items

@pytest.mark.cart_page
def test_remove_item_from_cart(driver):
    cart = login_and_navigate_to_cart(driver)
    cart.remove_product("Sauce Labs Backpack")
    items = cart.get_cart_items()
    assert "Sauce Labs Backpack" not in items

@pytest.mark.cart_page
def test_click_continue_shopping(driver):
    cart = login_and_navigate_to_cart(driver)
    cart.click_continue_shopping()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

@pytest.mark.cart_page
def test_click_checkout(driver):
    cart = login_and_navigate_to_cart(driver)
    cart.click_checkout()
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"