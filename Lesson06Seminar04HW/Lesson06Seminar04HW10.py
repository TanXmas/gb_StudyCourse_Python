# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint

n = randint(5, 20)
lst = [randint(0, 10) for _ in range(n)]
print(lst)

#[print(v, end=' ') for v in lst if lst.count(v) == 1]

count_dic = {}
for k in lst:
    count_dic[k] = count_dic.get(k, 0) + 1

[print(k, end=' ') for k, v in count_dic.items() if v == 1]
