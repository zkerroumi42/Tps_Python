pois=float(input("Sisaire le pois :"))
taille=float(input("Sisaire le La taille :"))

imc=pois/taille

print("Interprétation :")
if imc> 40 :
    print("obésité morbide ou massive")
elif 35<=imc<= 40 :
    print("obésité sévère")
elif 30<=imc<35 :
    print('obésité modérée')
elif 25<=imc<30 :
    print("Surpoids")
elif 18.5<=imc<25 :
    print("corpulence normale")
elif 16.5 <= imc<18.5 :
    print("Maigreur")
else :
    print("Famine")