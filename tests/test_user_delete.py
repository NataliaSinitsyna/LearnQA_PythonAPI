from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserDelete(BaseCase):
    def test_delete_user_2(self):
        #LOGIN
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        #DELETE
        response2 = MyRequests.delete(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == "Please, do not delete test users with ID 1, 2, 3, 4 or 5.", f"User ID in not equal {user_id_from_auth_method}"

        #GET
        response3 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_json_value_name(
            response3,
            "email",
            "vinkotov@example.com",
            "User with same ID deleted"
        )


    def test_delete_new_user(self):
        #REGISTER
        register_data = self.prepare_registration_data()
        response4 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response4, 200)
        Assertions.assert_json_has_key(response4, "id")
        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response4, "id")

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response5 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response5, "auth_sid")
        token = self.get_header(response5, "x-csrf-token")

        #DELETE
        response6 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response6, 200)

        #GET
        response7 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_code_status(response7, 404)
        assert response7.content.decode("utf-8") == "User not found", f"User ID in not equal {user_id}"


    def test_delete_another_user(self):
        #REGISTER
        register_data = self.prepare_registration_data()
        response8 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response8, 200)
        Assertions.assert_json_has_key(response8, "id")
        email = register_data['email']
        password = register_data['password']

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response9 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response9, "auth_sid")
        token = self.get_header(response9, "x-csrf-token")

        #REGISTER
        register_data = self.prepare_registration_data()
        response10 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response10, 200)
        Assertions.assert_json_has_key(response10, "id")
        another_user_id = self.get_json_value(response10, "id")

        # DELETE
        response11 = MyRequests.delete(
            f"/user/{another_user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response11, 200)

        #GET
        response12 = MyRequests.get(f"/user/{another_user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_code_status(response12, 200)
        assert "username" in response12.json(), f"User ID in not equal {another_user_id}"