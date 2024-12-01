# Devoir Surveillé 1 : Nombres Binaires et Bases de la programmation

**L'évaluation porte sur 3 exercices indépendants.**
**Les exercices sont notés sur 18 et la rigueur, rédaction et justifications sont notés sur 2 points.**
**La présence des  en-têtes de fonctions ou documentations compte dans les deux points de rigueur.**

## Exercice 1 : Conversions binaire décimal (3 points)

**1. Donner la représentation binaire des nombres en base 10 suivants:**

!!! fox_correction_eval "Correction"
    - $74_{10} = 1001010_2$
    - $132_{10} = 10000100_2$
    - $534_{10} = 1000010110_2$

**2. Donner la représentation décimale des nombres en base 2 suivants:**

!!! fox_correction_eval "Correction"
    - $11010_2 = 26_{10}$
    - $1001101_2 = 77_{10}$
    - $101111010_2 = 378_{10}$

## Exercice 2 : Complétion de code (6 points)

Un nombre est un nombre d'Armstrong si la somme de chacun de ses chiffres, élevés à la puissance de son nombre de chiffre, est égale au nombre lui-même.
Exemple : le nombre 153 comporte 3 chiffres, alors on réalisera : $153 = 1^3 + 5^3 + 3^3$

**Compléter la fonction `nombre_armstrong` qui prend en paramètre un nombre entier et renvoie `True` s'il est un nombre d'Armstrong, `False` sinon.**  
Rappel : la fonction `len(sequence)` permet de donner le nombre d'éléments dans la séquence :  
Exemple $len("Bonjour") = 7$.
$8208 = 8^4 + 2^4+ 0^4+8^4$  
*Exemple : nombre_armstrong(8208) doit renvoyer True.*
!!! fox_correction_eval "Correction"
    ```python
            def nombre_armstrong(nombre : int)-> bool:
                str_nombre = str(nombre)
                somme = 0
                taille = len(nombre)
                for chiffre in str_nombre:
                    int_chiffre = int(chiffre)
                    puissance = int_chiffre **taille
                    somme = somme + puissance
                if somme == nombre:
                    return True
                else:
                    return False
    ```

## Exercice 3 : Écriture de code (9 points)

Le but de cet exercice est de trouver ce que l'on appelle des nombres `parfaits`.

Un nombre est un nombre parfait s'il est égal à la somme de ses diviseurs (hormis lui-même).
*Par exemple 6 est un nombre parfait car : 6 = 1 + 2 + 3 car 1,2 et 3 divisent 6*.

### Les diviseurs

**Écrire une fonction `est_divisible` qui prend en paramètres deux entiers a et b et renvoie `True` si b est divisible par a, `False` sinon.**
*Exemple:*

``` python
    >>> est_divisible(10, 2)
    True
    >>> est_divisible(10, 3)
    False
```

!!! fox_correction_eval "Correction"

    ```python
        def est_divisible(a:int, b:int)->bool:
            if a % b == 0:
                return True
            else:
                return False
    ```


**Compléter la fonction `tous_les_diviseurs` qui prend en paramètre un entier et renvoie une liste contenant tous ses diviseurs ==(lui-même non compris)==.**
Vous utiliserez la fonction précédente.

!!! fox_correction_eval "Correction"

    ```python
        def tous_les_diviseurs(n : int)-> list:
        l = []
            for i in range(n): # Compléter le for
                if n % i == 0 : # Compléter le if
                    l = l + [i]
        return l
    ```

### Nombres parfaits

On dispose d'une fonction `somme_elements_listes` qui donne la somme des éléments d'une liste.
***Elle n'a pas a être réalisée !***
Elle fonctionne ainsi :

```python
        >>> l = [1,2,3,4]
        >>> somme_liste = somme_elements_listes(l)
        >>> print(somme_liste)
        10
```

**Écrire une fonction `est_parfait` qui prend en paramètre un entier n et renvoie `True` s'il est un nombre parfait, `False` sinon. Elle utilisera les fonctions précédentes.**  
*Pour 12, ses diviseurs sont 1,2,3,4 et 6. Comme 1+2+3+4+6 = 16, il n'est pas parfait.*  
*Pour 28, ses diviseurs sont 1,2,4,7,14. Comme 1+2+4+7+14 = 28, il est parfait*  
*Exemple :*  

```python
    >>> est_parfait(28)
    True
    >>> est_parfait(19)
    False
```

!!! fox_correction_eval "Correction"

    ```python
        def est_parfait(n:int)-> bool:
            liste_diviseurs = tous_les_diviseurs(n)
            somme = somme_elements_liste(liste_diviseurs)
            if somme == n:
                return True
            else:
                return False

    ```
**Écrire une fonction `nombres_parfaits_jusqu_a` qui prend en paramètre un entier n et renvoie une chaîne de caractères contenant tous les nombres parfaits de 1 à n (compris) séparés par un espace.**

```python
>>> nombres_parfaits_jusqu_a(3000)
    '6 28 496'
```

!!! fox_correction_eval "Correction"

    ```python

        def nombres_parfaits_jusqu_a(n:int)-> str:
            chaine = ""
            for i in range(1,n+1):
                if est_parfait(n):
                    chaine = chaine + str(i) + " "
            return chaine
    ```

Rappel : une liste est une séquence qui peut être parcourue comme une chaîne de caractères.

```pythonx
    l = [1,3,5,2] # une liste d'entiers
    for elt in l:
        print(l)
    # Va afficher les entiers
    1
    3
    5
    2
```

## Bonus

**Écrire la fonction `somme_elements_listes` qui prend en paramètre une liste d'entiers et renvoie la somme de ses éléments.**

!!! fox_correction_eval "Correction"

    ```python
        def somme_elements_listes(liste : list) -> int:
            somme = 0
            for elt in liste:
                somme = somme + elt
            return somme
    ```