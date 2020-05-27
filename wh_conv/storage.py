import json


def build_conf():
    options = {
        'api_key': 'YX6R15ZFYOR4L7OJ',
        'from_currency': 'USD',
        'to_currency': 'RUB',
        'last_call': {
            'USD-RUB': '2020-05-25 13',
            'RUB-USD': '2020-05-25 13'
        },
        'rates': {
            'USD-RUB': '55',
            'RUB-USD': '22'
        },
        'last_refresh': {
            'USD-RUB': '2020-05-25 13:00:00',
            'RUB-USD': '2020-05-25 13:00:00'
        }
    }
    save_conf(options)


def save_conf(data):
    with open('wh_conv/config.json', 'w') as f:
        json.dump(data, f, indent=4)


def get_apikey(data):
    return data['api_key']


def get_last_call(data, pair):
    return data['last_call'][pair]


def get_rates(data, pair):
    return data['rates'][pair], data['last_refresh'][pair]


def get_pair(data):
    return f"{data['from_currency']}-{data['to_currency']}"
