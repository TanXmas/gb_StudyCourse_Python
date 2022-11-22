# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
def get_point(axis):
    print(f'Введите координату {axis}: ', end='')
    n = input()
    try:
        return int(n)
    except ValueError:
        n = 0
        return n + get_point(axis)

x1, y1 = get_point('x1'), get_point('y1')
x2, y2 = get_point('x2'), get_point('y2')
print(f'{((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5:.02f}')
