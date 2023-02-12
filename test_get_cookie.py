import requests

class TestResponseCookie:
  def test_get_cookie(self):

      response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
      cookie_value = dict(response.cookies)
      name, value = list(cookie_value.items())[0]
      print(cookie_value)

      assert name in cookie_value, f"There is no {name} cookie in response"