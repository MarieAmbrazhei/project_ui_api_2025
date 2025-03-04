from selenium.webdriver.support import expected_conditions as EC

from config import Urls
from pages.base_page import BasePage
from pages.locators.login_locators import LoginLocators as LoginLoc
from pages.locators.my_account_locators import MyAccountLocators as AccountLoc


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.LOGIN_PAGE

    def fill_login_form(self, login, password):
        email_input = (self.wait.until
                       (EC.visibility_of_element_located(LoginLoc.LOCATOR_INPUT_EMAIL))
                       )
        pass_input = self.wait.until(
            EC.visibility_of_element_located(LoginLoc.LOCATOR_INPUT_PASS)
        )
        submit_button = self.wait.until(
            EC.visibility_of_element_located(LoginLoc.LOCATOR_BTN_SIGN_IN)
        )
        email_input.send_keys(login)
        pass_input.send_keys(password)
        submit_button.click()

    def check_error_alert_text_is(self):
        alert_message = self.wait.until(
            EC.visibility_of_element_located(LoginLoc.LOCATOR_ERROR_MSG)
        )
        return alert_message.text

    def check_title_is_log_in(self):
        title_is = self.wait.until(
            EC.visibility_of_element_located(AccountLoc.LOCATOR_LOGGED_IN)
        )
        return title_is.text
