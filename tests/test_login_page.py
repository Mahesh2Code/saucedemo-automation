import pytest


from saucelabs.pages.login_page import LoginPage


@pytest.mark.login
def test_login_valid_username_password(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    # driver.get("https://www.saucedemo.com/")
    # username_elem = driver.find_element(By.ID, "user-name")
    # password_elem = driver.find_element(By.ID, "password")
    # login_elem = driver.find_element(By.ID, "login-button")
    # username_elem.send_keys("standard_user")
    # password_elem.send_keys("secret_sauce")
    # login_elem.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

@pytest.mark.login
def test_login_invalid_username_password(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user1", "secret_sauce1")
    # driver.get("https://www.saucedemo.com/")
    # username_elem = driver.find_element(By.ID, "user-name")
    # password_elem = driver.find_element(By.ID, "password")
    # login_elem = driver.find_element(By.ID, "login-button")
    # username_elem.send_keys("standard_user1")
    # password_elem.send_keys("secret_sauce1")
    # login_elem.click()
    # error_elem = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    # error_message = error_elem.text
    # Epic sadface: Username and password do not match any user in this service
    assert page.is_error_displayed()


@pytest.mark.login
@pytest.mark.parametrize("username,password,expected_message", [
    ("", "", "username is required"),                     # both empty
    ("standard_user", "", "password is required"),        # password empty
    ("", "secret_sauce", "username is required"),         # username empty
    ("wrong_user", "wrong_pass", "username and password"),# invalid creds
    ("' OR '1'='1", "anything", "username and password"), # simple SQL-like injection
    ("<script>alert(1)</script>", "secret_sauce", "username and password"), # XSS-like payload
])
def test_login_negative_validation(driver, username, password, expected_message):
    page = LoginPage(driver)
    page.open()
    page.login(username, password)
    err = page.get_error()
    assert err is not None
    assert expected_message.lower() in err.lower()