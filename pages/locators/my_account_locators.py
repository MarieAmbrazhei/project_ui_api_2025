from selenium.webdriver.common.by import By


class MyAccountLocators:
    LOCATOR_MY_ACCOUNT = (By.XPATH, 'c')
    LOCATOR_OF_TITLE_REGISTRATION = (By.XPATH, '//div[@data-bind="html:'
                                               ' $parent.prepareMessageForHtml(message.text)"]')
    LOCATOR_LOGGED_IN = (By. XPATH, '//div[@class="panel header"]//span[@class="logged-in"]')