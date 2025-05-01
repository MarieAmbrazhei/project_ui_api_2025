import random
from config import Urls
from pages.base_page import BasePage
from pages.locators.women_locators import WomenLocators as WomenLoc


class WomenPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.WOMEN_PAGE

    def open_tops_category(self):
        self.click_button(WomenLoc.LOCATOR_BTN_TOPS)

    def select_random_tops(self):
        random_item = random.choice(self.find_all(WomenLoc.TOPS_ITEMS_LOCATOR))
        return random_item
