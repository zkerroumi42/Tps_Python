op = ""
while op != -1:
    op = input("Est ce que vous voulez Entrer dans le jeux (press yes or no)?")
    if op=="yes":
        print("1:dhs to euro  !")
        print("2:euro to dhs !")
        choix = input("Entrer votre choix ? :")
        monai = int(input("Entrer la somme que vous vouler convertir?:"))

        if choix == "1":
            monaieuro = monai / 10

            print(monai, "MAD =", monaieuro, "EURO")
            print(monaieuro, "EURO =",monai, "MAD")
        elif choix == "2":
            monaimad = monai * 10
            print(monai, "EURO =", monaimad, "MAD")
            print(monaimad, "MAD =", monai, "EURO")
        else:
            print("Entrer soit 1 ou 2 ! ")
    elif op == "no":
        exit()
