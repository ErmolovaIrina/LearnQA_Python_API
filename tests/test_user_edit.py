import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        data= self.prepare_registration_data()
        response1 = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

