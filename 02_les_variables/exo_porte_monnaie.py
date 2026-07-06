# Récupération du montant initial dans le porte-monnaie de l'utilisateur
wallet_person = float(input("Quelle somme contient votre porte-monnaie ? : "))

# Définition du prix du produit
product_price = 50

# Déduction du prix du produit du montant du porte-monnaie
wallet_person -= product_price

# Affichage du solde restant après l'achat
print(f"La nouvelle valeur de votre porte-monnaie est de : {wallet_person} €")
