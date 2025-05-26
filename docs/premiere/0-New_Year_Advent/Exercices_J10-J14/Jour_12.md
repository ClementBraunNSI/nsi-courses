# Jour 12 🦊❄️🎉 : Le budget du réveillon

Jean veut faire les comptes de la soirée. Il a gardé tous les tickets de caisse et veut répartir les dépenses entre les participants.

## Informations nécessaires

On considère :
- Une **dépense** est représentée par un **dictionnaire** contenant :
  - categorie (str)
  - montant (float)
  - payé_par (str)

```python
depenses = [
    {"categorie": "nourriture", "montant": 150.50, "payé_par": "Jean"},
    {"categorie": "boissons", "montant": 85.30, "payé_par": "Marie"},
    {"categorie": "decoration", "montant": 45.20, "payé_par": "Paul"},
    {"categorie": "musique", "montant": 30.00, "payé_par": "Lucas"},
    {"categorie": "jeux", "montant": 20.00, "payé_par": "Sophie"},
    {"categorie": "transport", "montant": 60.00, "payé_par": "Jean"},
    {"categorie": "nourriture", "montant": 50.00, "payé_par": "Marie"},
    {"categorie": "boissons", "montant": 40.00, "payé_par": "Sophie"},
    {"categorie": "decoration", "montant": 25.00, "payé_par": "Jean"},
    {"categorie": "musique", "montant": 10.00, "payé_par": "Paul"}
]

participants = ["Jean", "Marie", "Paul", "Sophie", "Lucas"]
```

## Exercice Principal

!!! fox_correction "Total par catégorie"
    **Écrire une fonction `total_par_categorie` qui calcule le total des dépenses par catégorie.**

    *Les montants doivent être arrondis à 2 décimales*

!!! fox_correction "Part par personne"
    **Écrire une fonction `calculer_parts` qui calcule combien chaque personne doit payer (répartition équitable du total).**

    *Les montants doivent être arrondis à 2 décimales*

!!! fox_correction "Bilan des comptes"
    **Écrire une fonction `bilan_comptes` qui indique pour chaque personne combien elle doit recevoir ou payer pour équilibrer les comptes.**

    *Les montants doivent être arrondis à 2 décimales*
    *Un montant positif indique que la personne doit recevoir de l'argent*
    *Un montant négatif indique que la personne doit payer*

**Pour valider cet exercice, vous devrez rendre à votre enseignant les trois fonctions ainsi qu'un exemple d'utilisation avec les dépenses fournies.**