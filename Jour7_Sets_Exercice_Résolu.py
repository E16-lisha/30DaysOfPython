'''
Nom du fichier : jour7_exercices_sets.py
Projet : Exercices du jour 7 du challenge 30 Days PyCon - Manipulation des sets
Auteur : Elisée N'TSOUKOU
Date : 29/07/2025
Version : 1.0
Communauté : PyCon Togo (30 Days PyCon)
Dernière Mise à jour :
'''

# -------------------------- Niveau 1 -------------------------- #
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("1. Longueur de l'ensemble IT_COMPANIES :", len(it_companies))

it_companies.add("Twitter")
print("2. Ajout de Twitter :", it_companies)

it_companies.update(["Samsung", "Intel", "Tesla"])
print("3. Ajout de plusieurs entreprises :", it_companies)

it_companies.remove("IBM")
print("4. Suppression de IBM :", it_companies)

print("5. ⚠️ Différence entre remove() et discard() :")
print("- remove() : génère une erreur si l'élément n'existe pas")
print("- discard() : ne génère pas d'erreur même si l'élément n'existe pas")

# -------------------------- Niveau 2 -------------------------- #
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print("6. Union de A et B :", A.union(B))
print("7. Intersection de A et B :", A.intersection(B))
print("8. A est-il un sous-ensemble de B ? :", A.issubset(B))
print("9. A et B sont-ils disjoints ? :", A.isdisjoint(B))
print("10. A.union(B) == B.union(A) :", A.union(B) == B.union(A))
print("11. Différence symétrique A △ B :", A.symmetric_difference(B))

# Suppression des ensembles
del A
del B
print("12. Les ensembles A et B ont été supprimés.")

# -------------------------- Niveau 3 -------------------------- #
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)
print("13. Liste des âges :", ages)
print("    Ensemble des âges (uniques) :", ages_set)
print("    Longueur de la liste :", len(ages))
print("    Longueur de l'ensemble :", len(ages_set))

print("14. Différences entre types de données :")
print("- string : chaîne de texte, ex : 'Hello'")
print("- list   : liste ordonnée et modifiable, ex : [1, 2, 3]")
print("- tuple  : liste non modifiable (immuable), ex : (1, 2, 3)")
print("- set    : ensemble non ordonné avec éléments uniques, ex : {1, 2, 3}")

phrase = "I am a teacher and I love to inspire and teach people"
mots_uniques = set(phrase.split())
print("15. Nombre de mots uniques dans la phrase :")
print("    Phrase :", phrase)
print("    Mots uniques :", mots_uniques)
print("    Total :", len(mots_uniques))
