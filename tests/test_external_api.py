import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_amount_rub

load_dotenv()
api_key = os.getenv('API_KEY')

test_operation_usd = {"id": 207126257,
                      "state": "EXECUTED",
                      "date": "2019-07-15T11:47:40.496961",
                      "operationAmount": {"amount": "92688.46",
                                          "currency": {"name": "USD",
                                                       "code": "USD"}},
                      "description": "Открытие вклада",
                      "to": "Счет 35737585785074382265"}

test_operation_rub = {"id": 441945886,
                      "state": "EXECUTED",
                      "date": "2019-08-26T10:50:58.294041",
                      "operationAmount": {"amount": "31957.58",
                                          "currency": {"name": "руб.",
                                                       "code": "RUB"}},
                      "description": "Перевод организации",
                      "from": "Maestro 1596837868705199",
                      "to": "Счет 64686473678894779589"}

test_operation_result = {"date": "2025-02-02",
                         "info": {"rate": 98.568878,
                                  "timestamp": 1738438205},
                         "query": {"amount": 92688.46,
                                   "from": "USD",
                                   "to": "RUB"},
                         "result": 9136197.505748,
                         "success": True}

test_url = 'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=92688.46'


@patch('requests.request')
def test_get_amount_usd_to_rub(mock_get):
    mock_get.return_value.json.return_value = test_operation_result
    mock_get.return_value.status_code = 200
    assert get_amount_rub(test_operation_usd) == 9136197.51
    mock_get.assert_called_once_with('GET',
                                     test_url,
                                     headers={'apikey': api_key},
                                     data={})


def test_get_amount_rub_to_rub():
    assert get_amount_rub(test_operation_rub) == 31957.58


@patch('requests.request')
def test_get_amount_error(mock_get):
    mock_get.return_value.json.return_value = test_operation_result
    mock_get.return_value.status_code = 404
    assert get_amount_rub(test_operation_usd) == 'Something went wrong'
    mock_get.assert_called_once_with('GET',
                                     test_url,
                                     headers={'apikey': api_key},
                                     data={})
