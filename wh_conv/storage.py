import json


def build_conf():
    options = {
        'api_key': 'YX6R15ZFYOR4L7OJ',
        'from_currency': 'USD',
        'to_currency': 'EUR',
        'last_call': {
        },
        'rates': {
        },
        'last_refresh': {
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


def check_pair(data, pair):
    return pair in data['rates']


def pair_valid_save(data, pair):
    if (len(pair) != 7) or pair[3] != '-':
        raise Exception('Unexpected format. Please use XXX-YYY format')
    from_curr, to_curr = pair.split('-')
    data['from_currency'] = from_curr.upper()
    data['to_currency'] = to_curr.upper()
    save_conf(data)
    print(
          f'Pair successfully changed to {from_curr.upper()}-{to_curr.upper()}'
        )
