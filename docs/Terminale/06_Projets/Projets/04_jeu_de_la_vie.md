# Projet : Jeu de la Vie (Conway) 🧬

## Introduction
Dans ce projet, tu vas programmer le célèbre "Jeu de la Vie" de John Conway. Il s'agit d'un automate cellulaire où l'état de chaque cellule d'une grille évolue au fil des générations selon des règles simples basées sur son voisinage, donnant naissance à des motifs complexes et parfois surprenants à partir de conditions initiales simples.

## Prérequis
- Connaissances de base en Python (variables, listes, listes imbriquées pour les grilles 2D, boucles `for`, conditions `if/else`).
- Compréhension de la manipulation des indices dans une liste 2D.
- *Optionnel :* Utilisation d'une bibliothèque graphique (Pygame, Tkinter, etc.) pour une visualisation plus agréable que la console.

## Objectifs
- Manipuler efficacement des structures de données en 2D (grilles).
- Implémenter un algorithme basé sur des règles locales pour simuler un système global.
- Gérer l'état d'un système sur plusieurs générations.
- Visualiser des données en 2D (console ou graphique).
- Découvrir un exemple classique d'automate cellulaire et de complexité émergente.

## Documentation
- [Présentation du Jeu de la Vie (Wikipédia)](https://fr.wikipedia.org/wiki/Jeu_de_la_vie)
- [Tutoriel Python sur les listes 2D (listes imbriquées)](https://python.sdv.univ-paris-diderot.fr/16_listes/) (ou ressources équivalentes)
- [Documentation Pygame (si utilisé pour le graphique)](https://www.pygame.org/docs/)
- [Exemples de motifs du Jeu de la Vie](https://www.conwaylife.com/wiki/Main_Page)

## Étapes guidées

!!! fox_exercice "1. Initialisation de la grille"
    - **Crée une fonction** qui génère une grille (liste de listes) de dimensions données (par exemple, `largeur` x `hauteur`).
    - **Initialise la grille** avec toutes les cellules "mortes" (représentées par 0 ou `False`).
    - **Permets de définir un état initial** : soit en plaçant quelques cellules "vivantes" (1 ou `True`) manuellement dans le code, soit en lisant une configuration depuis l'utilisateur ou un fichier simple.
    - *Alternative :* Initialise la grille avec des cellules vivantes aléatoires.

!!! fox_exercice "2. Affichage de la grille"
    - **Crée une fonction** qui affiche l'état actuel de la grille.
    - **En console :** Affiche des caractères différents pour les cellules vivantes (ex: 'O' ou '#') et mortes (ex: '.' ou ' ').
    - **En graphique (si utilisé) :** Dessine des carrés de couleurs différentes pour les cellules vivantes et mortes sur une surface Pygame ou un Canvas Tkinter.

!!! fox_exercice "3. Calcul de la génération suivante"
    - **Crée une fonction** `calculer_generation_suivante(grille_actuelle)` qui retourne la **nouvelle grille** après une étape d'évolution.
    - **Pour chaque cellule** de `grille_actuelle` :
        - **Compte ses voisines vivantes** : Parcours les 8 cellules adjacentes (attention aux bords de la grille !).
        - **Applique les règles du Jeu de la Vie** :
            - Une cellule vivante avec 2 ou 3 voisines vivantes reste vivante.
            - Une cellule morte avec exactement 3 voisines vivantes devient vivante.
            - Dans tous les autres cas, la cellule devient (ou reste) morte.
        - **Stocke l'état de la cellule pour la *nouvelle* génération** dans une nouvelle grille (ne modifie pas `grille_actuelle` pendant que tu la parcours !).
    - **Retourne la nouvelle grille** complètement calculée.

!!! fox_exercice "4. Boucle de simulation"
    - **Mets en place la boucle principale** du programme.
    - **À chaque tour de boucle** (génération) :
        - **Affiche** la grille actuelle.
        - **Calcule** la grille de la génération suivante en appelant ta fonction.
        - **Met à jour** la grille actuelle avec la nouvelle grille calculée.
        - **Ajoute une pause** (`time.sleep()` en console, ou gestion du framerate en graphique) pour pouvoir observer l'évolution.
    - Prévois un moyen d'arrêter la simulation (ex: après N générations, ou sur une action utilisateur).

## Questions pour t'aider

!!! question "Représentation de la grille 🤔"
    Une liste de listes est courante. Quels sont les avantages ? Comment accéder à la cellule à la ligne `y` et colonne `x` ? Comment connaître les dimensions de la grille ?

!!! question "Gestion des bords 🤔"
    Comment gérer le comptage des voisins pour les cellules situées sur les bords ou dans les coins de la grille ? Faut-il considérer que l'extérieur est toujours mort ? Ou imaginer que la grille "s'enroule" sur elle-même (tore) ? Quelle est l'approche la plus simple à implémenter ?

!!! question "Mise à jour simultanée 🤔"
    Pourquoi est-il crucial de calculer l'état de *toutes* les cellules de la nouvelle génération en se basant *uniquement* sur l'état de la génération actuelle, avant de faire la mise à jour ? Que se passerait-il si tu modifiais la grille actuelle au fur et à mesure que tu calcules les nouveaux états ?

!!! question "Visualisation 🤔"
    Comment rendre l'affichage clair et rapide, surtout si la grille est grande ? En console, comment éviter le scintillement (effacer l'écran avant de redessiner) ? En graphique, comment optimiser le dessin ?

## Pour aller plus loin (Attendus Libres)

!!! fox_exercice "Interface utilisateur interactive"
    - Si tu utilises une bibliothèque graphique, permets à l'utilisateur de **dessiner l'état initial** en cliquant sur les cellules.
    - Ajoute des boutons pour **démarrer/arrêter** la simulation, avancer d'une seule génération, ou **réinitialiser** la grille.
    - Affiche le **numéro de la génération** actuelle.

!!! fox_exercice "Chargement/Sauvegarde de motifs"
    - Implémente la possibilité de **sauvegarder** l'état actuel de la grille dans un fichier (format texte simple, JSON, etc.).
    - Permets de **charger** un motif depuis un fichier.
    - Propose quelques **motifs célèbres prédéfinis** (planeur, oscillateurs, etc.) que l'utilisateur peut charger.

!!! fox_exercice "Optimisation"
    - Pour de très grandes grilles, le calcul peut devenir lent. Recherche des techniques d'optimisation (ex: ne recalculer que les zones où il y a eu des changements, utiliser NumPy si tu connais).

!!! fox_exercice "Variantes des règles"
    - Permets à l'utilisateur de **modifier les règles** de survie et de naissance (ex: "HighLife" B36/S23).

!!! fox_exercice "Grille torique"
    - Implémente la gestion des bords en considérant la grille comme un **tore** (le bord droit est voisin du bord gauche, le haut est voisin du bas).

## Conseils
- **Commence petit** : Teste ta logique avec une grille de 3x3 ou 5x5 avant de passer à plus grand.
- **Teste les règles** : Vérifie manuellement le résultat pour quelques cellules dans des cas simples (cellule isolée, bloc stable, oscillateur simple).
- **Sépare les fonctions** : Avoir des fonctions distinctes pour l'initialisation, l'affichage, le comptage des voisins et le calcul de la génération rend le code plus clair et plus facile à déboguer.
- **Attention à la copie des listes** : Quand tu crées la nouvelle grille, assure-toi de créer une *nouvelle* liste de listes, pas juste une référence à l'ancienne. `nouvelle_grille = [ligne[:] for ligne in grille_actuelle]` peut être utile pour une copie superficielle si tu utilises des 0/1.

Bonne programmation et observation ! ✨