# Interrogation Première NSI - Listes et Tuples (20 min)
**Nom :** _________________ **Prénom :** _________________ **Classe :** _______

## Exercice 1 : Questions de cours (4 points)

**1.1** Quelle est la différence principale entre une liste et un tuple en Python ?

**1.2** Que renvoie l'instruction `len([1, 2, [3, 4], 5])` ? Justifier.

**1.3** Soit `ma_liste = [10, 20, 30, 40]`. Que contient `ma_liste` après l'exécution de `ma_liste[1:3] = [25]` ?

**1.4** Expliquer pourquoi l'instruction `(1, 2, 3)[0] = 5` provoque une erreur.

## Exercice 2 : Analyse de code (6 points)

Soit le code suivant :

```python
def mystere(liste):
    resultat = []
    for i in range(len(liste)):
        if i % 2 == 0:
            resultat.append(liste[i] * 2)
        else:
            resultat.append(liste[i])
    return resultat
```

**2.1** Que renvoie `mystere([1, 2, 3, 4, 5])` ? Détailler le déroulement.

**2.2** Réécrire cette fonction en utilisant une compréhension de liste.

**2.3** Proposer une version de cette fonction qui modifie la liste en place (sans créer de nouvelle liste).

## Exercice 3 : Programmation (10 points)

**3.1** Écrire une fonction `indices_element(liste, element)` qui renvoie la liste de tous les indices où apparaît un élément dans une liste.

```python
# Exemple d'utilisation
>>> indices_element([1, 3, 2, 3, 1, 3], 3)
[1, 3, 5]
>>> indices_element([1, 2, 4], 5)
[]
```

**3.2** Écrire une fonction `fusion_alternee(liste1, liste2)` qui fusionne deux listes en alternant leurs éléments. Si une liste est plus longue, ses éléments restants sont ajoutés à la fin.

```python
# Exemple d'utilisation
>>> fusion_alternee([1, 2, 3], ['a', 'b', 'c', 'd'])
[1, 'a', 2, 'b', 3, 'c', 'd']
>>> fusion_alternee([1, 2], ['a'])
[1, 'a', 2]
```

**3.3** Écrire une fonction `creer_couples(liste)` qui prend une liste et renvoie une liste de tuples contenant tous les couples d'éléments consécutifs.

```python
# Exemple d'utilisation
>>> creer_couples([1, 2, 3, 4])
[(1, 2), (2, 3), (3, 4)]
>>> creer_couples(['a', 'b'])
[('a', 'b')]
>>> creer_couples([5])
[]
```