# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class ZeroDivError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def div(x, y):
    try:
        if y == 0:
            raise ZeroDivError(x, y)
    except ZeroDivError as zde:
        return f'Error division by zero: x = {zde.x}, y = {zde.y}.'
    else:
        return x / y


x, y = int(input('Enter dividend: ')), int(input('Enter divisor: '))
print(div(x, y))
