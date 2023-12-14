import random

nombre_mystere = random.randint(0, 100)
compteur = 0

print("Bienvenue dans le jeu de devinette !")
print("Essayez de deviner un nombre entre 0 et 100.")

while True:
    essai = int(input("Votre proposition : "))
    compteur += 1

    if essai < nombre_mystere:
        print("Le nombre mystère est plus grand.")
    elif essai > nombre_mystere:
        print("Le nombre mystère est plus petit.")
    else:
        print("Félicitations ! Vous avez trouvé le nombre mystère en", compteur, "tentatives.")
        break
