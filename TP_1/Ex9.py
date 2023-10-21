liste1 = []
liste2 = []
for i in range(1,3):
    nom_article=input(f"donner le nom de l'article {i} :")
    qt_article=int(input(f"donner la quantity de l'article {i} :"))
    MontantHT=float(input(f"donner le prixunitaire de l'article {i} :"))
    MontantTTC=MontantHT*qt_article*1.2
    
    liste1 = liste1 + [MontantTTC]
    liste2 = liste2 + [nom_article]

for i in range(0,2):
  print(f"totale pour l'article {liste2[i]} est :{liste1[i]} ")

  
    
