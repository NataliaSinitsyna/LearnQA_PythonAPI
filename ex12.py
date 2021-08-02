import requests


class TestHeaders:
    def test_headers(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)
        headers = response.headers
        expected_headers = "x-secret-homework-header"
        expected_text_headers = "Some secret value"
        assert expected_headers in headers
        assert expected_text_headers in headers[expected_headers]