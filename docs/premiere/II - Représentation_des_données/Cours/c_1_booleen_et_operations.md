# Booléens et Fonctions booléennes

## Définitions

Une **variable** booléenne est une variable qui peut prendre **deux états** : **Vrai ou Faux**. Ces états peuvent être équivalents à des valeurs numériques : Vrai = 1 et Faux = 0.
Ces états correspondent en machine **à la présence du courant ou non**.

Une **fonction booléenne** est une fonction qui prend en paramètre **des variables booléennes** et en ressort un résultat.

Une **équation booléenne** est un ensemble de fonctions booléenne prenant en paramètre un certain nombre de variables et renvoie un résultat en sortie.

## Fonctions booléennes

Il existe un certain nombre d'opérations booléennes. Dans ce cours, on s'intéressera aux principales.

Ces fonctions donnent un résultat fini dépendant de l'état des variables en paramètre.
On appelle cet ensemble de couples états/résultat **une table de vérité**.

### Fonction NOT (NON)

La fonction NOT prend en paramètre une variable booléenne et renvoie son opposé.

**Table de vérité**

|a|s|
|-|-|
|0|1|
|1|0|

### Fonction AND (ET)

La fonction AND prend en paramètre deux variables booléennes et renvoie en sortie si les deux variables sont à l'état 1. L'opérateur est $\times$ ou $\cdot$.

**Table de vérité**

|a|b|s|
|-|-|-|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

### Fonction OR (OU)

La fonction OR prend en paramètre deux variables et renvoie 1 si l'une ou les deux variables booléennes sont à l'état 1.
L'opérateur est $+$.

**Table de vérité**

|a|b|s|
|-|-|-|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

### Fonction XOR (OU Exclusif)

La fonction XOR correspond à une fonction booléenne OR mais qui renvoie 1 uniquement si un des deux paramètre est à l'état 1.

**Table de vérité**

|a|b|s|
|-|-|-|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

## Équations booléennes

On rappelle qu'une équation booléenne est un ensemble de fonctions booléennes.
Ces fonctions répondent à l'algèbre booléenne créée par George Bool à la fin du XIXème siècle.

Les équations booléennes se lisent de gauche à droite et dépendent des priorités opératoires PEMDAS comme en mathématiques.

$S = (a + b)\times c$ se lit "a ou b et c".

Exemple :
Pour évaluer cette équation booléenne, on a besoin de valeurs pour les variables. On prend pour exemple a = 1, b = 0 et c = 1.

On évalue d'abord l'opération OU. Le résultat de cette opération sera utilisé comme paramètre pour l'opération ET.

$S = (1+0) \times 0 = 1 \times 0 = 0$.

On peut donc évaluer des équations booléennes à l'aide des tables de vérité précédentes.

## En python

Sur Python, on peut évaluer des équations booléennes. Les opérateurs sont quasiment transparents:

- La fonction OU correspond à l'opérateur **or**.
- La fonction ET correspond à l'opérateur **and**.
- La fonction NON correspond à l'opérateur **not**.

On peut associer à une variable en python un état booléen qui sera retranscrit par une valeur **True** (Vrai ou 1) et **False** (Faux ou 0).

En python, on peut écrire l'exemple précédent de cette manière :

```python
a = True
b = False
c = True

S = (a or b) and c
print(S)
```
