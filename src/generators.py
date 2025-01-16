from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, Any, None]:
    """
    Принимает список словарей и валюту транзакций и возвращает итератор, результат фильтрации
    """
    return (transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions: list[dict]) -> Generator[Any, Any, None]:
    """
    Принимает список словарей транзакций и возвращает итератор с описаниями каждой транзакции
    """
    return (transaction["description"] for transaction in transactions)


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    """
    Генератор номера карт в заданном диапазоне (начало и конец включительно)
    """
    return ('0' * (16 - len(str(number))) + str(number) for number in range(start, stop + 1))
