
def imc_maigreur() :
    print("Ton IMC est inférieur à 18.5,  ce qui signifie que tu es en insuffisance pondérale. Cela peut affaiblir ton système \nimmunitaire et causer fatigue, carences ou fragilité musculaire.")
    print("+" * 50)
    print("  -----------------")
    print("| RECOMMENDATIONS |")
    print("  -----------------")
    print("- Mange plus souvent et augmente tes portions avec des aliments riches en nutriments (avocats, fruits secs, céréales complètes)."
          "C\n- onsomme des protéines à chaque repas (œufs, légumineuses, laitages)."
          "\n- Dors suffisamment et réduis ton niveau de stress."
          "\n- Fais du sport doux pour développer ta masse musculaire."
          "\n- Consulte un médecin ou un nutritionniste si nécessaire.")

def imc_normal () :
    print("Ton IMC se situe entre 18.5 et 24.9, ce qui indique un poids normal et un bon équilibre corporel. \nC’est une zone de santé idéale à maintenir.")
    print("+"*50)
    print("  -----------------")
    print("| RECOMMENDATIONS |")
    print("  -----------------")
    print("- Continue à avoir une alimentation variée et équilibrée."
        "\n- Bois suffisamment d’eau chaque jour (au moins 1,5 L)."
        "\n- Pratique une activité physique régulière (30 min par jour minimum)."
        "\n- Évite les excès de sucre, sel et graisses saturées"
        "\n- Fais des bilans de santé réguliers pour surveiller ton état général.")

def imc_surpoids() :
    print("Un IMC compris entre 24,9 et 29,9 indique un surpoids, ce qui signifie que ton poids dépasse légèrement la norme et pourrait, \nà long terme, poser des risques pour la santé.")
    print("+" * 50)
    print("  -----------------")
    print("| RECOMMENDATIONS |")
    print("  -----------------")
    print("- Réduis la consommation d’aliments riches en sucre et en graisses saturées."
          "\n- Privilégie les fruits, légumes, céréales complètes et protéines maigres."
          "\n- Augmente ton activité physique (au moins 45 minutes, 3 à 5 fois par semaine)."
          "\n- Évite les grignotages entre les repas et mange à des heures régulières."
          "\n- Consulte un professionnel de santé ou un nutritionniste pour un suivi personnalisé.")


def imc_obesite_mod() :
    print("Un IMC compris entre 29,9 et 40 indique une situation d’obésité, qui augmente les risques de maladies cardiovasculaires, de \ndiabète, d’hypertension et d’autres complications.")
    print("+" * 50)
    print("  -----------------")
    print("| RECOMMENDATIONS |")
    print("  -----------------")
    print("- Consulte rapidement un médecin ou un nutritionniste pour un bilan de santé complet."
        "\n- Adopte une alimentation équilibrée et contrôlée en calories."
        "\n- Limite les produits industriels, le sucre raffiné et les aliments trop gras."
        "\n- Intègre une activité physique régulière adaptée à ton condition physique (marche, natation, vélo…)."
        "\n- Bois suffisamment d’eau (au moins 1,5L/jour) et dors suffisamment."
        "\n- Fixe-toi des objectifs progressifs avec un accompagnement professionnel.")

def imc_obesite_severe() :
    print( "Un IMC supérieur à 40 correspond à une obésité morbide ou sévère, un état de santé critique pouvant entraîner des "
           "\ncomplications graves comme les maladies cardiaques, le diabète de type 2, l’apnée du sommeil ou certains cancers.")
    print("+" * 50)
    print("  -----------------")
    print("| RECOMMENDATIONS |")
    print("  -----------------")
    print("Consulte immédiatement un médecin pour un suivi spécialisé (nutrition, métabolisme, chirurgie bariatrique si nécessaire)." 
        "\n- Établis un plan de perte de poids encadré par un professionnel de santé (nutritionniste, diététicien).Réduis les aliments transformés, "
        "\n- les boissons sucrées et adopte une alimentation riche en légumes, fibres, et protéines maigres. "
        "\n- Commence une activité physique adaptée, même douce (marche, exercices en piscine)."
        "\n- Surveille ton état psychologique (l’obésité sévère peut impacter le moral), et cherche un accompagnement si besoin."
        "\n- Fixe-toi des objectifs réalistes et durables : chaque kilo perdu est un pas vers une meilleure santé")



Taille = float(input("Entrez votre taille en m : "))
Poids = float(input("Entrez votre poids en Kg : "))
IMC = Poids/(Taille**2)
print(f"Ton IMC = {IMC:.2f}")
if IMC <18.5 :
    imc_maigreur()
if IMC >= 18.5 and IMC<=24.9 :
    imc_normal()
if IMC >= 24.9 and IMC<=29.9 :
    imc_surpoids()
if IMC >= 29.9 and IMC <= 40 :
    imc_obesite_mod()
if IMC >40 :
    imc_obesite_severe()