import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test.POM.BasePage import BasePage

locator_for_search = "//input[@title='Search']"
MAIN_PAGE_URL = "https://www.google.com/"
id_for_search = "search-input"


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_main_page_and_search(self):
        self.driver.get(MAIN_PAGE_URL)
        google_search = self.driver.find_element(By.XPATH, locator_for_search)
        google_search.click()
        google_search.send_keys("qa kursevi")

        google_search.send_keys(Keys.ENTER)

    def get_google_search(self):
        self.driver.get("https://www.google.com/")
        google_search = self.driver.find_element(By.XPATH, locator_for_search)
        google_search.click()
        google_search.send_keys("Selenium")
        button_search = self.driver.find_element(By.XPATH, '//div[@class="FPdoLc lJ9FBc"]//input[1]')
        button_search.click()

    def get_mixcloud_pro(self):
        self.driver.get("https://www.mixcloud.com/")
        mixcloud = self.driver.find_element(By.LINK_TEXT, "Pro")
        mixcloud.click()

    def get_github(self):
        self.driver.get("https://www.github.com/")
        github = self.driver.find_element_by_css_selector("#user_email")
        github.click()
        github.send_keys("marko@gmail.com")
        github.send_keys(Keys.ENTER)

    def get_google(self):
        self.driver.get("https://www.google.com/")
        google_search = self.driver.find_element_by_xpath("//input[@title='Search']")
        google_search.click()
        google_search.send_keys("DJ Marcuss")
        google_search.send_keys(Keys.ENTER)

    def get_ftn(self):
        self.driver.get("http://www.ftn.uns.ac.rs/691618389/fakultet-tehnickih-nauka")
        ftn = self.driver.find_element_by_xpath("//input[@name='value']")
        ftn.click()
        ftn.send_keys("Mehatronika")
        ftn.send_keys(Keys.ENTER)
