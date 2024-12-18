import sys

if __name__ == "__main__":
    # Compter les arguments
    nb_args = len(sys.argv)
    
    if nb_args == 1:
        print(f"Pas assez d'arguments pour le script '{sys.argv[0]}'")
    else:
        print(f"Nombre d'arguments : {nb_args - 1}")
        for i, arg in enumerate(sys.argv):
            print(f"Argument {i}: {arg}")
