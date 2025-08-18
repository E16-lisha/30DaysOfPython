'''
Nom du fichier : Jour27_Generateur_MotDePasse.py
Projet : Générateur de mot de passe aléatoire
Objectif : Utiliser random et string pour générer des mots de passe sécurisés
Auteur : Elisée N'TSOUKOU
Date : 18/08/2025
Version : 1.0
Communauté : PyCon Togo (30 Days Python)
Dernière mise à jour : 
'''

import random
import string

print("="*50)
print("Générateur de mot de passe sécurisé")
print("="*50)

# Demander la longueur du mot de passe (Proposé par l'IA)
longueur = int(input("Entrez la longueur du mot de passe : "))

# Caractères possibles (lettres, chiffres, symboles)
caracteres = string.ascii_letters + string.digits + string.punctuation

# Génération du mot de passe
mot_de_passe = ''.join(random.choice(caracteres) for i in range(longueur))

print(f"Ton mot de passe généré est : {mot_de_passe}")
