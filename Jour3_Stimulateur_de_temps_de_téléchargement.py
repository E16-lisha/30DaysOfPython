''''
Nom du fichier : Jour3_Stimulateur_de_temps_de_téléchargement.py
Projet : L'utilisateur renseigne des données on le programme retoure une durée
Auteur : Elisée N'TSOUKOU
Date :  24/07/2025
Version : 1.0
Communauté : PyCon Togo ( 30 Days Pycon)
Dernière Mise à jour :
'''
print("------------STIMULATUER DE TEMPS DE TELECHARGEMENT--------------")
print("")
print("Nous allons vous calculer le temps de téléchargement de vos fichiers en fonction de leurs tailles (en Ko) et la vitesse de votre connexion (en Mo/s)")
print("")
Taille = int(input("Entrez la taille de votre fichier en Ko (Ex: 1024 ) : "))
while Taille < 0 :
    print ("Valeur saisie incorrecte. Veuillez entrer une valeur Positive")
    Taille = int(input("Entrez la taille de votre fichier en Ko (Ex: 1024 ) : "))

print("")
Vitesse = int(input("Entrez la vitesse de votre connexion en Ko (Ex: 5 ) ) : "))
while Vitesse < 0 :
    print ("Valeur saisie incorrecte. Veuillez entrer une valeur Positive")
    Taille = int(input("Entrez la vitesse de votre connexion en Ko (Ex: 5 ) : "))

Temps = Taille/(Vitesse*1000)
Min = 0
Heure = 0
if Temps > 60 :
    Min = Temps / 60
    if Min > 60 :
        Heure = Min /60
        print(f"Le téléchargement de votre fichier terminera dans environs {Heure:.1f} heures...")
    else :
        print(f"Le téléchargement de votre fichier terminera dans environs {Min:.1f} minutes...")
else :
    print(f"Le téléchargement de votre fichier terminera dans environs {Temps:.1f} secondes...")
print("")
print("Merci d'avoir choisi le stimulateur de temps de téléchargement !!! ")

print("------------------- A plus --------------------")