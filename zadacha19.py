from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 7))

    def process(self):
        for color, sec in cycle(self.__color):
            print(color, '(wait ', sec, ' sec)')
            sleep(sec)


what_color = TrafficLight()
what_color.process()