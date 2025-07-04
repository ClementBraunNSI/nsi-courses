# Projet - Système de Gestion de Tournoi Sportif 🏆

L'objectif de ce projet est de développer une application pour gérer des tournois sportifs. L'application permettra d'enregistrer des équipes, de générer des matchs, d'enregistrer les scores et d'afficher un classement.

## Concepts Abordés

- Structures de données : listes de dictionnaires (équipes, matchs, classement).
- Algorithmes : génération de paires de matchs (par exemple, tournoi à la ronde), calcul de points et classement.
- Fonctions pour organiser le code.
- Saisie et validation des entrées utilisateur.
- Manipulation de fichiers (optionnel, pour sauvegarder l'état du tournoi).

## Fonctionnalités à Implémenter

### 1. Gestion des Équipes

!!! fox_exercice "Structure d'une équipe"
    Définir une structure pour représenter une équipe. Un dictionnaire peut contenir :
    - `nom_equipe` (chaîne de caractères, unique)
    - `joueurs` (liste de chaînes de caractères, noms des joueurs)
    - `points` (entier, initialisé à 0)
    - `matchs_joues` (entier, initialisé à 0)
    - `victoires` (entier, initialisé à 0)
    - `nuls` (entier, initialisé à 0)
    - `defaites` (entier, initialisé à 0)
    - `buts_marques` (entier, initialisé à 0)
    - `buts_encaisses` (entier, initialisé à 0)

!!! fox_exercice "Liste des équipes"
    Créer une liste globale `equipes_tournoi` pour stocker toutes les équipes participantes.

!!! fox_exercice "Ajouter une équipe"
    Créer une fonction `ajouter_equipe(equipes_tournoi, nom_equipe, liste_joueurs)` qui :
    1. Vérifie si une équipe avec `nom_equipe` existe déjà.
    2. Si non, crée un dictionnaire pour la nouvelle équipe et l'ajoute à `equipes_tournoi`.
    3. Renvoie `True` si ajoutée, `False` sinon.

!!! fox_exercice_test "Tests de la gestion des équipes"
    1. Initialiser `equipes_tournoi`.
    2. Ajouter plusieurs équipes avec leurs listes de joueurs.
    3. Essayer d'ajouter une équipe avec un nom déjà existant.
    4. Afficher la liste des équipes pour vérifier.

### 2. Génération des Matchs (Tournoi à la Ronde Simple)

Dans un tournoi à la ronde (ou "Round Robin"), chaque équipe rencontre toutes les autres équipes une fois.

!!! fox_exercice "Structure d'un match"
    Définir une structure pour un match (dictionnaire) :
    - `equipe_domicile` (nom de l'équipe)
    - `equipe_exterieur` (nom de l'équipe)
    - `score_domicile` (entier, `None` si non joué)
    - `score_exterieur` (entier, `None` si non joué)
    - `joue` (booléen, `False` initialement)

!!! fox_exercice "Générer le calendrier des matchs"
    Créer une fonction `generer_calendrier(equipes_tournoi)` qui :
    1. Prend la liste des noms d'équipes.
    2. Génère une liste de tous les matchs possibles où chaque équipe joue contre chaque autre équipe une seule fois. (Attention à ne pas faire jouer une équipe contre elle-même et à ne pas dupliquer les matchs, ex: A vs B est pareil que B vs A pour la génération initiale).
    3. Renvoie la liste des dictionnaires de matchs (scores à `None`, `joue` à `False`).
    *Astuce : Pour N équipes, il y aura N*(N-1)/2 matchs.*

!!! fox_exercice_test "Test de la génération des matchs"
    1. Créer une liste de 3 ou 4 équipes.
    2. Générer le calendrier des matchs.
    3. Afficher le calendrier pour vérifier que toutes les paires uniques sont présentes.

### 3. Enregistrement des Scores

!!! fox_exercice "Enregistrer un résultat de match"
    Créer une fonction `enregistrer_resultat(match, score_dom, score_ext, equipes_tournoi)` qui :
    1. Met à jour `score_domicile`, `score_exterieur` et `joue` pour le `match` donné.
    2. Met à jour les statistiques (`points`, `matchs_joues`, `victoires`, `nuls`, `defaites`, `buts_marques`, `buts_encaisses`) des deux équipes impliquées dans `equipes_tournoi`.
        - Victoire : 3 points
        - Nul : 1 point
        - Défaite : 0 points

!!! fox_exercice "Saisie des scores"
    Créer une fonction qui permet à l'utilisateur de parcourir les matchs non joués et de saisir les scores.
    La fonction demandera le nom de l'équipe à domicile, le nom de l'équipe à l'extérieur, puis les scores.

!!! fox_exercice_test "Test de l'enregistrement des scores"
    1. Prendre un calendrier de matchs généré.
    2. Enregistrer les résultats pour quelques matchs.
    3. Vérifier que les scores sont bien enregistrés dans les matchs et que les statistiques des équipes (points, victoires, etc.) sont correctement mises à jour.

### 4. Affichage du Classement

!!! fox_exercice "Calculer et afficher le classement"
    Créer une fonction `afficher_classement(equipes_tournoi)` qui :
    1. Trie les équipes dans `equipes_tournoi` en fonction des critères suivants (par ordre de priorité) :
        a. Le plus de `points`.
        b. La meilleure différence de buts (`buts_marques` - `buts_encaisses`).
        c. Le plus de `buts_marques`.
    2. Affiche le classement de manière lisible, incluant le rang, nom de l'équipe, points, matchs joués, V, N, D, BM, BE, Diff.

!!! fox_exercice_test "Test du classement"
    1. Après avoir enregistré plusieurs résultats de matchs, appeler `afficher_classement`.
    2. Vérifier que le classement est correct selon les règles de tri.

### 5. Interface Utilisateur

!!! fox_exercice "Menu principal"
    Créer une interface en mode texte pour :
    1. Ajouter des équipes.
    2. Générer/Afficher le calendrier des matchs.
    3. Enregistrer les résultats des matchs.
    4. Afficher le classement.
    5. Quitter.

!!! fox_exercice_test "Test de l'application complète"
    1. Lancer l'application.
    2. Ajouter 3-4 équipes.
    3. Générer les matchs.
    4. Enregistrer les scores pour tous les matchs.
    5. Afficher le classement final.

## Pour aller plus loin (Optionnel)

- **Gestion de plusieurs phases de tournoi** (poules puis phase finale à élimination directe).
- **Sauvegarde et chargement de l'état du tournoi** dans un fichier (JSON ou CSV).
- **Meilleur buteur** : Suivre les buts par joueur.
- **Interface graphique** avec Tkinter ou Pygame.
- **Génération de calendrier plus complexe** (ex: algorithme de Berger pour les tournois à la ronde avec gestion des matchs aller-retour ou des journées).