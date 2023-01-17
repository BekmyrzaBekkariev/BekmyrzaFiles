# 4. Определить, какое число в массиве встречается чаще всего.
import random

Size = 10
array = [random.randint(0, Size // 1) for _ in range(Size)]
print(array)

num = array[0]
max_frq = 1

for i in range(Size - 1):
    frq = 1

    for k in range(i + 1, Size):
        if array[i] == array[k]:
            frq += 1

    if frq > max_frq:
        max_frq = frq
        num = array[i]

if max_frq > 1:
    print(f'Число {num} встречается {max_frq} раз')
else:
    print('Все элементы уникальны')


# Вариант 2

diction = {}
for item in array:
    if item in diction.keys():
        diction[item] += 1
    else:
        diction[item] = 1

print(diction)
