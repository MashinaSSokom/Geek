def get_key(d, val):
    for key, value in d.items():
        if val == value:
            return key


with open("nginx_logs.txt", encoding="utf-8") as f:
    result = []
    spamers = {}
    for line in f:
        content = line.replace('"', '').split(' ')
        ip = content[0]
        if ip in spamers:
            spamers[ip] += 1
        else:
            spamers[ip] = 1
        method = content[5]
        url = content[6]
        result.append((ip, method, url))
    max_requests = max(spamers.values())

    print(result)
    print(f'IP спамера: {get_key(spamers, max_requests)}\nКоличество запросов: {max_requests}')

