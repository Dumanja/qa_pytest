import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_first_example(initialize_driver):
    driver = initialize_driver

    locator_for_search = "//input[@title='Search']"

    driver.get("https://www.google.com/")
    google_search = driver.find_element(By.XPATH, locator_for_search)
    google_search.click()
    google_search.send_keys("qa kursevi")

    time.sleep(5)

    google_search.send_keys(Keys.ENTER)

    time.sleep(5)
