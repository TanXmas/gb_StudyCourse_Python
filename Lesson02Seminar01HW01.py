# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
def get_num():
    print('Введите номер дня недели: ', end='')
    try:
        n = int(input())
    except ValueError:
        n = 0
    if 1 <= n <= 7: return n
    return get_num()


n = get_num()
if 1 <= n <= 5:
    ans = True
    print('нет')
elif 6 <= n <= 7:
    ans = True
    print('да')
