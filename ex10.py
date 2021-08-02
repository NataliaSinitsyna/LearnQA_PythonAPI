#Внимание, чтобы pytest не игнорировал команду ввода с клавиатуры, запускать тест нужно с ключиком "-s": python -m pytest -s my_test.py

class TestLengthString:
    def test_length_string(self):
        check_string = input('Введите фразу короче 15 символов \n')
        assert len(check_string) < 15
