from config import Urls
from pages.base_page import BasePage


class TopsWomenPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.TOPS_WOMEN_PAGE
