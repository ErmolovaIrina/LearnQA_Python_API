import requests
import random
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserGet(BaseCase):
    def test_user_details_with_other_auth(self):
        data = {
          'email': 'vinkotov@example.com',
          'password' : "1234"
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")


        response2 = requests.get("https://playground.learnqa.ru/api/user/2",
            headers={"x-csrf-token": self.token} ,
            cookies={"auth_sid": self.auth_sid})

        unexpeted_fields = ["username", "email", "firstName", "lastName"]

        #Assertions.assert_code_status(response2, 404)
        #Assertions.assert_invalid_request_message(response2, "User not found")
        Assertions.assert_json_has_not_keys(response2, unexpeted_fields)