taille = int(input("Entrer la taille du triangle :"))
for i in range(1, taille+1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print("\n")
