'''
Nom du fichier : Jour_8_Générateur_de_facture.py
Projet : Générateur de Facture
Objectif : Se familiariser avec les dictionnaires
Auteur : Elisée N'TSOUKOU
Date : 29/07/2025
Version : 1.0
Communauté : PyCon Togo (30 Days PyCon)
Dernière Mise à jour :
'''
from sys import prefix


def facture(Entrepise,Mail,Facture,Date,Nom,AdresseClient,qte,Articles) :
    print("--------------------------------FACTURE-------------------------------------")
    print(Entrepise)
    print(Mail)
    print(Facture)
    print(Date)
    print("A",Nom)
    print(AdresseClient)
    print("*"*100)
    print(Articles)



from fpdf import FPDF

print("+"*80)
print("Coordonnées de l'entreprise ")
#Recueil d'innformations concernant l'entreprise (Chercher plus tard comment mémoriser ces infos)
Entrepise = str(input("Entrez le nom de votre Entreprise : "))
Contact = str(input("Entrez le numero de l'entreprise : "))
Mail = str(input("Entrez l'adresse e-mail de l'entreprise : "))
print("")
print("Infos de l'entreprise recueilli avec succès ✅")
print("")
Facture = str(input("Entrez le numero de facture : "))
Date = str(input("Entrez la date de délivrance : "))
print("+"*80)
print("Coordonnées du client")
Nom = str(input("Entrez le nom du client : "))
AdresseClient = str(input("Entrez l'adresse du client : "))
print("+"*80)
print("+"*80)
qte = int(input("Combien de type d'articles le client a acheté ? : "))
while qte <= 0 :
    print("Erreur de saisie!!!")
    qte = int(input("Combien de type d'articles le client a acheté ? : "))
Articles = []
for cpt in range(qte) :
    nom_article = str(input(f"Entrez le nom de l'article N°{cpt+1} : "))
    Pu = int(input("Entrez en FCFA le prix unitaire de l'article : "))
    Nbr = int(input("Entre quantité acheté de ce produit : "))
    prix_total = Pu*Nbr
    article = {}
    article["Désignation"]=nom_article
    article["Prix_Unitaire"]= Pu
    article["Quantité"]= Nbr
    article["Prix_total"]= prix_total
    Articles.append(article)

facture(Entrepise,Mail,Facture,Date,Nom,AdresseClient,qte,Articles)

# Création du PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="FACTURE", ln=True, align="C")
pdf.ln(10)

pdf.cell(200, 10, txt=f"Entreprise : {Entrepise}", ln=True)
pdf.cell(200, 10, txt=f"Email : {Mail}", ln=True)
pdf.cell(200, 10, txt=f"N° Facture : {Facture}", ln=True)
pdf.cell(200, 10, txt=f"Date : {Date}", ln=True)
pdf.ln(5)
pdf.cell(200, 10, txt=f"Client : {Nom}", ln=True)
pdf.cell(200, 10, txt=f"Adresse : {AdresseClient}", ln=True)
pdf.ln(10)

pdf.set_font("Arial", size=10, style='B')
pdf.cell(60, 10, txt="Désignation", border=1)
pdf.cell(40, 10, txt="Prix Unitaire", border=1)
pdf.cell(30, 10, txt="Quantité", border=1)
pdf.cell(40, 10, txt="Prix Total", border=1)
pdf.ln()

pdf.set_font("Arial", size=10)

for article in Articles:
    pdf.cell(60, 10, txt=article["Désignation"], border=1)
    pdf.cell(40, 10, txt=str(article["Prix_Unitaire"]), border=1)
    pdf.cell(30, 10, txt=str(article["Quantité"]), border=1)
    pdf.cell(40, 10, txt=str(article["Prix_total"]), border=1)
    pdf.ln()

pdf.output("Facture.pdf")
print("✅ Facture générée avec succès : Facture.pdf")