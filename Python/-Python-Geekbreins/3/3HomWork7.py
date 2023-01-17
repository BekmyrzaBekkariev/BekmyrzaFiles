# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

Size = 10
array = [random.randint(-100, 100) for _ in range(Size)]
print(array)

if array[0] > array[1]:
    min_idx_1 = 0
    min_idx_2 = 1
else:
    min_idx_1 = 1
    min_idx_2 = 0

for i in range(2, Size):
    if array[i] < array[min_idx_1]:
        spam = min_idx_1
        min_idx_1 = 1

        if array[spam] < array[min_idx_2]:
            min_idx_2 = spam

    elif array[i] < array[min_idx_2]:
        min_idx_2 = i

print(f' Число {array[min_idx_1]} в ячейке {min_idx_1}')
print(f' Число {array[min_idx_2]} в ячейке {min_idx_2}')
