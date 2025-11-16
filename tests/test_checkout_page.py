import pytest

from saucelabs.pages.login_page import LoginPage
from saucelabs.pages.inventory_page import InventoryPage
from saucelabs.pages.cart_page import CartPage
from saucelabs.pages.checkout_page import CheckoutPage

def login_and_navigate_checkout_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.add_product_to_cart("Sauce Labs Backpack")
    cart = CartPage(driver)
    cart.click_shopping_cart()
    cart.click_checkout()
    checkout = CheckoutPage(driver)
    return checkout

@pytest.mark.cart_checkout
def test_cancel_checkout_returns_to_cart(driver):
    checkout = login_and_navigate_checkout_cart(driver)
    checkout.click_cancel()
    assert driver.current_url == "https://www.saucedemo.com/cart.html"

@pytest.mark.cart_checkout
def test_fill_info_and_continue_and_finish(driver):
    checkout = login_and_navigate_checkout_cart(driver)
    checkout.fill_checkout_info("Mahesh", "H", "561112")
    checkout.click_finish()
    assert checkout.is_confirmation_displayed()

@pytest.mark.cart_checkout
def test_cancel_before_finish(driver):
    checkout = login_and_navigate_checkout_cart(driver)
    checkout.fill_checkout_info("Mahesh", "H", "561112")
    checkout.click_cancel()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"