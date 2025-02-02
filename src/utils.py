import json

from src.logger import setup_logging

logger = setup_logging(__file__)


def get_transactions_from_json(path_to_file: str) -> list:
    """ Принимает путь до json файла и возвращает из него список """

    logger.info('Начало работы функции get_transactions_from_json')
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError) as ex:
        logger.error(f'Произошла ошибка: {ex}')
        return []
    if type(data) is not list:
        logger.error("data is not list")
        return []
    else:
        logger.info("Программа завершена успешно")
        return data
