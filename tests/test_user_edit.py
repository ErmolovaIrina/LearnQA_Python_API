import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        data= self.prepare_registration_data()
        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)