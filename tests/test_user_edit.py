from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure

@allure.feature("Редактирование пользователя")
class TestUserEdit(BaseCase):
    @allure.description("Редактирование имени пользователя на короткое в один символ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_change_user_with_too_short_firstName(self):
    #REGISTER
      with allure.step("Register"):
        register_data= self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email'],
        password = register_data['password'],
        user_id = self.get_json_value(response1, "id")

    #LOGIN
      with allure.step("Login"):
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid= self.get_cookie(response2, "auth_sid")
        token= self.get_header(response2, "x-csrf-token")
    #EDIT
      with allure.step("Edit"):
        new_name = "C"
        response3 = MyRequests.put(f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name})
        Assertions.assert_code_status(response3, 400)
        Assertions.assert_invalid_request_message(response3, '{"error":"Too short value for field firstName"}')

    @allure.description("Изменение пользователя на имейл без символа @")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_change_user_with_wrong_email(self):
    #REGISTER
      with allure.step("Register"):
        register_data= self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email'],
        password = register_data['password'],
        user_id = self.get_json_value(response1, "id")

    #LOGIN
      with allure.step("Login"):
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid= self.get_cookie(response2, "auth_sid")
        token= self.get_header(response2, "x-csrf-token")

    #EDIT
      with allure.step("Edit"):
        new_email = "i.ermolova.com"
        response3 = MyRequests.put(f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email})
        Assertions.assert_code_status(response3, 400)
        Assertions.assert_invalid_request_message(response3, 'Invalid email format')

    @allure.description("Изменение юзера под чужой авторизацией")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_change_user_with_other_auth(self):
    #REGISTER
      with allure.step("Register"):
        register_data= self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email'],
        password = register_data['password'],
        user_id = self.get_json_value(response1, "id")

    #LOGIN
      with allure.step("Login"):
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid= self.get_cookie(response2, "auth_sid")
        token= self.get_header(response2, "x-csrf-token")

    #EDIT
      with allure.step("Edit"):
        new_name = "My new name"
        response3 = MyRequests.put(f"/user/675",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name})
        print(response3.content)
        print(response3.status_code)
        Assertions.assert_code_status(response3, 422)
        Assertions.assert_invalid_request_message(response3, f"Can't edit user with id {user_id}")

    @allure.description("Изменение юзера без авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_change_user_without_auth(self):
    #REGISTER
      with allure.step("Register"):
        register_data= self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email'],
        password = register_data['password'],
        user_id = self.get_json_value(response1, "id")

    #EDIT
      with allure.step("Edit"):
        new_name = "My new name"
        response3 = MyRequests.put(f"/user/{user_id}",
            headers={"x-csrf-token": "af0e641ce8b7d58e9119b3f50202a0a15c06b0dd6e6d71318f4f3feb7b93c60b"},
            cookies={"auth_sid": "626eed1f2395e02f893b61e1c366a624a2ab05765c06b0dd6e6d71318f4f3feb7b93c60b"},
            data={"firstName": new_name})

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_invalid_request_message(response3, 'Auth token not supplied')




