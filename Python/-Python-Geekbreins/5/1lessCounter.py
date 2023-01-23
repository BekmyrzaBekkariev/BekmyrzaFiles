# Counter

from collections import Counter

a = Counter()
b = Counter('ababa')
c = Counter({"red": 2, "blue": 4})
d = Counter(cats=4, dog=5)
print(a, b, c, d, sep="\n")

print(b['z'])
b['z'] = 0
print(b)

print(list(b.elements()))

print(b.most_common(2))

q = Counter(a=4, b=6, c=-2, d=0)
f = Counter(a=1, b=2, c=3, d=-2)
q.subtract(f)
print(q)

print('*' * 50)
print(set(q))
print(dict(q))
q.clear()
print(q)

print('*' * 50)
x = Counter(a=3, b=1)
y = Counter(a=1, b=2)
print(x + y)
print(x - y)
print(x & y)
print(x | y)

print('*' * 50)
z = Counter(a=2, b=-4)
print(+ z)
print(-z)
