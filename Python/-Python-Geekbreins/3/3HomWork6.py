# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

Size = 10
array = [random.randint(-100, 100) for _ in range(Size)]
print(array)

ind_min = 0
ind_max = 0

for i in range(1, Size):
    if array[i] < array[ind_min]:
        ind_min = i
    elif array[i] > array[ind_max]:
        ind_max = i

print(array[ind_min], array[ind_max])

if ind_min > ind_max:
    ind_min, ind_max = ind_max, ind_min

summ = 0

for i in range(ind_min + 1, ind_max):
    summ += array[i]

print(summ)
