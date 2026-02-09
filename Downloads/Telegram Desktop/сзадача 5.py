z = [(0, 1, 3), (0, 4, 1), (1, 2, 1), (1, 3, 3), (1, 4, 1), (4, 2, 2), (4, 3, 1)]
s = input().split()
start = int(s[0])
end = int(s[1])
visited = [False] * (len(z)*2)
lengths = []
def dfs(v, cost):
    if v == end:
        lengths.append(cost)
        return
    visited[v] = True
    for u in range(len(z)):
        if z[u][0] == v and not visited[z[u][1]]:
            dfs(z[u][1], cost + z[u][2])
    visited[v] = False
dfs(start, 0)
if lengths:
    print(min(lengths))
else:
    print("Нет пути")