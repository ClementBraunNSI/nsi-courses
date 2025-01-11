# Ludopédagogie : Redstone dans Minecraft

## Pourquoi Minecraft ?

Minecraft est un jeu vidéo sorti en 2009 qui met le joueur dans un mode en 3D créé aléatoirement en utilisant la méthode procédurale.

Pour faire court, la génération d'un monde Minecraft est aléatoire grâce à du pseudo-aléatoire au niveau de la création des terrains en utilisant un outil mathématique appelé le **bruit de Perlin**. Un algorithme de bruit de Perlin permet de réaliser des calculs dans des matrices (tableaux à 2 dimensions) et permettent de générer des tableaux avec des valeurs ayant des micro-variations permettant pour le jeu de simuler des zones de température, de relief etc...

Minecraft est un jeu particulier car il met le joueur dans un monde composé de ***voxels*** qui ne sont que des pixels dans un univers en 3 dimensions (pixels étant un élément dans un univers de 2 dimensions).

De plus, ce jeu ayant reçu énormément d'évolutions depuis, a rajouté une mécanique assez novatrice qu'est la **redstone**.

La redstone (ou poudre rouge en français) permet de simuler des circuits électriques et de réaliser des opérations logiques.

La conséquence directe d'avoir une simulation de circuits électroniques via les composants proposés dans le jeu permettent de le rendre **Turing-complet**.


!!! tip Pour faire très simple

    On dit d'un langage de programmation qu'il est **Turing-complet** s'il peut réaliser tous types d'opérations possibles et de simuler des calculs mathématiques et logiques. Le but in-fine d'avoir un langage Turing-Complet est de pouvoir simuler des machines de Turing dans ce langages, mais cela n'est pas au programme du lycée.

L'avantage de la redstone de Minecraft est qu'elle peut simuler des circuits logiques complèxes et recréer dans le jeu des modèles de calculs et donc possiblement une machine de Turing ou une machine s'approchant du modèle de Von Neumann (modèle observé dans le cours).
Il a été prouvé que Minecraft est **Turing-Complet** grâce à ses composants et surtout la possibilité de construire un ordinateur avec 64ko de mémoire dans Minecraft et aussi de pouvoir faire un ordinateur qui joue à Minecraft dans Minecraft.

## Composants de redstone

Il existe un bon nombre de composants en redstone mais uniquement 3 composants seront necessaires pour ce TD.

| Composant          | Image | Explication                                                                                                                                                                                            |
|--------------------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Poudre de redstone |       | La poudre de redstone est l'élément principal des circuits. Elle permet de réaliser tous les tracés et de relier les composants à l'instar d'un cable de cuivre ou d'un tracé fait sur une carte-mère. |
| Répéteur de redstone |      | Le répéteur de redstone permet de redonner de l'intensité au tracé de poudre de redstone créé. En effet, comme pour un vrai câble électrique, on peut retrouver des déperditions lors de longues distances.|
| Lampe de redstone | | Comme son nom l'indique, la lampe de redstone est une représentation d'une ampoule que l'on peut relier à une platine comme lors des simulations de circuits électroniques au collège. Elle s'allume si elle reçoit un courant en entrée. Elle nous servira à analyser les résultats lors des tests.|

## Objectifs de la séance

L'objectif principal de la séance est la réalisation de circuits logiques dans Minecraft. Cela permet de se rendre compte de la difficulté de créer des circuits logiques compacts et qui sont entièrement fonctionnels (c'est à dire sans court-circuits par exemple).

Il faudra ainsi savoir créer les différentes portes logiques vues dans les cours précédents (AND, OR, NOT) et de les mettre ensemble pour recréer des circuits logiques analysés dans les exercices.

## Portes logiques dans Minecraft

Il est possible de réaliser toutes les portes logiques dans Minecraft.
