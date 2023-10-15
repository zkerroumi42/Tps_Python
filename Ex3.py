
d = float(input("Saisissez la distance en kilomètres : "))

temps_minutes = float(input("Saisissez le temps en minutes : "))
temps_secondes = temps_minutes * 60
vitesse = d * 1000 / temps_secondes
# on convert en m la distance en km !

print(f"La vitesse est de {vitesse:.2f} m/s.")
