import os

from src.utils import get_transactions_from_json

operations_result = [{"id": 441945886,
                      "state": "EXECUTED",
                      "date": "2019-08-26T10:50:58.294041",
                      "operationAmount": {"amount": "31957.58",
                                          "currency": {"name": "руб.",
                                                       "code": "RUB"}},
                      "description": "Перевод организации",
                      "from": "Maestro 1596837868705199",
                      "to": "Счет 64686473678894779589"},
                     {"id": 41428829,
                      "state": "EXECUTED",
                      "date": "2019-07-03T18:35:29.512364",
                      "operationAmount": {"amount": "8221.37",
                                          "currency": {"name": "USD",
                                                       "code": "USD"}},
                      "description": "Перевод организации",
                      "from": "MasterCard 7158300734726758",
                      "to": "Счет 35383033474447895560"}]


def test_get_transactions_from_json():
    path_to_json = os.path.join(os.path.dirname(__file__), "..", "data", "operations_for_test.json")
    wrong_path_to_json = os.path.join(os.path.dirname(__file__), "..", "data", "wrong_path")
    assert get_transactions_from_json(path_to_json) == operations_result
    assert get_transactions_from_json(wrong_path_to_json) == []
