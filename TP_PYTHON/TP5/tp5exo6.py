def calculer_taille_chaine(chaine):
    taille = 0
    for caractere in chaine:
        if caractere == '\0':  
            break
        taille += 1
    return taille

def calculer_pourcentage_voyelles(chaine):
    taille = calculer_taille_chaine(chaine)
    voyelles = "aeiouAEIOU"
    nombre_voyelles = sum(1 for char in chaine if char in voyelles)
    pourcentage_voyelles = (nombre_voyelles / taille) * 100
    return pourcentage_voyelles

def est_sous_chaine(chaine, sous_chaine):
    taille_chaine = calculer_taille_chaine(chaine)
    taille_sous_chaine = calculer_taille_chaine(sous_chaine)

    for i in range(taille_chaine - taille_sous_chaine + 1):
        sous_chaine_test = chaine[i:i + taille_sous_chaine]
        if sous_chaine_test == sous_chaine:
            return True, i

    return False, -1

def compter_occurrences(chaine, sous_chaine):
    taille_chaine = calculer_taille_chaine(chaine)
    taille_sous_chaine = calculer_taille_chaine(sous_chaine)

    occurrences = 0
    for i in range(taille_chaine - taille_sous_chaine + 1):
        sous_chaine_test = chaine[i:i + taille_sous_chaine]
        if sous_chaine_test == sous_chaine:
            occurrences += 1

    return occurrences

chaine = input("Entrez une chaîne de caractères : ")

taille_chaine = calculer_taille_chaine(chaine)
print(f"La taille de la chaîne est : {taille_chaine}")

pourcentage_voyelles = calculer_pourcentage_voyelles(chaine)
print(f"Le pourcentage de voyelles est : {pourcentage_voyelles:.2f}%")

est_present, debut_occurrence = est_sous_chaine(chaine, sous_chaine)
if est_present:
    print(f"'{sous_chaine}' est une sous-chaîne, début de la première occurrence : {debut_occurrence}")

occurrences = compter_occurrences(chaine, sous_chaine)
print(f"Le nombre d'occurrences de '{sous_chaine}' est : {occurrences}")
