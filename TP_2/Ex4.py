L = [1, -30, 0, -2, 500, 4, 2, 100]
nv_L = []
L_temp = []
for i in range(len(L)):
    if L[i] % 2 == 0:
        nv_L.append(L[i])
    else:
        L_temp.append(L[i])
nv_L += L_temp
print(nv_L)
