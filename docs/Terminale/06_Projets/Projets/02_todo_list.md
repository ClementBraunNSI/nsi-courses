# Projet : Application To-Do List ✅

## Introduction
Dans ce projet, tu vas concevoir une application de gestion de tâches (To-Do List). L'objectif est de permettre à un utilisateur d'ajouter, de visualiser, de cocher comme faites ou de supprimer des tâches.

## Prérequis
- Connaissances de base en Python (variables, listes, dictionnaires, boucles, conditions).
- Notions d'interface graphique (Tkinter, PyQt, Kivy, ou même une interface web simple avec Flask/Django).
- Gestion des événements (clics de bouton, saisie de texte).

## Objectifs
- Manipuler des listes ou d'autres structures de données pour stocker les tâches.
- Gérer les interactions utilisateur via une interface graphique.
- Mettre à jour dynamiquement l'affichage de la liste.
- Comprendre le cycle de vie d'une petite application.
- *Optionnel :* Aborder la persistance des données (sauvegarde/chargement).

## Documentation
- [Documentation Python - Listes](https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists)
- [Tutoriel interface graphique Tkinter (si utilisé)](https://python.developpez.com/cours/Tkinter/)
- [Tutoriel interface graphique PyQt (si utilisé)](https://python.developpez.com/cours/apprendre-python-pyqt/)
- [Gestion de fichiers en Python (pour la persistance)](https://docs.python.org/fr/3/tutorial/inputoutput.html#reading-and-writing-files)

## Étapes guidées

!!! fox_exercice "1. Initialisation de l'interface et de la liste"
    - **Crée l'interface graphique de base** : une zone pour afficher les tâches, un champ de saisie pour une nouvelle tâche, et un bouton "Ajouter".
    - **Initialise la structure de données** qui contiendra les tâches (une liste de chaînes de caractères pour commencer, ou une liste de dictionnaires si tu veux stocker plus d'infos comme l'état 'fait').
    - **Affiche la liste vide** au démarrage.

!!! fox_exercice "2. Ajout de tâches"
    - **Lie le bouton "Ajouter"** à une fonction.
    - Cette fonction doit :
        - Récupérer le texte saisi par l'utilisateur.
        - Ajouter la nouvelle tâche à ta structure de données.
        - Mettre à jour l'affichage pour montrer la nouvelle tâche.
        - Vider le champ de saisie.

!!! fox_exercice "3. Marquer une tâche comme faite"
    - **Modifie l'affichage** pour que chaque tâche ait un moyen d'être marquée comme faite (par exemple, une case à cocher à côté, ou un bouton "Fait").
    - **Lie cet élément** à une fonction qui met à jour l'état de la tâche correspondante dans ta structure de données (par exemple, ajouter un préfixe `[X]` ou changer une valeur booléenne dans un dictionnaire).
    - **Mets à jour l'affichage** pour refléter visuellement que la tâche est faite (texte barré, case cochée).

!!! fox_exercice "4. Suppression de tâches"
    - **Ajoute un bouton "Supprimer"** à côté de chaque tâche.
    - **Lie ce bouton** à une fonction qui :
        - Identifie la tâche à supprimer.
        - Retire la tâche de ta structure de données.
        - Met à jour l'affichage pour enlever la tâche.

## Questions pour t'aider

!!! question "Structure de données 🤔"
    Quelle est la meilleure façon de stocker les tâches ? Une simple liste de noms ? Une liste de dictionnaires avec le nom et l'état (faite/non faite) ? Quels sont les avantages et inconvénients de chaque approche ?

!!! question "Mise à jour de l'affichage 🤔"
    Comment faire pour que l'interface graphique reflète toujours l'état actuel de ta liste de tâches ? Faut-il tout redessiner à chaque modification, ou peut-on mettre à jour seulement les éléments concernés ?

!!! question "Liaison des événements 🤔"
    Comment associer un clic sur un bouton "Supprimer" spécifique à la bonne tâche dans ta liste ? Comment passer l'information nécessaire (par exemple, l'index de la tâche) à la fonction de suppression ?

!!! question "Persistance 🤔"
    Si tu veux sauvegarder les tâches pour les retrouver après avoir fermé l'application, comment ferais-tu ? Quel format de fichier serait simple à utiliser (texte brut, CSV, JSON) ? Quand faudrait-il sauvegarder et charger les données ?

## Pour aller plus loin (Attendus Libres)

!!! fox_exercice "Persistance des données"
    - **Implémente la sauvegarde** de la liste de tâches dans un fichier (texte, CSV, JSON) lorsque l'application se ferme ou sur demande.
    - **Implémente le chargement** de la liste depuis le fichier au démarrage de l'application.

!!! fox_exercice "Modification de tâches"
    - Permets à l'utilisateur de **modifier le texte** d'une tâche existante (par exemple, en double-cliquant dessus).

!!! fox_exercice "Priorités ou dates d'échéance"
    - Ajoute la possibilité de définir une **priorité** (Haute, Moyenne, Basse) ou une **date d'échéance** pour chaque tâche.
    - Permets de **trier ou filtrer** les tâches selon ces critères.

!!! fox_exercice "Interface améliorée"
    - **Personnalise l'apparence** de l'application (couleurs, polices, icônes).
    - Ajoute des **confirmations** avant de supprimer une tâche.
    - Affiche le **nombre de tâches restantes**.

!!! fox_exercice "Catégories/Tags"
    - Permets d'assigner des **catégories ou des tags** aux tâches (ex: "Travail", "Personnel", "Urgent").
    - Ajoute la possibilité de **filtrer** par catégorie/tag.

## Conseils
- **Commence par la logique de base** : Fais fonctionner l'ajout, l'affichage, le marquage et la suppression en console avant de te lancer dans l'interface graphique si cela te semble plus simple.
- **Sépare la logique et l'interface** : Essaie de garder les fonctions qui manipulent la liste de tâches séparées du code qui gère l'affichage. Cela rend le code plus facile à maintenir.
- **Teste chaque fonctionnalité** indépendamment avant de les combiner.
- **Choisis une bibliothèque graphique et tiens-t'y** pour ce projet, ne te disperse pas trop.

Bonne programmation ! 💻