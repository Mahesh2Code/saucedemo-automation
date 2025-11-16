# Saucedemo Automation Testing Framework

This repository contains an end-to-end automation testing framework for [saucedemo.com](https://www.saucedemo.com/), built using Python, Selenium WebDriver, and Pytest. The framework follows best practices with the Page Object Model (POM) pattern, supports multiple browsers, and generates detailed HTML reports.

---

## Features

- **Multi-browser support:** run tests on Chrome, Firefox, and Edge using WebDriver Manager.
- **Robust POM design:** clean separation of page elements and test logic.
- **Comprehensive test coverage:** login (positive and negative), inventory, cart, checkout, logout, and cancel flows.
- **Custom reusable Selenium methods:** centralized wait and element interaction methods in `BasePage`.
- **Flexible test execution:** use Pytest markers to run specific test groups.
- **Automated HTML reporting:** using `pytest-html` for rich, self-contained reports.
- **Configurable via CLI and pytest.ini:** easily specify browser and test markers.
- **Password alert handling:** Chrome configured to disable password manager prompts for uninterrupted tests.

---

## Installation

1. Clone the repo:

```
git clone https://github.com/yourusername/saucedemo-automation.git
cd saucedemo-automation
```

2. Install dependencies:

```commandline
pip install -r requirements.txt
```

---

## Running Tests

Run all tests on Chrome (default):

```commandline
pytest
```
Run tests on Firefox:

```commandline
pytest --browser=firefox
```

Run only login tests:

```commandline
pytest -m login
```

Run tests with generated HTML report (automatically configured):

```commandline
pytest
```
Report saved at reports/report.html

---

## Project Structure

```commandline
/pages/         # Page objects following POM
/tests/         # Test cases organized by functionality
/conftest.py    # Pytest fixtures and driver setup
/pytest.ini     # Pytest configuration (markers, browser default, reporting)
/requirements.txt   # Python dependencies
/reports/       # Generated test reports
```

---

## Key Components

### BasePage

Central reusable Selenium methods like `find_element()`, `find_elements()`, `click()`, and `enter_text()` to ensure stable element handling.

### Login, Inventory, Cart, Checkout Pages

Encapsulate UI interactions specific to each page following POM conventions, simplifying test upkeep.

### Tests

Use Pytest fixtures and parameterization to cover:

- Login (valid, invalid, locked out, empty fields)
- Inventory interactions (add/remove to cart)
- Cart functionalities (item checks, removal, checkout start)
- Checkout flows (information entry, finish, cancel)
- Logout actions and session verifications

---

## Troubleshooting

- Ensure a stable internet connection for WebDriver Manager to auto-download required browser drivers.
- Use the `--browser` CLI option to switch browsers.
- Chrome alerts for password changes are suppressed through ChromeOptions preferences in the framework.
- If driver downloads fail, manually download and configure driver paths in `conftest.py`.

---

## Contributions

Contributions and improvements to enhance functionality and robustness are welcome. Please fork the repo and open a pull request.

---

## License

MIT License

---

## Contact

For questions, reach out to: [your-email@example.com]


---

This README and config setup consolidate your entire automation framework documentation and configuration for easy copy-paste and usage.
