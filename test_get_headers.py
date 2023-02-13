import requests

class TestResponseHeader:
  def test_get_headers(self):

      response = requests.get("https://playground.learnqa.ru/api/homework_header")
      header_value = response.headers
      print(header_value)

      expected_headers = ["Content-Type","Content-Length","Connection","Keep-Alive","Server","x-secret-homework-header","Cache-Control","Expires"]
      for i in expected_headers:
        assert i in response.headers, f"There is no key header '{i}' in response"


