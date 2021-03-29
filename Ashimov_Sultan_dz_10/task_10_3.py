class Cell:

    def __init__(self, n):
        self.n = n

    def get_size(self):
        return self.n

    def __add__(self, other):
        try:
            sum = self.n + other.get_size()
            return sum
        except TypeError as e:
            raise TypeError("Клетка взаимодействует только с клеткой!")

    def __sub__(self, other):

        try:
            dif = self.n - other.get_size()
            if dif > 0:
                return dif
            raise ValueError("Вы уничтожили клетку!")
        except TypeError as e:
            raise TypeError("Клетка взаимодействует только с клеткой!")

    def __mul__(self, other):
        try:
            multi = self.n * other.get_size()
            if multi > 0:
                return multi
            raise ValueError("Вы уничтожили клетку!")
        except TypeError as e:
            raise TypeError("Клетка взаимодействует только с клеткой!")

    def __floordiv__(self, other):
        try:
            div = self.n // other.get_size()
            if div > 0:
                return div
            raise ValueError("Вы уничтожили клетку!")
        except TypeError as e:
            raise TypeError("Клетка взаимодействует только с клеткой!")

    def make_order(self, num):
        all = self.n
        end = ""
        while all:
            if all >= num:
                end += f"{'*'*num}\n"
                all -= num
            else:
                end += f"{'*'*(all%num)}\n"
                all -= all % num
        return end


cell1 = Cell(10)
cell2 = Cell(3)

print(cell1+cell2)
print(cell1-cell2)
print(cell1*cell2)
print(cell1//cell2)
print(cell1.make_order(4))

