class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def counting_road(self, weigth=25, thickness=5):
        return f'Масса асфальта: {(self._length * self._width * weigth * thickness) / 1000}'


road1 = Road(10000, 50)
print(road1.counting_road())
