''''
Nom du fichier : #Convertisseur_CFAEURODOLLAR.py
Projet : Concvertiseur de devise CFA <---> DOLLAR/EURO
Auteur : Elisée N'TSOUKOU
Date :  23/07/2025
Version : 1.1
Communauté : PyCon Togo ( 30 Days Pycon)
Dernière Mise à jour : 26/07/2025

'''
print("Bientôt le système vous permettra de faires des conversions FCFA vres EURO ou $ et vice verca ")
print("")
devise = int(input("Entrez la valeur du FCFA : "))
convt1 = devise/656
convt2 = devise/559.4
print(f"{devise} FCFA équivaut à {convt1:.2f}EUR et {convt2:.2f}$ USD.")