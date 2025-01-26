import os
from functools import wraps
from typing import Callable

from typing_extensions import ParamSpec, TypeVar

P = ParamSpec('P')
T = TypeVar('T')


def log(filename: str = '') -> Callable[[Callable[P, T]], Callable[P, str]]:
    """
    Декоратор вывода имени функции и ее результата выполнения.
    При ошибке выдает имя функции, тип ошибки и входные параметры функции
    """
    if filename:
        PATH_TO_LOGS = os.path.join(os.path.dirname(__file__), "..", "logs", str(filename))

    def decorator(func: Callable[P, T]) -> Callable[P, str]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> str:
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                content = f'''{func.__name__}
error: тип ошибки {e}
Входные параметры: {args}, {kwargs}'''
                if filename:
                    with open(PATH_TO_LOGS, 'w', encoding='utf-8') as file:
                        file.write(f'{content}')
                return content
            content = f'''{func.__name__}
Результат выполнения функции: {result}'''
            if filename:
                with open(PATH_TO_LOGS, 'w', encoding='utf-8') as file:
                    file.write(f'{content}')
            return content
        return wrapper
    return decorator
