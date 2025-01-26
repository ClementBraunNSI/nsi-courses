# Fiche d'exercices : Les conditions en Python

!!! danger "Attention"
    Pour tous les exercices :
    - N'oubliez pas les deux points `:` après la condition
    - Faites attention à l'indentation après une condition
    - Testez votre code avec différentes valeurs
    - Créez un fichier Python différent pour chaque exercice (ex: `exercice1.py`, `exercice2.py`, etc.)
    - Recopiez vos programmes sur votre cahier pour pouvoir les réviser plus tard

## Exercices d'introduction

!!! fox_exercice "Comparaison simple"
    **Écrire un programme qui:**
    - Demande un nombre à l'utilisateur
    - Affiche "Positif" si le nombre est supérieur à 0
    - Affiche "Négatif" si le nombre est inférieur à 0
    - Affiche "Nul" si le nombre est égal à 0

!!! fox_exercice "Pair ou impair"
    **Écrire un programme qui détermine si un nombre est pair ou impair.**
    
    *Utiliser l'opérateur modulo `%` qui donne le reste de la division*

!!! fox_exercice "Permission de sortie"
    **Écrire un programme qui:**
    - Demande l'âge d'une personne
    - Affiche "Tu peux sortir seul" si l'âge est supérieur ou égal à 18
    - Affiche "Tu dois être accompagné" sinon

## Conditions composées

!!! fox_exercice "Note et appréciation"
    **Écrire un programme qui:**
    - Demande une note sur 20
    - Affiche "Excellent" si la note est supérieure ou égale à 16
    - Affiche "Bien" si la note est entre 14 et 16
    - Affiche "Assez bien" si la note est entre 12 et 14
    - Affiche "Passable" si la note est entre 10 et 12
    - Affiche "Insuffisant" sinon

!!! fox_exercice "Calculatrice avec menu"
    **Écrire un programme qui:**
    - Demande deux nombres
    - Demande quelle opération effectuer (1: addition, 2: soustraction, 3: multiplication, 4: division)
    - Affiche le résultat de l'opération choisie

!!! fox_exercice "Jeu du plus ou moins"
    **Écrire un programme qui:**
    - Demande un nombre entre 1 et 100
    - Compare avec le nombre 42
    - Affiche "Plus grand" si le nombre est trop petit
    - Affiche "Plus petit" si le nombre est trop grand
    - Affiche "Gagné!" si c'est le bon nombre

!!! fox_exercice "Tarif de cinéma"
    **Écrire un programme qui calcule le prix d'un billet de cinéma:**
    - Demande l'âge
    - Demande si on est étudiant (réponse "oui" ou "non")
    - Affiche le tarif:
        - Moins de 14 ans: 5€
        - Étudiant: 7€
        - Normal: 9€

!!! fox_exercice "Année bissextile"
    **Écrire un programme qui détermine si une année est bissextile.**
    Une année est bissextile si:
    - Elle est divisible par 4 mais pas par 100
    - OU elle est divisible par 400

// ... existing content ...

!!! fox_exercice "Distributeur de boissons"
    **Écrire un programme qui simule un distributeur de boissons:**
    - Affiche un menu avec: 1-Eau (1€), 2-Soda (2€), 3-Jus (1.5€)
    - Demande le choix de boisson
    - Demande l'argent inséré
    - Affiche si l'achat est possible et la monnaie à rendre

!!! fox_exercice "Jeu Pierre-Feuille-Ciseaux"
    **Écrire un programme qui:**
    - Demande au joueur 1 de choisir entre "pierre", "feuille" ou "ciseaux"
    - Demande au joueur 2 de choisir
    - Affiche qui a gagné selon les règles du jeu

!!! fox_exercice "Catégories d'âge"
    **Écrire un programme qui détermine la catégorie sportive selon l'âge:**
    - Moins de 6 ans: "Baby"
    - De 6 à 8 ans: "Poussin"
    - De 9 à 11 ans: "Pupille"
    - De 12 à 14 ans: "Benjamin"
    - 15 ans et plus: "Cadet"