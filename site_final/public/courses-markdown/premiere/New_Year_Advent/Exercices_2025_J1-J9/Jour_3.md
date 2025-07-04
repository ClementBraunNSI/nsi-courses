# Jour 3 🎊🦊🎉 : Calcul des portions

Pour nourrir tous les invités, il faut calculer les bonnes quantités de nourriture. Chaque plat a des portions recommandées par personne et certains invités ont des régimes spéciaux.

Lucie doit calculer les quantités exactes à prévoir pour éviter le gaspillage.

## Informations nécessaires

On considère :
- Un **plat** est représenté par un **dictionnaire** contenant :
  - nom (str)
  - portion_par_personne (float) en grammes
  - vegetarien (bool)
  - prix_par_kg (float)

```python
plats = [
    {"nom": "Saumon fumé", "portion_par_personne": 80.0, "vegetarien": False, "prix_par_kg": 45.0},
    {"nom": "Foie gras", "portion_par_personne": 50.0, "vegetarien": False, "prix_par_kg": 120.0},
    {"nom": "Salade de quinoa", "portion_par_personne": 120.0, "vegetarien": True, "prix_par_kg": 8.0},
    {"nom": "Rôti de bœuf", "portion_par_personne": 150.0, "vegetarien": False, "prix_par_kg": 25.0},
    {"nom": "Gratin dauphinois", "portion_par_personne": 200.0, "vegetarien": True, "prix_par_kg": 6.0},
    {"nom": "Tarte aux fruits", "portion_par_personne": 100.0, "vegetarien": True, "prix_par_kg": 12.0},
    {"nom": "Fromages", "portion_par_personne": 60.0, "vegetarien": True, "prix_par_kg": 18.0}
]

nb_invites = 12
nb_vegetariens = 3
```

## Exercice Principal

!!! fox_correction "Quantité totale d'un plat"
    **Écrire une fonction `quantite_plat` qui prend en paramètre un plat (dictionnaire), le nombre d'invités total et le nombre de végétariens, et renvoie la quantité totale nécessaire en grammes.**

    *Si le plat n'est pas végétarien, seuls les non-végétariens en consomment.*
    *Si le plat est végétarien, tous les invités en consomment.*

!!! fox_correction "Coût d'un plat"
    **Écrire une fonction `cout_plat` qui prend en paramètre un plat, le nombre d'invités total et le nombre de végétariens, et renvoie le coût total du plat.**

    *Cette fonction doit utiliser la fonction précédente pour calculer la quantité, puis multiplier par le prix au kg.*
    *Le résultat doit être arrondi à 2 décimales.*

!!! fox_correction "Budget total du menu"
    **Écrire une fonction `budget_total_menu` qui prend en paramètre une liste de plats, le nombre d'invités total et le nombre de végétariens, et renvoie le coût total du menu.**

    *Cette fonction doit utiliser la fonction précédente pour chaque plat.*
    *Le résultat doit être arrondi à 2 décimales.*

**Pour valider cet exercice, vous devrez rendre à votre enseignant les trois fonctions ainsi qu'un exemple d'utilisation avec les données fournies.**