from wh_conv.app_source import show_currency, convert_currency
from wh_conv.storage import build_conf, pair_valid_save, save_conf
from wh_conv.storage import PATH as CONFIG_PATH
import os
import json
import argparse

FIRST_RUN_WARNING = """You're using default API key now. You can register \
your own key following this link https://www.alphavantage.co/support/#api-key
If you want to add your API key use wh-conv with argument --apikey [KEY]
"""


parser = argparse.ArgumentParser(description='Currency checker and converter')
parser.add_argument('-p', '--pair', type=str, help='set currency pair in \
    format XXX-YYY')
parser.add_argument('-n', '--num', type=str, help='set output format to \
    numeric')
parser.add_argument('--apikey', type=str, help='set your API key')
parser.add_argument('quantity', nargs='?', default=None)


def catch_exceptions(func):
    def safe_run():
        try:
            func()
        except Exception as e:
            print('Error:', str(e))
    return safe_run


@catch_exceptions
def main():
    args = parser.parse_args()
    if not os.path.isfile(CONFIG_PATH):
        build_conf()
        print(FIRST_RUN_WARNING)
    with open(CONFIG_PATH, 'r') as f:
        data = json.load(f)
    if args.apikey:
        data['api_key'] = args.apikey
        save_conf(data)
        print(f'API key successfully set to {data["api_key"]}')
    elif args.num:
        if args.num not in ('0', '1'):
            raise Exception('Please use 0 or 1 to enable or \
unable numeric output')
        else:
            data['numeric_output'] = int(args.num)
            save_conf(data)
            print('Output format succesfully changed!')
    elif args.pair:
        pair_valid_save(data, args.pair)
        if args.quantity:
            print(convert_currency(data, args.quantity))
        else:
            print(show_currency(data))
    elif args.quantity:
        print(convert_currency(data, args.quantity))
    else:
        print(show_currency(data))


if __name__ == "__main__":
    main()
