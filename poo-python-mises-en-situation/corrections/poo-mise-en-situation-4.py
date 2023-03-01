# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
nombre_de_personnes = 3

liste_personnes = []

for i in range(nombre_de_personnes):
    nom = input("nom de la personne " + str(i+1) + " : ")
    liste_personnes.append(Personne(nom))

for personne in liste_personnes:
    personne.SePresenter()