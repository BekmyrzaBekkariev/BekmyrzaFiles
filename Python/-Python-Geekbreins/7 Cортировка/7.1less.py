# Сортировка Пузырьком
# 1 РАНДОМНЫЕ числа перемешать

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)  # Перемешивает
print(array)

n = 1
while n < len(array):
    for i in range(len(array) - n):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

    n += 1
    print(array)

print(array)
