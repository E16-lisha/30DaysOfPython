'''
Nom du fichier : Jour13_List_Compréhension.py
Projet : Tester les fonctions max_liste, est_triangle, compter_mot
Objectif : Appliquer les fonctions, les boucles, les conditions et la gestion de liste
Auteur : Elisée N'TSOUKOU
Date : 04/08/2025
Version : 1.0
Communauté : PyCon Togo (30 Days PyCon)
Dernière Mise à jour :
'''

#Une fonction max_liste qui prend une liste de nombre et retourne le plus grand élément
def max_liste (n) :
    liste = []
    for i in range(1,n+1):
        # Permet de saisir les éléments
        liste.append(int(input(f"Entrez élément {i} de la liste: ")))
    max=0
    for i in liste:
        if i > max :
            max = i
    print("Me maximun de votre liste est : ", max)
    return max


#Une fonction est_triangle qui prend 3 longueurs et retourne "True" si ces longueurs peuvent former un triangle valide
def est_triangle(a,b,c) :
   if a + b > c and a + c > b and b + c > a :
       print("True")
   else :
       print("False")

#Fonction compter_mot qui prend une phrase et retourne le nombre de mots
def compter_mot(mot) :
    casse = mot.split()
    cpt = 0
    for i in casse :
        cpt = cpt + 1
    print(f"'{mot}' contient {cpt} mots.")


print("=" * 70)
print("Programme de test des fonctions Python")
print("=" * 70)

# 1. Test de max_liste
print("\nTest de la fonction max_liste")
taille = int(input("Combien d’éléments voulez-vous dans votre liste ? : "))
max_liste(taille)

# 2. Test de est_triangle
print("\n📐Test de la fonction est_triangle")
a = int(input("Longueur a : "))
b = int(input("Longueur b : "))
c = int(input("Longueur c : "))
est_triangle(a, b, c)

# 3. Test de compter_mot
print("\nTest de la fonction compter_mot")
phrase = input("Entrez une phrase : ")
compter_mot(phrase)

print("=" * 70)
print("Tous les tests sont terminés avec succès !")
print("=" * 70)
