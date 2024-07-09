# Constructions élémentaires en Python

## Qu'est ce qu'un programme ?

**Défintion:** On définit un **programme** comme étant une suite d'instruction élémentaires destinées à être exécutées par un ordinateur.

Le langage python est un langage dit de haut niveau. Cela veut dire qu'il est plus proche de nous (utilisateurs) que de l'ordinateur (du processeur).

Ce langage est basé sur nos ordinateurs qui réalise des instructions de manière séquentielle (c'est à dire réalisées les unes après les autres).

On peut dénombrer un certain nombre d'instructions élémentaires qui permettent de créer un programme.
Ces instructions élémentaires peuvent utiliser des opérateurs.

**Définition:** Un opérateur est un caractère ou un ensemble de caractère qui correspond à une opération pouvant être réalisée par le processeur.

## Instanciation

L'instanciation est une instruction qui permet d'associer une **valeur** à une **variable**.
Une variable en python est une chaîne de caractère que l'on associe à une **type** (domaine de valeurs).

L'instanciation utilise l'opérateur `=`.
Pour la machine, cela revient à associer un espace mémoire à la valeur désignée.

Par exemple :

```python
# Instancier a à la valeur 42
a = 42

#Instancier ma_chaine_de_caractere à la valeur 'Hello World!'
ma_chaine_de_caractere = 'Hello World!'
```

On a donc ici, l'explicitation des types entiers ou chaînes de caractères mais il en existe un certain nombre : tableaux, listes, nombres réels (réels à virgule flottante) ou d'autres objets que l'on peut créer nous même.

Cette opération est la base de la programmation. On utilisera le terme **instancier** pour définir le fait d'associer à une variable une valeur donnée.

## Opérations mathématiques

Le langage python est un langage informatique. En informatique, il est nécessaire de réaliser des opérations qui peuvent être du domaine mathématique.

Il existe un certain nombre d'opérations mathématiques qui sont associées à des opérateurs.
On peut citer :

- $+$: addition
- $-$: soustraction
- $\ast$: multiplication
- $/$ : division

Ces opérateurs utilisent 2 valeurs, à l'instar de nos opérations que l'on peut écrire sur papier.
Il en parait nécessaire d'instancier une variable à une opération, comme par exemple nos fonctions mathématiques $y = 3x+2$.

Par exemple:

```python
a = 3 + 2 
b = 5 - 3
c = a * b
d = b / a
```

Les exemples précédents montrent que l'on peut réaliser des opérations sur les différentes variables que l'on a déjà créée.

Il faut cependant prendre compte d'une chose importante : **le type des variables utilisées**.
En effet, les opérations **mathématiques** sont réservées à des variables de type entiers ou nombres réels. Il faut cependant faire attention aux nombres réels (flottants) à cause des imprécisions (cf cours précédent).

## Opérations de comparaisons

Comme les opérations mathématiques, il est possible de réaliser des comparaisons sur des variables.

!!! danger Erreurs de types
    **On ne peut comparer des éléments uniquement s'ils sont du même type** !
    Si jamais lors d'un programme on compare deux éléments de types différents, on pourrait faire face à ce que l'on appelle une erreur (**TypeError**).

Il existe un certain nombre d'opérateurs en python qui permettent de réaliser des comparaisons.  

On peut citer :

- $a > b$ : Cet opérateur correspond à une comparaison d'ordre (a plus grand que b).
- $a < b$ : Cet opérateur correspond à une comparaison d'ordre (a plus petit que b).
- $a >= b$ : Cet opérateur correspond à une comparaison d'ordre (a plus grand ou égal à b).
- $a <= b$ : Cet opérateur correspond à une comparaison d'ordre (a plus petit ou égal à b).
- $a == b$ : Cet opérateur correspond à une comparaison : a est égal à b.

!!! Danger Confusion des opérateurs
    Il ne faut pas confondre les opérateurs $=$ et $==$.
    En effet, $=$ ne sera utilisé uniquement lors d'instanciation de variables. Utiliser cet opérateur lors d'une comparaison peut mener à des erreurs!

## Conditions

TODO