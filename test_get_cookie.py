import requests

class TestResponseCookie:
  def test_get_cookie(self):

      response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
      cookie_value = dict(response.cookies)
      print(cookie_value)

      assert "HomeWork" in response.cookies, f"There is no cookie with 'HomeWork' key in response"

      expected_cookie_value = "hw_value"
      assert expected_cookie_value in response.cookies.values(), f"There is no cookie with value {expected_cookie_value} in response"