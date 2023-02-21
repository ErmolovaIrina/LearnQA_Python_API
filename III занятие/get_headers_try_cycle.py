import requests

class TestHeader:
  def test_get_headers_try_cycle(self):

      response = requests.get("https://playground.learnqa.ru/api/homework_header")
      header_value = response.headers
      print(header_value)

      expected_result = {'Content-Type':'application/json', 'Connection':'keep-alive', 'Server':'Apache', 'x-secret-homework-header':'Some secret value'}

      for key in expected_result.keys():
        print(key)
        assert key in response.headers, f"There is no header with key '{key}' in response"

      for value in expected_result.values():
        print(value)
        assert value in response.headers.values(), f"There is no header with key '{value}' in response"

      for pair in expected_result.items():
        print(pair)
        assert pair in response.headers.items(), f"There is no header with key '{pair}' in response"