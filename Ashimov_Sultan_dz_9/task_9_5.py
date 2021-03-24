class Stationery:
    def __init__(self):
        self.title = ""

    def draw(self):
        return f"Запуск отрисовки"


class Pen(Stationery):
    def __init__(self):
        self.title = "Ручка"
    def draw(self):
        return f"{super().draw()} инструментом '{self.title}'"


class Pencil(Stationery):
    def __init__(self):
        self.title = "Карандаш"
    def draw(self):
        return f"{super().draw()} инструментом '{self.title}'"


class Handle(Stationery):
    def __init__(self):
        self.title = "Маркер"
    def draw(self):
        return f"{super().draw()} инструментом '{self.title}'"


pen = Pen()
print(pen.draw())

pencil = Pencil()
print(pencil.draw())

handle = Handle()
print(handle.draw())
