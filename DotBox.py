edges = [None] * 6 #min:x, y, z, max: x, y, z
sides = 3
i = 0
while s:=input():
    i += 1
    tup = list(map(float, s.split(',')))
    for k in range(sides):
        edges[k] = tup[k] if edges[k] == None \
                   else min(edges[k], tup[k])
    for k in range(3):
        edges[k + 3] = tup[k] if edges[k + sides] == None \
                       else max(edges[k + sides], tup[k])

volume = 1
for k in range(sides):
    volume *= edges[k + sides] - edges[k]
print(volume)
        
