from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def get_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def get_consumption(self):
        return 2 * self.height + 0.3


coat = Coat(1)
print(coat.get_consumption)

suit = Suit(1)
print(suit.get_consumption)
