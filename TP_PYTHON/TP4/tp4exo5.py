def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def verifier_date(date):
    jours = int(date[:2])
    mois = int(date[2:4])
    annee = int(date[4:])

    if len(date) != 8 or mois < 1 or mois > 12 or jours < 1:
        print(f"{date} (incorrecte)")
        return
    
    jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mois > 12 or mois < 1:
        print(f"{date} (incorrecte)")
        return

    if jours > jours_par_mois[mois - 1]:
        print(f"{date} (incorrecte)")
        return

    if mois == 2 and est_bissextile(annee):
        if jours > 29:
            print(f"{date} (incorrecte)")
            return
    elif mois == 2 and jours > 28:
        print(f"{date} (incorrecte)")
        return

    print(f"{date} (correcte)")

date_saisie = input("Entrez la date (jjmmaaaa) : ")
verifier_date(date_saisie)
