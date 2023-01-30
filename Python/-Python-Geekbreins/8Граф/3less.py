# Кратчайший путь в ширину
#  Сделаем Алгоритм

from collections import deque

g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]


def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])

    while len(deq) > 0:

        curent = deq.pop()

        if curent == finish:
            break

        for i, vertex in enumerate(graph[curent]):
            if vertex == 1 and not is_visited[i]:

                is_visited[i] = True
                parent[i] = curent
                deq.append(i)

    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.append(start)

    return f'Кратчайший путь {list(way)} длиною в {cost} условных единиц'


s = int(input('ОТ какой вершини идти: '))
f = int(input('ДО какой вершини идти: '))
print(bfs(g, s, f))
