import pytest

from saucelabs.pages.login_page import LoginPage
from saucelabs.pages.menu_page import MenuPage


@pytest.mark.logout
def test_logout(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    menu_page = MenuPage(driver)
    menu_page.logout()
    assert driver.current_url == "https://www.saucedemo.com/"