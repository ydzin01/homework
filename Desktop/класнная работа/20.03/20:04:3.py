v = list(range(6))


def f(a):
    if not a:
        return 1

    x = a[0]
    res = 0

    for i in range(1, len(a)):
        y = a[i]
        b = a[1:i] + a[i + 1 :]
        res += f(b)

    return res


print(f(v))
