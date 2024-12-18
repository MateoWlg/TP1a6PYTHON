import random

def generer(nbr, vmin, vmax):
    return [random.randint(vmin, vmax) for _ in range(nbr)]

def combienInferieur(table, vseuil):
    return sum(1 for val in table if val < vseuil)

def main():
    nb = int(input("Nombre de valeurs à générer : "))

    vmin = int(input("Valeur minimale : "))
    vmax = int(input("Valeur maximale : "))

    reponse = input("Voulez-vous préciser le seuil ? (Oui/Non) ").lower()
    if reponse.startswith('o'):
        seuil = int(input("Seuil : "))
    else:
        seuil = 30  

    tab = generer(nb, vmin, vmax)

    tab.sort()
    print(tab)

    total = combienInferieur(tab, seuil)

    print(f"Il y en a {total} inférieurs à {seuil}")

if __name__ == "__main__":
    main()
