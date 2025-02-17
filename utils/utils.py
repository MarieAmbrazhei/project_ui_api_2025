import random
import string
from faker import Faker
from pages.locators.create_account_locators import CreateAccountLocators as CreateLoc
from pages.locators.my_account_locators import MyAccountLocators as AccountLoc
from utils.models import ValidateRegistrationData

fake = Faker()


class Random:

    @staticmethod
    def assemble_registration_data():
        pwd = Random.generate_password(8)
        fields = {
            CreateLoc.LOCATOR_FIRST_NAME: Random.first_name(),
            CreateLoc.LOCATOR_LAST_NAME: Random.last_name(),
            CreateLoc.LOCATOR_EMAIL: Random.generate_random_email(),
            CreateLoc.LOCATOR_PASSWORD: pwd,
            CreateLoc.LOCATOR_CONFIRM_PASSWORD: pwd
        }
        return ValidateRegistrationData(**fields)

    @staticmethod
    def first_name() -> str:
        return fake.unique.first_name()

    @staticmethod
    def last_name() -> str:
        return fake.unique.last_name()

    @staticmethod
    def generate_random_email() -> str:
        return fake.unique.email()

    @staticmethod
    def generate_words(length: int) -> str:
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_int(length: int) -> str:
        integers = string.digits
        return ''.join(random.choice(integers) for _ in range(length))

    @staticmethod
    def generate_password(length: int) -> str:
        return ''.join(
            random.choice(string.digits + string.ascii_letters +
                          string.punctuation) for _ in range(length)
        )
