lst = []

lst.append(1)
lst.extend([2, 3, 4])

print(lst)

lst.insert(1, 5)
print(lst)

last = lst.pop()
print(lst, last)

v = [1, 2, 4, 4, 5, 6, 7, 10]
f = v.pop()
print(f, v)

lst.remove(2)
print(lst)
