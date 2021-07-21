import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
num_responses = 0
for i in response.history:
    num_responses += 1
print(f"Number of responses is {num_responses}")
print(response.url)