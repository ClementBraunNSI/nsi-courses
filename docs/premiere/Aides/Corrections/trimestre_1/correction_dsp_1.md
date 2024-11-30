# DS pratique : Chaine de caractères et Boucles

Cette épreuve pratique compte pour $25\%$ de la note finale.

Les exercices sont sur 8 points chacuns pour un total de 16 points.
Les spécifications et les commentaires de code sont notés sur 2 points.
Appeler l'enseignant pour vérifier chaque fonction et question est noté sur 2 points.

## Exercice 1 (8 points)

**1. Écrire une fonction `renverse` qui prend en paramètre une chaîne de caractère non vide et renvoie une chaîne de caractère inverse de celle passée en paramètre.**

**2. Tester avec les exemples proposés.**

Exemple :

```python
    >>> renverse("informatique")
    "euqitamrofni"
    >>> renverse("Mr Braun c'est le meilleur prof de NSI")
    "ISN ed forp ruelliem el tse'c nuarB rM"
```

!!! fox_correction_eval "Correction"
    ```python
    def renverse(chaine:str)->str:
        chaine_renversee = ""
        for elt in chaine:
            chaine_renversee = elt + chaine_renversee
        return chaine_renversee
    ```

## Exercice 2 (8 points)

Le jeu du "plus ou moins" consiste à deviner un nombre entier choisi entre 1 et 99.

Un élève de NSI décide de le coder en langage Python de la manière suivante : 

- Le programme génère un nombre entier aléatoire compris entre 1 et 99;
- Si la proposition de l'utilisateur est plus petite que le nombre cherché, l'utilisateur est averti dans la console. Il peut en proposer un autre;
- Si la proposition de l'utilisateur est plus grande que le nombre cherché, l'utilisateur est averti dans la console. Il peut en tester un autre;
- Si l'utilisateur trouve le bon nombre en 10 essais ou moins, il gagne;
- Si l'utilisateur a fait plus de 10 essais sans trouver le bon nombre, il perd.

La fonction `randint` du module `random` est utilisée.
Si `a` et `b` sont des entiers tels que `a <= b, randint(a, b)` renvoie un nombre entier compris entre a et b inclus.

**1. Compléter le code ci-dessous et le tester.**

**2. Commenter les différentes partie de la fonction pour indiquer ce que font les différentes parties de la fonction.**

```python {.line-numbers}
    from random import randint

    def plus_ou_moins()-> None:
        nb_mystere = randint(1, ...)
        nb_test = int(input("Proposez un nombre enter 1 et 99 : "))
        compteur = ...
        
        while nb_mystere != ... and compteur < ... :
            compteur = compteur + ...
            if nb_mystere ... nb_test:
                nb_test = int(input("Trop petit ! Testez encore : "))
            else : 
                nb_test = int(input("Trop grand ! Testes encore : "))

        if nb_mystere ... nb_test : 
            print("Bravo ! Le nombre était ", ...)
            print("Nombre d'essais : ", ...)
        else :
            print("Perdu ! Le nombre était ", ...)
```

!!! fox_correction_eval "Correction"
    ```python {.line-numbers}
    from random import randint

    def plus_ou_moins()-> None:
        nb_mystere = randint(1, 99)
        nb_test = int(input("Proposez un nombre enter 1 et 99 : "))
        compteur = 10
        
        while nb_mystere != nb_test and compteur < 10 :
            compteur = compteur + 1
            if nb_mystere > nb_test:
                nb_test = int(input("Trop petit ! Testez encore : "))
            else : 
                nb_test = int(input("Trop grand ! Testes encore : "))

        if nb_mystere == nb_test : 
            print("Bravo ! Le nombre était ", nb_mystere)
            print("Nombre d'essais : ", compteur)
        else :
            print("Perdu ! Le nombre était ", nb_mystere)
    ```
