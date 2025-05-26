# Jour 11 🦊❄️🎉 : Les photos du réveillon

Jean veut organiser les photos prises pendant la soirée. Chaque photo est représentée par un dictionnaire contenant son nom, sa date, les personnes présentes et sa taille.

## Informations nécessaires

On considère :
- Une **photo** est représentée par un **dictionnaire** contenant :
  - nom (str)
  - date (str)
  - personnes (list de str)
  - taille (float) en Mo

```python
photos = [
    {
        "nom": "IMG_001.jpg",
        "date": "2024-01-01 00:01",
        "personnes": ["Marie", "Paul", "Sophie"],
        "taille": 2.5
    },
    {
        "nom": "IMG_002.jpg",
        "date": "2024-01-01 00:05",
        "personnes": ["Lucas", "Emma"],
        "taille": 1.8
    },
    {
        "nom": "IMG_003.jpg",
        "date": "2024-01-01 00:15",
        "personnes": ["Jean", "Marie"],
        "taille": 3.2
    },
    {
        "nom": "IMG_004.jpg",
        "date": "2024-01-01 00:20",
        "personnes": ["Paul", "Lucas", "Sophie"],
        "taille": 2.7
    },
    {
        "nom": "IMG_005.jpg",
        "date": "2024-01-01 00:25",
        "personnes": ["Jean", "Emma", "Sophie"],
        "taille": 4.0
    },
    {
        "nom": "IMG_006.jpg",
        "date": "2024-01-01 00:30",
        "personnes": ["Marie", "Lucas"],
        "taille": 1.6
    }
]
```

## Exercice Principal

!!! fox_correction "Photos par personne"
    **Écrire une fonction `photos_par_personne` qui prend en paramètre la liste des photos et renvoie un dictionnaire indiquant combien de fois chaque personne apparaît sur les photos.**

!!! fox_correction "Espace total"
    **Écrire une fonction `espace_total` qui calcule l'espace total occupé par les photos en Mo.**

    *Le résultat doit être arrondi à 2 décimales*

!!! fox_correction "Trouver photo"
    **Écrire une fonction `trouver_photos` qui prend en paramètre la liste des photos et une liste de personnes, et renvoie toutes les photos où ces personnes apparaissent ensemble.**

**Pour valider cet exercice, vous devrez rendre à votre enseignant les trois fonctions ainsi qu'un exemple d'utilisation avec les photos fournies.**
