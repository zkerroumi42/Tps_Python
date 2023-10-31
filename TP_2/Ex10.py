L1 = [1, 3, 6, 78, 35, 88,88,88, 55, 35]
L2 = [12, 24, 35, 24, 88,88,88, 120, 155, 35]
L3 = []
for i in L1:
    for j in L2:
        if j == i:
            L3.append(j)
            if L3.count(i) > 1:
                    L3.remove(i)

print(L3)
