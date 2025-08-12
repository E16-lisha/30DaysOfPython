
"""
Nom du fichier : Jour21_Calculatrice_simple_avec_Interface_graphique.py.py
Projet : Calculatrice qui effectue une somme et un produit
Objectif : L'utilisateur entre deux valeurs et le programme affiche la somme et le produit de ces deux nombres.
Auteur : Elisée N'TSOUKOU
Date :  12/08/2025
Version : 1.0
Communauté : PyCon Togo ( 30 Days of Python)
Dernière Mise à jour :
"""
import tkinter as tk

def addition():
    try:
        resultat.set(float(entree1.get()) + float(entree2.get()))
    except:
        resultat.set("Erreur")

def multiplication():
    try:
        resultat.set(float(entree1.get()) * float(entree2.get()))
    except:
        resultat.set("Erreur")

fenetre = tk.Tk()
fenetre.title("Mini Calculatrice")

entree1 = tk.Entry(fenetre)
entree1.pack()

entree2 = tk.Entry(fenetre)
entree2.pack()

tk.Button(fenetre, text="Addition", command=addition).pack()
tk.Button(fenetre, text="Multiplication", command=multiplication).pack()

resultat = tk.StringVar()
tk.Label(fenetre, textvariable=resultat).pack()

fenetre.mainloop()