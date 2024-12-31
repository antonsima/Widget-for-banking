from src.widget import get_date


def filter_by_state(operation_info: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Возвращает список операций по ключу state
    """

    filtered_by_state = []

    for operation in operation_info:
        if operation['state'] == state:
            filtered_by_state.append(operation)

    return filtered_by_state


def sort_by_date(operation_info: list[dict], is_reversed: bool = True) -> list[dict]:
    """
    Возвращает список операций, отсортированный по дате
    """

    for operation in operation_info:
        if (get_date(operation['date']) == 'Введите корректный формат даты' or
                get_date(operation['date']) == 'В дате должны содержаться только цифры'):
            return 'Введите корректный формат даты'

    sorted_by_date = operation_info.copy()
    sorted_by_date.sort(key=lambda x: x['date'], reverse=is_reversed)

    return sorted_by_date
