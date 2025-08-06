'''
Nom du fichier : Jour15_Challenge_30_Days_Of_Python.py
Projet : Manipuler les fonctions
Objectif : Créer un système d'analyse de notes d'étudiants
Auteur : Elisée N'TSOUKOU
Date : 06/08/2025
Version : 1.0
Communauté : PyCon Togo (30 Days PyCon)
Dernière Mise à jour :
'''

#Calcule la moyenne d'une liste de notes.
def calculer_moyenne(notes):
    somme = 0
    moyenne = 0
    for element in notes :
        somme = somme + element
    moyenne = somme / len(notes)
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
    tri = sorted(notes)
    classement = ()
    Classements = []
    for element in tri :
        classement = classement + tri.index(element) + element
        classements.append(classement)
    return classements

#Retourne un dictionnaire avec toutes les statistiques
def statistiques_completes(notes):
    mentions = {}
    mentions["Nombre de pesonnes échouées"] = nb_echecs
    mentions["Nombre de mentions passables"] = nb_passable
    mentions["Nombre de mentions ABien"] = nb_assez_bien
    mentions["Nombre de mentions Bien"] = nb_bien
    mentions["Nombre de mentions TBien"] = nb_tres_bien
    return mentions
