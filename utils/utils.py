import random
import string

from faker import Faker

from utils.models import ValidateRegistrationModel

fake = Faker()


class Random:

    @staticmethod
    def assemble_registration_data():
        pwd = Random.generate_password(8)
        return ValidateRegistrationModel(
            first_name=Random.first_name(),
            last_name=Random.last_name(),
            email=Random.generate_random_email(),
            password=pwd,
            confirm_password=pwd
        )

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
