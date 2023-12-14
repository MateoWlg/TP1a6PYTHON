import random

resultat_truque = random.randint(0, 1)

if resultat_truque == 0:
    resultat = "Pile"
else:
    resultat = "Face"

print(resultat)
