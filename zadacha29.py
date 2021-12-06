class road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_of_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass

road_1 = road(20, 5000)
print('{0:.0f}'.format(road_1.calculation_of_mass()), 'T')
