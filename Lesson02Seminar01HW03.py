#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
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

x, y = get_point(), get_point(axis='y')

if x > 0 and y > 0:
    print(1)
elif y < 0 < x:
    print(4)
elif x < 0 < y:
    print(2)
else:
    print(3)
