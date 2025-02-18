from selenium.webdriver.common.by import By


class GearLocators:
    LOCATOR_TITLE = (By.XPATH, '//span[@class="base"]')
    LOCATOR_BTN_BAGS = (By.XPATH, '//ol[@class="items"]//a[text()="Bags"]')