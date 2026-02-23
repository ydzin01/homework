import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

n, e, start, end = input().split()
n = int(n)
e = int(e)

z = []
w = [[0] * n for _ in range(n)]
v = []

for i in range(e):
    a, b, l = input().split()
    if a not in v:
        v.append(a)
    if b not in v:
        v.append(b)
    x = v.index(a)
    y = v.index(b)  # было a
    w[x][y] = int(l)
    w[y][x] = int(l)
    G.add_edge(a, b)

s = v.index(start)
INF = 10**10
dist = [INF] * n
dist1 = [""] * n
dist[s] = 0
dist1[s] = v[s]  # было s
used = [False] * n

while True:
    min_dist = INF
    min_vertex = -1
    for j in range(n):
        if not used[j] and dist[j] < min_dist:
            min_dist = dist[j]
            min_vertex = j

    if min_vertex == -1:
        break

    i = min_vertex
    used[i] = True

    for j in range(n):
        if w[i][j] != 0:
            new_cost = dist[i] + w[i][j]
            if dist[j] > new_cost:
                dist[j] = new_cost
                dist1[j] = dist1[i] + " " + v[j]
path = dist1[v.index(end)].split()
for i in range(len(path) - 1):
    G.add_edges_from([(path[i], path[i + 1])])
nx.draw(G, with_labels=True, arrows=True)
plt.savefig("graph.svg")
plt.show()
