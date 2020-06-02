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
        result = api_requests.parse_request(request)
        config_data['rates'][pair] = result[0]
        config_data['last_refresh'][pair] = result[1]
        config_data['last_call'][pair] = call_time
        storage.save_conf(config_data)
        return result


def show_currency(config_data):
    currency = get_currency(config_data)
    return f"{storage.get_pair(config_data)}: {currency[0][0:5]}. \
Last update: {currency[1]}"


def convert_currency(config_data, quantity):
    currency, _ = get_currency(config_data)
    currency = float(currency)
    return f"Converting {storage.get_pair(config_data)}:\
 {quantity} -> {str(currency * float(quantity))[0:5]}"
