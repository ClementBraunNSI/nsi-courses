# Projet : Jeu du Serpent 🐍

## Introduction
Dans ce projet, tu vas programmer le célèbre jeu du serpent (Snake). Le but est de contrôler un serpent qui grandit à chaque fois qu'il mange une pomme, tout en évitant de se mordre la queue ou de toucher les bords.

## Prérequis
- Connaissances de base en Python (variables, listes, boucles, conditions).
- Utilisation d'une bibliothèque graphique (Pygame recommandé, mais d'autres sont possibles comme Turtle ou Tkinter).
- Compréhension des coordonnées dans une fenêtre graphique.

## Objectifs
- Découvrir la gestion d'une boucle de jeu.
- Manipuler des listes pour représenter le serpent.
- Gérer les entrées clavier pour déplacer le serpent.
- Afficher dynamiquement le jeu à l'écran.
- Gérer les collisions.

## Documentation
- [Documentation Pygame](https://www.pygame.org/docs/)
- [Tutoriel Snake en Python (OpenClassrooms)](https://openclassrooms.com/fr/courses/4425126-apprenez-a-programmer-en-python/4439216-creez-le-jeu-du-snake)
- [Exemple de grille et coordonnées (Wikipédia)](https://fr.wikipedia.org/wiki/Jeu_du_serpent)

## Étapes guidées

!!! fox_exercice "1. Initialisation de la fenêtre et du serpent"
    - **Crée une fenêtre de jeu** avec des dimensions fixes (par exemple 600x400 pixels).
    - **Affiche un fond** (uni ou une grille).
    - **Représente le serpent** : Utilise une liste de coordonnées (tuples `(x, y)`) pour les segments du serpent. Commence avec un serpent de 3 segments au centre.
    - **Initialise la direction** du serpent (par exemple, vers la droite).

!!! fox_exercice "2. Déplacement du serpent"
    - **Mets en place la boucle de jeu principale** qui s'exécute à intervalles réguliers (tick).
    - **À chaque tick** :
        - Calcule la nouvelle position de la tête en fonction de la direction actuelle.
        - Ajoute la nouvelle tête au début de la liste représentant le serpent.
        - Supprime le dernier segment de la queue (pour que le serpent avance sans grandir).
    - **Gère les entrées clavier** (flèches directionnelles) pour changer la direction du serpent. Attention : le serpent ne doit pas pouvoir faire demi-tour sur lui-même (si va à droite, ne peut pas aller à gauche).
    - **Affiche le serpent** à chaque tick.

!!! fox_exercice "3. Ajout de la pomme et croissance"
    - **Représente la pomme** par ses coordonnées `(x, y)`.
    - **Place une pomme** à une position aléatoire sur la grille, en s'assurant qu'elle n'apparaît pas sur le serpent.
    - **Détecte la collision** : Si la tête du serpent atteint la même position que la pomme :
        - Le serpent **ne supprime pas** sa queue lors de ce tick (il grandit).
        - Une **nouvelle pomme** apparaît à une autre position aléatoire.
    - **Affiche la pomme**.

!!! fox_exercice "4. Gestion des collisions et fin de partie"
    - **Détecte les collisions avec les murs** : Si la tête du serpent sort des limites de la fenêtre, la partie s'arrête.
    - **Détecte les collisions avec le corps** : Si la tête du serpent touche l'un de ses propres segments (sauf la tête elle-même), la partie s'arrête.
    - **Affiche un message de "Game Over"** lorsque la partie est terminée.

## Questions pour t'aider

!!! question "Représentation du serpent 🤔"
    Comment une liste de coordonnées peut-elle représenter efficacement le serpent et faciliter son déplacement et sa croissance ?

!!! question "Boucle de jeu et vitesse 🤔"
    Comment contrôler la vitesse du serpent ? Comment la bibliothèque graphique choisie gère-t-elle le temps (ticks) ?

!!! question "Génération aléatoire 🤔"
    Comment s'assurer que la pomme apparaît à un endroit valide (pas sur un mur si tu en as, pas sur le serpent) ? Quelle fonction utiliser pour générer des nombres aléatoires ?

!!! question "Détection de collision 🤔"
    Quelle condition simple permet de vérifier si la tête du serpent touche un mur ? Comment vérifier si la tête touche une partie de son corps ?

## Pour aller plus loin (Attendus Libres)

!!! fox_exercice "Ajout d'un score"
    - **Implémente un score** qui augmente à chaque pomme mangée.
    - **Affiche le score** à l'écran pendant la partie et à la fin.

!!! fox_exercice "Relancer une partie"
    - Permets à l'utilisateur de **relancer une partie** après un "Game Over" sans avoir à fermer et rouvrir le programme.

!!! fox_exercice "Obstacles"
    - Ajoute des **obstacles fixes** sur la grille. Le serpent meurt s'il les touche.
    - *Plus difficile :* Ajoute des **obstacles mobiles**.

!!! fox_exercice "Accélération"
    - Fais en sorte que le serpent **accélère** légèrement à chaque pomme mangée ou toutes les N pommes.

!!! fox_exercice "Personnalisation graphique et sonore"
    - Utilise des **couleurs différentes** pour la tête, le corps, la pomme, le fond.
    - *Plus avancé :* Utilise des **images (sprites)** pour le serpent et la pomme.
    - Ajoute des **effets sonores** (manger une pomme, game over).

## Conseils
- **Commence simple** : Fais d'abord bouger un seul carré. Puis fais bouger une ligne de 3 carrés. Ensuite, gère la croissance.
- **Teste souvent** : Après chaque petite étape, vérifie que ton code fonctionne comme prévu.
- **Décompose le problème** : Si une étape te semble compliquée, essaie de la diviser en sous-problèmes plus petits.
- **Utilise des fonctions** : Organise ton code en fonctions logiques (ex: `dessiner_serpent()`, `verifier_collisions()`, `placer_pomme()`).
- **N'hésite pas à consulter la documentation** ou les tutoriels si tu bloques.

Bonne programmation ! 🚀