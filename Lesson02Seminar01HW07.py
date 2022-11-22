# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
def get_num():
    print(f'Введите натуральное число: ', end='')
    try:
        n = int(input())
    except ValueError:
        n = 0
    if n > 0: return str(n)
    return get_num()


n = get_num()
print(n, ' + ', n*2, ' + ', n*3, ' = ', int(n) + int(n * 2) + int(n * 3), sep='')
