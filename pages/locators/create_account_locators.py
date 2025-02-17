from selenium.webdriver.common.by import By


class CreateAccountLocators:
    LOCATOR_FIRST_NAME = (By.ID, "firstname")
    LOCATOR_LAST_NAME = (By.ID, "lastname")
    LOCATOR_EMAIL = (By.ID, "email_address")
    LOCATOR_PASSWORD = (By.ID, "password")
    LOCATOR_CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    LOCATOR_REGISTER_BUTTON = (By.XPATH, '//button[@class="action submit primary"]')
