# Nombres réels en Binaire

## Les nombres réels en binaire

Après avoir représenté les nombres entiers, il est necessaire de représenter les nombres réels, nombres dits décimaux ou à virgule.

Les nombres décimaux permettent de représenter des valeurs qui peuvent être analogiques (pi, température, altitude etc...).

La représentation des nombres réels a été approchée de plusieurs manières différentes.

### Écriture en binaire de la partie réelle

Il a été proposé d'écrire un nombre réel en convertissant la partie à gauche de la virgule (la partie entière) et la partie à droite de la virugle (la partie décimale) de manière indépendante en binaire.

On peut par exemple chercher à représenter $14,75$ en binaire.

On cherche dans un premier temps la partie entière (la partie à gauche de la virgule).
Ici, on sait que $14_{10} = 1110_2$

Pour représenter la représentation de la partie réelle (la partie à droite de la virgule), on va devoir retrouver les puissances correspondante et ce grâce à la méthode des multiplications successives.

On va multiplier par 2 successivement la partie réelle et ainsi, on retrouvera à la manière des divisions successives, la représentation des puissances négatives.

|partie décimale|bit de la représentation|multiplication successive|
|-|-|-|
|0,75|x|0,75|
|**1**,5|1|0,5|
|**1**,0|1|0,0|
|**0**,0|0|0|

On a donc pour représentation de $0,75_{10} \rightarrow 0,110_2$.

On peut donc représenter $14,25_{10}$ en binaire avec $14_{10} + 0,75_{10} \rightarrow 1110_2 + 0,110_2 = 1110,110_2$.

On a vu dans le cours précédent que pour qu'une représentation soit utilisable, elle doit permettre les opérations sans erreurs.

Faisons un test sur l'opération $14,75 + 1,25$.
On cherche la représentation de $1,25_{10}$ en binaire.

$1_{10} = 1_2$

|partie décimale|bit de la représentation|multiplication successive|
|-|-|-|
|0,25|x|0,25|
|**0**,5|0|0,5|
|**1**,0|1|0,0|
|**0**,0|0|0|

$0,25_{10} = 0,010_{2}$.
On a donc : $1,75_{10} = 1,110_{2}$.

Après réalisation de l'opération, on obtient le résultat : $1110,110_2 + 1,110_2 = 10000,000_2 = 16_{10}$. C'est bien le bon résultat.
Cependant, on remarque que beaucoup de bits sont utilisés pour représenter un si petit nombre, on se retrouve avec un problème grave d'utilisation inutile d'espace.

### La Norme IEEE754

La norme IEEE754 permet de répondre au problème de stockage énoncé précédemment.
La norme IEEE754 permet de représenter des nombres réels en utilisant 32 bits dont certains ont une utilité propre.