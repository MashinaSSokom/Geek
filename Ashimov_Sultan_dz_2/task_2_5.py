prices = [57.8, 46.51, 97, 34, 23.23, 78, 86.6, 89.23, 45, 211, 254.55]
reformed_prices = ''

for idx, price in enumerate(prices):
    reformed_prices += f'{int(price)} руб {int(price % 1 * 100):0>2} коп'
    if idx != len(prices) - 1:
        reformed_prices += ', '

for idx, price in enumerate(sorted(prices)):
    prices[idx] = f'{int(price)} руб {int(price%1*100):0>2} коп'
reversed_prices = list(reversed(prices))

print('Строка отформатированных цен:', reformed_prices)
print('Сортированный список цен по возрастанию:', prices)
print('Сортированный список цен по убыванию:', reversed_prices)
if len(prices)>5:
    print('Топ 5 самых больших цен из списка:', prices[-5:])
else:
    print('Топ самых больших цен из списка:', prices)
