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

Au début de l'algorithme, on cherche la plus petite valeur de la liste et on l'échange avec la valeur située à la première position.  
À partir de cette itération, on considère que la liste à trier est composée d'**une partie triée composée d'un élément** et **une partie non triée**.  
On va chercher à chaque itération du tri, on va chercher la valeur la plus petite de la zone non triée et on va la placer au début de celle-ci.  
Comme les valeurs de la zone non triée sont plus grandes que toutes les valeurs de la zone triée car sinon elles auraient été selectionnées, cette valeur se rajoute à la zone triée et ainsi de suite.  

### Exemple Illustratif

Liste initiale : [5, 2, 4, 6, 1, 3]

| Étapes  |   Liste en cours   | Min sélectionné |
|:-------:|:------------------:|:---------------:|
|  Début  | [5, 2, 4, 6, 1, 3] |        1        |
| Étape 1 | [1, 2, 4, 6, 5, 3] |        2        |
| Étape 2 | [1, 2, 3, 6, 5, 4] |        3        |
|   ...   |        ...         |       ...       |
|  Final  | [1, 2, 3, 4, 5, 6] |        -        |

### En Python

On va avoir besoin de **trois fonctions** :

- une fonction `indice_minimum_tranche` qui trouve l'indice du minimum dans une portion de la liste triée.
- une fonction `echange_valeur` qui échange la valeur à l'indice du début de la zone non triée avec celle qui est la plus petite.
- une fonction `tri_selection` qui va réaliser le tri et renvoyer la permutation triée de la liste.

!!! fox_exercice_important "Indice de la valeur minimum dans une tranche"
    **Écrire une fonction `indice_minimum_tranche` qui prend en paramètres une liste, un indice de début et un indice de fin et qui renvoie l'indice de la valeur la plus petite dans la tranche donnée.**  
    *Attention, cette fonction doit bien vérifier que les indices soient bien compris dans la liste pour éviter les erreurs de* ***Out Of Range****.*  
    *Exemple:*  
    ```python
    >>>liste = [1,5,2,4,0,8]
    >>> indice_minimum_tranche(liste,1,4)
    4
    ```

!!! fox_exercice_important "Échange de valeur à l'aide des indices"
    **Écrire une fonction `echange_valeur` qui prend en paramètre une liste et deux indices et échange les positions des deux valeurs dans la liste**  
    *Attention, cette fonction fait une modification par effet de bord et ne renvoie rien.*  
    *Exemple:*  
    ```python
    >>>liste = [1,5,2,4,0,8]
    >>>echange_valeur(liste, 0, 4)
    >>>print(liste)
    [0,5,2,4,1,8]
    ```

!!! fox_exercice_important "Tri par sélection du minimum"
    **Écrire une fonction `tri_selection_minimum` qui prend en paramètre une liste et renvoie sa permutation triée.**  
    *Attention, on ne doit pas modifier la liste passée en paramètre car cela pourrait la changer dans toute la suite du programme et il peut y avoir des cas d'usage où cette liste ne doit pas être modifiée.*  
    *Exemple:*  
    ```python
    >>>liste = [1,5,2,4,0,8]
    >>>print(tri_selection_minimum(liste))
    [0,1,2,4,5,8]
    ```

## Tri par Insertion

Le tri par insertion fonctionne comme le tri de cartes à jouer : on prend une carte, on la place au bon endroit dans une main déjà triée.

### Exemple Illustratif

Liste initiale : [5, 2, 4, 6, 1, 3]

| Étapes  |   Liste en cours   | Élément inséré |
|:-------:|:------------------:|:--------------:|
|  Début  | [5, 2, 4, 6, 1, 3] |       -        |
| Étape 1 | [2, 5, 4, 6, 1, 3] |       2        |
| Étape 2 | [2, 4, 5, 6, 1, 3] |       4        |
| Étape 3 | [2, 4, 5, 6, 1, 3] |       6        |
| Étape 4 | [1, 2, 4, 5, 6, 3] |       1        |
| Étape 5 | [1, 2, 3, 4, 5, 6] |       3        |
|  Final  | [1, 2, 3, 4, 5, 6] |       -        |

## Tris Sans Comparaison

### Tri par Dénombrement

Le tri par dénombrement est un algorithme de tri non comparatif qui se concentre sur le comptage des occurrences de chaque élément.  
Son principe repose sur trois étapes essentielles :  

- Premièrement, on parcourt le tableau initial pour déterminer la plage de valeurs des éléments.  
- Deuxièmement, on crée un tableau de comptage où chaque index représente une valeur possible, et on incrémente un compteur correspondant à chaque fois qu'un élément est rencontré.  
- Troisièmement, on reconstruit le tableau trié en utilisant ce tableau de comptage, en reproduisant chaque valeur selon son nombre d'occurrences.  

Cette méthode présente des conditions strictes : elle ne fonctionne qu'avec des données de type entier et nécessite une plage de valeurs limitée.
