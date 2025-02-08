import os
import re

from src.data_frame import get_transactions_from_csv, get_transactions_from_xlsx
from src.generators import filter_by_currency
from src.processing import filter_by_state, get_transactions_by_pattern, sort_by_date
from src.utils import get_transactions_from_json
from src.widget import get_date, mask_account_card

PATH_TO_JSON = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
PATH_TO_CSV = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
PATH_TO_XLSX = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")


def main() -> list[dict]:
    """ Основная функция для получения финального списка транзакций """

    main_choice = input('''Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла

Поле ввода: ''')

    while True:
        if main_choice == '1':
            state_input = input('''
Для обработки выбран JSON-файл.
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

Поле ввода: ''').lower()
            transactions = get_transactions_from_json(PATH_TO_JSON)
            break
        elif main_choice == '2':
            state_input = input('''
Для обработки выбран CSV-файл.
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

Поле ввода: ''').lower()
            transactions = get_transactions_from_csv(PATH_TO_CSV)
            break
        elif main_choice == '3':
            state_input = input('''
Для обработки выбран XLSX-файл.
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

Поле ввода: ''').lower()
            transactions = get_transactions_from_xlsx(PATH_TO_XLSX)
            break
        else:
            main_choice = input(f'''
Пункт меню "{main_choice}" недоступен.

Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла

Поле ввода: ''')

    while True:
        if state_input in ['executed', 'canceled', 'pending']:
            transactions = filter_by_state(transactions, state_input)
            print(f'Операции отфильтрованы по статусу "{state_input.upper()}"')
            break
        else:
            state_input = input(f'''
Статус операции "{state_input}" недоступен.

Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

Поле ввода: ''').lower()

    date_sort = input('''
Отсортировать операции по дате? Да/Нет

Поле ввода: ''').lower()

    while True:
        if date_sort == 'да':
            ascending_sort = input('''
Отсортировать по возрастанию или по убыванию?

Поле ввода: ''').lower()
            while True:
                if ascending_sort == 'по возрастанию':
                    transactions = sort_by_date(transactions, False)
                    break
                elif ascending_sort == 'по убыванию':
                    transactions = sort_by_date(transactions, True)
                    break
                else:
                    ascending_sort = input('''
Отсортировать по возрастанию или по убыванию

Поле ввода: ''').lower()
            break
        elif date_sort == 'нет':
            break
        else:
            date_sort = input('''
Отсортировать операции по дате? Да/Нет

Поле ввода: ''').lower()

    rub_sort = input('''
Выводить только рублевые транзакции? Да/Нет

Поле ввода: ''').lower()

    while True:
        if rub_sort == 'да':
            transactions = list(filter_by_currency(transactions, 'RUB'))
            break
        elif rub_sort == 'нет':
            break
        else:
            rub_sort = input('''
Выводить только рублевые транзакции? Да/Нет

Поле ввода: ''').lower()

    pattern_filter = input('''
Отфильтровать список транзакций по определенному слову  в описании? Да/Нет

Поле ввода: ''').lower()

    while True:
        if pattern_filter == 'да':
            pattern = input('''
По какому слову будет происходить фильтрация?

Поле ввода: ''')
            transactions = get_transactions_by_pattern(transactions, pattern)
            break
        elif pattern_filter == 'нет':
            break
        else:
            pattern_filter = input('''
Отфильтровать список транзакций по определенному слову  в описании? Да/Нет

Поле ввода: ''').lower()

    return transactions


def transaction_information(transaction: dict) -> str:
    ''' Принимает словарь транзакции, возвращает информацию о ней в виде строки '''

    transfer_pattern = re.compile(r'перевод')
    opening_pattern = re.compile(r'открытие')

    date = get_date(str(transaction.get("date")))
    description = transaction.get("description")
    requisite_from = mask_account_card(str(transaction.get("from")))
    requisite_to = mask_account_card(str(transaction.get("to")))
    amount = transaction["operationAmount"]['amount']
    currency = transaction["operationAmount"]["currency"]["code"]

    if transfer_pattern.search(transaction["description"].lower()) is not None:
        return f'''
{date} {description}
{requisite_from} -> {requisite_to}
Сумма: {amount} {currency}
'''
    elif opening_pattern.search(transaction["description"].lower()) is not None:
        return f'''
{date} {description}
{requisite_to}
Сумма: {amount} {currency}
'''
    else:
        return f'''
{date} {description}
{requisite_from} -> {requisite_to}
Сумма: {amount} {currency}
'''


if __name__ == '__main__':
    final_transactions = main()

    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке: {len(final_transactions)}')

    for transaction in final_transactions:
        print(transaction_information(transaction))
