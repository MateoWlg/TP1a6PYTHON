import os.path
from datetime import datetime

def afficher_taille_et_date_modification(fichier):
    taille = os.path.getsize(fichier)
    date_modification_timestamp = os.path.getmtime(fichier)
    date_modification = datetime.fromtimestamp(date_modification_timestamp)

    print(f"Le fichier {fichier} a une taille de {taille} octets.")
    print(f"Il a été modifié le {date_modification}.")

fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

if os.path.isfile(fichier1) and os.path.isfile(fichier2):

    afficher_taille_et_date_modification(fichier1)
    afficher_taille_et_date_modification(fichier2)

    date_modification1 = os.path.getmtime(fichier1)
    date_modification2 = os.path.getmtime(fichier2)

    if date_modification1 > date_modification2:
        print(f"Le fichier le plus récent est {fichier1}.")
    elif date_modification1 < date_modification2:
        print(f"Le fichier le plus récent est {fichier2}.")
    else:
        print("Les deux fichiers ont été modifiés en même temps.")
else:
    print("L'un ou les deux fichiers n'existent pas.")
