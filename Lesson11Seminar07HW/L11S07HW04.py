# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
from random import randint


class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} started moving.')

    def stop(self):
        print(f'{self.color} {self.name} stopped.')

    def turn(self, direction):
        print(f'{self.color} {self.name} turned {direction}.')

    def show_speed(self):
        print(f'{self.color} {self.name} is going at a speed of {self.speed} km/h.')


class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        self.is_police = False

    def show_speed(self):
        if self.speed <= 60:
            print(f'{self.color} {self.name} is going at a speed of {self.speed} km/h.')
        else:
            print(f'{self.color} {self.name} exceeded the speed limit!')


class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        self.is_police = False


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        self.is_police = False

    def show_speed(self):
        if self.speed <= 40:
            print(f'{self.color} {self.name} is going at a speed of {self.speed} km/h.')
        else:
            print(f'{self.color} {self.name} exceeded the speed limit!')


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        self.is_police = True


tc = TownCar('Lada', 'Red', randint(20, 80), False)
sc = SportCar('Audi', 'Blue', randint(40, 150), False)
wc = WorkCar('KAMAZ', 'Green', randint(15, 60), False)
pc = PoliceCar('Kia', 'Grey', randint(30, 160), True)

print(tc.name, tc.color, tc.speed, tc.is_police)
print(sc.name, sc.color, sc.speed, sc.is_police)
print(wc.name, wc.color, wc.speed, wc.is_police)
print(pc.name, pc.color, pc.speed, pc.is_police)
print()

tc.go()
tc.show_speed()

sc.turn('left')
sc.show_speed()

wc.show_speed()
wc.stop()

pc.go()
pc.show_speed()
