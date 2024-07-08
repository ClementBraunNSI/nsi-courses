# Photographie Numérique 1: Noir et Blanc, Niveaux de gris

## Qu'est ce qu'une image?

**Définition** : Une image est un tableau à deux dimensions de cases. Ces cases sont appelées des pixels (qui vient de *Picture element*).

Chaque pixel est assigné à une position que l’on nomme **coordonnées**.
Ces coordonnées sont un couple *( i , j )* où i est une valeur comprise sur la largeur (axe des abscisses) et j est une valeur comprise sur la hauteur (axe des ordonnées).

La **définition** d’une image correspond au nombre de pixels de celle-ci.
On la calcule : $\texttt{résolution} = \texttt{hauteur} \times \texttt{largeur}$.
Par exemple, une image ayant 800 pixels de hauteur et 600 pixels de largeur a une définition de 480 000 pixels.

La **résolution** d’une image correspond au nombre de pixels sur une longueur donnée. Son unité est le ppp (pixels par pouce). Un pouce est une longueur correspondant à 2,54cm.

Chaque pixel contient une information capitale : la valeur de la couleur qu’on lui affecte selon le **mode** utilisé.

**Exercice:**
Une télévision est munie d’un écran 4K, c’est à dire qu’elle a 4096 pixels sur la largeur et 2160 pixels sur la hauteur. Donner la définition de l’écran.
_______________________________________________________________________________________
______________________________________________________________________________________________________________________________________________________________________________

Une image possède 1920 pixels en largeur et 1080 pixels en hauteur. Celle-ci est imprimée sur une feuille dont les dimensions sont : 20cm de largeur et 30cm de longueur.
Donner sa résolution en largeur et sa résolution en hauteur.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Les images en noir et blanc

Une image en noir et blanc est un tableau à deux dimensions où les pixels peuvent être uniquement **noirs ou blancs**.

Un ordinateur ne comprend que nombres alors, comment une image est représentée en mémoire ?

On définit **le blanc avec le chiffre 1** et **le noir avec le chiffre 0**.

On peut donc dessiner des images grâce à des tableaux de nombres.

**Exercice** : Donner l’image associée au tableau de 0 et de 1 ci-dessous :

![tab01](tab_01.png)

**Exercice** : Donner le tableau de 0 et de 1 associé à cette image : 

![img_to_tab](img_to_tab.png)

Les images en noir et blanc sont basiques et n’ont pas par définition une palette de couleur variée.
Cependant, entre le noir et le blanc existe une quantité de nuances du mélange de celles-ci : le gris.

## Les images en nuances de gris

Pour donner de la profondeur à l’image ainsi que du contraste, on peut dans un premier temps utiliser les couleurs que l’on appelle des nuances de gris.
Une nuance de gris correspond à du noir auquel on ajoute une certaine luminosité (exprimée en pourcentages).

Une image en niveaux de gris est donc un tableau à deux dimensions dont chaque pixel qui la compose contient une valeur entre 0 et 255 (256 valeurs).

On a dit précédemment que plus on rajoutait de pourcentage de luminosité. Ainsi 100% de luminosité correspond à du blanc et 0% correspond à du noir.
Ce pourcentage correspond au nombre entre 0 et 255 qui représente la nuance de gris associée.

![nuances](nuances_gris.png)

**Remarque** : Plus la valeur est grande, plus le gris tendra sur du blanc, plus elle est faible, plus le gris tendra vers du noir.

**Exercice** : Remplir le tableau de droite avec les niveaux de gris correspondants. Aidez vous de la palette au dessus.

![img_nuances](img_nuances.png)

On a vu précédemment qu’un ordinateur ne comprend que des 0 et des 1 en mémoire, on a donc un problème : comment représenter les nombres entre 0 et 255 en mémoire ?
La solution : convertir les nombres décimaux que nous connaissons en 0 et 1.

**On appelle cela : convertir en binaire.**

## Le binaire : Définition

Nous comptons généralement en base 10, cela veut dire que nous utilisons 10 symboles pour représenter les chiffres. Combiner ces chiffres permet de créer des nombres.
Pour représenter des chiffres en informatique, on n’utilise que 2 symboles : 0 et 1.
On nomme ces symboles des **bits**.
Un ensemble de 8 bits se nomme un **octet**.

### Rappel : Comment compter en base 10

Pour compter, on utilise la notation en colonne, dite positionnelle.
La colonne la plus à droite correspond à celle des unités, suivie à gauche par celle des dizaines, puis des centaines et ainsi de suite.

Par exemple, on peut décomposer le nombre $154=10^2\times1 + 10^1\times5 + 10^0\times4$.
On appelle cela la **décomposition par base avec ici la base valant 10**.

### Conversion binaire vers décimal

Un nombre écrit en base 2 est écrit en notation positionnelle.

Pour convertir un nombre binaire en base décimale, on opère comme la décomposition précédente avec la base valant 2 :

$11001$ est un nombre représenté en base 2. On peut le décomposer de cette manière :
$11001_2 = 1 \times 2^4 + 1 \times 2^3 + 0 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 = 16 + 8 + 1 = 25_{10}$.

**Exercice:** Convertir les nombres binaires suivant en base 10 :
a. $1101_2$
b. $10101_2$
c. $111000_2$
d. $10010_2$

### Conversion décimal vers binaire

Pour passer de la base 10 à la base 2, on peut utiliser la méthode que l'on appelle des **divisions successives**.

On divise successivement le nombre à convertir par 2.
Chaque **reste** correspond au nombre dans la représentation et chaque **quotient** est à diviser à la suite par 2.
On répète ces opération jusqu'à ce que le quotient soit 0 et le reste 1.

![div_succ](div_succ.png)

La représentation du nombre binaire s’obtient en écrivant les restes dans le sens de la flèche ci dessus.

### Conséquences sur les images en niveaux de gris

Chaque pixel d’une image en niveau de gris comportera donc un nombre entre 0 et 255 écrit en binaire.  Ces valeurs iront donc de **0000 0000** à **1111 1111**.

**Exercice:** Pour la palette donnée de niveau de gris, donner l’écriture binaire de chaque nombre décimaux.