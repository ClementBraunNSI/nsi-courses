# Les blocs if en Python

## La structure d'un if

Le bloc if permet de réaliser des traitements suivant des conditions.
Le code à réaliser dans le bloc if doit être indenté pour être pris en charge. Sinon, il sera réalisé dans tous les cas.

```python
    if condition:
        # Bloc de code à exécuter si la condition est validée.
```

**Exemple**

```python
age = 18
if age >= 18:
    print("Vous êtes majeurs")
```

## Le else (sinon)

Le bloc else permet de réaliser un traitement si la condition proposée par le if n'est pas validée.
Ce bloc est facultatif si jamais il n'y a pas de traitement spécial à réaliser dans l'autre cas.

```python

if condition:
    # Traitement si la condition est vraie
else:
    # Traitement dans tous les autres cas
```

**Exemple:**

```python
age = 16
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")
```

## Le elif (sinon si)

Le elif permet de tester une condition supplémentaire si la précédente est fausse.

Il est possible d'enchaîner plusieurs elif.

```python
note = 15
if note >= 16:
    print("Très bien")
elif note >= 12:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Peut mieux faire")
```

## Les if imbriqués

Il est possible de mettre des blocs if dans d'autres blocs if.
Cela permet de préciser certains cas d'utilisation.

```python
age = 25
citoyen = True
if age >= 18:
    if citoyen:
        print("Vous pouvez voter.")
    else:
        print("Vous ne pouvez pas voter.")
```