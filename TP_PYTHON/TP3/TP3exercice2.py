//Version avec la boucle 'for' et utilisation de time.sleep() :
    import time

n = int(input("Entrez un nombre entier positif : "))

if n < 0:
    print("Veuillez entrer un nombre entier positif.")
else:
    for i in range(n, -1, -1):
        print(i)
        time.sleep(1)  # Pause d'une seconde entre chaque affichage

        

//Version avec la boucle 'while' et utilisation de time.sleep() :
    import time

n = int(input("Entrez un nombre entier positif : "))

if n < 0:
    print("Veuillez entrer un nombre entier positif.")
else:
    while n >= 0:
        print(n)
        n -= 1
        time.sleep(1)  # Pause d'une seconde entre chaque affichage
