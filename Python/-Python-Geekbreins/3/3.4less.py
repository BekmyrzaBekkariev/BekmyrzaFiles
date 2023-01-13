# Матрица ООООО

import random

# 1
matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
print(matrix)

# 2
matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
for line in matrix:
    print(line)

# 3
matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
