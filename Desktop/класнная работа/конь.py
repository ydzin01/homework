x = int(input())
y = int(input())
x_1 = int(input())
y_1 = int(input())

visited = [[x,y]]
used = {(x,y)} 
Qstart = 0

def bfs(visited, Qstart):
    Qstart += 1
    visit = []
    if Qstart > 64*64:
        return False

    for z in visited:
        cx = z[0]
        cy = z[1]

        visit.append([cx-2, cy+1])
        visit.append([cx-2, cy-1])
        visit.append([cx+2, cy+1])
        visit.append([cx+2, cy-1])
        visit.append([cx-1, cy+2])
        visit.append([cx-1, cy-2])
        visit.append([cx+1, cy+2])
        visit.append([cx+1, cy-2])

    new_visit = []

    for i in visit:
        if i[0]>64 or i[0]<1 or i[1]>64 or i[1]<1:
            continue

        if (i[0], i[1]) in used:
            continue

        if i[0] == x_1 and i[1] == y_1:
            return Qstart

        used.add((i[0], i[1]))
        new_visit.append(i)

    return bfs(new_visit, Qstart)

print(bfs(visited,Qstart))
        
    
            

