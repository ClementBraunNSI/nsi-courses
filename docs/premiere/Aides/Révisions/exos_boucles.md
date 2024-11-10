# Révisions boucles

## ASCII Art

L’ASCII art est une forme d’art numérique qui utilise les caractères de la table ASCII pour créer des images ou des illustrations.

### Exemples :

Quelles formes géométriques sont affichées à l'aide de ces fonctions ?

```python

    def f1(n:int) -> None:
        for i in range(n):
            ligne = "*"*n
            print(ligne)
    
    def f2(n:int) -> None:
        for i in range(1,n+1):
            ligne = "*"*i
            print(ligne)

    def f3(n:int) -> None:
        for i in range(n):
            ligne = " "*i + "\\"
            print(ligne)
```

### Exercices

Écrire les fonctions qui permettent d'obtenir les figures suivantes: 

```python
    >>> triangle2(3)

    ***
    **
    *
```

```python
    >>> carre_creux(4)

    ****
    *  *
    *  *
    ****

    # Aide

    def carre_creux(n):
        ligne='#'*......
        print(..............)
        for i in range(.......):
            ligne=..........
            print(.........)
        ligne=...........
        print(...........)
```

```python
    >>> triangle3(3)

    ***
     **
      *

    # Aide

    def triangle3(n):
        for i in range(n):
            ligne=.............
            print(..........)
```

```python
    >>> diagonale2(3)

          /
         /
        /  
```

```python
    >>> pyramide(3)

          *
         ***
        *****

    >>> pyramide(4)

           *
          ***
         *****
        *******
```

```python
    >>> losange(3)

          @
         @@@
        @@@@@
         @@@
          @

    >>> losange(4)

           @
          @@@
         @@@@@
        @@@@@@@
         @@@@@
          @@@
           @
```