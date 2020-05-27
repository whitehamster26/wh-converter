import requests
import json

API_KEY = "YX6R15ZFYOR4L7OJ"
API_URL = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
API_FUNCTION = "CURRENCY_EXCHANGE_RATE"


def send_request(from_currency, to_currency):
    params = {'function': API_FUNCTION,
              'from_currency': from_currency,
              'to_currency': to_currency,
              'apikey': API_KEY}
    try:
        request_object = requests.get(API_URL, params=params)
        print('request sent!')
        return parse_request(request_object.text)
    except Exception:
        return Exception('Request error occured.')


def parse_request(request_object):
    common_key = 'Realtime Currency Exchange Rate'
    request_data = json.loads(request_object)
    currency = request_data[common_key]['5. Exchange Rate']
    last_refresh = request_data[common_key]['6. Last Refreshed']
    if len(currency) > 0 and len(last_refresh) > 0:
        return currency, last_refresh
    else:
        raise Exception('API error occured')
