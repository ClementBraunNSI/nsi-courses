# Projet : Créer un Chatbot 🤖

## Introduction
Dans ce projet, tu vas concevoir un chatbot simple capable de répondre à des questions ou d'effectuer des actions de base. L'objectif est de découvrir la programmation événementielle (si interface graphique ou web), la gestion de chaînes de caractères et la logique conditionnelle pour créer une interaction textuelle simple.

## Prérequis
- Connaissances de base en Python (variables, chaînes de caractères, listes, dictionnaires, boucles, conditions `if/elif/else`).
- Compréhension des fonctions `input()` et `print()` pour l'interaction en console.
- *Optionnel :* Notions d'interface graphique (Tkinter, etc.) ou de framework web (Flask, etc.) si tu veux aller au-delà de la console.

## Objectifs
- Gérer une conversation simple basée sur des règles prédéfinies.
- Manipuler et analyser des chaînes de caractères (détection de mots-clés, découpage).
- Utiliser des structures conditionnelles pour déterminer la réponse appropriée.
- Mettre en place une boucle pour maintenir le dialogue.
- *Optionnel :* Explorer des techniques simples de traitement du langage naturel (NLP).

## Documentation
- [Documentation Python - Fonctions `input()` et `print()`](https://docs.python.org/fr/3/library/functions.html#input)
- [Documentation Python - Méthodes des chaînes de caractères](https://docs.python.org/fr/3/library/stdtypes.html#string-methods)
- [Tutoriel sur les conditions en Python](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7169676-utilisez-les-conditions)
- [Exemple de chatbot simple en Python (divers tutoriels en ligne)](https://www.google.com/search?q=python+simple+chatbot+tutorial)

## Étapes guidées

!!! fox_exercice "1. Accueil et première interaction"
    - **Affiche un message d'accueil** sympathique lorsque le programme démarre.
    - **Demande le nom** de l'utilisateur avec `input()`.
    - **Stocke le nom** dans une variable.
    - **Salue l'utilisateur** en utilisant son nom (ex: "Bonjour [nom] !").

!!! fox_exercice "2. Dialogue basé sur des règles simples"
    - **Mets en place une boucle `while`** qui continue tant que l'utilisateur n'a pas dit "au revoir" (ou un autre mot-clé de sortie).
    - **À chaque tour de boucle** :
        - Demande à l'utilisateur ce qu'il veut dire (`input()`).
        - Utilise des `if/elif/else` pour vérifier l'entrée de l'utilisateur :
            - Si l'utilisateur dit "bonjour", réponds "Bonjour !"
            - Si l'utilisateur demande "quel est ton nom ?", réponds "Je suis un chatbot." (ou un nom que tu lui donnes).
            - Si l'utilisateur demande "ça va ?", réponds "Je vais bien, merci !"
            - Si l'utilisateur dit "au revoir", affiche un message de départ et sors de la boucle (`break`).
            - **Sinon (cas par défaut)**, réponds quelque chose comme "Je ne comprends pas." ou "Pouvez-vous reformuler ?".

!!! fox_exercice "3. Amélioration : Ignorer la casse et les espaces"
    - Modifie tes conditions pour qu'elles fonctionnent **quelle que soit la casse** (majuscules/minuscules). Utilise la méthode `.lower()` sur l'entrée utilisateur.
    - Modifie tes conditions pour qu'elles fonctionnent même s'il y a des **espaces en trop** au début ou à la fin. Utilise la méthode `.strip()`.
    - *Exemple :* `if user_input.lower().strip() == "bonjour":`

!!! fox_exercice "4. Utilisation de mots-clés"
    - Au lieu de vérifier des phrases exactes, vérifie la **présence de mots-clés** dans l'entrée utilisateur. Utilise l'opérateur `in`.
    - *Exemple :* `if "météo" in user_input.lower():` réponds "Je ne connais pas la météo, désolé."
    - Ajoute quelques règles basées sur des mots-clés (heure, aide, musique, etc.).

## Questions pour t'aider

!!! question "Gestion des réponses 🤔"
    Comment pourrais-tu organiser les paires question/réponse de manière plus structurée qu'une longue suite de `if/elif/else` ? Un dictionnaire pourrait-il être utile ?

!!! question "Compréhension limitée 🤔"
    Comment gérer les cas où l'utilisateur pose une question complexe ou utilise un langage que le chatbot ne comprend pas du tout ? Quelles stratégies adopter pour que le chatbot reste utile ou au moins poli ?

!!! question "Mémorisation simple 🤔"
    Pourrais-tu faire en sorte que le chatbot se souvienne d'une information donnée par l'utilisateur (comme son nom) et la réutilise plus tard dans la conversation ?

!!! question "Sortie de boucle 🤔"
    Comment s'assurer que l'utilisateur peut toujours quitter la conversation ? Que se passe-t-il si l'utilisateur tape "Au revoir !" avec un point d'exclamation ?

## Pour aller plus loin (Attendus Libres)

!!! fox_exercice "Réponses aléatoires"
    - Pour les cas où le chatbot ne comprend pas, ou pour varier les salutations, prépare une **liste de réponses possibles** et choisis-en une au hasard (`import random`).

!!! fox_exercice "Apprentissage simple"
    - Quand le chatbot ne comprend pas, demande à l'utilisateur **quelle aurait été la bonne réponse**. Stocke cette nouvelle paire question/réponse pour pouvoir l'utiliser la prochaine fois.
    - *Attention :* Nécessite de sauvegarder ces nouvelles connaissances (voir persistance).

!!! fox_exercice "Fonctionnalités externes"
    - Connecte ton chatbot à une API simple pour récupérer une information réelle (ex: heure actuelle, météo simple via une API gratuite, définition d'un mot).

!!! fox_exercice "Interface graphique"
    - Crée une **interface graphique** (avec Tkinter, PyQt, etc.) pour rendre l'interaction plus visuelle qu'une simple console.

!!! fox_exercice "Analyse de sentiments basique"
    - Essaie de détecter si l'utilisateur exprime un sentiment positif ou négatif en cherchant des mots-clés simples ("content", "triste", "super", "nul") et adapte la réponse du chatbot.

## Conseils
- **Commence par la console** : Maîtrise la logique de base en console avant d'ajouter une interface graphique.
- **Garde les règles simples au début** : Ne cherche pas à comprendre toutes les subtilités du langage humain immédiatement.
- **Teste avec différentes formulations** : Vérifie si ton chatbot réagit correctement à "Bonjour", "bonjour !", "Salut", etc.
- **Utilise des fonctions** pour organiser ton code, par exemple une fonction `get_response(user_input)` qui retourne la réponse du chatbot.

Bonne programmation ! 💬