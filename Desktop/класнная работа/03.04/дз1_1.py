from collections import deque


def edmonds_karp(graph, source, sink):
    n = len(graph)
    residual_graph = [row[:] for row in graph]
    max_flow = 0

    while True:
        # Поиск кратчайшего пути с помощью BFS
        parent = [-1] * n
        queue = deque([source])
        parent[source] = source

        while queue:
            u = queue.popleft()
            for v, cap in enumerate(residual_graph[u]):
                if parent[v] == -1 and cap > 0:
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        break
            else:
                continue
            break
        else:
            # Если не дошли до стока, значит путей больше нет
            break

        # Находим "узкое горлышко" в найденном BFS-пути
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        # Обновляем остаточную сеть
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

    return max_flow


network = 1

while True:
    n = int(input())
    if n == 0:
        break

    s, t, c = map(int, input().split())

    graph = [[0] * n for _ in range(n)]

    for _ in range(c):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1

        graph[u][v] += w
        graph[v][u] += w

    result = edmonds_karp(graph, s - 1, t - 1)

    print("Network", network)
    print(f"The bandwidth is {result}.")
    print()

    network += 1
