def main(currency):
    currency = "".join(currency)
    from utils import currency_rates
    value, date = currency_rates(currency)
    print(f'Текущий курс {currency} в рублях: {value}\n'
          f'Отет был получен: {date}')


if __name__ == '__main__':
    import sys
    exit(main(sys.argv[1:]))
