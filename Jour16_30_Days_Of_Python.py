'''
Nom du fichier : Jour16_30_Days_Of_Python.py
Projet : Manipuler les fonctions
Objectif : Créer un système d'analyse de notes d'étudiants
Auteur : Elisée N'TSOUKOU
Date : 06/08/2025
Version : 2.0
Communauté : PyCon Togo (30 Days PyCon)
Dernière Mise à jour : 07/08/2025
'''

#Calcule la moyenne d'une liste de notes.
def calculer_moyenne(notes):
    somme = 0
    moyenne = 0
    for i in notes :
        somme=somme+i
    try :
        moyenne = somme/len(notes)
    except ZeroDivisionError :
        print("Erreur Mathématiques. Vous evez entré une liste vide.")
    return moyenne

#Retourne un tuple (note_min, note_max).
def trouver_extremes(notes):
    note_max = max(notes)
    note_min = min(notes)
    return (note_min,note_max)

#Retourne une liste avec [nb_echecs, nb_passable, nb_bien, nb_tres_bien].
def compter_mentions(moyennes):
    resultats = []
    nb_echecs = 0
    nb_passable = 0
    nb_assez_bien = 0
    nb_bien = 0
    nb_tres_bien = 0
    for element in moyennes :
        if element < 10 :
            nb_echecs = nb_echecs + 1
        elif element >= 10 and element < 12 :
            nb_passable = nb_passable + 1
        elif element >= 12 and element < 14 :
            nb_assez_bien = nb_assez_bien + 1
        elif element >= 14 and element < 16 :
            nb_bien = nb_bien + 1
        elif element >= 16 and element <= 20 :
            nb_tres_bien = nb_tres_bien + 1
    resultats.append(nb_echecs)
    resultats.append(nb_passable)
    resultats.append(nb_assez_bien)
    resultats.append(nb_bien)
    resultats.append(nb_tres_bien)
    return resultats

#Retourne une nouvelle liste avec les notes > seuil
def filtrer_notes_superieures(notes, seuil):
    nouvelle_liste = []
    for element in notes :
        if element > seuil :
            nouvelle_liste.append(element)
    return nouvelle_liste

#Retourne une liste de tuples (note, rang) triée par note décroissante
def notes_triees_avec_rang(notes):
    tri = sorted(notes, reverse=True)
    classements = []
    cpt = 0
    for element in tri :
        ctp = cpt + 1
        classement = (element,cpt)
        classements.append(classement)
    return classements

#Retourne un dictionnaire avec toutes les statistiques
def statistiques_completes(moyennes):
    nb_echecs = 0
    nb_passable = 0
    nb_assez_bien = 0
    nb_bien = 0
    nb_tres_bien = 0
    for element in moyennes:
        if element < 10:
            nb_echecs = nb_echecs + 1
        elif element >= 10 and element < 12:
            nb_passable = nb_passable + 1
        elif element >= 12 and element < 14:
            nb_assez_bien = nb_assez_bien + 1
        elif element >= 14 and element < 16:
            nb_bien = nb_bien + 1
        elif element >= 16 and element <= 20:
            nb_tres_bien = nb_tres_bien + 1
    mentions = {}
    mentions["Nombre de pesonnes échouées"] = nb_echecs
    mentions["Nombre de mentions passables"] = nb_passable
    mentions["Nombre de mentions ABien"] = nb_assez_bien
    mentions["Nombre de mentions Bien"] = nb_bien
    mentions["Nombre de mentions TBien"] = nb_tres_bien
    return mentions

#Fontion principale
notes = []
#Oligeons l'utilisateur à entrer un entier positif pour le nombre d'élèves.
while True :
    try :
        nb_notes = int(input("Combien de notes voulez vous entrer ? : "))
        break
        while nb_notes <= 0 :
            print("Erreur !!! Entrez une valeur positive non nulle.")
            nb_notes = int(input("Combien d'élèves woulez vous classer ? : "))
    except ValueError :
        print("Réessayez avec un entier positif non nul !")
# Remplissage de la liste des notes
for i in range(nb_notes) :
    try :
        note = float(input(f"Entrez la {i+1}e note : "))
        while note < 0:
            print("Erreur !!! Entrez une valeur positive.")
            note = float(input(f"Entrez la {i+1}e note : "))
    except ValueError:
        print("Réessayez avec une note positive !")
    notes.append(note)
#Calcul de la Moyenne des notes
print(f"La moyenne est égale à {calculer_moyenne(notes)}")
print("")
#Détermination des extrema
print(f"Les notes min et max de votre liste sont {trouver_extremes(notes):.2f}")
#Classement en fontion des moyennes
print(f"Nous allons vous montrer les classements et mentions : {compter_mentions(notes)}")
#Affichage des moyennes supérieurs au seuil
try:
    seuil = float(input(f"Entrez le seuil des notes : "))
    while note < 0:
        print("Erreur !!! Entrez une valeur positive.")
        seuil = float(input(f"Entrez le seuil des notes : "))
except ValueError:
    print("Réessayez avec une note positive !")
    seuil = float(input(f"Entrez le seuil des notes : "))
print("Voici une liste des notes supérieures au seuil : ",filtrer_notes_superieures(notes, seuil))
#Classement dans l'ordre décroissant :
print("Tri dans l'ordre décroissant des rangs")
print(notes_triees_avec_rang(notes))
print(" ")
print("Strastistiques générales : ", statistiques_completes(notes))