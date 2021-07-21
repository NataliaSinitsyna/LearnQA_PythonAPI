import json
import requests
import time


class TestRequests:
    def test_long_requests(self):
        url = "https://playground.learnqa.ru/ajax/api/longtime_job"
        response = requests.get(url)
        token = json.loads(response.text)["token"]
        time_response = json.loads(response.text)["seconds"]
        payload = {"token": f"{token}"}
        response2 = requests.get(url, params=payload)
        assert json.loads(response2.text)["status"] == 'Job is NOT ready', f"Task hasn't status ready"
        time.sleep(time_response)
        response3 = requests.get(url, params=payload)
        assert json.loads(response3.text)["status"] == 'Job is ready', f"Time execution task is not over yet"
        assert json.loads(response3.text)["result"] != 0, f"No result"