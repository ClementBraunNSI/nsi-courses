# Entiers négatifs en Binaire

## Les entiers négatifs

Le cours précédent a permis d'expliquer comment représenter les nombres entiers positifs en base 2 pour en permettre le traitement par un ordinateur.

Cependant, toutes les grandeurs ne sont pas exclusivement positives : tension alternative, accéleration d'un freinage etc...

Pour pouvoir réaliser des simulations ou des traitements, il va falloir pouvoir représenter les nombres négatifs.

### Première tentative : le bit de signe

Une première technique de représentation des nombres négatifs est d'ajouter un bit de poids fort (tout à gauche) qui représente le signe : 1 représente un nombre négatif et 0 un nombre positif.

Exemple  : $1001_2$ représente sur 4 bits signés le chiffre $-1$, $0100_2$ représente sur 4 bits signés le chiffre $4$.

Cela pourrait sembler être une bonne tentative cependant, deux problèmes se posent :

- Un chiffre peut avoir 2 représentations : Le cas du 0
  
En effet, 0 n'est ni positif ni négatif. On peut donc en déduire 2 représentations sur 4 bits par exemple : $1000_2$ et $0000_2$.
Cependant, avoir 2 représentations pour un même chiffre n'est pas concevable notamment pour les représentations en mémoire ou bien pour les opérations.

- Les opérations ne sont pas correctes :
  
On veut réaliser l'opération $-13 + 13$ en binaire sur 5 bits.
On a alors :
$11101_2 + 01101_2 = 101010_2$
Sur 5 bits, on a alors : $11101_2 + 01101_2 = 01010_2$. Cependant, $-13+13 = 0$ et $01010_2 = +10_{10}$.

Cela montre que cette représentation n'est pas utilisable.

### Seconde tentative : le complément à 2

Le complément à 2 est une technique qui a été proposée pour représenter les nombres négatifs.
On peut illustrer cela comme un compteur kilométrique de vielle voiture.
Sur les compteurs des vieilles voitures, faire une marche arrière permettait de réduire le nombre de kilomètres affichés sur le compteur.
Cependant pour les fourbes voulant trafiquer leur compteurs pour vendre leurs voitures plus chères, ils se sont heurtés au cas où ils reculent au kilomètre $000000$.
Le compteur étant circulaire, en reculant d'un kilomètre de plus, ce compteur va afficher quelque chose d'étonnant : $999999$.

Malgré cela, cette valeur permet de représenter le kilomètre $-1$.
Cela a donc donné l'idée pour représenter les nombres négatifs, on appelle cela le complément à 2.

On peut donc représenter :
$1_{10} = 0001_2 \rightarrow 0_{10} = 0000_2 \rightarrow -1_{10} = 1111_2 \rightarrow -2_{10} = 1110_2 \rightarrow ...$.

Il existe une méthode pour réaliser cette conversion.

**Méthode :**

1 - Convertir le nombre choisi en base 2.
2 - Inverser chaque bits : 0 devient 1 et inversement.
3 - Ajouter 1 à la représentation binaire du nombre inversé.

Exemple :
On souhaite représenter -14 en base 2 :
Étape 1 : $14_{10} = 1110_2$
Étape 2 : $1110_2 \rightarrow 0001_2$
Étape 3 : $0001_2 + 1_2 = 0010_2 = -14_{10}$

Cela permet de résoudre le premier problème, celui de la représentation de 0 mais cela résout-il le problème des opérations ?

On souhaite réaliser l'opération 14 + (-4) sur 4 bits.
$-4_{10} = 1100_2$
$14_{10} = 1110_2$

On calcule l'opération : 
$1110_2 + 1100_2 = 11010_2$
On remarque que l'on dépasse le nombre de bits aloués, ici 5 bits.
On a en réalité réalisé l'opération (en décimal) : $14 + (2^5-4) = 26$.
Il faut donc retrancher $2^5$ à la représentation que l'on avait :
$11010_2 - 10000_2 = 1010_2 = 10_{10}$.

Cela permet donc de réaliser toutes les opérations possibles sans erreur, on utilisera donc la méthode du complément à 2.
