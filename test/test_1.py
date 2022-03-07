from test.BaseTest import BaseTest
from test.POM.MainPageTest import MainPage


class SearchTest(BaseTest):

    def test_first_example(self):
        main_object = MainPage(self.driver)

        main_object.get_main_page_and_search()

    def test_second_example(self):
        main_object = MainPage(self.driver)

        main_object.get_main_page_and_search()

    def test_third_example(self):  # ovo mi svejedno i ne treba, jer ce sve ici preko POMa i u BasePage cu napraviti custom f-je
        self.driver.get("https://zlatiborbooking.rs/")