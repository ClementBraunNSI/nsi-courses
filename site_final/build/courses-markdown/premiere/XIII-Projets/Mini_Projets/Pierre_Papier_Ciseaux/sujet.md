# Projet - Pierre, Papier, Ciseaux

Le but de ce projet est de créer le jeu classique "Pierre, Papier, Ciseaux" où le joueur affronte l'ordinateur.

## Règles du jeu
- La pierre bat les ciseaux
- Les ciseaux battent le papier
- Le papier bat la pierre

## Étapes du projet

### 1. Choix de l'ordinateur

!!! fox_exercice "Choix aléatoire"
    **Créer une fonction `choix_ordinateur` qui :**
    - Ne prend pas de paramètres
    - Renvoie aléatoirement "pierre", "papier" ou "ciseaux"

### 2. Choix du joueur

!!! fox_exercice "Saisie du joueur"
    **Créer une fonction `choix_joueur` qui :**
    - Demande au joueur de choisir entre pierre, papier, ciseaux
    - Vérifie que le choix est valide
    - Redemande si le choix n'est pas valide
    - Renvoie le choix en minuscules

### 3. Détermination du gagnant

!!! fox_exercice "Vérification du gagnant"
    **Créer une fonction `determiner_gagnant` qui prend en paramètres :**
    - Le choix du joueur
    - Le choix de l'ordinateur
    
    **La fonction doit renvoyer :**
    - "Gagné!" si le joueur gagne
    - "Perdu!" si l'ordinateur gagne
    - "Égalité!" en cas d'égalité

### 4. Gestion du score

!!! fox_exercice "Score"
    **Créer une fonction `gerer_score` qui :**
    - Maintient le score du joueur et de l'ordinateur
    - Met à jour les scores après chaque manche
    - Affiche le score actuel

### 5. Boucle de jeu

!!! fox_exercice "Partie complète"
    **Créer une fonction `jouer_partie` qui :**
    1. Initialise les scores
    2. Tant que le joueur veut continuer :
        - Obtient les choix du joueur et de l'ordinateur
        - Détermine le gagnant
        - Met à jour les scores
        - Affiche le résultat
        - Demande si le joueur veut continuer

!!! fox_exercice_test "Test du jeu"
    **Tester le jeu avec les scénarios suivants :**
    1. Jouer plusieurs manches
    2. Tester toutes les combinaisons possibles
    3. Entrer des choix invalides
    4. Vérifier que les scores sont correctement mis à jour