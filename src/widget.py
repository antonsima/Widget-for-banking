import pandas as pd

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_requisites: str) -> str:
    """Возвращает строку с замаскированным номером"""

    if type_and_requisites is not None and pd.isna(type_and_requisites) is not True:
        tmp_list = type_and_requisites.split()
    else:
        return 'Реквизиты не найдены'

    if len(tmp_list) > 1:
        type_ = ' '.join(tmp_list[:-1])
    else:
        return 'Введите корректные данные (кажется, чего-то не хватает)'

    try:
        requisites = int(tmp_list[-1])
    except ValueError:
        return 'Номер счета или карты должен состоять из цифр'

    if type_ == "Счет":
        tmp_list.pop()

        tmp_list.append(get_mask_account(requisites))
    else:
        tmp_list.pop()

        tmp_list.append(get_mask_card_number(requisites))

    masked_account_card = " ".join(tmp_list)

    if '*' not in masked_account_card:
        if type_ == "Счет":
            return 'Номер счета должен содержать больше 7 цифр'
        else:
            return 'Номер карты должен состоять из 16 цифр и более'

    return masked_account_card


def get_date(date_and_time: str) -> str:
    """Возвращает только дату из входных данных"""

    tmp_list = date_and_time.split('-')

    if len(tmp_list) != 3:
        return 'Введите корректный формат даты'
    else:
        year = tmp_list[0]
        month = tmp_list[1]
        day = tmp_list[2][:2]

        if ((len(year) != 4 or len(month) != 2 or len(day) != 2)
                and (month not in range(1, 13) or day not in range(1, 32))):

            return 'Введите корректный формат даты'
        else:
            if not year.isdigit() or not month.isdigit() or not day.isdigit():

                return 'В дате должны содержаться только цифры'
            else:
                date = f'{day}.{month}.{year}'

    return date
