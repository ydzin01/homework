V = 5
E = 5
graph_array = {0: [1], 1: [0, 2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}


def is_cyclic(graph_array):
    used = [False] * len(graph_array)
    res = False

    def dfs(v, p=-1):
        used[v] = True
        res = False
        for u in graph_array[v]:
            if not used[u]:
                print(u)
                res = dfs(u, v)
            elif u != p:
                res = True
                break
        return res

    for i in range(len(graph_array)):
        if not used[i]:
            z1 = dfs(i)
            if z1 is True:
                return z1

    return res


res = is_cyclic(graph_array)
if res:
    print("YES")
else:
    print("NO")
