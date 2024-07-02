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
Cependant, les machines (ordinateurs et smartphones) n'utilisent pas cette méthode mais utilise la méthode de la **virgule flottante**.

### La Norme IEEE754

La norme IEEE754 permet de représenter les nombres réels en utilisant le principe de virgule flottante.

Pour simplifier, cette norme permet d'écrire chaque nombre comme une écriture scientifique d'un nombre avec pour base 2.

Un nombre N s'écrit : $N = -1^s * m \times 2^n$ avec $m \in [1;2[$.

- s correspond au signe du nombre : 0 est positif, 1 correspond à un négatif.
- m correspond à l'écriture scientifique du nombre.
- n correspond à la puissance permettant de l'écrire en notation scientifique.

### Problème : les imprécisions

On a remarqué que pour certains nombres, on ne peut pas trouver de représentation exacte d'un nombre par exemple 0.1.
Étant donné qu'il y a des imprécisions sur les flottants, les égalités sur les flottants ne sont pas forcément exactes.

**Exemple:**
Par exemple, à l'aide d'un intrepréteur Python, on peut obtenir ce curieux résultat :
```python
>>> 0.1 + 0.2
0.30000000000000004
```

Cela est du, comme expliqué précédemment, aux imprécisions des représentations des nombres réels.