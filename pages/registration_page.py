from selenium.webdriver.support import expected_conditions as EC

from config import Urls
from pages.base_page import BasePage
from pages.locators.my_account_locators import MyAccountLocators as AccountLoc
from pages.locators.registration_locators import RegistrationLocators as RegisterLoc
from utils.utils import Random


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.REGISTER_PAGE

    def fill_registration_form(self):
        validated_data = Random.assemble_registration_data()
        fields = {
            RegisterLoc.LOCATOR_FIRST_NAME: validated_data.first_name,
            RegisterLoc.LOCATOR_LAST_NAME: validated_data.last_name,
            RegisterLoc.LOCATOR_EMAIL: validated_data.email,
            RegisterLoc.LOCATOR_PASSWORD: validated_data.password,
            RegisterLoc.LOCATOR_CONFIRM_PASSWORD: validated_data.confirm_password
        }

        self.fill_forms(fields)
        self.click_button(RegisterLoc.LOCATOR_REGISTER_BUTTON)

    def check_successful_registration_title_is(self):
        title_is = self.wait.until(
            EC.visibility_of_element_located(AccountLoc.LOCATOR_OF_TITLE_REGISTRATION)
        )
        return title_is.text
