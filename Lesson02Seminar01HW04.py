#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)
ans = False
while not ans:
    print('Введите номер координатной четверти: ', end='')
    try:
        n = int(input())
    except ValueError:
        n = 0
    if n == 1:
        ans = True
        print('x > 0, y > 0')
    elif n == 2:
        ans = True
        print('x < 0, y > 0')
    elif n == 3:
        ans = True
        print('x < 0, y < 0')
    elif n == 4:
        ans = True
        print('x > 0, y < 0')
    else:
        ans = False
