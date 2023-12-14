def table_multiplication():
    nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))
    limite = 9

    resultats = []

    for i in range(limite + 1):
        resultat = round(nombre * i, 1)
        resultats.append((nombre, i, resultat))

    print(f"Table de multiplication de {nombre} jusqu'à {limite}:")
    for (n, i, res) in resultats:
        print(f"{n} * {i} = {res}") 

table_multiplication()
