# import pytest
# import json
# import requests

# payload = {"name": "User"} #создаем словарь с параментрами
# response = requests.get("http://playground.learnqa.ru/api/hello", params=payload) #создает запрос
# print(response.text) #текст ответа
#
# string_as_json_format = '{"answer": "Hello, User"}'
# obj = json.loads(string_as_json_format) #превращаем в объект, который по свойствам похож на словарь
# # print(obj['answer']) #обращаемся к ключу 'answer' в словаре obj / лучше не обращаться к ключу сразу, а проверять его наличие в словаре, поэтому будем использовать операцию ветвления
# key = 'answer'
# if key in obj: #проверяем наличие ключа в словаре
#     print(obj[key])
# else:
#     print(f"Key {key} in JSON not") #чтобы использовать переменную, нужно перед текстом поставить f, текст обернуть в двойные кавычки и переменную заключить в {}

# объединим знания об отправке запросов и парсинге json
# from json.decoder import JSONDecodeError
#
# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])
#
# response = requests.get("https://playground.learnqa.ru/api/hello")
# print(response.text)
# try: #необходимо проверять в каком формате приходит ответ и правильно обрабатывать ошибку
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("Response is not a JSON format")

# import requests

# response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"}) #после requests. выбираем тип запроса post/delete/put, params только для get запроса
# response2 = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
# print(response.text)
# print(response2.text)
# print(response2.status_code)
#
# response3 = requests.post("https://playground.learnqa.ru/api/get_500")
# print(response3.status_code)
# print(response3.text)
#
# response4 = requests.post("https://playground.learnqa.ru/api/something")
# print(response4.status_code)
# print(response4.text)
#
# response5 = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
# print(response5.status_code) #301
# response6 = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True) #содержит все данные ответа (откуда и куда редирект)
# print(response6.status_code) #200
# first_response = response6.history[0] #history - массив, в котором хранится информация о всех пердыдущих запросах
# second_response = response6 #информация о всех итговых запросах хранится в response6, но для наглядности переложим в другую переменную
# print(first_response.url) # смотрим на какие url были сделаны запросы
# print(second_response.url)
#
# headers = {"some_header": "123"}
# response7 = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
# print(response7.text)
# print(response7.headers)

# #cookie хранится в виде объекта!
# payload = {"login": "secret_login", "password": "secret_pass"}
# response8 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
# print(response8.text)
# print(response8.status_code)
# print(dict(response8.cookies))
# print(response8.headers)
# cookie_value = response8.cookies.get('auth_cookie') #получаем из запроса куки с названием auth_cookie
# #cookies = {'auth_cookie': cookie_value} #создаем словарь для следующего запроса, куда кладём авторизационную куки
# cookies = {}
# if cookie_value is not None:
#     cookies.update({'auth_cookie': cookie_value})
# response82 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
# print(response82.text)

# class TestExamples: #python -m pytest examples.py -k "test_check_math" в терминале
#     def test_check_math(self):
#         a = 5
#         b = 9
#         expected_sum = 14
#         assert a + b == expected_sum, f"Sum of variables a and b is not equal to {expected_sum}"
#
#     def test_check_math2(self):
#         a = 5
#         b = 11
#         expected_sum = 14
#         assert a+b == expected_sum, f"Sum of variables a and b is not equal to {expected_sum}"

# import requests
# import pytest
#
# class TestFirstApi: #создали класс по имени файла, обязательно должны начинаться с test
#
#     names = [
#         ("Vitalii"),
#         ("Arseniy"),
#         ("")
#     ]
#
#     @pytest.mark.parametrize('name', names) #(функция декоратора из библиотеки pytest)указываем именя переменной, в которую pytest будет передавать данные, далее через запятую переменную, в которой сейчас хранятся данные
#     def test_hello_call(self, name): #объявили функцию, обязательно должны начинаться с test_
#         url = "https://playground.learnqa.ru/api/hello" #переменные
#         # name = 'Vitalii'
#         data = {'name': name}
#
#         response = requests.get(url, params=data)
#         assert response.status_code == 200, "Wrong response code" #проверка на статус-кода
#
#         response_dict = response.json() #парсим json/словарь
#         assert "answer" in response_dict, "There is no field 'answer' in the response" #ищем поле/ключ 'answer'
#         if len(name) == 0:
#             expected_response_text = f"Hello, someone"
#         else:
#             expected_response_text = f"Hello, {name}" #ожидаемая строка
#         actual_response_text = response_dict["answer"] #реальный тескт ответа
#         assert actual_response_text == expected_response_text, "Actual text in the response is not correct" #значение поля = ожидаемому результату/ #проверка, которая контролирует что что-то прошло так (ожидаемый результат) требует помещение булева

# import requests
# import pytest
#
# class TestUserAuth:
#     exclude_params = [
#         ("no_cookie"),
#         ("no_token")
#     ]
#
#     def setup(self): #кладем в этот метод повторящуюся логику
#         data = {
#             'email': 'vinkotov@example.com',
#             'password': '1234'
#         }
#         response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
#         assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"  # проверяем наличие нужных куки
#         assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"  # проверяем наличие нужного заголовка
#         assert "user_id" in response1.json(), "There is no user id in the response"  # проверяем наличие нужный user_id
#
#         self.auth_sid = response1.cookies.get("auth_sid")  # перекладываем в отдельные переменные
#         self.token = response1.headers.get("x-csrf-token")
#         self.user_id_from_auth_method = response1.json()["user_id"]
#
#     def test_auth_user(self):
#
#         response2 = requests.get(
#             "https://playground.learnqa.ru/api/user/auth",
#             headers={"x-csrf-token": self.token},
#             cookies={"auth_sid": self.auth_sid}
#         )
#
#         assert "user_id" in response2.json(), "There is no user id in thr second response"
#         user_id_from_check_method = response2.json()["user_id"]
#         assert self.user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal to user id from check method"  # сравниваем user_id
#
#
#
#     @pytest.mark.parametrize('condition', exclude_params)
#     def test_negative_auth_check(self, condition):
#
#         if condition == "no_cookie":
#             response2 = requests.get(
#                 "https://playground.learnqa.ru/api/user/auth",
#                 headers={"x-csrf-token": self.token}
#             )
#         else:
#             response2 = requests.get(
#                 "https://playground.learnqa.ru/api/user/auth",
#                 cookies={"auth_sid": self.auth_sid}
#             )
#         assert "user_id" in response2.json(), "There is no user id in the second response"
#         user_id_from_check_method = response2.json()["user_id"]
#         assert user_id_from_check_method == 0, f"User is authorized with condition {condition}"



import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure

@allure.epic("Authorization cases")
class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self): #кладем в этот метод повторящуюся логику
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)
        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    @allure.description("This test successufully authorize user by email adn password")
    def test_auth_user(self):

        response2 = MyRequests.get("/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method "
        )

    @allure.description("This test checks authorization status w/o sending auth cookie or token")
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):

        if condition == "no_cookie":
            response2 = MyRequests.get(
                "/user/auth",
                headers={"x-csrf-token": self.token}
            )
        else:
            response2 = MyRequests.get(
                "/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )

        Assertions.assert_json_value_name(
            response2,
            "user_id",
            0,
            f"User is authorized with condition {condition}"
        )

class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"



class TestUserGet(BaseCase):
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")


    def test_get_user_details_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        #REGISTER
        register_data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response, "id")

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT

        new_name = 'Changed name'

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name})

        Assertions.assert_code_status(response3, 200)

        #GET

        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )
