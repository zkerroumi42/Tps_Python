import math
def somme(m, n):
    total = 0
    for i in range(m, n + 1):
        total += i
    return total


def delta(a, b, c):
    return b**2 - 4 * a * c

def NombreRacine(a, b, c):
    D = delta(a, b, c)
    if D > 0:
        return 2
    elif D == 0:
        return 1
    else:
        return 0

def AfficheNombreRacine(a, b, c):
    num_racines = NombreRacine(a, b, c)
    if num_racines == 2:
        print("Il y a deux racines réelles.")
    elif num_racines == 1:
        print("Il y a une racine réelle.")
    else:
        print("Il n'y a pas de racine réelle.")

def Racine1(a, b, c):
    D = delta(a, b, c)
    if D >= 0:
        return (-b + math.sqrt(D)) / (2 * a)
    else:
        return None

def Racine2(a, b, c):
    D = delta(a, b, c)
    if D >= 0:
        return (-b - math.sqrt(D)) / (2 * a)
    else:
        return None

def conversion_temps(h, m, s):
    return h * 3600 + m * 60 + s

def temps_ecoule(h1, m1, s1, h2, m2, s2):
    temps1 = conversion_temps(h1, m1, s1)
    temps2 = conversion_temps(h2, m2, s2)
    return abs(temps2 - temps1)

def conversion_distance(km, m, cm):
    return km * 1000 + m + cm / 100

def vitesse(distance, temps):
    distance_en_metres = conversion_distance(*distance)
    temps_en_secondes = conversion_temps(*temps)
    return distance_en_metres / temps_en_secondes

somme()