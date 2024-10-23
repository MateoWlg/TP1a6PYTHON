def calcul_factorielle_iterative_for(n):
    factorielle = 1
    print("Calcul de la factorielle de", n, "avec la boucle 'for'")
    for i in range(1, n + 1):
        factorielle *= i
        print(f"Itération {i} : {factorielle}")
    return factorielle

def calcul_factorielle_iterative_while(n):
    factorielle = 1
    i = 1
    print("Calcul de la factorielle de", n, "avec la boucle 'while'")
    while i <= n:
        factorielle *= i
        print(f"Itération {i} : {factorielle}")
        i += 1
    return factorielle


n = int(input("Entrez un entier pour calculer sa factorielle : "))

choix_boucle = input("Choisissez la boucle ('for' ou 'while') : ")

if choix_boucle == 'for':
    resultat = calcul_factorielle_iterative_for(n)
elif choix_boucle == 'while':
    resultat = calcul_factorielle_iterative_while(n)
else:
    print("Choix de boucle invalide. Veuillez entrer 'for' ou 'while'.")

print("La factorielle de", n, "est :", resultat)
