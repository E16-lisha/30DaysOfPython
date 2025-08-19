'''
Nom du fichier : Jour28_Calculateur_Age.py
Projet : Calculer l'âge d'une personne
Objectif : Utiliser datetime et les entrées utilisateur
Auteur : Elisée N'TSOUKOU
Date : 26/08/2025
Version : 1.0
Communauté : PyCon Togo (30 Days PyCon)
'''

from datetime import date

print("="*50)
print("Calculateur d'âge")
print("="*50)


annee = int(input("Entrez votre année de naissance (ex: 2000) : "))
mois = int(input("Entrez votre mois de naissance (1-12) : "))
jour = int(input("Entrez votre jour de naissance (1-31) : "))

# Date actuelle
aujourd_hui = date.today()

# Calcul de l'âge
naissance = date(annee, mois, jour)
age = aujourd_hui.year - naissance.year

# Ajustement si la date d'anniversaire n'est pas encore passée
if (aujourd_hui.month, aujourd_hui.day) < (naissance.month, naissance.day):
    age -= 1

print("="*50)
print(f"✅ Vous avez {age} ans.")
