# 1.5 Алгоритм с условиями Часть 2
# Сравнить числа и найти максимум из 3 пересенных
# 1 Ч
a = int(input("Ведите a: "))
b = int(input("Ведите b: "))
c = int(input("Ведите c: "))
m = a
if m < b:
    m = b
if m < c:
    m = c
print(f'Максимум {m}')

# 2 Ч
a = int(input("Ведите a: "))
b = int(input("Ведите b: "))
c = int(input("Ведите c: "))

if a > b:
    if a > c:
        print(f'Максимум = {a}')
    else:
        print(f'Максимум = {c}')
else:
    if b > c:
        print(f'Максимум = {b}')
    else:
        print(f'Максимум = {c}')
