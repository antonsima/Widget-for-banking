import os
from unittest.mock import patch

import pandas as pd

from src.data_frame import get_transactions_from_csv, get_transactions_from_xlsx

test_dict = pd.DataFrame({'id': [650703.0],
                          'state': ['EXECUTED'],
                          'date': ['2023-09-05T11:30:32Z'],
                          'amount': [16210.0],
                          'currency_name': ['Sol'],
                          'currency_code': ['PEN'],
                          'from': ['Счет 58803664561298323391'],
                          'to': ['Счет 39745660563456619397'],
                          'description': ['Перевод организации']})

test_result = [{"id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "operationAmount": {"amount": "16210.0",
                                    "currency": {"name": "Sol",
                                                 "code": "PEN"}},
                "description": "Перевод организации",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397"}]

path_to_csv = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
path_to_empty_csv = os.path.join(os.path.dirname(__file__), "empty.csv")
path_to_wrong_csv = os.path.join(os.path.dirname(__file__), "key_not_found.csv")
path_to_xlsx = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")
path_to_empty_xlsx = os.path.join(os.path.dirname(__file__), "empty.xlsx")
path_to_wrong_xlsx = os.path.join(os.path.dirname(__file__), "key_not_found.xlsx")


@patch('pandas.read_excel')
def test_get_transactions_from_xlsx(mock_get):
    mock_get.return_value = test_dict
    assert get_transactions_from_xlsx(path_to_xlsx) == test_result
    mock_get.assert_called_once_with(path_to_xlsx)


@patch("pandas.read_csv")
def test_get_transactions_from_csv(mock_get):
    mock_get.return_value = test_dict
    assert get_transactions_from_csv(path_to_csv) == test_result
    mock_get.assert_called_once_with(path_to_csv, delimiter=';')


def test_get_transactions_from_empty_csv():
    assert get_transactions_from_csv(path_to_empty_csv) == "No columns to parse from file: Пустой CSV файл"


def test_get_transactions_from_empty_xlsx():
    assert get_transactions_from_xlsx(path_to_empty_xlsx) == "[]: Пустой XLSX файл"


def test_get_transactions_from_not_found_csv():
    assert get_transactions_from_csv("test.csv") == "[Errno 2] No such file or directory: 'test.csv': Файл не найден"


def test_get_transactions_from_not_found_xlsx():
    assert (get_transactions_from_xlsx("test.xlsx")
            == "[Errno 2] No such file or directory: 'test.xlsx': Файл не найден")


def test_get_transactions_from_wrong_csv():
    assert get_transactions_from_csv(path_to_wrong_csv) == "'id': Не найден ключ"


def test_get_transactions_from_wrong_xlsx():
    assert get_transactions_from_xlsx(path_to_wrong_xlsx) == "'id': Не найден ключ"
