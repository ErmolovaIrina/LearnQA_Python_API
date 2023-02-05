import requests
import json
import time

#cоздаем задачу и парсим ответ
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.text)
jsonList = json.loads(response.text)

#делаем запрос с токеном из ответа
checkJobStatus = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": jsonList["token"]})
print(checkJobStatus.text)
#парсим ответ
jobStatus = json.loads(checkJobStatus.text)

#проверяем статус ответа и если он правильный, ждем отложенное время и спрашиваем еще раз
if jobStatus["status"] == "Job is NOT ready":
    time.sleep(jsonList["seconds"])
    readyResponse = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": jsonList["token"]})
    print(readyResponse.text)
else:
    print("чет не завелось")



#response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": "abc"})