t = int(input())

def bfs(g):
    dist = [[-1]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        q = [i]
        dist[i][i] = 0
        for u in q:
            for v in g[u]:
                if dist[i][v] == -1:
                    dist[i][v] = dist[i][u] + 1
                    q.append(v)
    return dist

for _ in range(t):
    n = int(input())
    cnt = [0]*(n+1)

    for _ in range(n):
        cnt[int(input())] += 1

    e = int(input())
    g = [[] for _ in range(n+1)]

    for _ in range(e):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
    dist = bfs(g)
    s = []
    d = []

    for i in range(1, n+1):
        if cnt[i] > 1:
            s += [i]*(cnt[i]-1)
        elif cnt[i] == 0:
            d.append(i)

    used = [0]*len(d)
    ans = 0

    for x in s:
        best = 10**9
        idx = -1
        for i in range(len(d)):
            if not used[i] and dist[x][d[i]] != -1 and dist[x][d[i]] < best:
                best = dist[x][d[i]]
                idx = i
        ans += best
        used[idx] = 1

    print(ans)