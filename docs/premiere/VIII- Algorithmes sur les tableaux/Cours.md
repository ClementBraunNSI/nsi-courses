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

On considère que la liste à trier est composée d'**une partie triée composée d'un élément** et **une partie non triée**.  
On va chercher à chaque itération `i` du tri, on va chercher à déplacer la valeur que l'on retrouve à la position `i` à sa bonne position dans la zone triée.  
Comme les valeurs de la zone non triée sont plus grandes que toutes les valeurs de la zone triée car sinon elles auraient été selectionnées, cette valeur se rajoute à la zone triée et ainsi de suite.  

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

### En Python

On va avoir besoin de **trois fonctions** :

- une fonction `echange_valeur` qui échange la valeur à l'indice du début de la zone non triée avec celle qui est la plus petite.
- une fonction `insertion` qui échange les valeurs dans la partie triée petit à petit jusqu'à trouver la bonne position.
- une fonction `tri_insertion` qui va réaliser le tri et renvoyer la permutation triée de la liste.

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

!!! fox_exercice_important "Insertion d'une valeur dans une zone triée"
    **Écrire une fonction `insertion_zone_triee` qui prend en paramètre une liste, et un indice correspondant à celui de la valeur qui est juste après la zone triée. Cette fonction échange la valeur à l'indice avec celles qui sont avant elles pour trouver sa bonne place.**
    *Attention, cette fonction doit bien vérifier que les indices soient bien compris dans la liste pour éviter les erreurs de* ***Out Of Range****.*  
    *Exemple:*  
    ```python
    >>>liste = [1,5,2,4,0,8]
    >>>insertion_zone_triee(liste,2)
    >>>print(liste)
    [1,2,5,4,0,8]
    ```

!!! fox_exercice_important "Tri par sélection du minimum"
    **Écrire une fonction `tri_insertion` qui prend en paramètre une liste et renvoie sa permutation triée.**  
    *Attention, on ne doit pas modifier la liste passée en paramètre car cela pourrait la changer dans toute la suite du programme et il peut y avoir des cas d'usage où cette liste ne doit pas être modifiée.*  
    *Exemple:*  
    ```python
    >>>liste = [1,5,2,4,0,8]
    >>>print(tri_insertion(liste))
    [0,1,2,4,5,8]
    ```

## Tris Sans Comparaison

### Tri par Dénombrement

Le tri par dénombrement est un algorithme de tri qui n'agit pas par comparaisons mais par comptage des éléments de la liste.

Exemple : Dans la liste L **[3,2,1,2]**, on peut dénombrer les valeurs de cette manière : une occurence de 1, deux occurences de 2 et une occurence de 3.

*Principe de fonctionnement :*
On considère la liste L précédente:

* On créée une liste d'occurences contenant un nombre de 0 équivalent à la valeur maximale + 1 de la liste à trier et une liste vide qui contiendra, à la fin, les éléments de la liste de départ triés.


    **L = [3, 2, 1, 2]
    occurences = [0,0,0,0]
    liste_triee = []**


* On parcourt la liste L à trier et à chaque élément, on incrémente la valeur à l'indice du nombre rencontré dans la liste d'occurences.

| itération | L                | occurences   |
| --------- | ---------------- | ------------ |
| 0         | [3,2,1,2]        | [0, 0, 0, 0] |
| 1         | [**3**, 2, 1, 2] | [0, 0, 0, 1] |
| 2         | [3, **2**, 1, 2] | [0, 0, 1, 1] |
| 3         | [3, 2, **1**, 2] | [0, 1, 1, 1] |
| 4         | [3, 2, 1, **2**] | [0, 1, 2, 1] |
  

* On peuple la liste vide de $x$ fois le nombre rencontré en balayant la liste d'occurences.

| itération | occurences       | liste_triee |
| --------- | ---------------- | ----------- |
| 1         | [**0**, 1, 2, 1] | []          |
| 2         | [0, **1**, 2, 1] | [1]         |
| 3         | [0, 1, **2**, 1] | [1, 2, 2]   |
| 4         | [0, 1, 2, **1**] | [1,2,2,3]   |
