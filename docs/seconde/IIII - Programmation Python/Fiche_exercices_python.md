# Fiche d'exercices : Introduction à Python

!!! danger "Attention"
    Pour tous les exercices :
    - N'oubliez pas les guillemets `"` ou `'` pour les chaînes de caractères  
    - Faites attention aux majuscules et minuscules  
    - Testez votre code après chaque modification  
    - Créez un fichier Python différent pour chaque exercice (ex: `exercice1.py`, `exercice2.py`, etc.)  
    - Recopiez vos programmes sur votre cahier pour pouvoir les réviser plus tard  

## Exercices d'introduction

!!! fox_exercice "Premier programme"
    **Écrire un programme qui affiche "Bonjour tout le monde!" dans le terminal.**

??? fox_correction "Premier programme"
    ```python
        print("Bonjour tout le monde")
    ```

!!! fox_exercice "Variables simples"
    **Créer une variable `age` qui contient votre âge et une variable `prenom` qui contient votre prénom.**
    **Afficher ces variables dans le terminal.**

??? fox_correction "Variables simples"
    ```python
        age = 16
        prenom = "Jean"
        print(prenom, age)
    ```

!!! fox_exercice "Calculs simples"
    **Créer deux variables `nombre1` et `nombre2` contenant respectivement les valeurs 42 et 7.**
    **Afficher leur somme, leur différence, leur produit et leur division.**

??? fox_correction "Calculs simples"
    ```python
        nombre1 = 42
        nombre2 = 7
        print(nombre1+nombre2, nombre1-nombre2, nombre1*nombre2, nombre1/nombre2)
    ```

## Interaction avec l'utilisateur

!!! fox_exercice "Demander le prénom"
    **Écrire un programme qui demande le prénom de l'utilisateur et affiche "Bonjour" suivi du prénom.**

!!! fox_exercice "Calculatrice simple"
    **Écrire un programme qui demande deux nombres à l'utilisateur et affiche leur somme.**
    
    *Attention : la fonction `input()` renvoie une chaîne de caractères, il faut convertir en nombre avec `int()`*

!!! fox_exercice "Présentation complète"
    **Écrire un programme qui demande le nom, l'âge et la classe d'un élève, puis affiche une phrase de présentation complète.**
    
    *Exemple : "Je m'appelle Jean, j'ai 15 ans et je suis en seconde."*

## Exercices d'application

!!! fox_exercice "Convertisseur d'euros"
    **Écrire un programme qui convertit un montant en euros vers des dollars (1 euro = 1.09 dollars).**
    
    *Le programme doit demander le montant en euros et afficher le résultat en dollars.*

!!! fox_exercice "Calcul d'âge"
    **Écrire un programme qui demande l'année de naissance d'une personne et calcule son âge en 2024.**

!!! fox_exercice "Message personnalisé"
    **Écrire un programme qui demande:**
    - Le prénom de l'utilisateur
    - Sa matière préférée
    - Sa note dans cette matière
    
    **Puis affiche un message personnalisé comme: "Bravo [prénom], tu as eu [note]/20 en [matière]!"**

!!! fox_exercice "Calculateur de moyenne"
    **Écrire un programme qui:**
    - Demande 3 notes à l'utilisateur
    - Calcule la moyenne de ces notes
    - Affiche la moyenne avec un message approprié
    
    *N'oubliez pas de convertir les entrées en nombres décimaux avec `float()`*

!!! fox_exercice "Générateur de pseudo"
    **Écrire un programme qui crée un pseudo à partir:**
    - Des 3 premières lettres du prénom
    - Des 2 premières lettres du nom
    - De l'âge
    
    *Exemple: Pour "Thomas Dupont, 15 ans" → "ThoDu15"*

!!! fox_exercice "Prix des bonbons"
    **Écrire un programme qui:**
    - Demande le prix d'un bonbon
    - Demande combien de bonbons on veut acheter
    - Affiche le prix total
    - Affiche combien il restera d'argent si on a 10 euros

!!! fox_exercice "Convertisseur de temps"
    **Écrire un programme qui convertit un nombre de minutes en heures et minutes.**
    
    *Exemple: 145 minutes = 2 heures et 25 minutes*

!!! fox_exercice "Message décoré"
    **Écrire un programme qui:**
    - Demande un mot à l'utilisateur
    - Affiche ce mot entre des symboles décoratifs
    
    *Exemple: Pour le mot "PYTHON" → "*** PYTHON ***"*