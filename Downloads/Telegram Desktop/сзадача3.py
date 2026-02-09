b = {'HKG': 'DXB', 'FRA': 'HKG', 'DEL': 'FRA'}
start = None
for a in b:
    if a not in b.values():
        s = a
        break
r = [s]
while s in b:
    s = b[s]
    r.append(s)
print(r)