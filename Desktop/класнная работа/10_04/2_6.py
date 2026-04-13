s = input()
l = len(s)
if l <= 2:
    print(ord(s[0]))
elif l < 10:
    mid = l // 2 - 1 if l % 2 == 0 else l // 2
    print(ord(s[0]) + ord(s[mid]) + ord(s[-1]))
else:
    print(ord(s[-1]))
