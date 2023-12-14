def saisie_personne():
    nom = input("Entrez le nom : ")
    prenom = input("Entrez le prénom : ")
    return nom, prenom

def afficher_nom_prenom(nom, prenom):
    nom_majuscules = nom.upper()
    prenom_capitalized = prenom.capitalize()
    
    print(f"{prenom_capitalized} {nom_majuscules}")
nom1, prenom1 = saisie_personne()
nom2, prenom2 = saisie_personne()
if nom1.lower() == nom2.lower():
    if prenom1.lower() < prenom2.lower():
        afficher_nom_prenom(nom1, prenom1)
        afficher_nom_prenom(nom2, prenom2)
    else:
        afficher_nom_prenom(nom2, prenom2)
        afficher_nom_prenom(nom1, prenom1)
else:
    if nom1.lower() < nom2.lower():
        afficher_nom_prenom(nom1, prenom1)
        afficher_nom_prenom(nom2, prenom2)
    else:
        afficher_nom_prenom(nom2, prenom2)
        afficher_nom_prenom(nom1, prenom1)
