# Jour 10 🎉🦊🎉 : Bilan financier

Après la soirée, il faut faire le bilan financier complet. Qui a payé quoi, qui doit de l'argent à qui, et comment équilibrer les comptes de manière optimale.

Sophie doit calculer les remboursements nécessaires entre tous les participants.

## Informations nécessaires

On considère :
- Une **dépense** est représentée par un **dictionnaire** contenant :
  - description (str)
  - montant (float)
  - payé_par (str)
  - beneficiaires (list) : liste des noms des personnes qui bénéficient de cette dépense

```python
depenses = [
    {"description": "Courses alimentaires", "montant": 180.50, "payé_par": "Sophie", "beneficiaires": ["Sophie", "Marc", "Julie", "Pierre", "Anna"]},
    {"description": "Boissons", "montant": 95.30, "payé_par": "Marc", "beneficiaires": ["Sophie", "Marc", "Julie", "Pierre", "Anna"]},
    {"description": "Décoration", "montant": 45.20, "payé_par": "Julie", "beneficiaires": ["Sophie", "Marc", "Julie", "Pierre", "Anna"]},
    {"description": "Taxi Pierre", "montant": 25.00, "payé_par": "Sophie", "beneficiaires": ["Pierre"]},
    {"description": "Taxi Anna", "montant": 30.00, "payé_par": "Marc", "beneficiaires": ["Anna"]},
    {"description": "Musique streaming", "montant": 12.99, "payé_par": "Julie", "beneficiaires": ["Sophie", "Marc", "Julie", "Pierre", "Anna"]},
    {"description": "Nettoyage", "montant": 80.00, "payé_par": "Anna", "beneficiaires": ["Sophie", "Marc", "Julie", "Pierre", "Anna"]}
]

participants = ["Sophie", "Marc", "Julie", "Pierre", "Anna"]
```

## Exercice Principal

!!! fox_correction "Calcul de la part individuelle"
    **Écrire une fonction `part_individuelle_depense` qui prend en paramètre une dépense et renvoie le montant que chaque bénéficiaire doit pour cette dépense.**

    *Le montant doit être réparti équitablement entre tous les bénéficiaires.*
    *Arrondir à 2 décimales.*

!!! fox_correction "Total payé par personne"
    **Écrire une fonction `total_paye_par_personne` qui prend en paramètre une liste de dépenses et un nom de personne, et renvoie le montant total que cette personne a payé.**

    *Additionner tous les montants des dépenses payées par cette personne.*

!!! fox_correction "Total dû par personne"
    **Écrire une fonction `total_du_par_personne` qui prend en paramètre une liste de dépenses et un nom de personne, et renvoie le montant total que cette personne doit.**

    *Pour chaque dépense où la personne est bénéficiaire, ajouter sa part (utiliser la première fonction).*
    *Arrondir à 2 décimales.*

!!! fox_correction "Bilan par personne"
    **Écrire une fonction `bilan_par_personne` qui prend en paramètre une liste de dépenses et un nom de personne, et renvoie le solde de cette personne (positif si elle doit recevoir, négatif si elle doit payer).**

    *Solde = Total payé - Total dû*
    *Arrondir à 2 décimales.*

**Pour valider cet exercice, vous devrez rendre à votre enseignant les quatre fonctions ainsi qu'un exemple d'utilisation montrant le bilan de chaque participant.**