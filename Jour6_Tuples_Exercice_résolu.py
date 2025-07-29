''''
Nom du fichier : Jour6_Tuples_Exercice_résolu.py
Projet : Manipuler le tupkes
Auteur : Elisée N'TSOUKOU
Date :  2_/07/2025
Version : 1.0
Communauté : PyCon Togo ( 30 Days Pycon)
Dernière Mise à jour :

'''

# 1. Créons un tuple vide
empty_tuple = ()
print("1. Tuple vide :", empty_tuple)

# 2. Créons un tuple contenant des noms de vos sœurs et de vos frères
soeurs = ("Aïcha", "Nadia", "Fatou")
freres = ("Koffi", "Junior", "Élie")

# 3. Rejoignons les tuples des frères et sœurs
freres_et_soeurs = soeurs + freres
print("3. Frères et Sœurs :", freres_et_soeurs)

# 4. Le nombre de frères et soeurs que nous avons au total :
print("4. Nombre total :", len(freres_et_soeurs))

# 5. Modifions le tuple des frères et sœurs en ajoutant les parents
# (Comme les tuples sont immuables, on crée un nouveau)
parents = ("Papa", "Maman")
Family_Members = freres_et_soeurs + parents
print("5. Famille complète :", Family_Members)

# Niveau 2

# 1. Déballons les frères, sœurs et parents
a, b, c, d, e, f, g, h = Family_Members
print("Niveau 2.1 - Parents :", g, h)
print("Niveau 2.1 - Frères et Sœurs :", a, b, c, d, e, f)

# 2. Créons des fruits, des légumes et des produits d'origine animale (sous forme de tuples)
fruits = ("banane", "mangue", "orange")
legumes = ("carotte", "chou", "tomate")
animaux = ("poisson", "poulet", "lait")

# Fusionons les trois dans un seul tuple
food_stuff_tp = fruits + legumes + animaux
print("2. Food Stuff Tuple :", food_stuff_tp)

# 3. Convertir en liste
Food_Stuff_LT = list(food_stuff_tp)
print("3. Food Stuff Liste :", Food_Stuff_LT)

# 4. Couper l’article moyen (milieu)
milieu = len(Food_Stuff_LT) // 2
print("4. Élément du milieu :", Food_Stuff_LT[milieu])

# 5. Slice : 3 premiers et 3 derniers éléments
print("5. Premiers éléments :", Food_Stuff_LT[:3])
print("5. Derniers éléments :", Food_Stuff_LT[-3:])

# 6. Supprimons le tuple food_stuff_tp
del food_stuff_tp
print("6. Tuple supprimé.")

# 7. Vérifions si un élément existe dans un tuple
pays_nordiques = ("Danemark", "Suède", "Finlande", "Islande", "Norvège", "Estonie")

print("7. 'estonie' est-il un pays nordique ?", "Estonie" in pays_nordiques)
print("7. 'Iceland' est-il un pays nordique ?", "Islande" in pays_nordiques)
