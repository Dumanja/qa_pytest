from test2.BaseTest import BaseTest
from test2.POM.MainPageTest import MainPage


class SearchTest(BaseTest):

    def test_first(self):               #id locator
        main_object = MainPage(self.driver)
        main_object.get_main_page_and_search()

    def test_second(self):              #name locator
        main_object = MainPage(self.driver)
        main_object.get_google_search()

    def test_third(self):       #link text locator
        main_object = MainPage(self.driver)
        main_object.get_mixcloud_pro()

    def test_fourth(self):      #css selector
        main_object = MainPage(self.driver)
        main_object.get_github()

    def test_fifth(self):      #Xpath
        main_object = MainPage(self.driver)
        main_object.get_ftn()

    def test_sixth(self):      #Xpath
        main_object = MainPage(self.driver)
        main_object.get_google()
