"""
Nous réalisons un jeu permettant de trouver un nombre (le prix) 
à l'aide d'une condition dans une boucle.
"""

price = 5345.45

# Utiliser la fonction float pour que le joueur puisse entrer des nombres à décimales
price_player = float(input("Entrer un prix pour trouver le bon : "))

# Utilisation de la boucle while pour faire tourner la condition tant qu'elle n'est pas vérifiée
while price_player != price: 

    if price_player < price : 
        print("C'est plus grand")
    else: 
        print("C'est plus petit")

    price_player = float(input("Entrer un prix pour trouver le bon : "))

# S'affiche une fois sorti de la boucle
print("C'est gagné !")
