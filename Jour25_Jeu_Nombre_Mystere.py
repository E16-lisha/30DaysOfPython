'''
Nom du fichier : Jour25_Jeu_Nombre_Mystere.py
Projet : Jeu du nombre mystère
Objectif : Boucles, conditions, random et gestion d’erreurs
Auteur : Elisée N'TSOUKOU
Date : 16/08/2025
Version : 1.0
Communauté : PyCon Togo (30 Days PyCon)
'''

import random

nombre_secret = random.randint(1, 100)
tentatives = 0
max_tentatives = 7

print("="*50)
print("Bienvenue dans le jeu du nombre mystère !")
print("Je pense à un nombre entre 1 et 100...")
print(f"Tu as {max_tentatives} tentatives pour le trouver.")
print("="*50)

while tentatives < max_tentatives:
    try:
        choix = int(input(f"Tentative {tentatives+1} : Entre ton nombre → "))
        tentatives += 1

        if choix == nombre_secret:
            print(f"Bravo ! Tu as trouvé en {tentatives} tentatives.")
            break
        elif choix < nombre_secret:
            print(" Trop petit !")
        else:
            print(" Trop grand !")
    except ValueError:
        print(" Erreur : tu dois entrer un nombre valide.")

if tentatives == max_tentatives and choix != nombre_secret:
    print(f" Dommage, le nombre mystère était {nombre_secret}.")
