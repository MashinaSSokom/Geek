def get_jokes(count = 1, flag = False):
    from random import choice
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    if not flag:
        for _ in range(count):
            joke = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
            jokes.append(joke)
        return jokes
    else:
        for _ in range(3):
            noun,adverb,adjective = choice(nouns), choice(adverbs), choice(adjectives)
            joke = f'{noun} {adverb} {adjective}'
            jokes.append(joke)
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
        return jokes


print(get_jokes(6))
print(get_jokes(3, True))
