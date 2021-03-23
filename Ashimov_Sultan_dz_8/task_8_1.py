import re
from collections import defaultdict


def email_parse(email_address):
    pattern = re.compile(r"^(\b\w+)@(\w+[.]\w{2,3}\b)", re.ASCII)
    end = []
    for em in email_address:
        #print(em)
        try:
            res = re.search(pattern, em)
            if res:
                end.append({'username' : res.group(1), 'domain' : res.group(2)})
            else:
                raise ValueError(f'wrong email: {em}')
        except Exception as e:
            raise ValueError(f'wrong email: {em}')
    return end


test_data = ["someonge@gekbrains.com", "someone@geekbrains.ru", "someone@gmail.ru", "al1ka01@mail.ru", "skltan@yandex.ru"]
#test_data = "someone@geekbrains.com"
print(email_parse(test_data))
