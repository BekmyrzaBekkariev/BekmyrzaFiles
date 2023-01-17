# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

Size = 5
# Рандом на 5 чисел на 5 столбоц
matrix = [[random.randint(0, 100) for _ in range(Size)] for _ in range(Size)]
print(matrix)

# Таким кодом можно раставить как матрицу
for line in matrix:
    print(*line, sep='\t')

max_ = matrix[0][0]

for j in range(Size):
    min_ = matrix[0][j]

    for i in range(Size):
        if matrix[i][j] < min_:
            min_ = matrix[i][j]

    if min_ > max_:
        max_ = min_

print(f'Max in min = {min_}')
