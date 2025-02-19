import os


class Timeout:
    SHORT_TIMEOUT = 5
    MEDIUM_TIMEOUT = 10
    LONG_TIMEOUT = 30


class Urls:
    BASE_URL = os.getenv('BASE_URL', "https://magento.softwaretestingboard.com")

    HOME_PAGE = f'{BASE_URL}/'
    LOGIN_PAGE = f'{BASE_URL}/customer/account/login/'
    REGISTER_PAGE = f'{BASE_URL}/customer/account/create/'
    WOMEN_PAGE = f'{BASE_URL}/women.html'
    MEN_PAGE = f'{BASE_URL}/men.html'
    GEAR_PAGE = f'{BASE_URL}/gear.html'
