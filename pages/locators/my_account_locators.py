from selenium.webdriver.common.by import By


class MyAccountLocators:
    LOCATOR_MY_ACCOUNT = (By.XPATH, '//span[@class="base"]')
    LOCATOR_OF_TITLE_REGISTRATION = (By.XPATH, '//div[@data-bind="html:'
                                               ' $parent.prepareMessageForHtml(message.text)"]')
