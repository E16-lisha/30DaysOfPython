'''
Nom du fichier : Jour11_add_two_numbers.py
Projet : Addition de deux nombres avec fonction
Objectif : Apprendre à créer une fonction avec des paramètres
Auteur : Elisée N'TSOUKOU
Date : 01/08/2025
Version : 1.0
Communauté : PyCon Togo (30 Days PyCon)
'''

def add_two_numbers(nombre1, nombre2):
    resultat = nombre1 + nombre2
    return resultat

print("="*60)
print("  Addition de deux nombres en Python (version débutant)")
print("="*60)

try:
    n1 = int(input("Entrez le premier nombre : "))
    n2 = int(input("Entrez le deuxième nombre : "))

    # Appel de la fonction
    somme = add_two_numbers(n1, n2)

    # Affichage du résultat
    print("-"*60)
    print(f"La somme de {n1} et {n2} est : {somme}")
    print("-"*60)

except ValueError:
    print("❗Erreur : tu dois entrer des nombres valides (ex : 10, 25)")
