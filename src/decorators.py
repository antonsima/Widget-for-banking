import os
from functools import wraps


def log(filename=''):
    if filename:
        PATH_TO_LOGS = os.path.join(os.path.dirname(__file__), "..", "logs", str(filename))

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
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
