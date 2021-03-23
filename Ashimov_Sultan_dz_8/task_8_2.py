import re


def logs_parser(file_name):
    pattern = re.compile(r'(?P<ip>(?:\d{,4}\.){3}\d{,4}) - - '
                         r'(?P<datetime>\[\d{,2}/\w+/\d{4}(?::\d{2}){3}\s\+\d{4}\])\s["]'
                         r'(?P<type>\w+)\s'
                         r'(?P<resource>(?:/\w+){2})\s\w+/\d+\.\d+"\s'
                         r'(?P<code>\d+)\s'
                         r'(?P<size>\d+)\s')
    with open(file_name) as f:
        for line in f:
            try:
                res = re.match(pattern, line)
                print(f'Строка {line}', end = '')
                print(f'parsed row = {res.group("ip")}{res.group("datetime")}{res.group("type")}{res.group("resource")}'
                      f'{res.group("code")}{res.group("size")}')
            except Exception as e:
                print(f'{line} - не смог обработат')
        return 1


file_name = 'nginx_logs.txt'
print(logs_parser(file_name))
