from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class WomenLocators:
    LOCATOR_TITLE = (By.XPATH, '//span[@class="base"]')
    LOCATOR_BTN_TOPS = (By.XPATH, '//a[text()="Tops"]')


