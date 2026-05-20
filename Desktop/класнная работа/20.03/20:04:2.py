with open("INPUT.TXT") as f:
    n = int(f.readline())
    c = [list(map(int, f.readline().split())) for _ in range(n)]

s = 2 * n
t = 2 * n + 1
g = [[] for _ in range(2 * n + 2)]


def add(a, b, cap, cost):
    g[a].append([b, cap, cost, len(g[b])])
    g[b].append([a, 0, -cost, len(g[a]) - 1])


for i in range(n):
    add(s, i, 1, 0)

for i in range(n):
    for j in range(n):
        add(i, n + j, 1, c[i][j])

for j in range(n):
    add(n + j, t, 1, 0)


ans = 0

for _ in range(n):
    d = [10**9] * (2 * n + 2)
    p = [-1] * (2 * n + 2)
    pe = [-1] * (2 * n + 2)
    used = [False] * (2 * n + 2)

    d[s] = 0

    for _ in range(2 * n + 2):
        v = -1

        for i in range(2 * n + 2):
            if not used[i] and (v == -1 or d[i] < d[v]):
                v = i

        used[v] = True

        for i in range(len(g[v])):
            to, cap, cost, rev = g[v][i]

            if cap > 0 and d[v] + cost < d[to]:
                d[to] = d[v] + cost
                p[to] = v
                pe[to] = i

    v = t

    while v != s:
        u = p[v]
        e = pe[v]

        ans += g[u][e][2]

        g[u][e][1] -= 1

        r = g[u][e][3]
        g[v][r][1] += 1

        v = u


with open("OUTPUT.TXT", "w") as f:
    f.write(str(ans))
