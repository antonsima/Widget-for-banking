import os
from typing import Any, Union

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')


def get_amount_rub(transaction: dict) -> Union[float, str]:
    """ Принимает транзакцию в виде словаря и возвращает итоговую сумму в рублях """

    currency_code = transaction['operationAmount']['currency']['code']
    amount = transaction['operationAmount']['amount']

    if currency_code == 'RUB':
        return float(amount)
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        payload: dict[str, Any] = {}
        headers = {
            "apikey": api_key
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code

        if status_code == 200:
            return round(float(response.json()['result']), 2)
        else:
            return 'Something went wrong'
