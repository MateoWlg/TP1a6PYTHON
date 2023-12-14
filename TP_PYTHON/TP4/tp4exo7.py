binome = ('login1', 'login2')
print(f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")

nouveau_login = input("Entrez le nouveau login pour le binôme : ")
binome = (binome[0], nouveau_login)
print(f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")

trinome = binome + ('login3',)
print(f"L'étudiant {trinome[0]} est en trinôme avec les étudiants {trinome[1]} et {trinome[2]}")
