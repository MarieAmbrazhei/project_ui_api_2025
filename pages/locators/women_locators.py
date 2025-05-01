from selenium.webdriver.common.by import By


class WomenLocators:
    LOCATOR_TITLE = (By.XPATH, '//span[@class="base"]')
    LOCATOR_BTN_TOPS = (By.XPATH, '//a[text()="Tops"]')
    TOPS_ITEMS_LOCATOR = (By.XPATH, '//li[@class="item product product-item"]')
    ADD_TO_CART_BUTTON = (By.XPATH, './/button')
    TITLE_OF_CHOSEN_TOP = (By.XPATH, '//span[@itemprop="name"]')
