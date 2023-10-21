nombre1=int(input("Entrer le 1ere nombre:"))
nombre2=int(input("Entrer le deuxieme nommre:"))
op=input("Choisir une operation ? :")

if op=="*":
  print (nombre1 * nombre2)
elif op=="/":
    print (nombre1 / nombre2)
elif op== "+":
      print (nombre1 + nombre2)
elif op=="-":
  print (nombre1 * nombre2)      
else:
  print ("operation non valide")
