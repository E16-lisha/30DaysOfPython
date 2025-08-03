'''
Nom du fichier : Jour12_Générateur_ID.py
Projet : Générateur d’identifiant utilisateur aléatoire
Objectif : Utiliser les modules et les fonctions
Auteur : Elisée N'TSOUKOU
Date : 03/08/2025
Version : 1.0
Communauté : PyCon Togo (30 Days PyCon)
Dernière Mise à jour :
'''

import random
import string

# Déclaration de la fonction pour générer un ID aléatoire
def random_user_id():
    caracteres = string.ascii_letters + string.digits  # Lettres A-Z, a-z et chiffres 0-9
    ID = ''.join(random.choice(caracteres) for i in range(6))  # 6 caractères aléatoires
    return ID


print("="*60)
print("Générateur d'ID utilisateur aléatoire (6 caractères)")
print("="*60)
print(f"Voici ton ID généré : {random_user_id()}")
print("="*60)
