nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []

for i in range(nombreEtudiants):
    while True:
        note = float(input(f"Note etudiant {i} : "))
        if 0 <= note <= 20:
            notes.append(note)
            moyenne += note
            break
        else:
            print("Veuillez entrer une note entre 0 et 20.")

moyenne /= nombreEtudiants

print(f"Moyenne de classe : {moyenne:.2f}")

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i, note in enumerate(notes):
    ecart = note - moyenne
    print(f"{i} | {note} | {ecart:.2f}")

