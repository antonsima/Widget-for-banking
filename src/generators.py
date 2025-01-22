from typing import Any, Generator

from tests.conftest import test_transactions


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, Any, None]:
    """
    Принимает список словарей и валюту транзакций и возвращает итератор, результат фильтрации
    """


    # filtered_transactions = filter(lambda x: x.get("operationAmount").get("currency").get("code") == currency, transactions)
    if transactions:
        for transaction in transactions:
            get_operation_amount = transaction.get('operationAmount')
            if get_operation_amount is not None:
                get_currency = get_operation_amount.get('currency')
                if get_currency is not None:
                    get_code = get_currency.get('code')
                    if get_code == currency:
                        yield transaction
            continue


def transaction_descriptions(transactions: list[dict]) -> Generator[Any, Any, None]:
    """
    Принимает список словарей транзакций и возвращает итератор с описаниями каждой транзакции
    """
    if transactions:
        for transaction in transactions:
            yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    """
    Генератор номера карт в заданном диапазоне (начало и конец включительно)
    """
    if start >= 0 and stop <= 9999999999999999:
        for number in range(start, stop + 1):
            card_number_gen = '0' * (16 - len(str(number))) + str(number)
            yield f'{card_number_gen[:4]} {card_number_gen[4:8]} {card_number_gen[8:12]} {card_number_gen[12:]}'
