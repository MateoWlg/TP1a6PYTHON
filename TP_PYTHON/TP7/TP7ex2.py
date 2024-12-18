import sys
import os

def affiche(dossier):
    try:
        contenu = os.listdir(dossier)
        print(f"Contenu du dossier {dossier} :")
        for elt in contenu:
            print(f"- {elt}")
    except FileNotFoundError:
        print(f"Erreur : Le dossier '{dossier}' n'existe pas.")

def aide():
    print("Usage : python find1.py <chemin_dossier>")
    print("Exemple : python find1.py C:/temp")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Erreur : nombre d'arguments incorrect.")
        aide()
    else:
        dossier = sys.argv[1]
        if os.path.exists(dossier) and os.path.isdir(dossier):
            affiche(dossier)
        else:
            print(f"Erreur : '{dossier}' n'est pas un dossier valide.")
