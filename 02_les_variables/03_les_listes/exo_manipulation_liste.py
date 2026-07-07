# Import de la fonction shuffle du module random
from random import shuffle

# Obtention de la liste saisie par l'utilisateur (découpée par les "/")
mots = input("Entrez des mots sous la forme mot 1/mot 2/mot 3... : ").split("/")

# Mélange aléatoire de la liste
shuffle(mots)

# Condition sur le nombre de mots
if len(mots) < 10:
    # Affiche une sous-liste contenant les 2 premiers éléments
    print(mots[:2])
else:
    # Affiche une sous-liste contenant les 3 derniers éléments
    print(mots[-3:])
    
