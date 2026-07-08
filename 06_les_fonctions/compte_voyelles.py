"""
Nous créons une fonction qui permet de calculer le nombre de
voyelles présentes dans un mot.
"""

# Nous définissons "mot" comme paramètre de la fonction
def get_vowels_numbers(mot):
    vowels_count = 0
    
    # On crée une boucle pour parcourir le mot lettre par lettre
    for lettre in mot:
       
        # Nous utilisons une condition qui permet de repérer toutes les voyelles
        if lettre in ["a", "e", "i", "o", "u", "y"]:
            vowels_count += 1
            
    # Cette commande permet de renvoyer le résultat
    return vowels_count 

# On demande le mot à l'utilisateur tout en "sécurisant" le format de la chaîne de caractères avec la commande lower().
mot_choisi = input("Rentrez votre mot : ").lower()

# On demande à notre fonction de traiter le mot choisi par l'utilisateur
resultat = get_vowels_numbers(mot_choisi)

# On affiche le résultat à l'aide d'une f-string pour simplifier la notation
print(f"Le nombre de voyelles est : {resultat}")
