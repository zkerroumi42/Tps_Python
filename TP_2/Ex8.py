L = [1, 1, 1, 1, 1, 2, 5, 8, 8, 8, 8, 2, 2, 2, 2, 9, 6, 2, 5, 9, 1, 8, 8, 8, 8, 8, 8, 8, 8]
nb_cherche = int(input("Entrer le nombre que vous voullez chercher? :"))
cpt = 0
index = []
for i in range(len(L)):
    if L[i] == nb_cherche:
        nb_occ = int(L.count(L[i]))
        index.append(i)

print("le nombre d'occurence du nombre ", nb_cherche, "est :", nb_occ, 'les indexs Sont :', index)
