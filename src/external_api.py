import json
import os

import requests
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('API_KEY')

def get_amount_rub(transaction: dict) -> float:
    """ Принимает транзакцию в виде словаря и возвращает итоговую сумму в рублях """

    currency_code = transaction['operationAmount']['currency']['code']
    amount = transaction['operationAmount']['amount']

    if currency_code == 'RUB':
        return float(amount)
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        payload = {}
        headers = {
            "apikey": api_key
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code

        if status_code == 200:
            result = round(float(dict(json.loads(response.text))['result']), 2)
        else:
            result = 'Something went wrong'

        return result
