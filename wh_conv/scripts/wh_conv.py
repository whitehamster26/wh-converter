from wh_conv.app_source import show_currency
from wh_conv.storage import build_conf
import os
import json


def main():
    #  print(get_currency('USD', 'RUB'))
    if not os.path.isfile('wh_conv/config.json'):
        build_conf()
    with open('wh_conv/config.json', 'r') as f:
        data = json.load(f)
    print(show_currency(data))


if __name__ == "__main__":
    main()
