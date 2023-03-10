import string
import allure
import pytest
import requests
import random

from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime

@allure.epic("Регистрация юзера")
class TestUserRegister(BaseCase):
    @allure.description("Подготовительный метод")
    def setup_method(self):
        basePart = "base"
        domain = "learnqa.com"
        ad = "@"
        randomPart = datetime.now().strftime("m%d%Y%H%M%S")

        self.correct_email = f"{basePart}{randomPart}{ad}{domain}"

    testData = [({"username":"Ivan123", "firstName":"Ivan", "lastName":"Ivanov", "email": "self.correct_email"}, "The following required params are missed: password"),
                ({"password": "123", "firstName": "Ivan", "lastName": "Ivanov", "email": "self.correct_email"}, "The following required params are missed: username"),
                ({"password": "123", "username": "Ivan123", "lastName":"Ivanov", "email": "self.correct_email"}, "The following required params are missed: firstName"),
                ({"password": "123", "username": "Ivan123", "firstName": "Ivan", "email": "self.correct_email"}, "The following required params are missed: lastName"),
                ({"password": "123", "username": "Ivan123", "firstName": "Ivan", "lastName": "Ivanov"}, "The following required params are missed: email")]

    @allure.description("Создание пользователя с невалидным имейлом")
    def test_create_user_with_wrong_email(self):
        data=self.prerare_registration_with_wrong_email()
        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", Assertions.assert_json_has_key(response, "id")


    @allure.description("Параметризированный тест с попыткой создания юзера с недостающими параметрами")
    @pytest.mark.parametrize("data, expected_message", testData)
    def test_create_user_with_wrong_request(self, data, expected_message):

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        Assertions.assert_invalid_request_message(response, expected_message)

    @allure.description("Создание юзера с очень коротким невалидным именем")
    def test_create_user_with_short_name(self):
        data={
            "password":"123",
            "username":"I",
            "firstName":"Ivan",
            "lastName":"Ivanov",
            "email": self.correct_email
        }
        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)

        error_message = "The value of 'username' field is too short"
        Assertions.assert_invalid_request_message(response, error_message)

    @allure.description("Создание юзера с очень длинными именем")
    def test_create_user_with_long_name(self):

        letters = string.ascii_letters
        random_string = ''.join(random.choice(letters) for i in range(251))

        data={
            "password":"123",
            "username": {random_string},
            "firstName":"Ivan",
            "lastName":"Ivanov",
            "email": self.correct_email
        }
        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)

        error_message = "The value of 'username' field is too long"
        Assertions.assert_invalid_request_message(response, error_message)

