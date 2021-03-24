import time


class TrafficLight:

    def __init__(self):
        self.__color = "\033[31mred"

    def light_switch(self):
        while True:
            print(self.__color)
            time.sleep(7)
            self.__color = "\033[33myellow"
            print(self.__color)
            time.sleep(3)
            self.__color = "\033[32mgreen"
            print(self.__color)
            time.sleep(5)
            self.__color = "\033[31mred"
        return 1


traffic_light = TrafficLight()
print(traffic_light.light_switch())
