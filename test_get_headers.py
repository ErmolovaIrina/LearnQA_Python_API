import requests

class TestResponseHeader:
  def test_get_headers(self):

      response = requests.get("https://playground.learnqa.ru/api/homework_header")
      header_value = response.headers
      print(header_value)

      expected_result = {'Content-Type':'application/json', 'Connection':'keep-alive', 'Server':'Apache', 'x-secret-homework-header':'Some secret value'}

      for key in expected_result.keys():
        assert key in response.headers, f"There is no header with key '{key}' in response"

      assert "Some secret value" in expected_result.get("x-secret-homework-header"), f"There is no header with value in response"


