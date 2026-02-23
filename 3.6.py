v = int(input())
e = int(input())
graph = {}
for i in range(e):
    a, b = [int(x) for x in input().split()]
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]
visited = [False] * v


def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


count = 0
for i1 in graph:
    if not visited[i1]:
        dfs(i1)
        count += 1
print(count)
