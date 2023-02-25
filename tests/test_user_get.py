import requests
import allure
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

@allure.feature("Получение информации о юзере")
class TestUserGet(BaseCase):
    @allure.description("Получение информации о юзере с авторизацией под другим")
    def test_user_details_with_other_auth(self):
        data = {
          'email': 'vinkotov@example.com',
          'password' : "1234"
        }

        response1 = MyRequests.post("/user/login", data=data)
        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")


        response2 = MyRequests.get("/user/5",
            headers={"x-csrf-token": self.token} ,
            cookies={"auth_sid": self.auth_sid})
        print(response2.text)

        unexpeted_fields = ["id", "email", "firstName", "lastName"]

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "username")
        Assertions.assert_json_has_not_keys(response2, unexpeted_fields)