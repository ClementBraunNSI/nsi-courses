# Interrogation : Fonctions en python

**L'évaluation porte sur 3 exercices indépendants.**
**Les exercices sont notés sur 18 et la rigueur, rédaction et justifications sont notés sur 2 points.**
**La présence des  en-têtes de fonctions ou documentations compte dans les deux points de rigueur.**

## Exercice 1 : Étude de fonction : Suite de Fibonacci et Bonnes pratiques (3 points)

La suite de Fibonacci est une séquence de nombres où chaque terme est la somme des deux termes précédents.  

Elle commence généralement par 0 et 1, puis chaque terme suivant est calculé comme :

$F(n) = F(n-1) + F(n-2)$
$$F(0) = 0\newline F(1) = 1\newline F(2) = 1 + 0 = 1\newline F(3) = 1 + 1 = 2\newline
\cdots$$

```python
    def f(n):
        x = 0
        y = 1
        chaine = ''
        for i in range(n):
            print(x)
            y = x + y
            x = y - x
```

Cette fonction ne répond pas aux bonnes pratiques de développement.

1) **Quels principes des bonnes pratiques de développement ne sont pas respectés par cette fonction? Les corriger.**

!!! fox_correction_eval Correction
    Le nom de la fonction n'est pas explicite, les noms de variable non plus.
    La signature de fonction ou la spécification n'est pas non plus présente.

2) **Quels sont les affichages réalisés dans la boucle lorsque l'on souhaite afficher `f(7)`**

!!! fox_correction_eval Correction
    
    ```python
    >>> f(7)
    0
    1
    1
    2
    3
    5
    8
    ```


3) **Modifier la fonction en ajoutant chacune des valeurs de `x` dans la chaîne de caractères `chaine` et la renvoyer. (Si possible rajouter un espace à chaque itération dans `chaine`.)**

!!! fox_correction_eval Correction
    
    ```python
        def fibonacci(n:int)-> None:
            x = 0
            y = 1
            chaine = ''
            for i in range(n):
                chaine = chaine + x + ' '
                y = x + y
                x = y - x
            return chaine
    ```
    


<br>
<br>
<br>
<br>
<br>
<br>

## Exercice 2 : Complétion de code (3 points)

**Compléter la fonction `nombres_diviseurs` qui prend en paramètre un entier et renvoie son nombre de diviseurs.**  
Rappel : Un chiffre/nombre A est un diviseur d'un autre nombre B si le reste de la division euclidienne de B par A est 0.  
*L'opérateur `%` permet d'avoir le reste de la division de deux nombres.*  
*Exemple :*  
*nombre_diviseurs(6) doit renvoyer 4 (car ses diviseurs sont 1,2,3 et 6).*  
*nombre_diviseurs(10) doit renvoyer 4 (car ses diviseurs sont 1,2,5 et 10).* 

```python
    def nombres_diviseurs(n : int) -> int:
        compteur = ...
        for i in range(...):
            if ... :
                compteur = ...
        return ...
```

!!! fox_correction_eval Correction
    
    ```python
    def nombres_diviseurs(n : int) -> int:
        compteur = 0
        for i in range(n):
            if n % i == 0 :
                compteur = compteur + 1
        return compteur
    ```

## Exercice 3 : Écriture de programmes simples (12 points)

**Écrire une fonction `puissance_nombre` qui prend en paramètres deux entiers par exemple a et b et renvoie a à la puissance b.**  
Contrainte : Vous ne devez pas utiliser l'opérateur `**` mais utiliser une boucle.  
*Exemple :*
*puissance_nombre(3,3) doit renvoyer 27.*
*puissance_nombre(2,5) doit renvoyer 32.*

!!! fox_correction_eval Correction
    
    ```python
    def puissance_nombre(a:int, b:int)->int:
        res = 1
        for i in range(b):
            res = res * a
        return res
    ```

**Écrire une fonction `valeur_absolue` qui prend en paramètre un entier et renvoie sa valeur absolue (entier).**
Rappel : La valeur absolue d'un nombre correspond à la valeur positive du nombre. Si le nombre est positif, sa valeur absolue est la même que sa valeur, s'il est négatif, elle correspond à sa valeur positive.
*Exemple:*
*valeur_absolue(8) doit renvoyer 8.*
*valeur_absolue(-56) doit renvoyer 56.*

!!! fox_correction_eval Correction
    
    ```python
    def valeur_absolue(a:int)->int:
        if a < 0 : 
            return -1 * a
        else:
            return a
    ```

**Écrire une fonction `somme_chiffres` qui prend en paramètre une chaîne de caractère représentant un entier positif et renvoie la somme de ses chiffres (entier).**
*Exemple :*  
*somme_chiffres('1234') doit renvoyer 10 (car 1+2+3+4 = 10).*  
*somme_chiffres('56789') doit renvoyer 35 (car 5+6+7+8+9 = 35)*

!!! fox_correction_eval Correction
    
    ```python
    def somme_chiffres(chaine : str)->int:
        res = 0
        for chiffre in chaine:
            res = res + int(chiffre)
        return res
    ```
