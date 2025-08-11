"""
Nom du fichier : Jour21_Calcul_IMC_GUI.py
Projet : Calculateur d'IMC avec recommandations - Interface Tkinter
Objectif : L'utilisateur renseigne des matières et et l'heure de revision le programme lui fait un rappel


Auteur : Elisée N'TSOUKOU
Date :  26/07/2025
Version : 2.0
Communauté : PyCon Togo ( 30 Days of Python)
Dernière Mise à jour : 11/08/2025
"""

import tkinter as tk
from tkinter import messagebox


# ---- Fonctions ----
def calculer_imc():
    try:
        taille = float(entry_taille.get())
        poids = float(entry_poids.get())
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides.")
        return

    if taille <= 0 or poids <= 0:
        messagebox.showerror("Erreur", "Taille et poids doivent être supérieurs à zéro.")
        return

    imc = poids / (taille ** 2)
    label_resultat.config(text=f"Ton IMC = {imc:.2f}")

    afficher_recommandations(imc)


def afficher_recommandations(imc):
    if imc < 18.5:
        texte = ("Ton IMC est inférieur à 18.5 → insuffisance pondérale.\n"
                 "Recommandations :\n"
                 "- Mange plus souvent et augmente tes portions.\n"
                 "- Consomme des protéines à chaque repas.\n"
                 "- Dors suffisamment et réduis le stress.\n"
                 "- Fais du sport doux.\n"
                 "- Consulte un médecin ou un nutritionniste.")
        couleur = "blue"

    elif 18.5 <= imc <= 24.9:
        texte = ("IMC normal (18.5 - 24.9).\n"
                 "Recommandations :\n"
                 "- Continue une alimentation équilibrée.\n"
                 "- Bois au moins 1,5 L d'eau/jour.\n"
                 "- Pratique une activité physique régulière.\n"
                 "- Évite les excès de sucre, sel, graisses.\n"
                 "- Bilans de santé réguliers.")
        couleur = "green"

    elif 24.9 < imc <= 29.9:
        texte = ("Surpoids (24.9 - 29.9).\n"
                 "Recommandations :\n"
                 "- Réduis sucre et graisses saturées.\n"
                 "- Mange fruits, légumes, protéines maigres.\n"
                 "- Sport 45 min, 3-5 fois/semaine.\n"
                 "- Pas de grignotage.\n"
                 "- Suivi nutritionnel recommandé.")
        couleur = "orange"

    elif 29.9 < imc <= 40:
        texte = ("Obésité modérée (29.9 - 40).\n"
                 "Recommandations :\n"
                 "- Consulte un médecin rapidement.\n"
                 "- Alimentation équilibrée et contrôlée.\n"
                 "- Limite produits industriels.\n"
                 "- Activité physique adaptée.\n"
                 "- Objectifs progressifs avec suivi.")
        couleur = "red"

    else:
        texte = ("Obésité sévère (> 40).\n"
                 "Recommandations :\n"
                 "- Consultation médicale urgente.\n"
                 "- Plan de perte de poids encadré.\n"
                 "- Réduis aliments transformés et boissons sucrées.\n"
                 "- Activité physique douce.\n"
                 "- Soutien psychologique si besoin.")
        couleur = "darkred"

    label_recommandations.config(text=texte, fg=couleur)


# ---- Interface ----
root = tk.Tk()
root.title("Calculateur d'IMC")
root.geometry("500x500")
root.resizable(False, False)

# Saisie
tk.Label(root, text="Taille (m) :", font=("Arial", 12)).pack(pady=5)
entry_taille = tk.Entry(root, font=("Arial", 12))
entry_taille.pack()

tk.Label(root, text="Poids (kg) :", font=("Arial", 12)).pack(pady=5)
entry_poids = tk.Entry(root, font=("Arial", 12))
entry_poids.pack()

tk.Button(root, text="Calculer l'IMC", font=("Arial", 12), command=calculer_imc).pack(pady=15)

# Résultat
label_resultat = tk.Label(root, text="", font=("Arial", 14, "bold"))
label_resultat.pack(pady=10)

label_recommandations = tk.Label(root, text="", font=("Arial", 11), justify="left", wraplength=450)
label_recommandations.pack(pady=10)

root.mainloop()
