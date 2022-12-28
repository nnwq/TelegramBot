import requests
import json
from APIKEY import APIKey
from config import keys


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if base == quote:
            raise APIException(f'Cannot convert {base} to {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Wrong currency {quote}, please check available /values')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Wrong currency {base}, please check available /values')

        url = requests.get(
            f'https://anyapi.io/api/v1/exchange/convert?apiKey={APIKey}&base={keys[base]}&to={keys[quote]}&amount={amount}')
        response = json.loads(url.content)['converted']

        return response
