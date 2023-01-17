# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

Size = 10
array = [random.randint(-100, 100) for _ in range(Size)]
print(array)

ind_min = 0
ind_max = 0

for i in range(Size):
    if array[i] < array[ind_min]:
        ind_min = i
    elif array[i] > array[ind_max]:
        ind_max = i

print(f'Min = {array[ind_min]} в ячейке {ind_min} '
      f'\nMax = {array[ind_max]} в ячейке {ind_max}')
array[ind_min], array[ind_max] = array[ind_max], array[ind_min]
print(array)

print('=' * 20)

min_num = min(array)
max_nim = max(array)

ind_min = array.index(min_num)
ind_max = array.index(max_nim)

print(f'Min = {array[ind_min]} в ячейке {ind_min} '
      f'\nMax = {array[ind_max]} в ячейке {ind_max}')
array[ind_min], array[ind_max] = array[ind_max], array[ind_min]
print(array)
