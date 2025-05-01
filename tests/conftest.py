import pytest
from typing import Tuple
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.women_page import WomenPage
from pages.locators.women_locators import WomenLocators
from utils.models import ValidateRegistrationModel
from utils.utils import Random


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-cache")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.delete_all_cookies()

    yield chrome_driver

    chrome_driver.quit()


@pytest.fixture()
def register_user(driver):
    register_page = RegistrationPage(driver)
    register_page.open_page()
    user_data = Random.assemble_registration_data()
    register_page.fill_registration_form()
    return user_data


@pytest.fixture()
def login_user(register_user: ValidateRegistrationModel, driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.fill_login_form(register_user.email, register_user.password)
    return register_user


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def register_page(driver):
    return RegistrationPage(driver)


@pytest.fixture()
def women_page(driver):
    return WomenPage(driver)


@pytest.fixture()
def chose_random_top(register_user, women_page) -> Tuple[WomenPage, str]:
    women_page.open_page()
    women_page.open_tops_category()
    # choose random item
    random_item: WebElement = women_page.select_random_tops()
    chosen_top = random_item.text.split('\n')[0]
    print('chosen_top is', chosen_top)
    women_page.hover_element(random_item)
    random_item_button = random_item.find_element(*WomenLocators.ADD_TO_CART_BUTTON)
    random_item_button.click()
    item_desc_name = women_page.find_element_visible(WomenLocators.TITLE_OF_CHOSEN_TOP)
    assert item_desc_name.text == chosen_top


