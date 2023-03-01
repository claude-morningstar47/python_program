# POO EXERCICE DE MISE EN SITUATION 3

# ---
class Chat:
    def __init__(self, nom_facultatif="inconnu"):
        self.nom = nom_facultatif

    def SePresenter(self):
        print("Bonjour, je suis un chat et je m'appelle " + self.nom)

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je suis une personne et je m'appelle " + self.nom)

# ---
chat1 = Chat()
chat1.SePresenter()    # Bonjour, je suis un chat et je m'appelle inconnu

chat2 = Chat("Garfield")
chat2.SePresenter()    # Bonjour, je suis un chat et je m'appelle Garfield

personne = Personne("Jean")
personne.SePresenter() # Bonjour, je suis une personne et je m'appelle Jean
