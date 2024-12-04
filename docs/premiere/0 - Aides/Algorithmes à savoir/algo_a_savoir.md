# Algorithmes à savoir pour le BAC

## Algorithme sur les listes

**Écrire une fonction `presence`qui prend en paramètre une valeur et une liste et renvoie `True` si la valeur demandée est dans la liste, `False` sinon.**
*Exemple :*
*presence(3, [1, 2, 3, 4]) doit renvoyer True.*
*presence(5, [1, 2, 3, 4]) doit renvoyer False.*

!!! fox_correction "Algorithme de recherche d'une valeur"

    ```python
        def presence(liste:list[int], val:int)->int:
            present = False
            for elt in liste:
                if elt == valeur:
                    mini = elt
            return mini
    ```

**Écrire une fonction `minimum` qui prend une liste d'entiers et renvoie l'entier minimum.**  
*Exemple :*  
*max_et_min([3, 1, 9, 2]) doit renvoyer 1.*

!!! fox_correction "Algorithme de recherche du minimum d'une liste"

    ```python
        def minimum(liste:list[int])->int:
            mini = liste[0]
            for elt in liste:
                if elt < mini:
                    mini = elt
            return mini
    ```

**Écrire une fonction `maximum` qui prend une liste d'entiers et renvoie l'entier maximum.**  
*Exemple :*  
*max_et_min([3, 1, 9, 2]) doit renvoyer 9.*

!!! fox_correction "Algorithme de recherche du maximum d'une liste"

    ```python
        def maximum(liste:list[int])->int:
            maxi = liste[0]
            for elt in liste:
                if elt > maxi:
                    maxi = elt
            return maxi
    ```

**Écrire une fonction `indice_minimum` qui prend une liste d'entiers et renvoie l'indice de l'entier minimum.**  
*Exemple :*  
*max_et_min([3, 1, 9, 2]) doit renvoyer 1.*

!!! fox_correction "Algorithme de recherche de l'indice du minimum d'une liste"

    ```python
        def indice_minimum(liste:list[int])->int:
            mini = liste[0]
            indice = 0
            for i in range(len(liste)):
                if liste[i] < mini:
                    mini = liste[i]
                    indice = i
            return indice
    ```

**Écrire une fonction `indice_maximum` qui prend une liste d'entiers et renvoie l'indice de l'entier maximum.**  
*Exemple :*  
*max_et_min([3, 1, 9, 2]) doit renvoyer 2.*

!!! fox_correction "Algorithme de recherche de l'indice du minimum d'une liste"

    ```python
        def indice_maximum(liste:list[int])->int:
            maxi = liste[0]
            indice = 0
            for i in range(len(liste)):
                if liste[i] > maxi:
                    maxi = liste[i]
                    indice = i
            return indice
    ```

## Algorithmes avancés sur les listes

**Écrire une fonction `recherche_dichotomique` qui prend en paramètre une liste et un entier et renvoie `True` si la valeur demandée est dans la liste, `False` sinon. Elle devra utiliser le pricipe de la dichotomie**
*Exemple :*
*recherche_dichotomique(3, [1, 2, 3, 4]) doit renvoyer True.*
*recherche_dichotomique(5, [1, 2, 3, 4]) doit renvoyer False.*

**Écrire une fonction `tri_selection` qui prend en paramètre une liste et renvoie une liste correspondant à sa permutation triée dans l'ordre croissant**
*Exemple:*
*tri_selection([5,2,4,1,3]) doit renvoyer [1,2,3,4,5]*
*tri_selection([]) doit renvoyer []*

**Écrire une fonction `tri_insertion` qui prend en paramètre une liste et renvoie une liste correspondant à sa permutation triée dans l'ordre croissant**
*Exemple:*
*tri_insertion([5,2,4,1,3]) doit renvoyer [1,2,3,4,5]*
*tri_insertion([]) doit renvoyer []*