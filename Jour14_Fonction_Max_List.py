'''
Nom du fichier : Jour14_Fonction_Max_List.py
Projet : Une fonction qui retourne l'elément maximal d'une liste
Objectif : Appliquer les fonctions
Auteur : Elisée N'TSOUKOU
Date : 05/08/2025
Version : 1.0
Communauté : PyCon Togo (30 Days PyCon)
Dernière Mise à jour :
'''

def max_liste(liste) :
    if not liste :
        return None
    max_element = liste[0]
    for element in liste :
        if element > max_element :
            max_element = element
    return max_element

#Programme principal
print("Salut ! Heureux de vous retrouver...")
print("Le travail d'aujourd'hui ressemble un peu à celui fait hier. Nous allons juste rechercher le maximun d'une liste.")
taille = int(input("Combien d’éléments voulez-vous dans votre liste ? : "))
max_liste(taille)
