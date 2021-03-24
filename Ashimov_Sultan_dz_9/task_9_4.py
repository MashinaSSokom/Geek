class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self. speed = speed
        self. color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f"Скорость сейчас {self.speed} км/ч"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Вы гонщик? Зачем так превышаете по городу?! Скорость сейчас {self.speed} км/ч"
        return f"Скорость сейчас {self.speed} км/ч"


class SportCar(Car):
    def show_speed(self):
        if self.speed < 90:
            return f"А что так медленно? Вы же на спорткаре, значит штрафы Вам не так страшны:3 Скорость сейчас {self.speed} км/ч"
        return f"Скорость сейчас {self.speed} км/ч"


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Вы гонщик? Скорость сейчас {self.speed} км/ч"
        return f"Скорость сейчас {self.speed} км/ч"


class PoliceCar(Car):
    def show_speed(self):
        if self.speed > 120:
            return f"За кем Вы так гонитесь, офицер? Скорость сейчас {self.speed} км/ч"
        return f"Скорость сейчас {self.speed} км/ч"


print(f"Первая машина")
car1 = TownCar(60, "green", "Lada", False)
print(f"Модель: {car1.name}, цвет {car1.color}, Полиция? - {'Да' if car1.is_police == True else 'Нет'}")
print(car1.show_speed())
print()

print(f"Вторая машина")
car2 = SportCar(60, "green", "Lamborghini", False)
print(f"Модель: {car2.name}, цвет {car2.color}, Полиция? - {'Да' if car2.is_police == True else 'Нет'}")
print(car2.show_speed())
print()

print(f"Третья машина")
car3 = WorkCar(55, "green", "The Tractor", False)
print(f"Модель: {car3.name}, цвет {car3.color}, Полиция? - {'Да' if car3.is_police == True else 'Нет'}")
print(car3.show_speed())
print()

print(f"Четвертая машина")
car4 = PoliceCar(90, "blue", "VAZ", True)
print(f"Модель: {car4.name}, цвет {car4.color}, Полиция? - {'Да' if car4.is_police == True else 'Нет'}")
print(car4.show_speed())
print()
