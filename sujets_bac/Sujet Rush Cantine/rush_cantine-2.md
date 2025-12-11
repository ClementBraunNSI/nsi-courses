---
title: "Épreuve pratique BAC NSI "
author: "DELPLACE Nicolas"
date: "02/12/2025"
---

Les banques alimentaires sont de plus en plus solicité par l'ensemble de la population.
Depuis le printemps 2021 une majorité des centres de distribution d’aide alimentaire déclarent
une augmentation de leur fréquentation – forte (dans 21 % des cas) ou modérée (36 %)  par rapport
à la situation d’avant-crise sanitaire, d’après une enquête réalisée par l’Insee et la DREES.

Des centres de distributions sont souvent fixe mais également mobile. Nous allons essayer d'aider les bénévoles des distributions mobiles.
Ils recoivent une liste d'endroit à visiter pour y distribuer de la soupe et des biens de première nécessité.
Cependant, ils ne savent pas toujours comment aller d'un endroit à un autre ou même si il existe un chemin possible entre deux points.

Il faut donc concevoir une solution qui permette de savoir si deux points sont bien reliés pour assurer la distribution.

Les points de distributions sont modélisés par un **graphe orienté pondéré** représenté par un dictionnaire d'adjacence nommé `distribution`.

* Les **clés** sont les lieux (sommets).
* Les **valeurs** sont des dictionnaires représentant les connexions possibles avec le temps pour s'y rendre: `{destination: temps_en_secondes}`.

```python
distribution = {
    'Gare': {'Mairie': 30, 'Salle de sport': 45},
    'Mairie': {'Gare': 30, 'Lycée': 60, 'Musée': 20},
    'Salle de sport': {'Gare': 45, 'Médiathèque': 10},
    'Médiathèque': {'Salle de sport': 10, 'Lycée': 50},
    'Musée': {'Mairie': 20, 'Piscine': 120},
    'Lycée': {'Mairie': 60, 'Médiathèque': 50, 'Piscine': 15},
    'Piscine': {'Lycée': 15, 'Musée': 120}
}
```

1. **Compréhension du sujet**

**Indiquer** si chacun de ces chemins est possible d'être emprunté?

* Gare, Musée, Piscine
* Escalier, Gare, Salle de sport, Médiathèque, Lycée, Salle de sport, Médiathèque, Lycée, Piscine.
* Piscine
* Musée, Piscine
  
La voierie de la commune décider de rajouter un chemin de la piscine à la salle de sport qui prendrait que 5 minutes.
**Modifier** le graphe `distribution` en rajoutant ce chemin. 


1. **Durée d'un chemin**

On définit un itinéraire comme une liste de chaînes de caractères.
Exemple : `mon_trajet = ['Gare', 'Mairie', 'Musée', 'Piscine']`

**Écrire** la fonction `calculer_duree(graphe, chemin)` qui prend en paramètres le graphe représenté par un dictionnaire et une liste de lieux sous forme de liste de chaînes de caractères.
***Indication: On considère que tous les chemins sont corrects et possibles pour cette fonction à cette étape.***

**Appel 1 : Appeler le professeur pour lui présenter vos réponses et votre fonction ou en cas de difficultés de compréhension de la représentation.**

3. **Tests et vérifications**

Pour valider le fonctionnement 
Votre code de la question 2 doit être vérifié avant d'être utilisé en conditions réelles.

**a)** Écrire une procédure `test_verification()` utilisant le mot-clé `assert` pour vérifier que :
* Le trajet `['Gare', 'Mairie']` renvoie bien `30`.
* Le trajet sur place `['Piscine']` renvoie bien `0`.

**b)** On souhaite maintenant gérer les erreurs. Proposez une modification de la fonction `calculer_duree` (ou réécrivez-la ci-dessous) pour qu'elle renvoie
 `-1` si on essaie de passer entre deux lieux qui ne sont pas connectés (ex: sauter du 3ème étage directement à la Piscine).


## Question 4 : L'Algorithme de la Survie (Dijkstra)
*Objectif : Correction d'un algorithme de plus court chemin.*

On veut cartographier l'ensemble des chemins possible.
Il faut trouver le temps minimal absolu pour aller d'un point de départ vers tous les autres lieux.
> reformuler l'exercice pour que ce soit plus "joli" ?

Corriger l'algorithme de Dijkstra ci-dessous au niveau des instruction A et B.

L'objectif est de remplir la logique de **relâchement** : si on trouve un chemin plus court vers un voisin en passant par le sommet actuel `u`, on met à jour sa distance.

**Travail demandé :** Corriger uniquement la ligne `(Condition A)` et la ligne `(Instruction B)`.
Expliquer les raisons de vos changement.
> **Appel 2**
