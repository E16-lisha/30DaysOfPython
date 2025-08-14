''''
Nom du fichier : Jour23_Jeu_de_course.py
Projet : Calculer la probalibité que la partie de course entre la tortue et le lièvre soient remportées des deux parties
Objectif : Maitriser la bibliothèque random
Auteur : Elisée N'TSOUKOU
Date : 14/08/2025
Version : 1.0
Communauté : PyCon Togo ( 30 Days of Python)
Dernière Mise à jour :
'''

from random import *
p = 0
q = 0
n=int(input("Entrez le nombre de partie ou le nombre de fois que le jeu se repètre pour connaitre les probabilités : "))

for i in range(n) :
  gagne = 0
  tortue = 0
  while gagne == 0 :
    x = randint(1,6)
    if x == 6 :
      gagne = 1
      p = p + 1
    else :
      tortue = tortue + 1
      if tortue == 6 :
        gagne = -1
        q = q + 1
print("La tortue gagne ",q, "fois et le lièvre gagne ", p , "fois pour",n," parties consécutives")
print("")
print("La probabilité que la tortue gagne est alors de ", q/n , "et celle du lièvre est de ", p/n)