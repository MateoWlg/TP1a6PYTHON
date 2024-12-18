def decomposer_somme(somme):
    billet_100 = somme // 100
    reste = somme % 100

    billet_50 = reste // 50
    reste = reste % 50

    billet_10 = reste // 10
    reste = reste % 10

    piece_2 = reste // 2
    reste = reste % 2

    piece_1 = reste

    return billet_100, billet_50, billet_10, piece_2, piece_1

somme_entree = int(input("Veuillez entrer une somme d'argent en euros : "))

billet_100, billet_50, billet_10, piece_2, piece_1 = decomposer_somme(somme_entree)

print(f"{somme_entree} euros, c'est donc {billet_100} billets de 100, {billet_50} de 50, {billet_10} de 10, {piece_2} pièces de 2 et {piece_1} pièce de 1.")
