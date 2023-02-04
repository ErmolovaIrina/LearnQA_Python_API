import requests

#список с значением параметров, методов и урл запроса
methods = ["GET", "POST", "PUT", "DELETE"]
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
types = ["get", "post", "put", "delete"]

print("Вопрос 1")
response = requests.get(url, params={"other": "get"})
print(response.text)

print("Вопрос 2")
response = requests.get(url, params={"method": "HEAD"})
print(response.text)

print("Вопрос 3 и 4")
def getCycle():
    for method in methods:
        response = requests.request(types[0], url, params={"method": method})
        print(response.text)

def otherMethCycle():
    for type in types:
        print()
        for method in methods:
            response = requests.request(type, url, data={"method": method})
            print(response.text)

getCycle()
print()
otherMethCycle()