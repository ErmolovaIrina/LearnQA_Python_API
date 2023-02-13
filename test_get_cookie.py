import requests

class TestResponseCookie:
  def test_get_cookie(self):

      response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
      cookie_value = dict(response.cookies)
      print(cookie_value)

      assert "HomeWork" in response.cookies, f"There is no cookie with 'HomeWork' key in response"