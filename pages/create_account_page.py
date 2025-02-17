from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators.create_account_locators import CreateAccountLocators as CreateLoc
from pages.locators.my_account_locators import MyAccountLocators as AccountLoc
from utils.utils import Random


class CreateAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://magento.softwaretestingboard.com/customer/account/create/'

    def fill_registration_form(self):
        fields = Random.assemble_registration_data()
        self.fill_forms(fields)
        self.click_button(CreateLoc.LOCATOR_REGISTER_BUTTON)

    def check_successful_registration_title_is(self):
        title_is = self.wait.until(
            EC.visibility_of_element_located(AccountLoc.LOCATOR_OF_TITLE_REGISTRATION)
        )
        return title_is.text
