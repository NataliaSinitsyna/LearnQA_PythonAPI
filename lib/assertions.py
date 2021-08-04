from requests import Response
import json

class Assertions:
    @staticmethod #статический метод, так как этот класс не является прямым наследником для наших тестов
    def assert_json_value_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message