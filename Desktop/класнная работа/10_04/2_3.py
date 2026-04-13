def part(a, b):
    return a[1] + a[0] + a[2:] + "-" + b[1] + b[0] + b[2:]


a = input().split()
print(part(a[0], a[1]))
