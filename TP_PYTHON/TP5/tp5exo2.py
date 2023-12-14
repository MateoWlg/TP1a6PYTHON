def saisie_notes_coefficients():
    notes = []
    coefficients = []

    for i in range(5):
        saisie = input(f"Veuillez entrer la note du module {i + 1} et le coefficient correspondant (séparés par un espace) : ")
        valeurs = saisie.split()
        note = float(valeurs[0])
        coefficient = int(valeurs[1])
        notes.append(note)
        coefficients.append(coefficient)

    return notes, coefficients

def calcul_moyenne_generale(notes, coefficients):
    somme_ponderee = sum(note * coeff for note, coeff in zip(notes, coefficients))
    somme_coefficients = sum(coefficients)
    moyenne_generale = somme_ponderee / somme_coefficients
    return moyenne_generale

def evaluer_admission(moyenne_generale, notes):
    if moyenne_generale > 10 and all(note >= 8 for note in notes):
        return "Admis"
    else:
        return "Non admis"

notes, coefficients = saisie_notes_coefficients()

moyenne_generale = calcul_moyenne_generale(notes, coefficients)

resultat_admission = evaluer_admission(moyenne_generale, notes)

print(f"Moyenne générale : {moyenne_generale:.2f}")
print(f"Résultat de l'admission : {resultat_admission}")