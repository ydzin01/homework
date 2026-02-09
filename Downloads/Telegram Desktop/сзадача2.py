z = [[0, 1], [1, 2], [2, 3], [3, 6], [7, 1]]
s = input().split()
start = int(s[0])
end = int(s[1])
visited = [False] * (len(z)*2)
prev = [None] * (len(z)*2)
def dfs(start, visited, prev, z):
    visited[start] = True
    if start == end:
        return(True)
    for u in range(len(z)):
        if z[u][0] == start and visited[z[u][1]] is False:
            prev[z[u][1]] = start 
            return(dfs(z[u][1], visited, prev, z))
    if prev[start] != None:
        return(dfs(prev[start], visited, prev, z))
    else:
        return(False)
print(dfs(start, visited, prev, z))