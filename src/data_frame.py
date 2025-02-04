import pandas as pd


def get_transactions_from_csv(path_to_file: str) -> list:
    """ Принимает имя csv файла из директории data и возвращает из него список """

    transactions_df = pd.read_csv(path_to_file, delimiter=";")
    transactions = []

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

    return transactions


def get_transactions_from_xlsx(path_to_file: str) -> list:
    """ Принимает имя xlsx файла из директории data и возвращает из него список """

    transactions_df = pd.read_excel(path_to_file)
    transactions = []

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

    return transactions

