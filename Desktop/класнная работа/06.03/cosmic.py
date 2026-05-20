def bellman_ford(n, holes):
    inf = 10**20

    dist = [inf] * n
    dist[0] = 0

    for _ in range(n - 1):
        for x, y, t in holes:
            if dist[x] != inf and dist[x] + t < dist[y]:
                dist[y] = dist[x] + t

    for x, y, t in holes:
        if dist[x] != inf and dist[x] + t < dist[y]:
            return True

    return False


c = int(input())

for _ in range(c):
    n, m = map(int, input().split())

    holes = []

    for _ in range(m):
        x, y, t = map(int, input().split())
        holes.append((x, y, t))

    if bellman_ford(n, holes):
        print("Возможно")
    else:
        print("не возможно")
