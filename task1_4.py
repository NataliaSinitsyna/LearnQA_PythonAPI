import requests

requests = requests.get('https://playground.learnqa.ru/api/get_text')
print(requests.text)