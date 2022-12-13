# 1.4 Алгоритм с условиями
# Вычеслить занчение функции y = f(x)
x = int(input("Ведите x: "))
if x > 0:
    y = 2 * x - 10
elif x == 0:
    y = 0
else:
    y = 2 * abs(x) - 1
print(f'y = {y}')
