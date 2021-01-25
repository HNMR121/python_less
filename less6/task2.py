class Road:
    def __init__(self, length, width, mass, thickness):
        self._length = length
        self._width = width
        self._mass = mass
        self._thickness = thickness

    def masscalc(self):
        return self._length * self._width * self._mass * self._thickness / 1000


a = Road(20, 5000, 25, 5)
print(a.masscalc())
