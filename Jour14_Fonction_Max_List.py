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
print("="*50)
print("Salut ! Heureux de vous retrouver...")
print("="*50)
print("")
print("Le travail d'aujourd'hui ressemble un peu à celui fait hier. Nous allons juste rechercher le maximun d'une liste.")
taille = int(input("Combien d’éléments voulez-vous dans votre liste ? : "))
liste = []
for i in range(taille) :
    elements = int(input(f"Entrez la valeur N° {i+1} : "))
    liste.append(elements)
print(f"L'élément maximal de votre liste est : {max_liste(liste)}")
