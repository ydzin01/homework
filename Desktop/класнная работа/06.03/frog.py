def floyd(a):
    n = len(a)

    d = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            d[i][j] = a[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                x = max(d[i][k], d[k][j])

                if x < d[i][j]:
                    d[i][j] = x

    return d


n = int(input())

p = []
for _ in range(n):
    x, y = map(int, input().split())
    p.append((x, y))


a = [[0] * n for _ in range(n)]

for i in range(n):
    x1, y1 = p[i]

    for j in range(n):
        x2, y2 = p[j]

        a[i][j] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


d = floyd(a)

print(f"{d[0][1]:.3f}")
