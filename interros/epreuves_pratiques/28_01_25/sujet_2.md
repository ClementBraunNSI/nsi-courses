# Épreuve Pratique 2 : Sujet 2

## Exercice 1 (10 points)

**Écrire une fonction recherche qui prend en paramètres elt nombre entier et tab un
tableau de nombres entiers (type list), et qui renvoie l’indice de la première occurrence de elt dans tab si elt est dans tab et None sinon.**  

L’objectif de cet exercice est de parcourir un tableau, il est interdit d’utiliser la méthode index des listes Python.

*Exemples:*

```python
    >>> recherche(1, [2, 3, 4])
    None
    >>> recherche(1, [10, 12, 1, 56])
    2
    >>> recherche(50, [1, 50, 1])
    1
    >>> recherche(15, [8, 9, 10, 15])
    3
```

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## Exercice 2 (10 points)

On considère la fonction eleves_du_mois prenant en paramètres eleves et notes
deux tableaux de même longueur, le premier contenant le nom des élèves et le second, des entiers positifs désignant leur note à un contrôle de sorte que eleves[i] a obtenu la note notes[i].

Cette fonction renvoie le couple constitué de la note maximale attribuée et des noms des élèves ayant obtenu cette note regroupés dans un tableau.

Ainsi, l'instruction :

```python
    >>> eleves_du_mois(['a','b','c','d'],[15,18,12,18])
    (18, ['b', 'd'])
```

**Compléter le code suivant et le tester :**

```python
    def eleves_du_mois(eleves, notes):
        note_maxi = 0
        meilleurs_eleves = ...
        for i in range(...):
            if notes[i] == ...:
                meilleurs_eleves.append(...)
            elif notes[i] > note_maxi:
                note_maxi = ...
                meilleurs_eleves = [...]
        return (note_maxi, meilleurs_eleves)
```

*Exemples :*

```python
    >>> eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
    >>> notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
    >>> eleves_du_mois(eleves_nsi, notes_nsi)
    (80, ['c', 'f', 'h'])
    >>> eleves_du_mois([],[])
    (0, [])
```