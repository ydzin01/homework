with open("INPUT.TXT", "r") as f:
    z = f.readlines()
n = int(z[0])
name = z[1]
cubes = [z[i] for i in range(2, len(z))]


match = [-1] * n


def cube(pos, used):
    for cube_num in range(n):

        if used[cube_num]:
            continue

        if name[pos] not in cubes[cube_num]:
            continue

        used[cube_num] = True

        if match[cube_num] == -1 or cube(match[cube_num], used):
            match[cube_num] = pos
            return True

    return False


possible = True
m = len(name)
for pos in range(m):
    used = [False] * n
    if not cube(pos, used):
        possible = False
        break


with open("OUTPUT.TXT", "w") as f:
    if not possible:
        f.write("NO")
    else:
        answer = [0] * m

        for cube_num in range(n):
            pos = match[cube_num]
            if pos != -1:
                answer[pos] = cube_num + 1

        f.write("YES")
        f.write(" ".join(map(str, answer)))
