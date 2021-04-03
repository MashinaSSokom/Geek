class InvalidInput(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, capacity):
        self.capacity = capacity
        self.filling = {}

    def get_to_warehouse(self, obj):
        name = obj.name
        description = obj.__dict__
        del description['name']
        if name not in self.filling.keys():
            description['Количество'] = 1
            self.filling[name] = description
        else:
            self.filling[name]["Количество"] += 1

    def transfer(self, name: str, count: int, department: str):
        try:
            if not isinstance(name, str) or not isinstance(count, int) or not isinstance(department, str):
                raise InvalidInput('Неккоректный ввод! Трансфер не произведен.')
            if self.filling[name]['Количество'] >= count:
                self.filling[name]['Количество'] -= count
                if self.filling[name]['Количество'] == 0:
                    del self.filling[name]
                    return print(f'"{name}" в количестве {count} передали в {department}.\n'
                                 f'На складе "{name}" закончились.')
                return print(f'"{name}" в количестве {count} передали в {department}.\n'
                             f'На складе осталось "{name}" {self.filling[name]["Количество"]} штук.')
            return print(f'На складе недостаточно "{name}"')
        except InvalidInput as err:
            return print(err)

    def __str__(self):
        return f"Вместимость склала {self.capacity}\n" \
               f"Загруженность {self.filling if self.filling != {} else 'Склад пуст:('}"


class OfficeEquipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, name: str, price: int, speed: int, type_of_printer: str):
        super().__init__(name, price)
        self.speed = speed
        self.type_of_printer = type_of_printer

    def __str__(self):
        return f"{self.name}; {self.price}; {self.speed}; {self.type_of_printer}."


class Monitor(OfficeEquipment):
    def __init__(self, name: str, price: int, matrix: str, diagonal: float):
        super().__init__(name, price)
        self.matrix = matrix
        self.diagonal = diagonal

    def __str__(self):
        return f"{self.name}; {self.price}; {self.matrix}; {self.diagonal}."


warehouse = Warehouse(56)
print(warehouse)
print()

printer = Printer('Принтер 1', 8200, 25, 'Лазерный')
printer2 = Printer('Принтер 1', 8200, 25, 'Лазерный')
print(printer)
print()

monitor = Monitor('Монитор 1', 11000, 'IPS', 15.6)
print(monitor)
print()

warehouse.get_to_warehouse(printer)
print(warehouse)
print()

warehouse.get_to_warehouse(printer2)
print(warehouse)
print()

warehouse.transfer('Принтер 1', "1", 'Бухгалтерия')
print(warehouse)
