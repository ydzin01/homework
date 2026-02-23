a = input().split(" ")
n = int(a[0])
m = int(a[1])
s = int(a[2])
f = int(a[3])
w = [[0] * n for i in range(n)]
for i in range(m):
    z = input().split()
    w[int(z[0])][int(z[1])] = int(z[2])
    w[int(z[1])][int(z[0])] = int(z[2])
INF = 10**10
dist = [INF] * n
dist1 = [0] * n
dist[s] = 0
dist1[s] = 0
used = [False] * n
min_dist = 0
min_vertex = s

while min_dist < INF:
    i = min_vertex
    used[i] = True
    for j in range(n):
        new_cost = dist[i] + w[i][j]
        if dist[j] > new_cost:
            dist[j] = new_cost
            dist1[j] += 1

    min_dist = INF
    for j in range(n):
        if not used[j] and dist[j] < min_dist:
            min_dist = dist[j]
            min_vertex = j
print(dist1[f])
