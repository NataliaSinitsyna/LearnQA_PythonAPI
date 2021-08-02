# Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py
import requests


class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.cookies)
        cookies = response.cookies
        expected_cookies = "HomeWork"
        expected_text_cookies = "hw_value"
        assert expected_cookies in cookies
        assert expected_text_cookies in cookies["HomeWork"]