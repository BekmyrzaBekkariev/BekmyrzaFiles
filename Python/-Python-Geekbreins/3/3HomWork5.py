# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

Size = 10
array = [random.randint(-100, 100) for _ in range(Size)]
print(array)

# Вариант 1
i = 0
index = -1

while i < Size:
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i

    i += 1

print(f'Число {array[index]} на позиции {index}')

# Вариант 2
num = float('-inf')
index = -1
for i, item in enumerate(array):
    if 0 > item > num:
        num = item
        index = i
print(f'Число {num} на позиции {index}')
