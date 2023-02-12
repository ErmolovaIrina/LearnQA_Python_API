import requests
import json
import time

#cоздаем задачу и парсим ответ
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
jsonList = response.json()

#делаем запрос с токеном из ответа и парсим ответ
checkJobStatus = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": jsonList["token"]})
jobStatus = checkJobStatus.json()

#проверяем статус ответа и если он правильный, ждем нужное время и спрашиваем еще раз
if jobStatus["status"] == "Job is NOT ready":
    time.sleep(jsonList["seconds"])
    readyResponse = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": jsonList["token"]})
    print(readyResponse.text)
else:
    print("Статус ответа неверный")

#проверяем что в ответе есть поле result и поле status = Job is ready
checkResponse = json.loads(readyResponse.text)
keyResult = "result"

if (keyResult in checkResponse and checkResponse.get("status") == "Job is ready"):
    print("YES")
else:
    print("NO")
