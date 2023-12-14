L1 = [0] * 3
print(f"Liste : {L1}, Type : {type(L1)}, Identifiant : {id(L1)}")

for elem in L1:
    print(f"Valeur : {elem}, Type : {type(elem)}, Identifiant : {id(elem)}")

L1[1] += 1
print(f"Liste après modification : {L1}, Type : {type(L1)}, Identifiant : {id(L1)}")

for elem in L1:
    print(f"Valeur : {elem}, Type : {type(elem)}, Identifiant : {id(elem)}")

chaine = "machaine"
print(f"Identifiant de la chaîne : {id(chaine)}")
for char in chaine:
    print(f"Caractère : {char}, Type : {type(char)}, Identifiant : {id(char)}")