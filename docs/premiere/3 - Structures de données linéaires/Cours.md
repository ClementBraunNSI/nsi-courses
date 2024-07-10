# Cours

## Définition

Les tableaux de données font partie des collections (structures permettant de stocker des variables). Ce type de structure permet d’organiser et stocker diverses variables. Ces tableaux sont nommés *list* en **python.** 

Un tableau est une structure mutable. Elle peut changer, ajouter, supprimer des éléments etc… C’est aussi une structure ordonnée et de zone mémoire contigüe. 

Utiliser des tableaux / listes permet de ne pas avoir à créer une variable pour chaque valeur pour la stocker.

On peut accéder à une valeur d’un tableau en utilisant des indices. Un indice correspond au numéro de la case du tableau.

Cas particulier, en **python**, comme dans la plupart des autres langages de programmation, les indices de tableaux commencent à 0.

Un exemple de tableau représenté de manière naturelle :

| indice | valeur |
| --- | --- |
| 0 | 312 |
| 1 | 354 |
| 2 | 1234 |

L’écriture d’un tableau se fait à l’aide de crochets [ ] et on ne s’intéresse qu’à la colonne bleue car la colonne orange est implicite.

Pour initialiser un tableau vide, on l’associe à une variable. 

L’écriture se fait ainsi de cette manière :

```python
#instance d'un tableau vide
>>> mon_tableau = []

>>> mon_tableau
<type 'list'>
```

Avoir un tableau vide, c’est bien, mais traiter des valeurs, c’est mieux.

On peut créer des tableaux possédant diverses valeurs, leur taille étant limitée par l’espace mémoire de la machine :

```python
tableau_de_notes = [14,15,20,19]
tableau_animaux = ["chien", "chat", "oiseau", "poisson"]
```

Dans l’optimal et la majorité des cas, il est préférable de **créer des tableaux pour des données de même type**.

Cela permet d’éviter des erreurs pour l’interpréteur et éviter des incompréhensions pour la suite du code.

## Taille d’une liste

Les listes possèdent des fonctions qui leurs sont propres et qui peuvent être appelées pour elles.

Ces fonctions s’appellent des méthodes.

La méthode len permet d’obtenir la longueur d’un tableau, ie sa taille. Cela fonctionne de la même manière que lorsque l’on souhaite obtenir la longueur d’une chaîne de caractère.

```python
tableau_animaux = ["chien", "chat", "oiseau", "poisson"]
>>>print(len(tableaux_animaux))
4
```

## Accéder à un élément d’un tableau

### Notion d’indice

Pour accéder à un élément du tableau, on peut s’intéresser à sa position dans le tableau, c’est à dire son **indice**.
**Important : L’indice commence à 0 !**

On peut accéder à un élément dans une liste avec la syntaxe.

```python
tableau = ["chien", "chat", "poisson", "vache"]

#On veut l'élément à la position 3 du tableau

>>>element_3 = tableau[3]
vache
```

On peut vouloir accéder à tous les éléments d’une liste, ou en partie d’une liste. Pour ce faire, on peut utiliser les boucles **tant que et pour** de manière à accéder aux éléments d’une liste.

```python
tableau = ["chien", "chat", "poisson", "vache"]
chaine = ""

#pour i allant de 0 à la taille du tableau:
for i in range(len(tableau)):
	print(tableau[i])
```

De cette même manière, on fait varier i pour qu’il prenne tous les indices du tableau et on arrive à accéder à tous les éléments du tableau.

### Notion de *in*

Python permet d’utiliser bon nombres de mots-clefs. Le mot-clef ***in*** en fait partie.

Celui ci permet de savoir si un élément fait partie d’une autre variable. On peut l’utiliser notamment pour savoir si un caractère ou un mot fait partie d’une chaîne de caractère.

En reprenant l’exemple précédent:

```python
tableau = ["chien", "chat", "poisson", "vache"]
chaine = ""

#pour i allant de 0 à la taille du tableau:
for element in tableau:
	print(element)
```

De ce fait, on accède aussi à tous les éléments du tableau.

***Exercice 1***

## Initialisation de listes

Pour créer une liste d’entiers, on peut procéder de diverses méthodes.

### Ajout d’élément dans une liste

On peut rajouter des éléments dans une liste créée de diverses manières.

Exemple : *On veut créer une liste qui correspond à la table de multiplication de 2*

```python
#Initialisation d'une liste vide
multiples_de_2 = []

#Boucle for pour remplir notre liste
for i in range(0,11):

	#On ajoute la valeur i dans le tableau.
	multiples_de_2 = multiples_de_2 + [i]
```

En procédant de cette manière, on créée implicitement un tableau d’une valeur contenant ici notre nombre *i*.

Le procédé utilisé ici est la **construction par concaténation**. Cette méthode par concaténation a un inconvénient implicite : elle créée une nouvelle liste à la place de modifier la liste en place.

L’avantage d’utiliser des listes en python pour créer des tableaux provient de l’essence de la liste : **utiliser les méthodes** de listes.

Au lieu de créer des “sous-listes” de taille 1, on peut utiliser la méthode *append* qui permet d’ajouter une variable à la fin du tableau.

```python
#Initialisation d'une liste vide
multiples_de_2 = []

#Boucle for pour remplir notre liste
for i in range(0,11):

	#On ajoute la valeur i dans le tableau.
	multiples_de_2 = multiples_de_2.append(i)
```

La méthode *append* a l’avantage sur la méthode par concaténation **de modifier en place la liste au lieu d’en créer une autre.**

## Retirer des éléments d’une liste

Pour retirer des éléments d’une liste, on peut utiliser les méthodes des listes / tableaux.

### La méthode pop

La méthode pop est utilisable dans 2 cas:

$$
\begin{equation*}
  {element~retiré}=
     \begin{cases}
        tableau[i] & \text{si } tableau.pop(i) \\
        tableau[len(tableau)] & \text{si } tableau.pop(~)
     \end{cases}
\end{equation*}
$$

```python
tableau = [1,2,3,4]
>>> print(tableau.pop(1))
2
>>> print(tableau.pop())
4
```

### La méthode remove

La méthode remove permet de retirer la première occurence d’un élément passé en paramètre.

On a donc :

```python
>>> tableau = [1,2,2,3,4,4]
>>> tableau.remove(2)
>>> print(tableau)
[1,2,3,4,4]
```

## Pour aller plus loin

### Construction de liste par compréhension

On peut simplifier le code utilisé précédemment en une seule ligne. Cela a pour but de rendre le code plus concis, de réduire le nombre de lignes et de se rapprocher de notions et écritures plus mathématiques.

```python
#On initialise la liste directement avec les valeurs

multiples_de_3 = [i for i in range(0,11)]
```

L’écriture ici peut être scindée en plusieurs blocs :

- multiple_de_3 : nom de la variable
- = assignation de la valeur à la variable
- i : valeur qui sera renseignée dans le tableau
- for i in range(0,11) : on fait varier i entre 0 et 11 non compris

Cette notation peut être difficile à lire aux premiers abords mais il est utile de la maîtriser pour rendre son code plus aéré.