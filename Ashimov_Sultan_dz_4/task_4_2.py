from requests import get, utils


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
        Value = decoded_response[decoded_response.index(f'CharCode {code}') + 6][6:]
        return float(Value.replace(',','.'))
    else:
        return None


print(currency_rates('USD'))
