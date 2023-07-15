import json
import requests
from config import keys

# импорт ключей из конфига


class ExchangeException(Exception):
    pass


class Exchange:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ExchangeException(f'Нельзя перевести одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ExchangeException(f'Не смог обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount
        total_base = round(total_base, 2)
        return total_base

    # внесла некоторые поправки в код, в условие r = quote_ticker и base_ticker поменяла местами,
    # а так же в значение amount = убрала int, заменив на float