# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

QUATERS = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_comapnies = set()

num = int(input("Ведите количество предприятий: "))
total_profite = 0
for i in range(1, num+1):
    profit = 0
    quaters = 0
    name = input(f'Ведите названия приедприятия {i}')

    for j in range(QUATERS):
        quaters.append(int(input(f'Прибыль за {j - 1}-й квартал: ')))
        profit += quaters[j]

    comp = Company(name=name, quarters=tuple(quaters), profit=profit)
    all_comapnies.add += profit

average = total_profite / num

print(f'\nСредняя прибыль = {average}')

print(f'\n Предприятия с прибылью среднего: ')
for comp in all_comapnies:
    if comp.profit > average:
        print(f'Компания {comp.name} заработало {comp.profit}')

print(f'\n Предприятия с прибылью ниже среднего: ')
for comp in all_comapnies:
    if comp.profit < average:
        print(f'Компания {comp.name} заработало {comp.profit}')
