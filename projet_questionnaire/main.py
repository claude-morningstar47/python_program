# LES COLLECTIONS : PROJET QUESTIONNAIRE
#
# Partez de ce code source pour réaliser la version 2 du projet questionnaire
#
#############################################################################
# FORMATION COMPLÈTE "DÉVELOPPEUR PYTHON"
# 
# Pour progresser en programmation et aller plus loin avec le langage Python,
# découvrez ma formation complète ici : 
# https://codeavecjonathan.com/formations.html
#############################################################################

def poser_question(question, r1, r2, r3, r4, choix_bonne_reponse):
    global score
    print("QUESTION")
    print("  " + question)
    print("  (a)", r1)
    print("  (b)", r2)
    print("  (c)", r3)
    print("  (d)", r4)
    print()
    reponse = input("Votre réponse : ")
    if reponse == choix_bonne_reponse:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
        
    print()


score = 0

poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)
