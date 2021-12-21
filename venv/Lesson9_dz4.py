class Car:
    is_police = False

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0

    def go(self, speed=35):
        self.speed = speed
        print(f'Car {self.name} is going. Speed is {self.speed}')

    def stop(self, speed=0):
        self.speed = 0
        print(f' Car {self.name} is stoping. Speed is {self.speed}')

    def turn(self, direction):
        if direction == 'left' or direction == 'right':
            print(f' Car {self.name} turned on {direction}')
        else:
            print(f' Car dont turn')

    def show_speed(self):
        print(f'Car speed is {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed >= 61:
            print(f'Car {self.name} speed is {self.speed}. Overspeed')
        else:
            print(f' Car {self.name} speed is {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 41:
            print(f'Car {self.name} speed is {self.speed}. Overspeed')
        else:
            print(f' Car {self.name} speed is {self.speed}')


class PoliceCar(Car):
    is_police = True


auto_1 = PoliceCar('white', 'BMW')
auto_1.go(20)
auto_2 = SportCar('red', 'Mersedes')
auto_2.go(80)
auto_2.show_speed()
auto_3 = WorkCar('black', 'Nissan')
auto_3.go(60)
auto_3.show_speed()
auto_4 = TownCar('green', 'lexus')
auto_4.go(65)
auto_4.show_speed()
auto_4.stop()
auto_4.show_speed()
