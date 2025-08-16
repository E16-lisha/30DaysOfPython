'''
Nom du fichier : Jour24_Convertisseur_Temperature.py
Projet : Convertisseur Celsius ↔ Fahrenheit
Objectif : Utiliser les fonctions et conditions.
Auteur : Elisée N'TSOUKOU
Date : 15/08/2025
Version : 1.0
Communauté : PyCon Togo (30 Days Python)
Dernière Mise à jour :
'''

def celsius_vers_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_vers_celsius(f):
    return (f - 32) * 5/9

print("="*50)
print("Convertisseur de Température")
print("="*50)
print("1 - Celsius vers Fahrenheit")
print("2 - Fahrenheit vers Celsius")
choix = input("Choisissez une option (1 ou 2) : ")

try:
    if choix == "1":
        c = float(input("Entrez la température en °C : "))
        print(f"{c}°C = {celsius_vers_fahrenheit(c):.2f}°F")
    elif choix == "2":
        f = float(input("Entrez la température en °F : "))
        print(f"{f}°F = {fahrenheit_vers_celsius(f):.2f}°C")
    else:
        print(" Choix invalide. Veuillez entrer 1 ou 2.")
except ValueError:
    print(" Erreur : vous devez entrer un nombre valide.")
