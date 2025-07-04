# Interrogation Première NSI - Dictionnaires (20 min)
**Nom :** _________________ **Prénom :** _________________ **Classe :** _______

## Exercice 1 : Questions de cours (4 points)

**1.1** Qu'est-ce qu'une clé dans un dictionnaire ? Quels types de données peuvent servir de clés ?

**1.2** Soit `dico = {'a': 1, 'b': 2, 'c': 3}`. Que se passe-t-il si on exécute `dico['d']` ?

**1.3** Quelle est la différence entre `dico.get('d')` et `dico.get('d', 0)` ?

**1.4** Comment peut-on parcourir à la fois les clés et les valeurs d'un dictionnaire ?

## Exercice 2 : Analyse de code (6 points)

Soit le code suivant :

```python
def traitement(dico):
    nouveau = {}
    for cle, valeur in dico.items():
        if valeur > 10:
            nouveau[cle.upper()] = valeur * 2
    return nouveau
```

**2.1** Que renvoie `traitement({'nom': 15, 'age': 8, 'taille': 12})` ?

**2.2** Réécrire cette fonction en utilisant une compréhension de dictionnaire.

**2.3** Que se passerait-il si une des clés du dictionnaire n'était pas une chaîne de caractères ?

## Exercice 3 : Programmation (10 points)

**3.1** Écrire une fonction `compter_lettres(texte)` qui prend une chaîne de caractères et renvoie un dictionnaire où les clés sont les lettres et les valeurs sont leur nombre d'occurrences.

```python
# Exemple d'utilisation
>>> compter_lettres("hello")
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
>>> compter_lettres("Python")
{'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
```

**3.2** Écrire une fonction `inverser_dictionnaire(dico)` qui prend un dictionnaire et renvoie un nouveau dictionnaire où les clés deviennent les valeurs et vice versa. On suppose que toutes les valeurs sont uniques.

```python
# Exemple d'utilisation
>>> inverser_dictionnaire({'a': 1, 'b': 2, 'c': 3})
{1: 'a', 2: 'b', 3: 'c'}
>>> inverser_dictionnaire({'nom': 'Alice', 'ville': 'Paris'})
{'Alice': 'nom', 'Paris': 'ville'}
```

**3.3** Écrire une fonction `fusionner_dictionnaires(dico1, dico2)` qui fusionne deux dictionnaires. Si une clé existe dans les deux dictionnaires, on additionne les valeurs.

```python
# Exemple d'utilisation
>>> fusionner_dictionnaires({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
{'a': 1, 'b': 5, 'c': 4}
>>> fusionner_dictionnaires({'x': 10}, {'y': 20, 'z': 30})
{'x': 10, 'y': 20, 'z': 30}
```

**3.4** Écrire une fonction `grouper_par_valeur(dico)` qui prend un dictionnaire et renvoie un nouveau dictionnaire où les clés sont les valeurs uniques du dictionnaire original, et les valeurs sont des listes contenant toutes les clés qui avaient cette valeur.

```python
# Exemple d'utilisation
>>> grouper_par_valeur({'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2})
{1: ['a', 'c'], 2: ['b', 'e'], 3: ['d']}
```