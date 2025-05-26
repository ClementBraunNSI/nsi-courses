# Structures de données linéaires

## Définition

Une **structure de données linéaire** est une collection d'**éléments** stockés séquentiellement. En Python, les deux principales implémentations de tableaux (un concept général de structure de données linéaire) sont les **listes** (mutables, c'est-à-dire modifiables après création) et les **tuples** (immuables, c'est-à-dire non modifiables après création).

Ces structures permettent d’organiser et de stocker divers éléments. Elles sont ordonnées, ce qui signifie que chaque élément a une position spécifiques (indice), et les éléments sont généralement stockés dans des zones mémoires contiguës ou liées.

Utiliser des tableaux (listes ou tuples) permet de ne pas avoir à créer une variable distincte pour chaque élément à stocker.

On peut accéder à un élément d'un tableau en utilisant son **indice**. Un indice correspond à la position de l'élément dans le tableau.

!!! Danger Important
	Cas particulier, en **python**, comme dans la plupart des autres langages de programmation, les indices de tableaux commencent à 0.

Pour initialiser un **tuple** vide (un type de tableau immuable), on l’associe à une variable :

```python
# Instance d'un tuple vide
>>> mon_tuple_vide = ()
>>> print(type(mon_tuple_vide))
<class 'tuple'>
>>> print(mon_tuple_vide)
()
```

Pour initialiser une **liste** vide (un type de tableau mutable), on utilise des crochets `[]` :

```python
# Instance d'une liste vide
>>> ma_liste_vide = []
>>> print(type(ma_liste_vide))
<class 'list'>
>>> print(ma_liste_vide)
[]
```

Considérons un exemple de tableau d'entiers :

| indice | élément |
| --- | --- |
| 0 | 312 |
| 1 | 354 |
| 2 | 1234 |

En Python, pour un **tuple**, on l'écrirait avec des parenthèses `()` :

```python
mon_tuple = (312, 354, 1234)
# print(mon_tuple) # Pourrait afficher (312, 354, 1234)
```

Pour une **liste**, on l'écrirait avec des crochets `[]` :

```python
ma_liste = [312, 354, 1234]
# print(ma_liste) # Pourrait afficher [312, 354, 1234]
```

On peut créer des tableaux possédant diverses valeurs, leur taille étant limitée par l’espace mémoire de la machine :

```python
tableau_de_notes = (14,15,20,19)
tableau_animaux = ("chien", "chat", "oiseau", "poisson")
```

!!! Tip
	Dans la majorité des cas, il est préférable de **créer des tableaux pour des données de même type**.
	Cela permet d’éviter des erreurs pour l’interpréteur et éviter des incompréhensions pour la suite du code.

!!! Danger Mutabilité : Tuples (immuables) vs Listes (mutables)
	Attention à la distinction entre tuples et listes concernant la mutabilité !

	**Tuples (immuables) :**
	Un tuple est **immuable**. Cela signifie qu'une fois qu'un tuple est créé, ses éléments ne peuvent pas être modifiés, ajoutés ou supprimés directement. Toute tentative de modifier un élément d'un tuple existant résultera en une erreur `TypeError`.
	Par exemple :
	```python
	mon_tuple = (10, 20, 30)
	# mon_tuple[0] = 5 # Ceci lèverait une TypeError: 'tuple' object does not support item assignment
	```
	Pour "modifier" un tuple, on doit en réalité créer un nouveau tuple.

	**Listes (mutables) :**
	Une liste est **mutable**. Cela signifie que l'on peut modifier ses éléments, en ajouter ou en supprimer après sa création.
	Par exemple :
	```python
	ma_liste = [10, 20, 30]
	ma_liste[0] = 5  # Modifie l'élément à l'indice 0
	ma_liste.append(40) # Ajoute un élément à la fin
	# print(ma_liste) # Afficherait [5, 20, 30, 40]
	```
	L'erreur `TypeError` mentionnée dans le contexte original ("les valeurs d'un tuple ne supportent pas l'assignation de valeurs") s'applique spécifiquement aux tuples.

## Taille d’un tableau

Les tableaux possèdent des fonctions qui leurs sont propres.

Ces fonctions s’appellent des méthodes.

La méthode `len` permet d’obtenir la longueur d’un tableau, ie sa taille. Cela fonctionne de la même manière que lorsque l’on souhaite obtenir la longueur d’une chaîne de caractère.

```python
tableau_animaux = ("chien", "chat", "oiseau", "poisson")
>>>print(len(tableaux_animaux))
4
```

## Accéder à un élément d’un tableau

### Notion d’indice

Pour accéder à un élément du tableau, on peut s’intéresser à sa position dans le tableau, c’est à dire son **indice**.
**Rappel important : L’indice commence à 0 !**

On peut accéder à un élément d'un tableau (liste ou tuple) en utilisant son indice avec la syntaxe `nom_du_tableau[indice]`:

```python
# Exemple avec un tuple
mon_tuple_animaux = ("chien", "chat", "poisson", "vache")
# On veut l'élément à la position 3 du tuple (le quatrième élément)
# >>> print(mon_tuple_animaux[3]) # Afficherait 'vache'

# Exemple avec une liste
ma_liste_animaux = ["chien", "chat", "poisson", "vache"]
# >>> print(ma_liste_animaux[1]) # Afficherait 'chat'
```

On peut vouloir accéder à tous les éléments d’un tableau (liste ou tuple), ou à une partie de celui-ci.
Pour ce faire, on peut utiliser les boucles **`while` (tant que) et `for` (pour)** afin de parcourir les éléments.

```python
tableau = ("chien", "chat", "poisson", "vache")

#pour i allant de 0 à la taille du tableau:
for i in range(len(tableau)):
	print(tableau[i])

# tant que i est plus petit que la taille du tableau
i=0
while i < len(tableau):
	print(tableau[i])
	i = i + 1
```

De cette même manière, on fait varier i pour qu’il prenne tous les indices du tableau et on arrive à accéder à tous les éléments du tableau.

### Notion de *in*

Python permet d’utiliser bon nombres de mots-clefs. Le mot-clef ***in*** en fait partie.

Celui ci permet de savoir si un élément fait partie d’une autre variable. On peut l’utiliser notamment pour savoir si un caractère ou un mot fait partie d’une chaîne de caractère.

En reprenant l’exemple précédent, on veut une autre méthode de parcours de tableau:

```python
tableau = ("chien", "chat", "poisson", "vache")
chaine = ""

#pour i allant de 0 à la taille du tableau:
for element in tableau:
	print(element)
```

De ce fait, on accède aussi à tous les éléments du tableau.

On peut aussi fusionner des tableaux. On peut utiliser l'opérateur `+` qui sert à **concaténer** des tableaux.

En clair :
```python
	tableau_1 = (1,2,3)
	tableau_2 = (4,5,6)
	tableau_3 = tableau_1 + tableau_2
```

## Les listes

Les listes sont des tableaux mutables. Cela veut dire que l'on peut rajouter des éléments, en retirer ou même modifier le contenu de ce tableau.

### Ajout d’élément dans une liste

On peut rajouter des éléments dans une liste créée de diverses manières.

Exemple : *On veut créer une liste qui correspond à la table de multiplication de 2*

```python
#Initialisation d'une liste vide
multiples_de_2 = []

#Boucle for pour remplir notre liste
for i in range(0,11):

	#On ajoute la valeur i dans le tableau.
	multiples_de_2 = multiples_de_2 + [i*2]
```

En procédant de cette manière, on créée implicitement un tableau d’une valeur contenant ici notre nombre *i multiplié par 2*.

Le procédé utilisé ici est la **construction par concaténation**. Cette méthode par concaténation a un inconvénient implicite : elle créée une nouvelle liste à la place de modifier la liste en place.

L’avantage d’utiliser des listes en python pour créer des tableaux provient de l’essence de la liste : **utiliser les méthodes** de listes.

Au lieu de créer des “sous-listes” de taille 1, on peut utiliser la méthode *append* qui permet d’ajouter une variable à la fin du tableau.

```python
#Initialisation d'une liste vide
multiples_de_2 = []

#Boucle for pour remplir notre liste
for i in range(0,11): # i prendra les valeurs de 0 à 10

	#On ajoute la valeur i*2 à la fin de la liste.
	#La méthode append() modifie la liste en place et retourne None.
	multiples_de_2.append(i*2)

# print(multiples_de_2) # Pourrait afficher [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
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

# Comment instancier à l'aide de la méthode par compréhension:
# nom_variable = [expression for element in iterable]
# ou avec une condition:
# nom_variable = [expression for element in iterable if condition]

# Exemple: On initialise la liste directement avec les multiples de 3 de 0*3 à 10*3
multiples_de_3 = [i * 3 for i in range(0, 11)] # i prend les valeurs de 0 à 10
# print(multiples_de_3) # Afficherait [0, 3, 6, ..., 30]
```

L’écriture ici peut être scindée en plusieurs blocs :

- multiple_de_3 : nom de la variable
- = assignation de la valeur à la variable
- i : valeur qui sera renseignée dans le tableau ou la liste
- for i in range(0,11) : on fait varier i entre 0 et 11 non compris

Cette notation peut être difficile à lire aux premiers abords mais il est utile de la maîtriser pour rendre son code plus aéré.