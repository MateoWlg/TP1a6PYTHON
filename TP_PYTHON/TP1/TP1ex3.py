jour = int(input("Entrez le jour du mois (0-31) : "))
heure = int(input("Entrez l'heure (0-23) : "))
minute= int(input("Entrez les minutes (0-59) : "))
minutes_ecoulees = (jour -1 ) * 24 * 60 + heure *60 + minute
print ("Depuis le début du mois, il s'est écoulé {} minute.".format(minutes_ecoulees))
