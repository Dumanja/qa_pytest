from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test.POM.BasePage import BasePage

locator_for_search = "//input[@title='Search']"
MAIN_PAGE_URL = "https://www.google.com/"


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_main_page_and_search(self):
        self.driver.get(MAIN_PAGE_URL)
        google_search = self.driver.find_element(By.XPATH, locator_for_search)
        google_search.click()
        google_search.send_keys("qa kursevi")

        google_search.send_keys(Keys.ENTER)
