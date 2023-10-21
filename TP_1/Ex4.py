nombre=int(input("donner un nombre en seconde"))

nb_heure=nombre // 360 
rest1=nombre-nb_heure*360
nb_minutes=rest1 // 60
rest2=rest1-nb_minutes*60
nb_seconde=rest2
print (str(nb_heure) + ":"+ str(nb_minutes)+ ":"+ str(nb_seconde))