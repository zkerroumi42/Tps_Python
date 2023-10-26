import random

nb_rand = random.randint(1, 100)


nb_essai = 0
cpt = 0

print("******** on va jouer un petit jeux ********")
while nb_essai != 7:
    nombre = int(input("Entrer un nombre entre 1 et 100 :"))
    if 1 <= nombre <= 100:
        if nombre < nb_rand:
            print("Entrer un nombre plus grand")
        elif nombre < nb_rand:
            print("Entrer un nombre plus petit ")
        else:
            print("Félécitation vous avez trouvé le bon nombre .")
            cpt += 1
    else:
        print("vous avez sisaire un nombre en dehors de l'intervalle")

    nb_essai += 1
if cpt >= 4:
    print("j'ai gagné ,je suis le millieur ")
    print("Au revoire")
else:
    print("Au revoire")
