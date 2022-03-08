from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from test2.POM.BasePage import BasePage

MAIN_PAGE_URL = "https://www.youtube.com/"
id_for_search = "search-input"


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_main_page_and_search(self):
        self.driver.get(MAIN_PAGE_URL)
        youtube_search = self.driver.find_element(By.ID, id_for_search)
        youtube_search.click()
        youtube_search.send_keys("Movies")
        youtube_search.send_keys(Keys.ENTER)

    def get_google_search(self):
        self.driver.get("https://www.google.com/")
        google_search = self.driver.find_element(By.NAME, "q")
        google_search.click()
        google_search.send_keys("Selenium")
        google_search = self.driver.find_element(By.NAME, "btnK")
        google_search.click()

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