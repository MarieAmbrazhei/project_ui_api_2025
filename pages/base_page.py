from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import Timeout


class BasePage:
    def __init__(self, driver: WebDriver):
        self.url = None
        self.driver = driver
        self.wait = WebDriverWait(driver, Timeout.MEDIUM_TIMEOUT, poll_frequency=1)

    def open_page(self):
        self.driver.get(self.url)

    def find(self, locator, time=Timeout.MEDIUM_TIMEOUT):
        try:
            return self.wait.until(
                EC.presence_of_element_located(locator),
                message=f'Element {locator} was not found after {time} seconds'
            )
        except TimeoutException as e:
            print(f'Error: {e}')
            raise

    def find_all(self, locator, time=Timeout.MEDIUM_TIMEOUT):
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_all_elements_located(locator),
                message=f'Elements {locator} were not found after {time} seconds'
            )
            return self.driver.find_elements(*locator)

        except TimeoutException as e:
            print(f'Error: {e}')
            return []

    def refresh_page(self):
        self.driver.refresh()

    def find_element_visible(self, locator, time=Timeout.MEDIUM_TIMEOUT):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Cant find visible element by locator {locator} after {time} seconds')

    def find_element_invisible(self, locator, time=Timeout.MEDIUM_TIMEOUT):
        return self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element located by {locator} is still visible after {time} seconds'
        )

    def click_button(self, locator, time=Timeout.MEDIUM_TIMEOUT):
        button = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Button {locator} is not clickable after {time} seconds'
        )
        button.click()

    def fill_form(self, locator, data):
        field = self.wait.until(EC.element_to_be_clickable(locator))
        field.clear()
        field.send_keys(data)

    def fill_forms(self, fields: dict):
        for locator, data in fields.items():
            self.fill_form(locator, data)
