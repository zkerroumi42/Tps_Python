L = [1, 2, 2, 2, 3, 4, 5, 5]
nb_supp = int(input("Entrer le nombre que vous voullez supprimer :"))
nv_L = []
cpt = L.count(nb_supp)
if cpt == 1:
    print(L)
else:
    for i in range(len(L)):
        if nb_supp == L[i] & cpt > 0:
            L.remove(nb_supp)
            cpt -= 1
            if cpt == 1:
                print(L)
                break
