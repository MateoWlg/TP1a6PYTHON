etudiant_info = {
    "firstname": "VotrePrénom",
    "name": "VotreNom",
    "promo": "VotrePromo",
    "group": "VotreGroupeTP"
}

print(f"Votre nom est '{etudiant_info['name']}', prénom est '{etudiant_info['firstname']}', vous faites partie de la promo '{etudiant_info['promo']}' et votre groupe est '{etudiant_info['group']}'")

dic = {"name": "toto", "firstname": "titi", "promo": 2022, "group": 202}

print("Les clés du dictionnaire sont :")
for key in dic.keys():
    print(f"-{key}")

print("\nLes valeurs du dictionnaire sont :")
for value in dic.values():
    print(f"-{value}")

print("\nLes tuplets du dictionnaire sont :")
for item in dic.items():
    print(f"-{item}")

autre_etudiant_info = {"name": "tata", "firstname": "tutu", "promo": 2023, "group": 102}

binome = {
    "identifiant_etudiant1": etudiant_info,
    "identifiant_etudiant2": autre_etudiant_info
}

print("\nLes étudiants formant le binôme sont :")
for identifiant, info in binome.items():
    print(f"- L'étudiant {info['name']} {info['firstname']} du groupe {info['group']}")

