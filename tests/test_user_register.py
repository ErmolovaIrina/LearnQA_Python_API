import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime


class TestUserRegister(BaseCase):
    def setup(self):
        self.basePart = "base"
        self.domain = "learnqa.com"
        self.ad = "@"
        self.randomPart = datetime.now().strftime("m%d%Y%H%M%S")

        self.correct_email = f"{self.basePart}{self.randomPart}{self.ad}{self.domain}"

    def test_create_user_with_wrong_email(self):
        email = f"{self.basePart}{self.randomPart}{self.domain}"
        data={
            "password":"123",
            "username":"Ivan123",
            "firstName":"Ivan",
            "lastName":"Ivanov",
            "email": email
        }
        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
        print(response.content)

        Assertions.assert_code_status(response, 400)

