from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure

@allure.feature("Удаления созданного пользователя")
class TestUserDelete(BaseCase):
    @allure.description("Удаление пользователя которого нельзя удалять")
    @allure.severity("Critical")
    def test_delete_undedeliteble_user(self):
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id = self.get_json_value(response1, "user_id")
    #DELETE
        response2 = MyRequests.delete(f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid})
        print(response2.content)
        print(response2.status_code)
        Assertions.assert_code_status(response2, 400)
        Assertions.assert_invalid_request_message(response2, 'Please, do not delete test users with ID 1, 2, 3, 4 or 5.')

    @allure.description("Успешное удаление пользователя")
    @allure.severity("Critical")
    def test_delete_user(self):
    #REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email'],
        password = register_data['password'],
        user_id = self.get_json_value(response1, "id")

    #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
    #DELETE
        response3 = MyRequests.delete(f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid})
        Assertions.assert_code_status(response3, 200)

    #GET
        response4 = MyRequests.get(f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid})
        Assertions.assert_code_status(response4, 404)
        Assertions.assert_invalid_request_message(response4, 'User not found')

    @allure.description("Удаление пользователя с авторизацией под другим пользователем")
    @allure.severity("Critical")
    def test_delete_user_with_other_auth(self):
    #REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email'],
        password = register_data['password'],
        user_id = self.get_json_value(response1, "id")

    #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        Assertions.assert_json_has_key(response2, "user_id")

    #DELETE
        response3 = MyRequests.delete(f"/user/63028",
            headers={"x-csrf-token": "af0e641ce8b7d58e9119b3f50202a0a15c06b0dd6e6d71318f4f3feb7b93c60b"},
            cookies={"auth_sid": "626eed1f2395e02f893b61e1c366a624a2ab05765c06b0dd6e6d71318f4f3feb7b93c60b"})
        Assertions.assert_code_status(response3, 400)
        Assertions.assert_invalid_request_message(response3, 'Auth token not supplied')

    #GET
        response4 = MyRequests.get(f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid})
        Assertions.assert_code_status(response4, 200)

        expected_fields = ["id", "username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response4, expected_fields)

        expected_user_id = self.get_json_value(response4, "id")
        assert user_id == expected_user_id, f"Values don't match"




