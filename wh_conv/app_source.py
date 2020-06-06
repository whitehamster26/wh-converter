from wh_conv import api_requests, storage
from datetime import datetime


def get_currency(config_data):
    call_time = str(datetime.now())[0:13]
    pair = storage.get_pair(config_data)
    if not storage.check_pair(config_data, pair):
        config_data['rates'][pair] = None
        config_data['last_refresh'][pair] = None
        config_data['last_call'][pair] = None
    if storage.get_last_call(config_data, pair) == call_time:
        return storage.get_rates(config_data, pair)
    else:
        request = api_requests.send_request(config_data['from_currency'],
                                            config_data['to_currency'],
                                            config_data['api_key']
                                            )
        rates, last_refresh = api_requests.parse_request(request)
        config_data['rates'][pair] = rates
        config_data['last_refresh'][pair] = last_refresh
        config_data['last_call'][pair] = call_time
        storage.save_conf(config_data)
        return rates, last_refresh


def represent_currency(string):
    integer, modulo = string.split('.')
    return f'{integer}.{modulo[0:2]}'


def show_currency(config_data):
    pair = storage.get_pair(config_data)
    currency, last_update = get_currency(config_data)
    represented_curr = represent_currency(currency)
    return f"{pair}: {represented_curr}. Last update: {last_update}"


def convert_currency(config_data, quantity):
    if not quantity.replace('.', '', 1).isdigit():
        raise Exception('Integer or float number expected')
    pair = storage.get_pair(config_data)
    currency, _ = get_currency(config_data)
    currency = float(currency)
    converted_curr = currency * float(quantity)
    represented_curr = represent_currency(str(converted_curr))
    return f"Converting {pair}: {quantity} -> {represented_curr}"
