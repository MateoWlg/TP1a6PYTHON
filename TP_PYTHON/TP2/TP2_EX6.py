import random

nombre_aleatoire = random.randint(0, 100)

if nombre_aleatoire < 50:
    resultat = "Pile !"
else:
    resultat = "Face !"

print(resultat)
