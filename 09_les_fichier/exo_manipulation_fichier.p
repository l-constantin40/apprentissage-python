"""
Ce script permet d'enregistrer des mots de passe
dans un fichier texte de manière persistante.
"""

# On demande le mot de passe à l'utilisateur
passwords = input("Écrivez votre mot de passe : ")

# On ouvre le fichier en mode ajout (append)
with open("passwords.txt", "a") as file: 
    # On écrit le mot de passe suivi d'un saut de ligne
    file.write(passwords + "\n")

# Message de confirmation
print(f"Votre mot de passe <{passwords}> a bien été enregistré !")
