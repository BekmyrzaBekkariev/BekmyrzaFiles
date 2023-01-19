x1, y1, x2, y2, x3, y3 = map(int, input().split())

steps = max(abs(x1 - x2), abs(x1 - x3), abs(x2 - x3)) + \
    max(abs(y1 - y2), abs(y1 - y3), abs(y2 - y3))

print(steps)
