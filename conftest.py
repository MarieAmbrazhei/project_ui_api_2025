from selenium import webdriver
import pytest

from pages.customer_login_page import CustomerLogin
from pages.home_page import HomePage
from pages.create_account_page import CreateAccountPage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def create_page(driver):
    return CreateAccountPage(driver)
