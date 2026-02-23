n = int(input())
start = input().split()
end = input().split()

for i in range(n):
    start[i] = [int(start[i]), int(end[i])]

# сортируем по времени окончания
start.sort(key=lambda x: x[1])

graphs = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if start[j][0] > start[i][1]:
            graphs[i].append(j)

p = [1] * n

for i in range(n):
    for j in graphs[i]:
        p[j] = max(p[j], p[i] + 1)

print(max(p))
