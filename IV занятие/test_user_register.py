import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import random


class TestUserRegister(BaseCase):
    def setup(self):
        basePart = "base"
        domain = "learnqa.com"
        ad = "@"
        randomPart = random.randint(1,260)

        self.email = f"{basePart}{randomPart}{ad}{domain}"
        print(self.email)

    def test_create_user_with_existing_email(self):
        data={
            "password":"123",
            "username":"Ivan123",
            "firstName":"Ivan",
            "lastName":"Ivanov",
            "email": self.email
        }
        response = requests.post('https://playground.learnqa.ru/api/user/', data={data})
