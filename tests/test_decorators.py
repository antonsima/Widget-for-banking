import os

from src.decorators import log


def test_log_console():
    @log()
    def my_function(x: int, y: int) -> int:
        """
        Сложение двух чисел
        """
        return x + y

    result = my_function(1, 6)
    assert result == '''my_function
Результат выполнения функции: 7'''


def test_log_file():
    @log(filename='mylog.txt')
    def my_function(x: int, y: int) -> int:
        """
        Сложение двух чисел
        """
        return x + y

    my_function(1, 6)
    PATH_TO_LOGS = os.path.join(os.path.dirname(__file__), "..", "logs", 'mylog.txt')
    with open(PATH_TO_LOGS, 'r', encoding='utf-8') as file:
        my_log = file.read()
    assert my_log == '''my_function
Результат выполнения функции: 7'''


def test_log_console_error():
    @log()
    def my_function(x: int, y: int) -> int:
        """
        Сложение двух чисел
        """
        return x + y

    result = my_function(1, '6')
    assert result == '''my_function
error: тип ошибки unsupported operand type(s) for +: 'int' and 'str'
Входные параметры: (1, '6'), {}'''


def test_log_file_error():
    @log(filename='mylog.txt')
    def my_function(x: int, y: int) -> int:
        """
        Сложение двух чисел
        """
        return x + y

    my_function(1, '6')
    PATH_TO_LOGS = os.path.join(os.path.dirname(__file__), "..", "logs", 'mylog.txt')
    with open(PATH_TO_LOGS, 'r', encoding='utf-8') as file:
        my_log = file.read()
    assert my_log == '''my_function
error: тип ошибки unsupported operand type(s) for +: 'int' and 'str'
Входные параметры: (1, '6'), {}'''
