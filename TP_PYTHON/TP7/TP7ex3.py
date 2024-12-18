import sys
import os

def recherche(dossier):
    liste_fichiers = []
    liste_dossiers = []
    
    for root, dirs, files in os.walk(dossier):
        for file in files:
            liste_fichiers.append(os.path.join(root, file))
        for dir in dirs:
            liste_dossiers.append(os.path.join(root, dir))
    
    return liste_fichiers, liste_dossiers

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python find2.py <chemin_dossier>")
    else:
        dossier = sys.argv[1]
        if os.path.exists(dossier) and os.path.isdir(dossier):
            fichiers, dossiers = recherche(dossier)
            print("Fichiers trouvés :")
            for fichier in fichiers:
                print(f"- {fichier}")
            print("\nDossiers trouvés :")
            for dossier in dossiers:
                print(f"- {dossier}")
        else:
            print(f"Erreur : '{dossier}' n'est pas un dossier valide.")
