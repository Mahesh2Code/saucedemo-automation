import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "edge"],
        help="Browser to run tests on: chrome (default), firefox or edge"
    )

@pytest.fixture
def driver(request):
    # chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    # driver = webdriver.Chrome(options=chrome_options)
    # driver.maximize_window()
    # yield driver
    # driver.quit()
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        chrome_prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        }
        options.add_experimental_option("prefs", chrome_prefs)
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == "edge":
        # options = webdriver.EdgeOptions()
        # service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()