from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators.home_locators import HomeLocators as HomeLoc


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://magento.softwaretestingboard.com/')

    def check_title_is(self):
        title_is = self.wait.until(
            EC.visibility_of_element_located(HomeLoc.LOCATOR_HOME_PAGE)
        )
        return title_is.text
