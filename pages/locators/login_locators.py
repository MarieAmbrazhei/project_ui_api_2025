from selenium.webdriver.common.by import By


class LoginLocators:
    LOCATOR_INPUT_EMAIL = (By.XPATH, '//input[@id="email"]')
    LOCATOR_INPUT_PASS = (By.XPATH, '//input[@name="login[password]"]')
    LOCATOR_BTN_SIGN_IN = (By.XPATH, '//button[@class="action login primary"]')
    LOCATOR_ERROR_MSG = (By.XPATH, '//div[@class="message-error error message"]')
