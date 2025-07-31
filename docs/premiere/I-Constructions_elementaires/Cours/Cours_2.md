# 📚 Types de données en Python

## 📖 Les booléens

Le type booléen en Python est utilisé pour représenter des valeurs de vérité. Il n'a que deux valeurs possibles : True (vrai) et False (faux). Les booléens sont souvent utilisés dans les conditions et les boucles pour contrôler le flux d'exécution d'un programme.

```python
est_jeune = True
a_termine_cours = False
```

Les opérateurs logiques tels que and, or, et not permettent de combiner ou d'inverser les valeurs booléennes :

```python
est_jeune_et_a_termine_cours = est_jeune and a_termine_cours 
est_vrai = not a_termine_cours  
```

## 📖 Les nombres

### Les entiers

Il existe plusieurs types en Python pour définir des nombres.
Il existe le type **int** qui permet d'instancier des nombres.

La syntaxe est assez claire : on veut instancier une variable *a* valant 42.

```python
a = 42
b = -54
```

On peut réaliser des opérations sur ce type entier, elles sont répertoriées dans le cours sur les **constructions élémentaires**.

### Les flottants

Pour décrire des nombres réels (à virgule), python associe la valeur à un type appelé **flottant** qui correspond à une écriture à virgule flottante (IEEE754).

> **⚠️ Attention**
> Attention, pour rappel, en informatique pour représenter les nombres réels, il y a des arrondis qui sont réalisés.
> Ainsi, réaliser des opérations mathématiques sur des flottants **est strictement interdit** car les résultats, même s'ils nous paraissent corrects, ne le seront pas forcément pour la machine.

Comme pour les entiers, l'instanciation est triviale.

```python
pi = 3.14159
racine_de_deux = 1.4132
```

> **⚠️ Le point**
> Pour décrire un réel, on utilise le point et non la virgule comme habituellement à la main.
> Cela vient de l'écriture américaine qui utilise les **.** pour les parties entières et décimales et **,** pour les milliers, millions...

## 📖 Les caractères et chaînes de caractères

En Python, les caractères sont représentés comme des chaînes de longueur 1, et il n'y a pas de type char distinct comme dans certains autres langages. Les chaînes de caractères sont représentées par le type str.

> **💡 Astuce pour se repérer**
> Il est conseillé pour mieux s'y retrouver, d'écrire les caractères seuls entre **'** et les chaînes de caractère entre **"**

```python
nom = "Alice"
lettre = 'a'
```

On peut aussi accéder aux caractères individuels d'une chaîne en utilisant des indices, commencer par 0 :

```python
premiere_lettre = nom[0]  # 'A'
derniere_lettre = nom[-1]  # 'e'
```

Les chaînes peuvent être concaténées (**opérateur +**), répétées et comparées, et elles offrent une multitude de méthodes pour effectuer diverses opérations telles que la recherche, le remplacement ou la modification de la casse des caractères.