n = int(input())
z = set()
x = set()
z1 = []
for i in range(n):
    s = input().split()
    z1.append(s)
    x.add(s[1])
    x.add(s[0])
for _ in range(n):
    for i in range(n):
        s = z1[i]
        if z == set():
            z.add(s[0])
            z.add(s[1])
        if s[0] in z or s[1] in z:
            z.add(s[1])
            z.add(s[0])
    if len(x) == len(z):
        print('True')
        break
if len(x) != len(z):
    print('False')
