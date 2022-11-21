#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
def get_point(n=0, axis='x'):
    while not n:
        print(f'Введите координату {axis}: ', end='')
        try:
            n = int(input())
            if n != 0:
                return n
            else:
                n = 0
        except ValueError:
            n = 0

x1, y1 = get_point(axis='x1'), get_point(axis='y1')
x2, y2 = get_point(axis='x2'), get_point(axis='y2')
print(f'{((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5:.02f}')
