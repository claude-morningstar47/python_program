import pygame
import random

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
largeur_fenetre = 640
hauteur_fenetre = 480
taille_case = 20
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu de Tetris")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)
bleu = (0, 0, 255)
vert = (0, 255, 0)
jaune = (255, 255, 0)
cyan = (0, 255, 255)
violet = (255, 0, 255)
couleurs = [rouge, bleu, vert, jaune, cyan, violet]

# Tableau de jeu
tableau_jeu = [[0] * (largeur_fenetre // taille_case)
               for i in range(hauteur_fenetre // taille_case)]

# Pièces de Tetris
pieces = [
    # L
    [
        [1, 0],
        [1, 0],
        [1, 1]
    ],
    # J
    [
        [0, 1],
        [0, 1],
        [1, 1]
    ],
    # Z
    [
        [1, 1, 0],
        [0, 1, 1]
    ],
    # S
    [
        [0, 1, 1],
        [1, 1, 0]
    ],
    # T
    [
        [1, 1, 1],
        [0, 1, 0]
    ],
    # I
    [
        [1],
        [1],
        [1],
        [1]
    ],
    # O
    [
        [1, 1],
        [1, 1]
    ]
]

# Position et couleur de la pièce en cours
position_piece = [0, largeur_fenetre // (2 * taille_case) - 1]
piece = random.choice(pieces)
couleur_piece = random.choice(couleurs)

# Fonction pour dessiner une case


def dessiner_case(x, y, couleur):
    pygame.draw.rect(fenetre, couleur, (x * taille_case, y *
                     taille_case, taille_case, taille_case))

# Fonction pour dessiner le tableau de jeu


def dessiner_tableau_jeu():
    for i in range(len(tableau_jeu)):
        for j in range(len(tableau_jeu[0])):
            if tableau_jeu[i][j] == 0:
                dessiner_case(j, i, blanc)
            else:
                dessiner_case(j, i, couleurs[tableau_jeu[i][j] - 1])

# Fonction pour dessiner la pièce en cours


def dessiner_piece():
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == 1:
                dessiner_case(position_piece[1] + j,
                              position_piece[0] + i, couleur_piece)

# Fonction pour déplacer la pièce à gauche


def deplacer_gauche():
    global position_piece
    position_piece[1] -= 1
    if collision():
        position_piece[1] += 1

# Fonction pour déplacer la pièce à droite


def deplacer_droite():
    global position_piece
    position_piece[1] += 1
    if collision():
        position_piece[1] -= 1

# Fonction pour faire tomber la pièce d'une case


def tomber():
    global position_piece
    position_piece[0] += 1
    if collision():
        position_piece[0] -= 1
        placer_piece()

# Fonction pour faire pivoter la pièce


def pivoter():
    global piece
    piece = [[piece[j][i] for j in range(len(piece))]
             for i in range(len(piece[0]))]
    if collision():
        piece = [[piece[j][i] for j in range(len(piece))]
                 for i in range(len(piece[0]))]

# Fonction pour vérifier si la pièce entre en collision avec une autre pièce ou le bord du tableau


def collision():
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == 1:
                if position_piece[0] + i >= len(tableau_jeu) or position_piece[1] + j < 0 or position_piece[1] + j >= len(tableau_jeu[0]) or tableau_jeu[position_piece[0] + i][position_piece[1] + j] != 0:
                    return True
    return False

# Fonction pour placer la pièce dans le tableau de jeu et en générer une nouvelle


def placer_piece():
    global tableau_jeu, position_piece, piece, couleur_piece
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == 1:
                tableau_jeu[position_piece[0] + i][position_piece[1] +
                                                   j] = couleurs.index(couleur_piece) + 1
                position_piece = [0, largeur_fenetre // (2 * taille_case) - 1]
                piece = random.choice(pieces)
                couleur_piece = random.choice(couleurs)


# Boucle principale du jeu
while True:
    # Gestion des événements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_LEFT:
                deplacer_gauche()
            elif evenement.key == pygame.K_RIGHT:
                deplacer_droite()
            elif evenement.key == pygame.K_DOWN:
                tomber()
            elif evenement.key == pygame.K_SPACE:
                pivoter()

  # Mise à jour du jeu
                tomber()
                # Affichage du jeu
                dessiner_tableau_jeu()
                dessiner_piece()
                pygame.display.update()
                fenetre.fill(noir)
                pygame.time.Clock().tick(5)
