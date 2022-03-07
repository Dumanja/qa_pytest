import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def initialize_driver(request):
    browser_name = request.config.getoption("--browser")
    web_driver = None

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-extensions")

        web_driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = web_driver
    yield
    web_driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="type browser name here, example --browser "
                                                                         "chrome")
