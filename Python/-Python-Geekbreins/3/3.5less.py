k = int(input('Ведите количество предприятий: '))
enterprises = {}

for i in range(1, k + 1):
    name = input('Ведите названия предприятия: ')
    enterprises[name] = [float(input('План :')), float(input('Факт: '))]

    enterprises[name].append(enterprises[name][1] / enterprises[name][0])

print('Фактическая прибыль больше 10, но план не выполнен на 100%')
for key, value in enterprises.items():
    if value[1] > 10 and value[2] < 1:
        print(
            f'Предприятия {key} заработало{value[1]}, что составило {value[2] * 100:.2f}% ')
