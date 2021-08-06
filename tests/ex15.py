# В соответствующем классе TestUserRegister, который мы создали на уроке,
# необходимо написать больше тестов на создающий пользователя POST-метод: https://playground.learnqa.ru/api/user/
import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    missing_params = [
        ("email"),
        ("password"),
        ("username"),
        ("firstName"),
        ("lastName")
    ]

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"


# - Создание пользователя с некорректным email - без символа @
    def test_create_user_with_incorrect_email(self):
        email = 'learnqaexample.ru'
        data = self.prepare_registration_data(email)
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format", f"Unexpected response content {response.content}"


# - Создание пользователя без указания одного из полей - с помощью @parametrize необходимо проверить,
    # что отсутствие любого параметра не дает зарегистрировать пользователя
    @pytest.mark.parametrize('condition', missing_params)
    def test_create_user_without_params(self, condition):
        if condition == "email":
            data = self.prepare_registration_data().copy()
            data.pop(condition)
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", f"Unexpected response content {response.content}"

        if condition == "password":
            data = self.prepare_registration_data().copy()
            data.pop(condition)
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", f"Unexpected response content {response.content}"

        if condition == "username":
            data = self.prepare_registration_data().copy()
            data.pop(condition)
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", f"Unexpected response content {response.content}"

        if condition == "firstName":
            data = self.prepare_registration_data().copy()
            data.pop(condition)
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", f"Unexpected response content {response.content}"

        if condition == "lastName":
            data = self.prepare_registration_data().copy()
            data.pop(condition)
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", f"Unexpected response content {response.content}"

# - Создание пользователя с очень коротким именем в один символ
    def test_create_user_with_short_name(self):
        data = self.prepare_registration_data().copy()
        short_value = 'l'
        data.update({'firstName': short_value})
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too short", f"Unexpected response content {response.content}"

# - Создание пользователя с очень длинным именем - длиннее 250 символов
    def test_create_user_with_long_name(self):
        data = self.prepare_registration_data().copy()
        long_value = self.generate_random_string(251)
        print(long_value)
        data.update({'firstName': long_value})
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        print(response.content)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too long", f"Unexpected response content {response.content}"