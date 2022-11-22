# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
def get_num():
    err = True
    while err:
        print(f'Введите целое положительное число: ', end='')
        try:
            n = int(input())
            if n >= 0: return n
        except ValueError:
            err = True

n = get_num()
print(f'Самая большая цифра в числе {n} = ', end='')
max_num = -1
while n > 0:
    if n % 10 > max_num: max_num = n % 10
    n //= 10
print(max_num)
