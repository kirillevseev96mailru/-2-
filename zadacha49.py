class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))

    def show_speed(self):
        print('Current speed:', self.speed)

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 90:
            print('You exceed!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('You exceed!')


class PoliceCar(Car):
    pass

sport_car = SportCar(300, 'Красный', 'Ferrari', False)
town_car = TownCar(120, 'Белая', 'KIA Optima', False)
work_car = WorkCar(70, 'Серый', 'Мусоровоз', False)
police_car = PoliceCar(310, 'Синия', 'Гайцы', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('left')
town_car.turn('left')
work_car.turn('left')
police_car.turn('left')