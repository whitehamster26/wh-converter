import requests
import json

API_URL = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
API_FUNCTION = "CURRENCY_EXCHANGE_RATE"


def send_request(from_currency, to_currency, api_key):
    params = {'function': API_FUNCTION,
              'from_currency': from_currency,
              'to_currency': to_currency,
              'apikey': api_key}
    try:
        request_object = requests.get(API_URL, params=params)
        return request_object.text
    except Exception:
        raise Exception('Request error occured.')


def parse_request(request_object):
    common_key = 'Realtime Currency Exchange Rate'
    request_data = json.loads(request_object)
    try:
        currency = request_data[common_key]['5. Exchange Rate']
        last_refresh = request_data[common_key]['6. Last Refreshed']
        return currency, last_refresh
    except KeyError:
        raise Exception('API error occured. Check your currency pair.')
