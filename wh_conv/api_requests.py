import requests
import json
from wh_conv.database import push as db_push

API_KEY = "YX6R15ZFYOR4L7OJ"
API_URL = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
API_FUNCTION = "CURRENCY_EXCHANGE_RATE"


def get_currency(from_currency, to_currency):
    params = {'function': API_FUNCTION,
              'from_currency': from_currency,
              'to_currency': to_currency,
              'apikey': API_KEY}
    request_object = requests.get(API_URL, params=params)
    return parse_currency(request_object.text)


def parse_currency(request_object):
    common_key = 'Realtime Currency Exchange Rate'
    request_data = json.loads(request_object)
    currency = request_data[common_key]['5. Exchange Rate']
    last_refresh = request_data[common_key]['6. Last Refreshed']
    return currency, last_refresh
