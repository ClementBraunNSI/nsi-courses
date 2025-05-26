# Projet - Jeu de Devinette

Le but de ce projet est de créer un jeu où l'ordinateur choisit un nombre aléatoire et le joueur doit le deviner.

## Fonctionnalités requises

Le jeu doit :
- Générer un nombre aléatoire entre 1 et 100
- Permettre au joueur de faire des propositions
- Indiquer si le nombre proposé est trop grand ou trop petit
- Compter le nombre d'essais
- Permettre de rejouer

## Étapes du projet

### 1. Génération du nombre aléatoire

!!! fox_exercice "Nombre aléatoire"
    **Créer une fonction `generer_nombre` qui ne prend pas de paramètres et renvoie un nombre aléatoire entre 1 et 100.**
    
    *Indication : Utiliser le module `random` et la fonction `randint`.*

### 2. Vérification de la proposition

!!! fox_exercice "Vérification"
    **Créer une fonction `verifier_proposition` qui prend en paramètres :**
    - le nombre à deviner
    - la proposition du joueur
    
    **La fonction doit renvoyer :**
    - "Trop grand!" si la proposition est supérieure
    - "Trop petit!" si la proposition est inférieure
    - "Gagné!" si la proposition est correcte

### 3. Gestion des entrées utilisateur

!!! fox_exercice "Saisie sécurisée"
    **Créer une fonction `demander_nombre` qui :**
    - Demande au joueur de saisir un nombre
    - Vérifie que l'entrée est bien un nombre
    - Renvoie le nombre si valide
    - Redemande si l'entrée n'est pas valide

### 4. Boucle de jeu principale

!!! fox_exercice "Boucle de jeu"
    **Créer une fonction `jouer` qui :**
    1. Génère un nombre aléatoire
    2. Initialise le compteur d'essais
    3. Tant que le joueur n'a pas gagné :
        - Demande une proposition
        - Affiche le résultat de la vérification
        - Incrémente le compteur d'essais
    4. Affiche le nombre d'essais nécessaires
    5. Propose de rejouer

### 5. Interface utilisateur

!!! fox_exercice "Interface"
    **Créer une fonction `afficher_accueil` qui :**
    - Affiche un message de bienvenue
    - Explique les règles du jeu
    - Lance la partie

!!! fox_exercice_test "Test du jeu"
    **Tester le jeu avec les scénarios suivants :**
    1. Trouver le nombre en moins de 5 essais
    2. Entrer des valeurs invalides (lettres, symboles)
    3. Jouer plusieurs parties d'affilée