'''
Nom du fichier : Jour17_Interface_graphique.py
Projet : Création d'interface graphique avec Tkinter
Objectif : Apprendre les bases et manipuler des widgets
Auteur : Elisée N'TSOUKOU
Date : 08/08/2025
Version : 2.2
Communauté : PyCon Togo (30 Days PyCon)
Dernière Mise à jour : 09/08/2025
'''

import os
from tkinter import *

# ----------- Fonctions pour les boutons ----------- #
def dire_bonjour():
    label_message.config(text=f"👋 Bonjour {entry_nom.get()} ! Bienvenue sur WINSIDE.")

def effacer_message():
    label_message.config(text="")
    entry_nom.delete(0, END)

def quitter():
    window.destroy()

# ----------- Création de la fenêtre ----------- #
window = Tk()
window.title("WINSIDE - Interface Graphique")
window.config(background='#005490')

# Centrer la fenêtre
window_width = 900
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
pos_x = (screen_width // 2) - (window_width // 2)
pos_y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

# Définir l'icône
if os.path.exists("logo.ico"):
    window.iconbitmap("logo.ico")
else:
    print("⚠️ Icône logo.ico introuvable, icône par défaut utilisée.")

# ----------- Widgets ----------- #
label_title = Label(
    window,
    text="Bienvenue sur la plateforme de WINSIDE",
    font=("Montserrat", 20, "bold"),
    bg='#005490',
    fg='white',
    wraplength=850,
    justify="center"
)
label_title.pack(pady=10)

# Champ de saisie
entry_nom = Entry(window, font=("Arial", 14), width=30)
entry_nom.pack(pady=5)

# Label message dynamique
label_message = Label(window, text="", font=("Arial", 14), bg='#005490', fg="white")
label_message.pack(pady=5)

# Boutons
frame_buttons = Frame(window, bg='#005490')
frame_buttons.pack(pady=10)

btn_bonjour = Button(frame_buttons, text="Dire Bonjour", font=("Arial", 12), command=dire_bonjour)
btn_bonjour.grid(row=0, column=0, padx=5)

btn_effacer = Button(frame_buttons, text="Effacer", font=("Arial", 12), command=effacer_message)
btn_effacer.grid(row=0, column=1, padx=5)

btn_quitter = Button(frame_buttons, text="Quitter", font=("Arial", 12), command=quitter)
btn_quitter.grid(row=0, column=2, padx=5)

#----------- Lancer l'application ----------- #
window.mainloop()
