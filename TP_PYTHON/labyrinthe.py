import sys
import random
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QColor, QPen, QBrush
from PyQt5.QtCore import Qt

# Constantes globales
DIM_LABY = 10  # Taille du labyrinthe (10x10)
DIM_FENETRE = 600  # Dimension de la fenêtre
DIM_CASE = DIM_FENETRE // DIM_LABY  # Taille d'une case dans le labyrinthe

# Directions
NORD, EST, SUD, OUEST = "NORD", "EST", "SUD", "OUEST"
MUR_OPPOSE = {NORD: SUD, EST: OUEST, SUD: NORD, OUEST: EST}

def initialise_case(lig, col):
    """
    Initialise une case du labyrinthe.
    Chaque case est un dictionnaire contenant :
    - numero : un identifiant unique basé sur sa ligne et sa colonne
    - murs : un dictionnaire de la forme {"NORD": True, "EST": True, "SUD": True, "OUEST": True}
    - couleur : une couleur aléatoire
    """
    numero = lig * DIM_LABY + col
    couleur = QColor(random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
    return {
        "numero": numero,
        "murs": {NORD: True, EST: True, SUD: True, OUEST: True},
        "couleur": couleur
    }

def initialise_ligne(lig):
    """Initialise une ligne du labyrinthe."""
    return [initialise_case(lig, col) for col in range(DIM_LABY)]

def initialise_laby():
    """Initialise le labyrinthe complet (une liste de listes de cases)."""
    return [initialise_ligne(lig) for lig in range(DIM_LABY)]

def dessine_case(scene, case, x, y):
    """
    Dessine une case individuelle :
    - Un rectangle de la couleur de la case
    - Les murs (si présents)
    - Le numéro de la case
    """
    numero = case["numero"]
    murs = case["murs"]
    couleur = case["couleur"]

    mur_pen = QPen(Qt.black, 2)

    # Dessin de la zone de la case
    brush = QBrush(couleur)
    scene.addRect(x, y, DIM_CASE, DIM_CASE, QPen(Qt.NoPen), brush)

    # Dessin des murs
    if murs[NORD]:
        scene.addLine(x, y, x + DIM_CASE, y, mur_pen)
    if murs[EST]:
        scene.addLine(x + DIM_CASE, y, x + DIM_CASE, y + DIM_CASE, mur_pen)
    if murs[SUD]:
        scene.addLine(x, y + DIM_CASE, x + DIM_CASE, y + DIM_CASE, mur_pen)
    if murs[OUEST]:
        scene.addLine(x, y, x, y + DIM_CASE, mur_pen)

    # Affichage du numéro de la case (facultatif)
    text = scene.addText(str(numero))
    text.setPos(x + DIM_CASE / 3, y + DIM_CASE / 4)
    text.setScale(DIM_CASE / 50)

def dessine_laby(scene, laby):
    """Dessine l'intégralité du labyrinthe."""
    scene.clear()
    for lig, ligne in enumerate(laby):
        for col, case in enumerate(ligne):
            x, y = col * DIM_CASE, lig * DIM_CASE
            dessine_case(scene, case, x, y)

def voisins_non_visites(laby, l, c, visites):
    """
    Retourne la liste des voisins non visités de la case (l,c).
    Un voisin est une case adjacente (NORD, EST, SUD, OUEST) 
    """
    directions = []
    if l > 0 and (l-1, c) not in visites:  # NORD
        directions.append((NORD, (l-1, c)))
    if c < DIM_LABY - 1 and (l, c+1) not in visites:  # EST
        directions.append((EST, (l, c+1)))
    if l < DIM_LABY - 1 and (l+1, c) not in visites:  # SUD
        directions.append((SUD, (l+1, c)))
    if c > 0 and (l, c-1) not in visites:  # OUEST
        directions.append((OUEST, (l, c-1)))
    return directions

def genere_laby_parfait(laby):
    """
    Génère un labyrinthe parfait en utilisant un algorithme de backtracking DFS.
    """
    # Choisir une case de départ au hasard
    start_l = random.randint(0, DIM_LABY - 1)
    start_c = random.randint(0, DIM_LABY - 1)

    stack = [(start_l, start_c)]
    visites = {(start_l, start_c)}

    while stack:
        l, c = stack[-1]  # case courante
        v = voisins_non_visites(laby, l, c, visites)
        
        if v:
            # Choisit un voisin au hasard parmi les non visités
            direction, (ln, cn) = random.choice(v)
            # Enlève les murs entre la case courante et le voisin
            laby[l][c]["murs"][direction] = False
            laby[ln][cn]["murs"][MUR_OPPOSE[direction]] = False
            # Marque le voisin comme visité
            visites.add((ln, cn))
            # Ajoute le voisin à la pile
            stack.append((ln, cn))
        else:
            # Pas de voisins non visités, backtrack
            stack.pop()

def ajoute_entree_sortie(laby):
    """
    Ajoute une entrée et une sortie au labyrinthe parfait.
    On peut par exemple :
    - Ouvrir le mur OUEST de la première colonne pour l'entrée
    - Ouvrir le mur EST de la dernière colonne pour la sortie

    Pour qu'il n'y ait qu'un unique chemin entre ces points, pas d'inquiétude,
    le labyrinthe étant parfait, il n'y aura pas de boucles.
    """
    entree = random.randint(0, DIM_LABY - 1)
    sortie = random.randint(0, DIM_LABY - 1)

    # Ouvrir le mur OUEST de la case d'entrée (première colonne)
    laby[entree][0]["murs"][OUEST] = False
    laby[entree][0]["couleur"] = QColor(255, 0, 0)  # Couleur d'entrée

    # Ouvrir le mur EST de la case de sortie (dernière colonne)
    laby[sortie][DIM_LABY - 1]["murs"][EST] = False
    laby[sortie][DIM_LABY - 1]["couleur"] = QColor(0, 255, 0)  # Couleur de sortie

# Configuration de l'application PyQt5
app = QApplication(sys.argv)
view = QGraphicsView()
scene = QGraphicsScene()
view.setScene(scene)
view.setWindowTitle("Labyrinthe Parfait")
view.setGeometry(100, 100, DIM_FENETRE + 4, DIM_FENETRE + 4)
scene.setBackgroundBrush(QBrush(QColor(200, 200, 200)))
view.show()

# Initialisation du labyrinthe
laby = initialise_laby()

# Génération du labyrinthe parfait
genere_laby_parfait(laby)

# Ajouter l'entrée et la sortie
ajoute_entree_sortie(laby)

# Dessiner le labyrinthe final
dessine_laby(scene, laby)

# Lancer l'application
sys.exit(app.exec_())