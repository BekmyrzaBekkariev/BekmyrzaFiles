# namedtuple === одращение кортежу по именам

# Создаем игру с помощью кортежа

from collections import namedtuple

hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_1[4])  # Просим покозать значение по индексу

# Чтобы не запоминать индексы можно просто дать всем в котреже класс - класс)


class Person:

    def __init__(self, name, race, health, mana, streinght):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.streinght = streinght


hero_2 = Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_2.mana)

# ====================
# Теперь посмотрим на namedtuple в прошлам на класс ушло гдето 10 строк а тут нудно 3 как ? сейчас покажу

New_Person = namedtuple('New_Person', 'name, race, health, mana, streinght')
hero_3 = New_Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_3.race)

# Если данные в списке то проблем не будет

prop = ['name', 'race', 'health', 'mana', 'strenght']
New_Person_1 = namedtuple('New_Person_1', prop)
hero_4 = New_Person_1('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_4.health)

print('*' * 50)

Point = namedtuple('Point', 'x,y,z')

p1 = Point(2, z=3, y=4)
print(p1)

# Методы с _
t = [5, 10, 15]
p2 = Point._make(t)
print(p2)

d2 = p2._asdict()
print(d2)

p3 = p2._replace(x=6)
print(p3)

print(p3._fields)

# dct = {'x': 10, 'y': 20, 'z': 30}
# p4 = New_Point(**dct)
# print(p4)
