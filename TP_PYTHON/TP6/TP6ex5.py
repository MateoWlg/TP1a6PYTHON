import unicodedata

def nettoyer_texte(texte):
    texte_propre = ''.join(c.lower() for c in texte if c.isalnum())

    return texte_propre

def supprimer_accents(texte):
    texte_sans_accents = ''.join(char for char in unicodedata.normalize('NFD', texte) if unicodedata.category(char) != 'Mn')
    
    return texte_sans_accents

def est_palindrome(texte):
    texte_propre = nettoyer_texte(texte)
    return texte_propre == texte_propre[::-1]

def main():
    mot_phrase = input("Veuillez entrer un mot ou une phrase : ")

    mot_phrase_sans_accents = supprimer_accents(mot_phrase)

    if est_palindrome(mot_phrase_sans_accents):
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")

if __name__ == "__main__":
    main()
