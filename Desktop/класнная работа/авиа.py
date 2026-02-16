a = [[1,2], [2,3], [3,1], [4,1], [4,5], [5,4], [6,5], [6,7]]

b = {}
for r in a:
    if r[0] in b:
        b[r[0]].append(r[1])
    else:
        b[r[0]] = [r[1]]

b1 = {}
for r in a:
    if r[1] in b1:
        b1[r[1]].append(r[0])
    else:
        b1[r[1]] = [r[0]]

finishing_times = []
visited = [False]*10

def dfs(start, visited):
    visited[start] = True
    if start in b:
        for i in b[start]:
            if not visited[i]:
                dfs(i, visited)
    finishing_times.append(start)

def dfs1(start, visited):
    visited[start] = True
    total1.append(start)
    if start in b1:
        for i in b1[start]:
            if not visited[i]:
                dfs1(i, visited)

for i in range(10):
    if not visited[i] and (i in b or i in b1):
        dfs(i, visited)

visited = [False]*10
total = []

for i in reversed(finishing_times):
    if not visited[i]:
        total1 = []
        dfs1(i, visited)
        total1.sort()
        total.append(total1)

total.sort(key=lambda x: -len(x))
print(total)

        

