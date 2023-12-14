def calculer_salaire(nombre_heures, salaire_horaire):
    heures_normales = min(nombre_heures, 160)
    heures_majorees_25 = max(min(nombre_heures - 160, 40), 0)
    heures_majorees_50 = max(nombre_heures - 200, 0)

    salaire_normal = heures_normales * salaire_horaire
    salaire_majore_25 = heures_majorees_25 * (salaire_horaire * 1.25)
    salaire_majore_50 = heures_majorees_50 * (salaire_horaire * 1.5)

    salaire_total = salaire_normal + salaire_majore_25 + salaire_majore_50
    return salaire_total

nombre_heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

salaire_total = calculer_salaire(nombre_heures_travaillees, salaire_horaire)

print(f"Le salaire total est de : {salaire_total:.2f} euros")
