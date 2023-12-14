# Demander à l'utilisateur l'heure de début de la location
heure_debut = int(input("Donnez l'heure de début de la location (un entier) : "))

# Demander à l'utilisateur l'heure de fin de la location
heure_fin = int(input("Donnez l'heure de fin de la location (un entier) : "))

# Vérifier la validité des heures fournies
if heure_debut < 0 or heure_fin < 0 or heure_debut > 24 or heure_fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !\n")
elif heure_debut == heure_fin:
    print("Attention ! L'heure de fin est identique à l'heure de début.\n")
elif heure_debut > heure_fin:
    print("Attention ! L'heure de début de la location est après l'heure de fin.\n")
else:
    # Calculer la durée totale de la location
    duree_totale = heure_fin - heure_debut

    # Calculer le coût de la location
    if heure_debut < 7 or (heure_debut >= 17 and heure_fin <= 24):
        tarif = 1.0
    else:
        tarif = 2.0

    montant_total = duree_totale * tarif

    # Afficher le résultat
    print(f"Vous avez loué votre vélo pendant\n{duree_totale} heure(s) au tarif horaire de {tarif} euro(s)")
    print(f"Le montant total à payer est de {montant_total} euro(s).")
  
