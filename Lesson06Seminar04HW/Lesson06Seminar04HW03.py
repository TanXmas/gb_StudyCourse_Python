# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

# в пределах от 20 до 240 - включая границы ???
[print(n, end=' ') for n in range(20, 241) if not n % 20 or not n % 21]
