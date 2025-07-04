# Jour 13 🦊❄️🎉 : Les résolutions du Nouvel An

Jean propose à ses invités d'écrire leurs bonnes résolutions pour l'année à venir. Pour rendre le jeu plus amusant, chacun doit aussi estimer ses chances de réussite pour chaque résolution.

## Informations nécessaires

On considère :
- Une **résolution** est représentée par un **dictionnaire** contenant :
  - texte (str)
  - categorie (str) : "sport", "travail", "personnel", "voyage", "autre"
  - chance_reussite (int) : un pourcentage entre 0 et 100
  - delai (str) : "1 mois", "3 mois", "6 mois" ou "1 an"

```python
resolutions = [
    {
        "texte": "Faire du sport 3 fois par semaine",
        "categorie": "sport",
        "chance_reussite": 75,
        "delai": "1 mois",
        "personne": "Marie"
    },
    {
        "texte": "Apprendre le piano",
        "categorie": "personnel",
        "chance_reussite": 40,
        "delai": "1 an",
        "personne": "Paul"
    },
    {
        "texte": "Voyager au Japon",
        "categorie": "voyage",
        "chance_reussite": 60,
        "delai": "6 mois",
        "personne": "Sophie"
    }
]
```

## Exercice Principal

!!! fox_correction "Résolutions optimistes"
    **Écrire une fonction `resolutions_optimistes` qui prend en paramètre la liste des résolutions et renvoie les résolutions dont la chance de réussite est supérieure à 70%.**

    ```python
    >>> optimistes = resolutions_optimistes(resolutions)
    >>> for r in optimistes:
    ...     print(r['personne']+  "est optimiste pour : "+r['texte']+ "("+r['chance_reussite']+"%)")
    Marie est optimiste pour : Faire du sport 3 fois par semaine (75%)
    ```

!!! fox_correction "Statistiques par catégorie"
    **Écrire une fonction `stats_categories` qui prend en paramètre la liste des résolutions et renvoie pour chaque catégorie :**
    - Le nombre de résolutions
    - La moyenne des chances de réussite
    - Le délai le plus fréquent

    *La moyenne doit être arrondie à 2 décimales*

    ```python
    >>> stats = stats_categories(resolutions)
    >>> print(stats["sport"])
    {'nombre': 1, 'moyenne_chances': 75.00, 'delai_frequent': '1 mois'}
    ```

**Pour valider cet exercice, vous devrez rendre à votre enseignant les deux fonctions ainsi qu'un exemple d'utilisation avec les résolutions fournies.**
