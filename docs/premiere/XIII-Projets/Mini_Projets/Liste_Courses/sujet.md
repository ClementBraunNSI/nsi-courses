# Projet - Liste de Courses

Le but de ce projet est de créer un gestionnaire de liste de courses simple permettant d'ajouter, supprimer et modifier des articles.

## Fonctionnalités requises
- Ajouter des articles avec leur quantité
- Supprimer des articles
- Modifier la quantité d'un article
- Afficher la liste complète
- Sauvegarder et charger la liste

## Étapes du projet

### 1. Gestion des articles

!!! fox_exercice "Manipulation de la liste"
    **Créer les fonctions suivantes :**
    - `ajouter_article(liste, article, quantite)`
    - `supprimer_article(liste, article)`
    - `modifier_quantite(liste, article, nouvelle_quantite)`
    - `afficher_liste(liste)`

### 2. Sauvegarde et chargement

!!! fox_exercice "Persistance des données"
    **Créer les fonctions suivantes :**
    - `sauvegarder_liste(liste, nom_fichier)`
    - `charger_liste(nom_fichier)`

### 3. Interface utilisateur

!!! fox_exercice "Menu principal"
    **Créer une fonction `afficher_menu` qui propose :**
    1. Ajouter un article
    2. Supprimer un article
    3. Modifier une quantité
    4. Afficher la liste
    5. Sauvegarder la liste
    6. Charger une liste
    7. Quitter

### 4. Programme principal

!!! fox_exercice "Gestion de la liste"
    **Créer une fonction `gerer_liste` qui :**
    1. Initialise une liste vide
    2. Affiche le menu
    3. Exécute l'action choisie
    4. Continue jusqu'à ce que l'utilisateur choisisse de quitter

!!! fox_exercice_test "Test du programme"
    **Tester le programme en :**
    1. Ajoutant plusieurs articles
    2. Modifiant des quantités
    3. Supprimant des articles
    4. Sauvegardant et rechargeant la liste