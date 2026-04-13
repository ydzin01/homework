a = input()
if len(a) >= 4:
    b = a[:4]
    print(set(b.upper()) - set(b))
    if len(set(b.upper()) - set(b)) <= 1:
        print(a.upper(), len(set(b.upper()) - set(b)))
    else:
        print(a)
else:
    print(a)
