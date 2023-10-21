grad=input("sisaire votre grad(A,B,C,D,E) ? :")
nb_heure=int(input("sisaire le nombre des heures du travial ?:"))


if grad=='A':
   salaire=(200*nb_heure) + (1000*nb_heure/20)
elif grad=='B':
   salaire=(150*nb_heure) + (800*nb_heure/20)
elif grad=='C':
    salaire=(120*nb_heure) + (500*nb_heure/15)
elif grad=='C':
    salaire=(100*nb_heure) + (350*nb_heure/15)
elif grad=='C':
    salaire=(80*nb_heure) + (100*nb_heure/10)

print("Salaire :",salaire)