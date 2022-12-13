# 1.6 Алгоритм с условиями Часть 2
num = int(input('Ведите целое число: '))
ans = input('b- в байты  k- килобайты: ')
if ans == 'b':
    print(f'{num} Кб = {num * 1024} байт')
elif ans == 'k':
    print(f'{num} байт = {num / 1024} Кб')
else:
    print('Неверный ввод')
