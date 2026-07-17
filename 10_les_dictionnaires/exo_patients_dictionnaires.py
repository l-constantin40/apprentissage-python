"""Code permettant d'afficher les données de trois patients, d'ajouter un patient
et de sauvegarder les données au format JSON."""

import json

# Le dictionnaire des patients de l'hôpital
patients = {
    "Jean Dupont": {"age": 45, "symptome": "Toux et fièvre"},
    "Marie Curie": {"age": 32, "symptome": "Fracture du poignet"}
}

# Ajout d'un patient dans le dictionnaire des patients
patients["Lucas Martin"] = {"age": 12, "symptome": "Mal de ventre"}

# Boucle permettant d'afficher les données de chaque patient
for patient in patients:
    print("Patient :", patient, 
          " Âge :", patients[patient]["age"], 
          " Symptôme :", patients[patient]["symptome"])

# Enregistrement des données sous format JSON
with open("registre_hopital.json", "w") as file:
    json.dump(patients, file)
    
