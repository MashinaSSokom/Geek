class Road:

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width
        self._m = 25 # масса на 1 см^3
        self._k = 5 # количество см в слое

    def road_mass(self):
        mass = self._k*self._m*self._width*self._length
        return f"Масса асфальа = {mass} кг ({mass/1000} т)"


road = Road(5, 5)
print(road.road_mass())
