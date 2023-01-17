# Обмен значений диогональной квадратной матрицы
#    8   9   1   1  10
#    9   1   7   2   8
#    5   7   2  10  10
#    4   3   1   2   8
#    3   6   7   2   5
# ***********************
#   10   9   1   1   8
#    9   2   7   1   8
#    5   7   2  10  10
#    4   2   1   3   8
#    5   6   7   2   3

import random

size = 5

matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

for i in range(size):
    for j in range(size):
        if i == j:

            spam = matrix[i][j]
            matrix[i][j] = matrix[i][size - 1 - j]
            matrix[i][size - 1 - j] = spam

print('*' * 23)

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
