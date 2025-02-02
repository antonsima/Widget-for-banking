import json


def get_transactions_from_json(path_to_file: str) -> list:
    """ Принимает путь до json файла и возвращает из него список """

    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []
    if type(data) != list:
        return []
    else:
        return data
