# Optimisation du Tri : Algorithmes de Comparaison

## Définitions et Problématiques

### Qu'est-ce que trier ?

Trier consiste à organiser un ensemble d'éléments dans un ordre précis (généralement croissant ou décroissant).  
C'est une opération fondamentale en informatique, utilisée dans de nombreux domaines :  

- Classement de données
- Préparation de données pour d'autres algorithmes
- Optimisation des performances de recherche

### Stratégies de Tri

On peut trier des données de plusieurs manières :

- Par comparaison : on compare les éléments entre eux
- Sans comparaison : on utilise des propriétés spécifiques des données

## Tri par Sélection

### Principe

Le tri par sélection consiste à :
1. Trouver le plus petit élément du tableau
2. Le placer au début
3. Recommencer avec le reste du tableau

### Exemple Illustratif

Liste initiale : [5, 2, 4, 6, 1, 3]

| Étapes | Liste en cours | Min sélectionné |
|:------:|:--------------:|:--------------:|
| Début  | [5, 2, 4, 6, 1, 3] | 1 |
| Étape 1 | [1, 2, 4, 6, 5, 3] | 2 |
| Étape 2 | [1, 2, 3, 6, 5, 4] | 3 |
| Final   | [1, 2, 3, 4, 5, 6] | - |

## Tri par Insertion

Le tri par insertion fonctionne comme le tri de cartes à jouer : on prend une carte, on la place au bon endroit dans une main déjà triée.

### Exemple Illustratif

Liste initiale : [5, 2, 4, 6, 1, 3]

| Étapes | Liste en cours | Élément inséré |
|:------:|:--------------:|:--------------:|
| Début  | [5] | 2 |
| Étape 1 | [2, 5] | 4 |
| Étape 2 | [2, 4, 5] | 6 |
| Étape 3 | [1, 2, 4, 5] | 3 |
| Final   | [1, 2, 3, 4, 5, 6] | - |

## Tris Sans Comparaison

### Tri par Dénombrement

Le tri par dénombrement est un algorithme de tri non comparatif qui se concentre sur le comptage des occurrences de chaque élément.  
Son principe repose sur trois étapes essentielles :  

- Premièrement, on parcourt le tableau initial pour déterminer la plage de valeurs des éléments. 
- Deuxièmement, on crée un tableau de comptage où chaque index représente une valeur possible, et on incrémente un compteur correspondant à chaque fois qu'un élément est rencontré. 
- Troisièmement, on reconstruit le tableau trié en utilisant ce tableau de comptage, en reproduisant chaque valeur selon son nombre d'occurrences. 

Cette méthode présente des conditions strictes : elle ne fonctionne qu'avec des données de type entier et nécessite une plage de valeurs limitée.
