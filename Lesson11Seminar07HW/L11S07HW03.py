# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
from random import randint

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Employee name is: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Employee salary is: {sum(self._income.values())}')


wage = randint(50, 150)
bonus = randint(wage//4, wage//2)
#print(wage, bonus)

ak = Position('Kevin', 'Brown', 'Agent', wage*1000, bonus*1000)
print(ak.position, ak.name, ak.surname, ak._income)
ak.get_full_name()
ak.get_total_income()
