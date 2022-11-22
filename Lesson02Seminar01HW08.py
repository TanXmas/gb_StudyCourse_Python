# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
def get_num():
    print(f'Введите целое положительное число: ', end='')
    try:
        n = int(input())
    except ValueError:
        n = 0
    if n > 0: return n
    return get_num()


n = get_num()
print(f'Самая большая цифра в числе {n} = ', end='')
max_num = -1
while n > 0:
    if n % 10 > max_num: max_num = n % 10
    n //= 10
print(max_num)
