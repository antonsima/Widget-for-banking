from functools import wraps
from time import time


def log(filename=''):
    if filename:
        filename = '../logs/' + str(filename)
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                content = \
f'''{func.__name__}
error: тип ошибки {e}
Входные параметры: {args}, {kwargs}'''
                if filename:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(f'{content}')
                else:
                    print(f'{content}')
                return content
            stop = time()
            content = \
f'''{func.__name__}
Время выполнения: {stop - start:6f}
Результат функции: {result}'''
            if filename:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(f'{content}')
            else:
                print(f'{content}')
            return content
        return wrapper
    return decorator


