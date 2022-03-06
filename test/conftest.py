import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def initialize_driver(request):
    browser_name = request.config.getoption("--browser")
    driver = None

    if browser_name == "Chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="type browser name here, example --browser "
                                                                         "chrome")
