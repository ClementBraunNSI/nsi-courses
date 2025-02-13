# Travail Pratique : Cartes Micro:bit

## Définitions

Les cartes Micro:bit sont des cartes électroniques qui sont une introduction à l'informatique embarquée et à la réalisation d'affichages, sons etc... à l'aide de boutons et de leds.

Une carte Micro:bit est consituée de plusieurs éléments :

|Présentation de la carte|Carte avec une tête renard minimaliste en pixel art|
|-|-|
|![carte](microbit.png)|![fox](fox_microbit.png)|

Pour pouvoir utiliser cette carte et programmer, on utilisera le site [Site de Micro:Bit](https://python.microbit.org/v/3/reference).

![site](editor.png)

Le bloc orange correspond à la bibliothèque des blocs pouvant être utilisés pour profiter de l'ensemble des fonctionnalités de la carte.

Le bloc marron est l'éditeur de code, dans celui-ci vous modifierez le blocs de code que vous choisirez dans la bibliothèque.

Le bloc vert permet d'envoyer le programme à la carte **micro:bit** pour pouvoir l'utiliser.

Ce genre de carte doit être alimenté pour fonctionner car elle ne dispose pas d'une batterie intégrée.  
Pour faciliter les choses, on utilisera un cable USB pour l'alimenter et pour envoyer les programmes.

Le programme proposé permet d'afficher un coeur sur le panneau de LED.

```python
# Importer les paquets necessaire au fonctionnement
from microbit import *


# Boucle tant que qui est valable tout le temps
while True:
    # On choisit d'afficher un coeur grâce à la bibliothèque display.
    # Pour choisir ce que l'on souhaite afficher, on regarde dans la bibliothèque ce qui est disponible,
    # ici, un coeur
    display.show(Image.HEART)
    # On attend 1 seconde en faisant "dormir" la carte
    sleep(1000)
    # On affiche un message 'Hello' sur l'écran de la carte grâce à la fonction 
    # scroll de la bibliothèque display
    display.scroll('Hello')
```

## À faire

