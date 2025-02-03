import logging
import os


def setup_logging(path_to_py: str) -> logging.Logger:
    """ Инициализация логгера, на вход подается путь до файля в котором используется логгер"""
    file_name = os.path.splitext(os.path.basename(path_to_py))[0]
    path_to_log = os.path.join(os.path.dirname(__file__), "..", "logs", f"{file_name}.log")

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s %(levelname)s: %(message)s',
                        filename=path_to_log,  # Запись логов в файл
                        filemode='w',  # Перезапись файла при каждом запуске
                        encoding="utf-8")

    return logging.getLogger()
