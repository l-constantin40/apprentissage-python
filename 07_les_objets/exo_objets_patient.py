"""
Nous réalisons une classe qui permet de créer des patients en
leur attribuant différents types de caractéristiques.
"""


# On définit la classe
class Patient:

    # Le constructeur qui initialise les attributs du patient
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    # On récupère le nom grâce à la méthode get_name
    def get_name(self):
        return self.name


# On définit les variables (objets) par leur "moule"
patient1 = Patient("Jean", 37.2)
patient2 = Patient("Marie", 39.5)

# On affiche les noms dans le message en les récupérant avec le getter
print(f"Admission du patient, {patient1.get_name()}, aux urgences !")
print(f"Admission du patient, {patient2.get_name()}, aux urgences !")
