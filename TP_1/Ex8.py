note1=float(input("Entrer la 1ere note :"))
q1=int(input("Entrer le coifficiant 1ere note :"))
note2=float(input("Entrer le 2eme note:"))
q2=int(input("Entrer le coifficiant 2ere note :"))
note3=float(input("Entrer la 3eme note:"))
q3=int(input("Entrer le coifficiant 3ere note :"))
note4=float(input("Entrer la 4eme note:"))
q4=int(input("Entrer le coifficiant 4ere note :"))
moyenne=(note1*q1+note2*q2+note3*q3+note4*q4)/float((q1+q2+q3+q4))
print(f"la moyenne est {moyenne}")
if moyenne>10:
  print("semester à été validé")
elif 7<moyenne<10:
    print("Vous avez un rattrapage !")
else:
  print("Semester a été annulé ")


# on peut aussi faire ceci avec les tableau