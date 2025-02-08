import pandas as pd


def get_transactions_from_csv(path_to_file: str) -> list:
    """ Принимает имя csv файла из директории data и возвращает из него список """

    try:
        transactions_df = pd.read_csv(path_to_file, delimiter=";")
    except pd.errors.EmptyDataError as ex:
        print(f'{ex}: Пустой CSV файл')
        return []
    except FileNotFoundError as ex:
        print(f'{ex}: Файл не найден')
        return []

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
        print(f'{ex}: Не найден ключ')
        return []

    return transactions


def get_transactions_from_xlsx(path_to_file: str) -> list:
    """ Принимает имя xlsx файла из директории data и возвращает из него список """

    try:
        transactions_df = pd.read_excel(path_to_file)
    except FileNotFoundError as ex:
        print(f'{ex}: Файл не найден')
        return []

    if transactions_df.empty:
        print('[]: Пустой XLSX файл')
        return []

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
        print(f'{ex}: Не найден ключ')
        return []

    return transactions
