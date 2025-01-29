# Épreuve Pratique 2 : Sujet 3

## Exercice 1

On a relevé les valeurs moyennes annuelles des températures à Paris pour la période allant de 2013 à 2019. 
Les résultats ont été récupérés sous la forme de deux tableaux (de type list) : l’un pour les températures, l’autre pour les années :

```python
    >>> annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
    >>> t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
```

**Écrire la fonction annee_temperature_minimale qui prend en paramètres ces deux tableaux et qui renvoie la plus petite valeur relevée au cours de la période et l'année correspondante.**

On suppose que la température minnimale est atteinte une seule fois.

*Exemple :*

```python
    >>> annee_temperature_minimale(t_moy, annees)
    (12.5, 2016)
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


## Exercice 2

Le but de l’exercice est de compléter une fonction qui détermine si une valeur est présente dans un tableau de valeurs triées dans l’ordre croissant.
**Compléter l’algorithme de dichotomie donné ci-après et le tester :**

```python
    def dichotomie(tab, x):
        """applique une recherche dichotomique pour déterminer
        si x est dans le tableau trié tab.
        La fonction renvoie True si tab contient x et False sinon"""
        debut = 0
        fin = ...
        while debut <= fin:
            m = ...
            if x == tab[m]:
                return...
            if x > tab[m]:
                debut = ...
            else:
                fin = ...
        return False
```

*Exemples:*

```python
    >>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28)
    True
    >>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27)
    False
```
