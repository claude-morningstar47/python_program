# POO EXERCICE DE MISE EN SITUATION 2
# 1 - Résoudre l'erreur
# 2 - votre avis sur le code
class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        if self.EstMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")
        print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25)
personne2 = Personne("Emilie", 17)

personne1.SePresenter()
personne2.SePresenter()