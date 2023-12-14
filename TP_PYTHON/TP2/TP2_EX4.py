
BASE = 4
fromage_base = 800.0
eau_base = 2
ail_base = 2
pain_base = 400


nbConvives = int(input("Entrez le nombre de convives pour la fondue : "))


fromage = fromage_base * nbConvives / BASE
eau = eau_base * nbConvives / BASE
ail = ail_base * nbConvives / BASE
pain = pain_base * nbConvives / BASE


print("Recette pour", nbConvives, "convives :")
print("Fromage (en grammes) :", fromage)
print("Eau (en décilitres) :", eau)
print("Ail (en gousses) :", ail)
print("Pain (en grammes) :", pain)
