import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def create_user(self):
    #REGISTER
        register_data= self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email'],
        first_name = register_data['firstName'],
        password = register_data['password'],
        user_id = self.get_json_value(response1, "id")

        return {email, first_name, password, user_id}
    #LOGIN
    def login_user(self, email, password):
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid= self.get_cookie(response2, "auth_sid")
        token= self.get_header(response2, "x-csrf-token")

        return {auth_sid, token}
    def test_change_firstName_for_too_short_value(self, auth_sid, token, user_id):
        new_name = "C"
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name})

        Assertions.assert_invalid_request_message(response3, '{"error":"Too short value for field firstName"}')

        #GET
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid})

