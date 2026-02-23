v, e = [int(x) for x in input().split()]
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
D = [None] * (v)
D[0] = 0
Q = [0]
Qstart = 0
while Qstart < len(Q):
    u = Q[Qstart]
    Qstart += 1
    for v in graph[u]:
        if D[v] is None:
            D[v] = D[u] + 1
            Q.append(v)
for i in D:
    print(i)
