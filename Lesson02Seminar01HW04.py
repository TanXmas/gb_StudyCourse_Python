# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)
def get_num():
    print('Введите номер координатной четверти: ', end='')
    try:
        n = int(input())
    except ValueError:
        n = 0
    if 1 <= n <= 4: return n
    return get_num()


n = get_num()
if n == 1:
    print('x > 0, y > 0')
elif n == 2:
    print('x < 0, y > 0')
elif n == 3:
    print('x < 0, y < 0')
else:
    print('x > 0, y < 0')
