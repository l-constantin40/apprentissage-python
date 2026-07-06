# Saisie de l'âge de l'utilisateur et conversion en entier
age = int(input("Quel est votre âge ? : "))

# Détermination du prix de base du ticket selon l'âge
if age < 18:
    prix_ticket = 7
else:
    prix_ticket = 12

# Demande d'option pop-corn (conversion immédiate en minuscules)
popcorn_demande = input("Souhaitez-vous du pop-corn ? (Oui/Non) : ").lower()

# Calcul du prix total (intégration du supplément pop-corn via une condition ternaire)
prix_total = prix_ticket + (5 if popcorn_demande == "oui" else 0)

# Affichage du montant final à payer
print(f"Le prix total à payer est de {prix_total} €.")
