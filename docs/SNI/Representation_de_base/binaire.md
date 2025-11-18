# Représentation des nombres en bases

## Différencier comptage et dénombrement

On appelle **dénombrer** le fait de donner un par un les nombres d'une suite ou d'un ensemble.
On appelle **compter** le fait de réaliser des opérations sur des nombres.

## Définition

Une **base** est un ensemble de caractères uniques qui permettent de représenter des nombres.

Il existe un certain nombre de bases très connues :

- Base 10 : La base 10 est la base que nous utilisons quotidiennement pour compter. $B_{10}=\lbrace 0,1,2,3,4,5,6,7,8,9 \rbrace $.
- Base 12 : La base 12 est la base que nous utilisons pour remplir des boites d'oeufs, pour représenter les parties d'une journée.

La base 2 est la base utilisée par les ordinateurs pour fonctionner. Un ordinateur fonctionne grâce au courant électrique et analyse en permanence si du courant passe pour permettre de réaliser des calculs différents.

## Représentation d'un nombre

Un nombre est une combinaison de chiffres positionnés sur des colonnes.

Par exemple :  

Le nombre $154 = 1*100 + 5*10 + 4*1$.

On remarque une chose : les colonnes sont en 100 / 10 / 1 qui sont des multiples de 10.

|1000|100|10|1|
|----|---|--|-|
|$10*10*10$|$10*10$|$10*1$|$10*\frac{1}{10}$|

On peut même aller plus loin. Ces nombres sous la forme de 10*10*...*10 sont appelés **puissances de 10**.

On peut écrire $1000 = 10^3 = 10*10*10$ ou $1000000 = 10^6 = 10*10*10*10*10*10$ où la puissance correspond au nombre de fois où l'on a multiplié ou divisé par le même nombre.

**Remarque :** Si l'on compte le nombre de fois où l'on a divisé, la puissance sera négative.  

Cependant, nous représentons nos nombres en base 10 et chaque colonne est une puissance de 10. Il y a donc un lien entre les colonnes et la base utilisée et cela nous permettra de représenter des nombres dans n'importe quelle base.