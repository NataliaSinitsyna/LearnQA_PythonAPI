import requests

url = "https://playground.learnqa.ru/api/compare_query_type"
#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
response = requests.get(url)
print(response.text, response.status_code)

#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response2 = requests.head(url)
print(response2.text, response2.status_code)

#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
payload = {"method": "POST"}
response3 = requests.post(url, data=payload)
print(response3.text, response3.status_code)

#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса.
# Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок.

list_methods = ["GET", "POST", "PUT", "DELETE"]
result = []
for i in list_methods:
    payload2 = {"method": i}
    response4 = requests.get(url, params=payload2)
    response5 = requests.post(url, data=payload2)
    response6 = requests.put(url, data=payload2)
    response7 = requests.delete(url, data=payload2)
    result.extend((i, response4.text, response5.text, response6.text, response7.text))
print(result)




