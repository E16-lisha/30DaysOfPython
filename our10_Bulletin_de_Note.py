'''
Nom du fichier : Jour10_Bulletin_de_Note.py
Projet : Générateur de Note avec PDF
Objectif : Se familiariser avec les conditions et le module fpdf
Auteur : Elisée N'TSOUKOU
Date : 1er/08/2025
Version : 1.0
Communauté : PyCon Togo (30 Days PyCon)
Dernière Mise à jour : :
'''

from fpdf import FPDF

# Entrée des informations de l'élève
print("="*60)
print(" 📘 Bienvenue dans le système de bulletin de note 📘 ")
print("="*60)

Nom = input("Nom complet de l'élève : ")
Matiere = input("Nom de la matière : ")
Note = int(input("Entrez la note obtenue (sur 100) : "))

# Attribution de la mention
if 80 <= Note <= 100:
    Mention = "A"
    Commentaire = "Excellent travail "
elif 70 <= Note < 80:
    Mention = "B"
    Commentaire = "Très bien "
elif 60 <= Note < 70:
    Mention = "C"
    Commentaire = "Bon effort "
elif 50 <= Note < 60:
    Mention = "D"
    Commentaire = "Peux mieux faire ⚠️"
elif 0 <= Note < 50:
    Mention = "F"
    Commentaire = "Échec ❌ Courage !"
else:
    Mention = "Erreur"
    Commentaire = "Note invalide"

# Affichage à l'écran
print("-"*60)
print("Bulletin de l'élève :")
print(f"Nom : {Nom}")
print(f"Matière : {Matiere}")
print(f"Note : {Note}/100")
print(f"Mention : {Mention}")
print(f"Commentaire : {Commentaire}")
print("-"*60)

# Génération du PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", size=14)

pdf.cell(200, 10, txt="BULLETIN DE NOTE", ln=True, align="C")
pdf.ln(10)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=f"Nom de l'élève : {Nom}", ln=True)
pdf.cell(200, 10, txt=f"Matière : {Matiere}", ln=True)
pdf.cell(200, 10, txt=f"Note obtenue : {Note}/100", ln=True)
pdf.cell(200, 10, txt=f"Mention : {Mention}", ln=True)
pdf.multi_cell(200, 10, txt=f"Commentaire : {Commentaire}", align="L")

# Enregistrement
pdf.output("Bulletin_Note.pdf")
print("✅ PDF généré avec succès : Bulletin_Note.pdf")
