def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

lst1 = [0, 1, 2]

lst2 = ajouter_elt(lst1, len(lst1))

print(f"Contenu de lst1 : {lst1}, Type : {type(lst1)}, Identifiant : {id(lst1)}")
print(f"Contenu de lst2 : {lst2}, Type : {type(lst2)}, Identifiant : {id(lst2)}")
