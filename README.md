# Widget for bank  
## Описание
Данный проект - это реализация виджета для банка в рамках домашнего задания от *SkyPro*.
С каждым новым домашним заданием реализуются новые функции для данного виджета, что позволяет закрепить усвоенный теоретический материал.  
  
## Инструкция по установке  
Для того, чтобы проверить код из данного репозитория вам понадобятся **Python**, **Poetry** и **Pycharm**, так что перед началом убедитесь, что они установлены на ваш ПК (проект пишется на версии Python 3.12.7).
Если хотите использовать Python версии ниже, чем 3.12, необходимо отредактировать файл **pyproject.toml**.  
Найдите в нем строчки и вместо **3.12** впишите версию Python, которую хотите использовать:  
```
[tool.poetry.dependencies]  
python = "^3.12"  
```

После чего скачайте все файлы проекта одним архивом:  
```
<> Code -> Download ZIP  
```

Разархивируйте скачанный файл в любое удобное для Вас место.  
Откройте папку проекта **widget_for_bank** с помощью **PyCharm**. 

|24.12.2024|
На данный момент никаких дополнительных зависимостей для работы кода не требуется.
## Инструкция по использованию
|24.12.2024|
В пакете **src** содержится 4 модуля: **main**, **masks**, **processing** и **widget**:
1. *main.py*
В данном модуле в будущем будет написан основной алгоритм работы виджета.
2.  *masks.py*
В данном модуле реализованы функции по маскировке номера счета и номера карты.
```
Функция 
get_mask_card_number
 принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате 
XXXX XX** **** XXXX
, где 
X
 — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами. Пример работы функции:
7000792289606361     # входной аргумент
7000 79** **** 6361  # выход функции
```

```
Функция 
get_mask_account
 принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате 
**XXXX
, где 
X
 — это цифра номера. То есть видны только последние 4 цифры номера, а перед ними — две звездочки. Пример работы функции:
73654108430135874305  # входной аргумент
**4305  # выход функции
```
3.  *processing.py*
В данном модуле реализованы функции по фильтрации и сортировке списков операций.
```
Функция
filter_by_state
принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
state
соответствует указанному значению.

Примеры работы функции
# Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

Пример входных данных для проверки функции
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

```
Функция
sort_by_date
принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Функция возвращает новый список, отсортированный по дате.

Примеры работы функции
# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Пример входных данных для проверки функции
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
4.  *widget.py*
В данном модуле реализованы функция для маскировки реквизитов в зависимости от их типа и функция для конвертации даты в нужный формат.
```
Функция
mask_account_card
обрабатывает информацию как о картах, так и о счетах.
Функция принимает один аргумент — строку, содержащую тип и номер карты или счета.
Аргументом может быть строка типа 
Visa Platinum 7000792289606361
, или 
Maestro 7000792289606361
, или 
Счет 73654108430135874305

Возвращает строку с замаскированным номером.

Примеры работы функции
# Пример для карты
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции

# Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции

Примеры входных данных для проверки функции
Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305
```

```
Функция
get_date
принимает на вход строку с датой в формате
"2024-03-11T02:26:18.671407"
 и возвращает строку с датой в формате
"ДД.ММ.ГГГГ"
("11.03.2024")
```

|31.12.2024|

Существующие функции переписаны по результатам проверок кода.

|23.01.2025|
В пакете **src** добавлен пятый модуль **generators**

5.  *generators.py*
В данном модуле написаны функции-генераторы фильтрации по валюте, вывода описаний транзакций и генерации номеров карт.
```
функция filter_by_currency, которая принимает на вход список словарей, представляющих транзакции.
Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).
```
```
Генератор transaction_descriptions, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
```
```
Генератор card_number_generator, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
```
```
Примеры входных данных для проверки функций filter_by_currency и transaction_descriptions:

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)
```

|26.01.2025|
В пакете **src** добавлен пятый модуль **decorators**

5.  *decorators.py*
В данном модуле написан декоратор log, который автоматически логирует ее результаты или возникшие ошибки.

Декоратор принимает необязательный аргумент **filename**, который определяет, куда будут записываться логи (в файл или в консоль):

- Если **filename** задан, логи записываются в указанный файл.
- Если **filename** не задан, логи выводятся в консоль.

Логирование включает:

- Имя функции и результат выполнения при успешной операции.
- Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.

**Пример использования декоратора:**
~~~
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
~~~
Ожидаемый вывод в лог-файл **mylog.txt**

 при успешном выполнении:

```
my_function  
Результат выполнения функции: 3
```

Ожидаемый вывод при ошибке:

```
my_function  
error: тип ошибки unsupported operand type(s) for +: 'int' and 'str'  
Входные параметры: (1, '2'), {}
```

|02.02.2025|
В пакете **src** добавлены шестой и седьмой модули **external_api** и **utils** соответственно

6.  *external_api.py*
В данном модуле реализована функция, которая принимает на вход транзакцию и возвращает сумму транзакции (**amount**) в рублях, тип данных — **float**. Если транзакция была в **USD** или **EUR**, происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли. Для конвертации валюты используется Exchange Rates Data API: [https://apilayer.com/exchangerates_data-api](https://apilayer.com/marketplace/exchangerates_data-api).
7. *utils.py*
В данном модуле реализована функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список.

Файл с данными о финансовых транзакциях 
```
operations.json
```

находится в директории
```
data/
```

 в корне проекта.

|02.02.2025|
Добавлено логирование в модулях **masks** и **utils**
## Тестирование проекта
Тестирование осуществляется при помощи фреймворка pytest, а также определяется процент покрытия кода с помощью pytest-cov.

Для установки, если используете poetry, пропишите в терминале:
```
poetry add --group dev pytest pytest-cov
```

Если пользуетесь стандартным виртуальным окружением, для установки пропишите:
```
pip install pytest pytest-cov
```

Для запуска тестов, которые написаны в папке tests, пропишите в терминале:
```
pytest
```

Для проверки процента покрытия кода и генерации результатов в отдельный html файл пропишите в терминале следующее:
```
pytest --cov=src --cov-report=html
```

|31.12.2024|

На данный момент все написанные проверки проходят успешно.

Процент покрытия кода составляет **100%**.

|23.01.2025|

На данный момент все написанные проверки проходят успешно.

Процент покрытия кода составляет **100%**.

|26.01.2025|

На данный момент все написанные проверки проходят успешно.

Процент покрытия кода составляет **100%**.

|02.02.2025|

На данный момент все написанные проверки проходят успешно.

Процент покрытия кода составляет **100%**.