''''
Nom du fichier : Jour22_Exercices_de_progression_Tkinter.py
Projet :
Objectif : Commencer par maitriser de vrai le module Tkinter
Auteur : Elisée N'TSOUKOU
Date : 13/08/2025
Version :
Communauté : PyCon Togo ( 30 Days of Python)
Dernière Mise à jour :
'''

'''
Partie 1 : Questions Théoriques

1- Qu’est-ce que Tkinter et pourquoi est-il souvent utilisé pour créer des interfaces graphiques en Python ?
2-  a.) Quelle est la ligne de code obligatoire pour créer une fenêtre Tkinter ?
    b.) Quelles sont les étapes indispensables pour créer un Tkinter ?
3- Dans Tkinter, quel est le rôle de la méthode mainloop() ?
4- Cite trois widgets de base de Tkinter et explique à quoi ils servent.
5- Explique la différence entre les méthodes pack(), grid() et place() pour organiser les widgets.

Résolution 

1- Tkinter est un module Python utilisé pour créer des applications GUI : Grafical User Interface (Interface Graphique Utilisateur)
Il est souvant utilisé en Python car c'est la GUI la plus simple et facile à utiliser en python.

2-  a.) La ligne de code obligatoire pour crée une fenêtre Tkinter est la dernière du type : Nom_de_la_fenêtre.mainloop()
    b.) Les étapes indispensables pour créer un Tkinter sont : 
        - Importation de la bibliothèque Tkinter : (from tkinter import * )
        - Définition de la fenêtre principale : (Nom_de_la_fenêtre = Tk() )
        - Personnaliser la fenêtre (titre, dimensions, couleurs, etc.)
        - Ajouter des widgets (Labels, Buttons, Entry, etc.)
        - Placer les widgets dans la fenêtre avec pack(), grid() ou place()
        - Lancer la boucle principale avec mainloop()
        
3- La méthode mainloop() est une boucle infinie qui garde la fenêtre Tkinter ouverte et en attente d’actions de l’utilisateur
   (clics, saisies, fermetures…). Sans cette méthode, la fenêtre se fermerait immédiatement après son ouverture.

4- Trois widgets de base :
    - Label : pour afficher du texte ou une image
    - Button : pour créer un bouton cliquable
    - Entry : pour permettre à l’utilisateur de saisir du texte

5- Différences entre pack(), grid() et place() :
    - pack() : place les widgets les uns par rapport aux autres (haut, bas, gauche, droite) de manière simple.
    - grid() : place les widgets dans un tableau (lignes et colonnes), idéal pour organiser les formulaires.
    - place() : positionne les widgets exactement à des coordonnées x et y, permet un placement très précis.
'''

'''
Partie 2 : Questions Pratiques (Création d’interface simple)

6- Créer une fenêtre vide
Écris le code minimal pour afficher une fenêtre Tkinter vide avec le titre "Ma première fenêtre" et une taille de 400x300.

7-Ajouter un label
Ajoute dans ta fenêtre un Label affichant le texte "Bienvenue dans Tkinter !" au centre de la fenêtre.

8- Ajouter un bouton
Ajoute un bouton nommé "Fermer" qui ne fait rien pour le moment.

9- Ajouter plusieurs widgets
Crée une interface avec :
Un label (titre)
Un label de texte "Nom :"
Un champ de saisie (Entry)
Un bouton "OK"
(Pas besoin de gérer ce qui se passe quand on clique)

10- Utiliser une autre méthode de placement
Reprends l’exercice précédent mais dispose les éléments avec grid() au lieu de pack().
'''

# 6- Fenêtre vide
from tkinter import *

fenetre = Tk()  # Crée la fenêtre principale
fenetre.title("Ma première fenêtre")  # Définit le titre de la fenêtre
fenetre.geometry("400x300")  # Définit la taille en pixels : largeur x hauteur
fenetre.mainloop()  # OBLIGATOIRE : garde la fenêtre ouverte
# ⚠ Erreur fréquente : oublier mainloop(), la fenêtre se ferme immédiatement.


# 7- Ajouter un label
from tkinter import *

fenetre = Tk()
fenetre.title("Fenêtre avec Label")
fenetre.geometry("400x300")

label = Label(fenetre, text="Bienvenue dans Tkinter !")
label.pack()  # ⚠ pack() doit être appelé pour afficher le widget
# Erreur fréquente : créer un Label mais oublier de l’afficher avec pack(), grid() ou place().

fenetre.mainloop()


# 8- Ajouter un bouton
from tkinter import *

fenetre = Tk()
fenetre.title("Fenêtre avec Bouton")
fenetre.geometry("400x300")

bouton = Button(fenetre, text="Fermer")
bouton.pack()
# ⚠ Pour que ce bouton ferme la fenêtre, il faudrait ajouter : command=fenetre.destroy
# Mais ici, il ne fait rien car aucun "command" n'est défini.

fenetre.mainloop()


# 9- Formulaire simple avec pack()
from tkinter import *

fenetre = Tk()
fenetre.title("Formulaire simple")
fenetre.geometry("300x200")

titre = Label(fenetre, text="Formulaire d'inscription")
titre.pack()

label_nom = Label(fenetre, text="Nom :")
label_nom.pack()

champ_nom = Entry(fenetre)
champ_nom.pack()

bouton_ok = Button(fenetre, text="OK")
bouton_ok.pack()
# ⚠ Avec pack(), les éléments s'empilent verticalement
# Impossible de placer "Nom :" à gauche du champ sans utiliser grid() ou place().

fenetre.mainloop()


# 10- Formulaire avec grid()
from tkinter import *

fenetre = Tk()
fenetre.title("Formulaire avec grid")
fenetre.geometry("300x150")

titre = Label(fenetre, text="Formulaire d'inscription")
titre.grid(row=0, column=0, columnspan=2)  # columnspan=2 = occupe 2 colonnes

label_nom = Label(fenetre, text="Nom :")
label_nom.grid(row=1, column=0)

champ_nom = Entry(fenetre)
champ_nom.grid(row=1, column=1)

bouton_ok = Button(fenetre, text="OK")
bouton_ok.grid(row=2, column=0, columnspan=2)

fenetre.mainloop()
# ⚠ Important : Ne jamais mélanger pack() et grid() dans la même fenêtre.
# ⚠ row et column commencent à 0, pas à 1.

