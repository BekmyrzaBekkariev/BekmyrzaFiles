# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.


print('Координаты точки А(x1, y1): ')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

print('Координаты точки B(x2, y2): ')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

print('Уравнение прямой, проходящей через эти точки: ')
if x1 == x2:
    print(f'x = {x1:.2f}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k:.2f} * x + {b:.2f}')