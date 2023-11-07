import math


def somme(m, n):
    total = 0
    a = max( m, n )
    b = min( m, n )
    for i in range( b, a + 1 ):
        total += i
    return total


print( somme( 10, 20 ) )


def delta(a, b, c):
    deltaa = (b * b) - (a * c)
    return deltaa


def nb_solutions(a, b, c):
    deltmp = delta( a, b, c )
    if deltmp > 0:
        return 2
    elif deltmp < 0:
        return 0
    else:
        return 1


def AfficheNombreRacine(a, b, c):
    nb_racines = nb_solutions( a, b, c )
    if nb_racines == 2:
        print( "Il y a deux racines reelles" )
    elif nb_racines == 1:
        print( "Il y a une racine reelle" )
    else:
        print( "Il n'y a pas de racine" )


def Racine1(a, b, c):
    delt = delta(a, b, c)
    if delt >= 0:
        return (-b + math.sqrt(delt)) / (2 * a)
    else:
        return None


def Racine2(a, b, c):
    delt = delta(a, b, c)
    if delt >= 0:
        return (-b - math.sqrt(delt)) / (2 * a)
    else:
        return None

def conversion_temps(h, m, s):
    return h * 3600 + m * 60 + s

def temps_ecoule(h1, m1, s1, h2, m2, s2):
    temps1 = conversion_temps(h1, m1, s1)
    temps2 = conversion_temps(h2, m2, s2)
    return abs( temps2 - temps1 )

def conversion_distance(km, m, cm):
    return km * 1000 + m + cm / 100

def vitesse(distance, temps):
    distance_metres = conversion_distance(*distance)
    temps_secondes = conversion_temps(*temps)
    return distance_metres / temps_secondes

