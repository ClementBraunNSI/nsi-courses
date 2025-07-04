# Les boucles en python

## Boucles while

La boucle while s'exécute tant qu'une condition est vraie.

```python
while condition:
    # bloc de code à exécuter tant que la condition est vraie
```

**Exemple**

```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur = compteur + 1  # Incrémentation
```

**Fonctionnement**

- Initialisation : compteur = 0
- Condition : La boucle continue tant que conteur < 5
- Incrémenttion : compteur = compteur + 1 permet d'augmenter la valeur de compteur pour qu'elle atteigne 5.

La boucle s'exécutera si compteur vaut 4 mais quand compteur vaudra 5, le code à l'interieur ne sera pas exécuté. 
Si on veut par exemple afficher les nombres jusque 5, on peut utiliser la condition `compteur <= 5`.

## Boucle for

La boucle for permet de parcourir des séquences.

```python
for variable in sequence:
    # Bloc de code à exécuter
```

Il existe différents types de séquences : chaines de caractères, liste d'objets et `range`.

**Exemple avec `range` :**

```python
for i in range(5):
    print(i)
```

**Fonctionnement de range**:

`range(n)` permet de créer une séquence d'éléments telle que $\texttt{range(n)} = [0,n[$ avec $n \in \N$.

**Exemple sur une chaîne de caractère**:

```python
mot = "python"
for lettre in mot:
    print(lettre)
```

Ce bout de code affichera chacune des lettres du mot ici python, les unes après les autres.

```python
p
y
t
h
o
n
```