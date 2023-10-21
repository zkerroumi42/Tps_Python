# on 2 methodes de concatenation soit par v+ "" ou avec f" {var} "
age = input("quel est votre age ? ")
taille = input("quelle est votre taille (en mètres) ? ")
message = "Vous avez " + age + " ans et vous mesurez " + taille + " m."
print(f"{message}")