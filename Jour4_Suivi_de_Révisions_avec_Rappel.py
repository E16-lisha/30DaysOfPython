''''
Nom du fichier : Jour4_Suivi_de_Révisions_avec_Rappel.py
Projet : L'utilisateur renseigne des matières et et l'heure de revision le programme lui fait un rappel
Auteur : Elisée N'TSOUKOU
Date :  25/07/2025
Version : 1.0
Communauté : PyCon Togo ( 30 Days Pycon)
Dernière Mise à jour :
'''
import time
from datetime import datetime
print("------------Accueil----------------")
print("")
nom = str(input("Entrez votre Nom : "))
print("")
print("------------MESSAGE----------------")
print(f"     Bonjour {nom} !  ")
print("Je suis l'assistant console qui va t'aider à faire tes revisions par rappel. Tu vas me donner toutes les matières à réviser ")
print("ainsi que leurs temps de révision et je vais te rappeler dès que l'heure arrive. Voici un exemple :  ")
print("")
print("📕MTH 1220 (Structure alébrique de base) : O4:30")
print("📕INF 122 (SDD et programmation en C)    : 14:00")
print("📕2GME 1221 (Dessin Technique)           : 18:45")
print("📕1MTH 1221 (Calcul Différentiel)        : 22:30")
print("")
print("----------C'est Parti !-------------")
matieres = []
matiere = {}
print("")
print("------------------------------------------------------------------------------")
nbr = int(input("combien de matières voulez-vous programmer ? : " ))
for i in range(nbr) :
    print("")
    mat = input(f"Entrez la Matière N° {i+1} : ")
    tps = input("Entrez l'heure de révision (formet HEURE:MINUTE) : ")
    #A ne plus oublier !!! Pour ajouter un élément à un dictionnaire, on fait : dictionnaire[clé] = valeur
    matiere[mat]=tps
    matieres.append(matiere)
print("-------------------------------------------------------------------------------")
print("")
#Nous devons afficher la liste des matières
print("Voici la liste générale des matières que vous avez entrées : ")
for mat, tps in matiere.items() :
    print("📕", mat, ": ", tps)
print("--------------------------------------------------------------------------------")
#Seulement, Cette partie est généreée par l'IA. A relire, comprendre et à recoder proprement dans les versions à venir
print("⏰ En attente des heures de rappel...")

while True:
    heure_actuelle = datetime.now().strftime("%H:%M")
    for mat, tps in matiere.items():
        if heure_actuelle == tps:
            print(f"🔔 Il est {heure_actuelle} : C’est le moment de réviser {mat} !")
            # Supprimer la matière après le rappel pour ne pas l'afficher à nouveau
            matiere[mat] = "FAIT"
    time.sleep(30)  # Vérifie toutes les 30 secondes




