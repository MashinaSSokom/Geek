class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"Общий доход {sum(self._income.values())}"


w1 = Position("Иван", "Иванов", "Красава", {"salary": 35000, "bonus": 1})
print(w1.name)
print(w1.surname)
print(w1.position)
print(w1._income)
print(w1.get_full_name())
print(w1.get_total_income())
