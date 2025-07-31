'''
Nom du fichier : Jour9_Système_de_notes.py
Projet : Système de notation d’un élève
Objectif : Appliquer les conditions (if, elif, else)
Auteur : Elisée N'TSOUKOU
Date : 31/07/2025
Version : 1.0
Communauté : PyCon Togo (30 Days PyCon)
Dernière Mise à jour :
'''

print("="*70)
print("Bienvenue dans le système de notation d’un élève 📚")
print("="*70)

# Demander la note de l'élève
score = int(input("Entrez la note de l'élève (sur 100) : "))

# Vérification des intervalles de la note
if score >= 80 and score <= 100:
    print("Résultat : ⭐ Tu as la note A. Excellent travail !")
elif score >= 70:
    print("Résultat : 👍 Tu as la note B. Très bien !")
elif score >= 60:
    print("Résultat : 🙂 Tu as la note C. Pas mal, continue !")
elif score >= 50:
    print("Résultat : ⚠️ Tu as la note D. Tu peux mieux faire.")
elif score >= 0:
    print("Résultat : ❌ Tu as la note F. Courage, il faut travailler encore.")
else:
    print("❗Erreur : La note entrée n’est pas valide. Elle doit être entre 0 et 100.")
