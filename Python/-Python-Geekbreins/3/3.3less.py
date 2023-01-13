# Задача 1
# Разложить полжительные и отрицательные числа по разным масивам

# Вариант 1 Опытный програмиста код

# Этот код показывает от -100 до 100 в масиве 100 раз рандомными числами
# import random

# array = [random.randint(-100, 100) for _ in range(100)]
# print(array)
# -------------------

# arr_below = []
# arr_lager = []

# for item in array:

#     if item > 0:
#         arr_lager.append(item)

#     elif item < 0:
#         arr_below.append(item)

# print(f' Отрицательные {arr_below}')
# print(f' Положительные {arr_lager}')

# Код не опытного програмиста

# Оличие в том что 1 код пройдет по масиву только 1 раз,
# А 2 код пройдет по отрицательным пото по положительным дважды работы

# arr_below1 = [item for item in array if item < 0]
# arr_lager1 = [item for item in array if item > 0]


# Задача 2
# Вставка элемента в произвольное место

# Вариант 1

import random

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

num = int(input('Ведите число для вставки: '))
pos = int(input('На какую позицию вставить число: '))

# Использование циклла
# array.append(None)
# i = len(array) - 1
# while i > pos:
#     array[i], array[i - 1] = array[i - 1], array[i]
#     i -= 1

# Можно использовать .isert
array.insert(pos, num)

# Можно использовать срезы
array_new = array[:pos] + [num] + array[pos:]


array[pos] = num
print(array)
