def nettoyer_chaine(chaine):
    chaine_epuree = ''.join(c.lower() for c in chaine if c.isalpha())
    return chaine_epuree

def est_palindrome(chaine):
    return chaine == chaine[::-1]

entree_utilisateur = input("Entrez un mot ou une phrase : ")

chaine_epuree = nettoyer_chaine(entree_utilisateur)

if est_palindrome(chaine_epuree):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")