import json
import logging
import os

logger = logging.getLogger(__name__)
path_to_log = os.path.join(os.path.dirname(__file__), "..", "logs", "utils.log")
file_handler = logging.FileHandler(path_to_log, "w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


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
