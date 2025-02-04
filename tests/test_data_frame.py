import pandas as pd
import os
from unittest.mock import patch

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
path_to_xlsx = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")

@patch('pandas.read_excel')
def test_get_transactions_from_xlsx(mock_get):
    mock_get.return_value = test_dict
    assert get_transactions_from_xlsx(path_to_xlsx) == test_result
    mock_get.assert_called_once_with(path_to_xlsx)


@patch(f"pandas.read_csv")
def test_get_transactions_from_csv(mock_get):
    mock_get.return_value = test_dict
    assert get_transactions_from_csv(path_to_csv) == test_result
    mock_get.assert_called_once_with(path_to_csv, delimiter=';')