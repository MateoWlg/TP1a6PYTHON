import sys
import os

def recherche(dossier, fichier_recherche):
    liste_fichiers = []
    for root, dirs, files in os.walk(dossier):
        for file in files:
            if file == fichier_recherche:
                liste_fichiers.append(os.path.join(root, file))
    return liste_fichiers

def aide():
    print("Usage : python find.py -d <chemin_dossier> -f <nom_fichier>")
    print("Exemple : python find.py -d C:/temp -f toto.txt")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Erreur : nombre d'arguments incorrect.")
        aide()
    else:
        try:
            dossier_idx = sys.argv.index("-d") + 1
            fichier_idx = sys.argv.index("-f") + 1
            dossier = sys.argv[dossier_idx]
            fichier = sys.argv[fichier_idx]
            
            if os.path.exists(dossier) and os.path.isdir(dossier):
                resultats = recherche(dossier, fichier)
                if resultats:
                    print("Fichiers trouvés :")
                    for chemin in resultats:
                        print(f"- {chemin}")
                else:
                    print(f"Aucun fichier nommé '{fichier}' trouvé dans '{dossier}'.")
            else:
                print(f"Erreur : '{dossier}' n'est pas un dossier valide.")
        except (ValueError, IndexError):
            print("Erreur : syntaxe incorrecte.")
            aide()
