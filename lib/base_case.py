import json.decoder
from datetime import datetime
from requests import Response

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find header with name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:
            assert False, f"Response is not in JSON Format. Response text is '{response.text}'"
        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

        return response_as_dict[name]

    def prepare_registration_data(self, email=None):
        if email is None:
            basePart = "base"
            domain = "learnqa.com"
            ad = "@"
            randomPart = datetime.now().strftime("m%d%Y%H%M%S")

            wrong_email = f"{basePart}{randomPart}{domain}"
            email = f"{basePart}{randomPart}{ad}{domain}"

        return {
            "password": "123",
            "username": "Ivan123",
            "firstName": "Ivan",
            "lastName": "Ivanov",
            "email": email
        }
    def prerare_registration_with_wrong_email(self, wrong_email=None):
        if wrong_email is None:
            basePart = "base"
            domain = "learnqa.com"
            randomPart = datetime.now().strftime("m%d%Y%H%M%S")
            wrong_email = f"{basePart}{randomPart}{domain}"

        return {
            "password": "123",
            "username": "Ivan123",
            "firstName": "Ivan",
            "lastName": "Ivanov",
            "email": wrong_email
        }