from typing import Union

import pandas as pd


def get_transactions_from_csv(path_to_file: str) -> Union[list, str]:
    """ Принимает имя csv файла из директории data и возвращает из него список """

    try:
        transactions_df = pd.read_csv(path_to_file, delimiter=";")
    except pd.errors.EmptyDataError as ex:
        return f'{ex}: Пустой CSV файл'
    except FileNotFoundError as ex:
        return f'{ex}: Файл не найден'

    transactions = []

    try:
        for index, row in transactions_df.iterrows():
            tmp_dict = {"id": row["id"],
                        "state": row["state"],
                        "date": row["date"],
                        "operationAmount": {"amount": str(row["amount"]),
                                            "currency": {"name": row["currency_name"],
                                                         "code": row["currency_code"]}},
                        "description": row["description"],
                        "from": row["from"],
                        "to": row["to"]}
            transactions.append(tmp_dict)
    except KeyError as ex:
        return f'{ex}: Не найден ключ'

    return transactions


def get_transactions_from_xlsx(path_to_file: str) -> Union[list, str]:
    """ Принимает имя xlsx файла из директории data и возвращает из него список """

    try:
        transactions_df = pd.read_excel(path_to_file)
    except FileNotFoundError as ex:
        return f'{ex}: Файл не найден'

    if transactions_df.empty:
        return '[]: Пустой XLSX файл'

    transactions = []

    try:
        for index, row in transactions_df.iterrows():
            tmp_dict = {"id": row["id"],
                        "state": row["state"],
                        "date": row["date"],
                        "operationAmount": {"amount": str(row["amount"]),
                                            "currency": {"name": row["currency_name"],
                                                         "code": row["currency_code"]}},
                        "description": row["description"],
                        "from": row["from"],
                        "to": row["to"]}
            transactions.append(tmp_dict)
    except KeyError as ex:
        return f'{ex}: Не найден ключ'

    return transactions
