# Jour 4 🎊🦊🎉 : Organisation des tables

Pour que la soirée se déroule bien, il faut organiser les places à table. Certains invités se connaissent bien, d'autres moins, et il faut éviter les conflits tout en favorisant les bonnes ambiances.

Thomas doit créer un plan de table optimal pour ses 16 invités.

## Informations nécessaires

On considère :
- Un **invité** est représenté par un **dictionnaire** contenant :
  - nom (str)
  - age (int)
  - affinites (list) : liste des noms des personnes qu'il apprécie
  - incompatibilites (list) : liste des noms des personnes à éviter

```python
invites = [
    {"nom": "Alice", "age": 25, "affinites": ["Bob", "Charlie"], "incompatibilites": ["Eve"]},
    {"nom": "Bob", "age": 28, "affinites": ["Alice", "Diana"], "incompatibilites": []},
    {"nom": "Charlie", "age": 22, "affinites": ["Alice", "Frank"], "incompatibilites": ["Grace"]},
    {"nom": "Diana", "age": 30, "affinites": ["Bob", "Eve"], "incompatibilites": []},
    {"nom": "Eve", "age": 26, "affinites": ["Diana", "Frank"], "incompatibilites": ["Alice"]},
    {"nom": "Frank", "age": 29, "affinites": ["Charlie", "Eve"], "incompatibilites": []},
    {"nom": "Grace", "age": 24, "affinites": ["Henry"], "incompatibilites": ["Charlie"]},
    {"nom": "Henry", "age": 27, "affinites": ["Grace"], "incompatibilites": []}
]

places_par_table = 4
```

## Exercice Principal

!!! fox_correction "Nombre de tables nécessaires"
    **Écrire une fonction `nombre_tables` qui prend en paramètre le nombre d'invités et le nombre de places par table, et renvoie le nombre minimum de tables nécessaires.**

    *Utiliser la division entière et gérer le cas où il reste des places.*

!!! fox_correction "Vérifier compatibilité"
    **Écrire une fonction `verifier_compatibilite` qui prend en paramètre deux noms d'invités et la liste des invités, et renvoie True si les deux personnes peuvent être à la même table.**

    *Deux personnes sont compatibles si aucune des deux n'a l'autre dans sa liste d'incompatibilités.*

!!! fox_correction "Affinités communes"
    **Écrire une fonction `affinites_communes` qui prend en paramètre une liste de noms d'invités (une table) et la liste complète des invités, et renvoie le nombre total d'affinités satisfaites à cette table.**

    *Une affinité est satisfaite quand deux personnes qui s'apprécient sont à la même table.*
    *Attention à ne pas compter deux fois la même affinité (A apprécie B = B apprécie A).*

**Pour valider cet exercice, vous devrez rendre à votre enseignant les trois fonctions ainsi qu'un exemple d'utilisation avec les données fournies.**