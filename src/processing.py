import re
from collections import Counter

import pandas as pd

from src.widget import get_date


def filter_by_state(operation_info: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Возвращает список операций по ключу state
    """

    filtered_by_state = []

    for operation in operation_info:
        if operation.get('state') is not None and pd.isna(operation.get('state')) is not True:
            if operation['state'].lower() == state.lower():
                filtered_by_state.append(operation)

    return filtered_by_state


def sort_by_date(operation_info: list[dict], is_reversed: bool = True) -> list[dict]:
    """
    Возвращает список операций, отсортированный по дате
    """

    for operation in operation_info:
        if (get_date(operation['date']) == 'Введите корректный формат даты'
                or get_date(operation['date']) == 'В дате должны содержаться только цифры'):
            print('Введите корректный формат даты')
            return []

    sorted_by_date = operation_info.copy()
    sorted_by_date.sort(key=lambda x: x['date'], reverse=is_reversed)

    return sorted_by_date


def get_transactions_by_pattern(transactions: list[dict], to_search: str) -> list[dict]:
    """
    Принимает список словарей транзакций и строку поиска,
    возвращает транзакции, в описании которых есть строка поиска
    """

    pattern = re.compile(fr'{to_search.lower()}')
    filtered_transactions = []

    for transaction in transactions:
        description = transaction["description"].lower()

        if pattern.search(description) is not None:
            filtered_transactions.append(transaction)

    return filtered_transactions


def get_category_count(transactions: list[dict], categories: list[str]) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории
    """

    tmp_list = []

    for index, category in enumerate(categories):
        categories[index] = category.lower()

    for transaction in transactions:
        if transaction['description'].lower() in categories:
            tmp_list.append(transaction['description'].capitalize())

    category_count = dict(Counter(tmp_list))

    return category_count
