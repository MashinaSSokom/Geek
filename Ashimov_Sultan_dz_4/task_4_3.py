from requests import get, utils
from datetime import date

def currency_rates(code=None):
    """Пока не красиво распаршивает response, но работает:)"""
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encoding = utils.get_encoding_from_headers(response.headers)
    decoded_response = response.content.decode(encoding=encoding)
    if code in decoded_response:
        replace_dict = {'<': ' ', '>': ' ', '/': ' '}
        for i, j in replace_dict.items():
            decoded_response = decoded_response.replace(i, j)
        decoded_response = decoded_response.split('  ')
        date_response = decoded_response[1][14:24]
        date_response = date(day=int(date_response[:2]),month=int(date_response[3:5]),year=int(date_response[6:]))
        Value = decoded_response[decoded_response.index(f'CharCode {code}') + 6][6:]
        return float(Value.replace(',', '.')), date_response
    else:
        return None


value, date = currency_rates('USD')
print(f'Текущий курс в рублях: {value}\n'
      f'Отет был получен: {date}')