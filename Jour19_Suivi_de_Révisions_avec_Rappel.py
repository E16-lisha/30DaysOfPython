''''
Nom du fichier : Jour19_Suivi_de_Révisions_avec_Rappel.py
Projet : Suivi de révisions avec rappels - Interface Tkinter
Objectif : L'utilisateur renseigne des matières et et l'heure de revision le programme lui fait un rappel
Auteur : Elisée N'TSOUKOU
Date :  25/07/2025
Version : 3.1
Communauté : PyCon Togo ( 30 Days of Python)
Dernière Mise à jour : 10/08/2025
'''
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ---------- Variables globales ----------

matieres = {}  # {matiere: heure}

# ---------- Fonctions ----------
def ajouter_matiere():
    """Ajoute une matière avec l'heure de révision"""
    matiere = entry_matiere.get().strip()
    heure = entry_heure.get().strip()

    if not matiere or not heure:
        messagebox.showwarning("Erreur", "Veuillez remplir les deux champs.")
        return

    # Vérification format HH:MM
    try:
        datetime.strptime(heure, "%H:%M")
    except ValueError:
        messagebox.showwarning("Erreur", "Format de l'heure invalide. Utilisez HH:MM.")
        return

    matieres[matiere] = heure
    afficher_matieres()

    # Vider les champs
    entry_matiere.delete(0, tk.END)
    entry_heure.delete(0, tk.END)

def afficher_matieres():
    """Met à jour la liste affichée"""
    liste_matieres.delete(0, tk.END)
    for mat, heure in matieres.items():
        liste_matieres.insert(tk.END, f"📕 {mat} : {heure}")

def verifier_rappels():
    """Vérifie si une matière doit être rappelée"""
    heure_actuelle = datetime.now().strftime("%H:%M")
    for mat, heure in list(matieres.items()):
        if heure == heure_actuelle:
            messagebox.showinfo("Rappel de Révision",
                                f"🔔 Il est {heure_actuelle} : C’est le moment de réviser {mat} !")
            matieres[mat] = "FAIT"
            afficher_matieres()
    root.after(30000, verifier_rappels)  # Vérifie toutes les 30s

def demarrer():
    """Démarre le programme après saisie du nom"""
    nom = entry_nom.get().strip()
    if not nom:
        messagebox.showwarning("Erreur", "Veuillez entrer votre nom.")
        return

    label_bonjour.config(text=f"Bonjour {nom} !\nAjoutez vos matières et heures de révision ci-dessous.")
    frame_nom.pack_forget()
    frame_programme.pack(pady=10)
    verifier_rappels()

# ---------- Interface ----------
root = tk.Tk()
root.title("Suivi de Révisions avec Rappel")

frame_nom = tk.Frame(root)
frame_nom.pack(pady=30)

tk.Label(frame_nom, text="Entrez votre Nom :", font=("Arial", 12)).pack()
entry_nom = tk.Entry(frame_nom, font=("Arial", 12))
entry_nom.pack(pady=5)

btn_nom = tk.Button(frame_nom, text="Commencer", font=("Arial", 12), command=demarrer)
btn_nom.pack(pady=10)

# Frame programme
frame_programme = tk.Frame(root)
label_bonjour = tk.Label(frame_programme, text="", font=("Arial", 14), fg="blue")
label_bonjour.pack(pady=5)

# Saisie matière et heure
frame_saisie = tk.Frame(frame_programme)
frame_saisie.pack(pady=10)

tk.Label(frame_saisie, text="Matière :", font=("Arial", 12)).grid(row=0, column=0, padx=5)
entry_matiere = tk.Entry(frame_saisie, font=("Arial", 12))
entry_matiere.grid(row=0, column=1, padx=5)

tk.Label(frame_saisie, text="Heure (HH:MM) :", font=("Arial", 12)).grid(row=1, column=0, padx=5)
entry_heure = tk.Entry(frame_saisie, font=("Arial", 12))
entry_heure.grid(row=1, column=1, padx=5)

btn_ajouter = tk.Button(frame_saisie, text="Ajouter", font=("Arial", 12), command=ajouter_matiere)
btn_ajouter.grid(row=2, column=0, columnspan=2, pady=5)

# Liste des matières
liste_matieres = tk.Listbox(frame_programme, font=("Arial", 12), width=40, height=10)
liste_matieres.pack(pady=10)

root.mainloop()
