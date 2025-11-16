import pytest

from saucelabs.pages.login_page import LoginPage
from saucelabs.pages.inventory_page import InventoryPage


def login_to_inventory(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    return InventoryPage(driver)


@pytest.mark.inventory
def test_inventory_products_load(driver):
    inv_page = login_to_inventory(driver)
    products = inv_page.get_product_names()
    assert len(products) > 0


@pytest.mark.inventory
def test_add_and_remove_product(driver):
    inv_page = login_to_inventory(driver)
    products = inv_page.get_product_names()
    first_product = products[0]
    inv_page.add_product_to_cart(first_product)
    inv_page.remove_product_from_cart(first_product)


@pytest.mark.inventory
def test_inventory_access_without_login(driver):
    driver.get("https://www.saucedemo.com/inventory.html")
    assert driver.current_url == "https://www.saucedemo.com/"