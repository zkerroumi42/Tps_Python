L = [1,1,1,1,1,2,5,8,8,8,8,2,2,2,2,9,9,9,9,6,2,5,9,1,8,8,8,8,8,8,8,8,8,8,8]
L.sort()
for i in L:
    if L.count(i)>1:
        L.remove(i)
L.sort()
for i in L:
    if L.count(i)>1:
        L.remove(i)
L.sort()
for i in L:
    if L.count(i)>1:
        L.remove(i)
print(L)