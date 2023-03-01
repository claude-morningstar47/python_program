# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
noms = []
noms.append(input("nom de la personne 1 : "))
noms.append(input("nom de la personne 2 : "))
noms.append(input("nom de la personne 3 : "))

l = []

for nom in noms:
    l.append(Personne(nom))

for p in l:
    print(p.SePresenter())