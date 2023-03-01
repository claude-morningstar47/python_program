# POO EXERCICE DE MISE EN SITUATION 3

# ---
class Chat:
    def __int__(self):
        self.nom = "inconnu"

    def SePresenter(self, nom_facultatif=""):
        self.nom = nom_facultatif
        print("Bonjour, je suis un chat et je m'appelle " + self.nom)

# ---
class Personne:
    def __int__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je suis une personne et je m'appelle " + self.nom)

# ---
chat1 = Chat()
chat1.SePresenter()  # Bonjour, je suis un chat et je m'appelle inconnu

chat2 = Chat("Garfield")
chat2.SePresenter()  # Bonjour, je suis un chat et je m'appelle Garfield

personne = Personne("Jean")
Personne.SePresenter()  # Bonjour, je suis une personne et je m'appelle Jean
