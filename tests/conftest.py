import pytest
from selenium import webdriver

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def register_page(driver):
    return RegistrationPage(driver)
