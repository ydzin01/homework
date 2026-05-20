z = input()
with open(z, "r", encoding="utf-8") as f:
    con = f.readlines()
n, m = map(int, con[0].split())

g = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, con[i + 1].split())
    g[a].append(b)
    g[b].append(a)

color = [0] * (n + 1)


def dfs(v, c):
    color[v] = c

    for u in g[v]:
        if color[u] == 0:
            if not dfs(u, -c):
                return False
        elif color[u] == color[v]:
            return False

    return True


ok = True

for i in range(1, n + 1):
    if color[i] == 0:
        if not dfs(i, 1):
            ok = False
            break
with open("OUTPUT.txt", "w", encoding="utf-8") as f1:

    if ok:
        f1.write("YES")
    else:
        f1.write("NO")
