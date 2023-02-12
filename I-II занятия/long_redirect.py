import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

redirects = len(response.history)
final_redirect = response

print(redirects)
print(final_redirect.url)