INF = 10 ** 10
dist = [INF] * n
dist[start] = 0
used = [False] * n
min_dist = 0
min_vertex = start

while min_dist < INF:
    i = min_vertex
    used[i] = True

    for j in range(n):
        new_cost = max(dist[i], w[i][j])
        if dist[j] > new_cost:
            dist[j] = new_cost

    min_dist = INF
    for j in range(n):
        if not used[j] and dist[j] < min_dist:
            min_dist = dist[j]
            min_vertex = j

INF = 10 ** 10
dist = [INF] * n
dist[start] = 1
used = [False] * n
min_dist = 1
min_vertex = start

while min_dist < INF:
    i = min_vertex
    used[i] = True

    for j in range(n):
        new_cost = dist[i] * w[i][j]
        if dist[j] > new_cost:
            dist[j] = new_cost

    min_dist = INF
    for j in range(n):
        if not used[j] and dist[j] < min_dist:
            min_dist = dist[j]
            min_vertex = j

INF = "-" * 1000   # строка больше любой нормальной
dist = [INF] * n
dist[start] = ""
used = [False] * n
min_dist = ""
min_vertex = start

while min_dist != INF:
    i = min_vertex
    used[i] = True

    for j in range(n):
        new_cost = dist[i] + w[i][j]
        if dist[j] > new_cost:
            dist[j] = new_cost

    min_dist = INF
    for j in range(n):
        if not used[j] and dist[j] < min_dist:
            min_dist = dist[j]
            min_vertex = j

INF = -10 ** 10
dist = [INF] * n
dist[start] = 0
used = [False] * n
min_dist = 0
min_vertex = start

while min_dist < INF:
    i = min_vertex
    used[i] = True

    for j in range(n):
        new_cost = min(dist[i], w[i][j])
        if dist[j] < new_cost:
            dist[j] = new_cost

    min_dist = INF
    for j in range(n):
        if not used[j] and dist[j] > min_dist:
            min_dist = dist[j]
            min_vertex = j
