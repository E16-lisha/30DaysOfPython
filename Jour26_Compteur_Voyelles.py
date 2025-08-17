'''
Nom du fichier : Jour26_Compteur_Voyelles.py
Projet : Compter les voyelles et consonnes dans une phrase
Objectif : Utiliser les boucles et conditions sur les chaînes.
Auteur : Elisée N'TSOUKOU
Date : 17/08/2025
Version : 1.0
Communauté : PyCon Togo (30 Days Python)
Dernière Mise à jour :
'''


phrase = input("Entrez une phrase : ")


voyelles = "aeiouyAEIOUY"
nb_voyelles = 0
nb_consonnes = 0


for char in phrase:
    if char.isalpha():  # On ne compte que les lettres
        if char in voyelles:
            nb_voyelles += 1
        else:
            nb_consonnes += 1


print("="*50)
print(f"Phrase analysée : {phrase}")
print(f"Nombre de voyelles : {nb_voyelles}")
print(f"Nombre de consonnes : {nb_consonnes}")
print("="*50)
