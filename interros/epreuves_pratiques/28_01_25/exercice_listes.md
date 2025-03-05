# Exercice : Manipulation de Listes

## Recherche d'éléments dans une liste

### Exercice 1 : Trouver le Plus Grand

**Écrire une fonction `trouve_maximum` qui prend en paramètre une liste de nombres et renvoie la plus grande valeur de la liste.**

*Exemple :*
```python
>>> liste = [12, 5, 8, 15, 3, 7]
>>> trouve_maximum(liste)
15
```

### Exercice 2 : Compter les Occurrences

**Écrire une fonction `compte_occurrences` qui prend en paramètres une liste et une valeur, et qui renvoie le nombre de fois où cette valeur apparaît dans la liste.**

*Exemple :*
```python
>>> liste = [1, 2, 3, 2, 4, 2, 5]
>>> compte_occurrences(liste, 2)
3
```

### Exercice 3 : Trouver les Positions

**Écrire une fonction `trouve_positions` qui prend en paramètres une liste et une valeur, et qui renvoie une nouvelle liste contenant tous les indices où cette valeur apparaît dans la liste.**

*Exemple :*
```python
>>> liste = [1, 2, 3, 2, 4, 2, 5]
>>> trouve_positions(liste, 2)
[1, 3, 5]
```

## Template de départ

```python
def trouve_maximum(liste):
    """Renvoie la plus grande valeur de la liste"""
    # À compléter
    pass

def compte_occurrences(liste, valeur):
    """Renvoie le nombre d'occurrences de la valeur dans la liste"""
    # À compléter
    pass

def trouve_positions(liste, valeur):
    """Renvoie la liste des positions où se trouve la valeur"""
    # À compléter
    pass
```