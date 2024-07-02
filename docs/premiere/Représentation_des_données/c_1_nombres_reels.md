# Nombres réels en Binaire

## Les nombres réels en binaire

Après avoir représenté les nombres entiers, il est necessaire de représenter les nombres réels, nombres dits décimaux ou à virgule.

Les nombres décimaux permettent de représenter des valeurs qui peuvent être analogiques (température, altitude etc...).

La représentation des nombres réels a été approchée de plusieurs manières différentes.

### Écriture en binaire de la partie réelle

Il a été proposé d'écrire un nombre réel en convertissant la partie à gauche de la virgule (la partie entière) et la partie à droite de la virugle (la partie décimale) de manière indépendante en binaire.

On peut essayer de représenter $14,75$ en base 2.

$14_{10} = 1110_2$
$75_{10} = 1001011_2$
On aurait donc $14,75_{10} = 1110,1001011$.
Cela permet de représenter facilement les nombres réels mais cela permet-il de réaliser les opérations entre réels ?

On va chercher à représenter l'addition $14,75 + 1,25$. Cette addition devrait être égale à $16_{10}$ ou $10000_2$.

$14,75_{10} = 1110,100 1011_2$
$1,25_{10} = 1,001 1001_2$

On réalise l'addition et l'on trouve $1111,1100100_2$. On voit bien que cela ne fonctionne pas car les résultats ne sont pas égaux !

On doit donc chercher une norme qui permet de réaliser les opérations sans faire de fautes.

### La Norme IEEE754

La norme IEEE754 permet de réaliser les opérations. On ne cherchera pas à le démontrer.

La norme IEEE754 permet de représenter des nombres réels en utilisant 32 bits dont certains ont une utilité propre.
