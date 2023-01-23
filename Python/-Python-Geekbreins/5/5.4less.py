from collections import OrderedDict

a = {'cat': 5, 'mouse': 4, 'dog': 2}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(new_a)

# СОРТИВРОВКА ПО ЗНАЧЕНИЮ
b = {'cat': 5, 'mouse': 4, 'dog': 2}
new_b = OrderedDict(sorted(a.items(), key=lambda x: x[1]))
print(new_b)

print(new_a == new_b)

# есть last=False тогда в конец не передвинется а в начало
new_b.move_to_end('mouse')
print(new_b)

# есть last=False тогда в конец не удалится а в начало
new_b.popitem()
print(new_b)

new_b['cow'] = 1
print(new_b)

new_b['cow'] = 8
print(new_b)

print('*' * 50)

# Отсортировка по длине ключа
new_c = OrderedDict(sorted(a.items(), key=lambda x: len(x[0])))
print(new_c)

# Вывод элемента в обратном порядке
for key in reversed(new_c):
    print(key, new_c[key])
