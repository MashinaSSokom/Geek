from utils import currency_rates

currencies = ['USD', 'EUR', 'AUD']
for currency in currencies:
    value, date = currency_rates(currency)
    print(f'Текущий курс {currency} в рублях: {value}\n'
          f'Отет был получен: {date}')