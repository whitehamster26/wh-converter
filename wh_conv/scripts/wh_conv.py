from wh_conv.database import init as db_init
from wh_conv.api_requests import get_currency


def main():
    db_init()
    print(get_currency('USD', 'RUB'))


if __name__ == "__main__":
    main()
