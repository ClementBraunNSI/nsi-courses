# Fiche d'exercices : Les conditions en Python

## 🎯 Exercices d'introduction

### Important ⚠️ - Consignes importantes

**Pour tous les exercices :**

- N'oubliez pas les deux points `:` après la condition
- Faites attention à l'indentation dans les blocs if/else
- Testez votre code avec différentes valeurs
- Créez un fichier Python différent pour chaque exercice (ex: `exercice1.py`, `exercice2.py`, etc.)
- Recopiez vos programmes sur votre cahier pour pouvoir les réviser plus tard

### Introduction 🦊 - Majorité

**Écrire un programme qui :**

- Demande l'âge d'une personne
- Affiche "Vous êtes majeur" si l'âge est supérieur ou égal à 18
- Affiche "Vous êtes mineur" sinon

### Introduction 🦊 - Nombre positif ou négatif

**Écrire un programme qui :**

- Demande un nombre
- Affiche si le nombre est positif, négatif ou nul

### Introduction 🦊 - Comparaison de deux nombres

**Écrire un programme qui :**

- Demande deux nombres
- Affiche lequel est le plus grand (ou s'ils sont égaux)

### Introduction 🦊 - Mot de passe

**Écrire un programme qui :**

- Demande un mot de passe
- Affiche "Accès autorisé" si le mot de passe est "secret123"
- Affiche "Accès refusé" sinon

### Introduction 🦊 - Nombre pair ou impair

**Écrire un programme qui :**

- Demande un nombre entier
- Affiche si le nombre est pair ou impair

*Astuce : Un nombre est pair si le reste de sa division par 2 est égal à 0. En Python, on utilise l'opérateur `%` pour obtenir le reste d'une division.*

### Introduction 🦊 - Calculatrice simple

**Écrire un programme qui :**

- Demande deux nombres et une opération (+, -, *, /)
- Affiche le résultat de l'opération
- Gère le cas de la division par zéro

## 🌟 Niveau Facile

### Facile 🦊 - Note et mention

**Écrire un programme qui :**

- Demande une note sur 20
- Affiche la mention correspondante :
  - Note >= 16 : "Très bien"
  - Note >= 14 : "Bien"
  - Note >= 12 : "Assez bien"
  - Note >= 10 : "Passable"
  - Note < 10 : "Insuffisant"

### Facile 🦊 - Température et conseil

**Écrire un programme qui :**

- Demande la température extérieure
- Donne un conseil vestimentaire :
  - Moins de 0°C : "Portez un manteau d'hiver"
  - De 0 à 15°C : "Portez une veste"
  - De 16 à 25°C : "Un pull suffit"
  - Plus de 25°C : "T-shirt recommandé"

### Facile 🦊 - Jours du mois

**Écrire un programme qui :**

- Demande un numéro de mois (1-12)
- Affiche le nombre de jours dans ce mois
- Considère février avec 28 jours

### Facile 🦊 - Triangle possible

**Écrire un programme qui :**

- Demande trois longueurs
- Vérifie si on peut former un triangle avec ces longueurs
- (Un triangle est possible si la somme de deux côtés est toujours supérieure au troisième)

### Facile 🦊 - Réduction magasin

**Écrire un programme qui :**

- Demande le montant d'achat
- Applique une réduction :
  - Plus de 100€ : 10% de réduction
  - Plus de 50€ : 5% de réduction
  - Sinon : pas de réduction
- Affiche le montant final

## 🔥 Niveau Intermédiaire

### Intermédiaire 🦊🦊 - Équation du second degré

**Écrire un programme qui résout une équation du second degré ax² + bx + c = 0 :**

- Demande les coefficients a, b et c
- Calcule le discriminant (Δ = b² - 4ac)
- Affiche les solutions selon le cas :
  - Δ > 0 : deux solutions réelles
  - Δ = 0 : une solution double
  - Δ < 0 : pas de solution réelle

### Intermédiaire 🦊🦊 - Tarif de cinéma

**Écrire un programme qui calcule le prix d'un billet de cinéma :**

- Demande l'âge
- Demande si on est étudiant (réponse "oui" ou "non")
- Affiche le tarif :
  - Moins de 14 ans : 5€
  - Étudiant : 7€
  - Normal : 9€

### Intermédiaire 🦊🦊 - Année bissextile

**Écrire un programme qui détermine si une année est bissextile.**

Une année est bissextile si :

- Elle est divisible par 4 mais pas par 100
- OU elle est divisible par 400

### Intermédiaire 🦊🦊 - Catégories d'âge

**Écrire un programme qui détermine la catégorie sportive selon l'âge :**

- Moins de 6 ans : "Baby"
- De 6 à 8 ans : "Poussin"
- De 9 à 11 ans : "Pupille"
- De 12 à 14 ans : "Benjamin"
- 15 ans et plus : "Cadet"

## 🚀 Niveau Difficile

### Difficile 🦊🦊🦊 - Distributeur de boissons

**Écrire un programme qui simule un distributeur de boissons :**

- Affiche un menu avec : 1-Eau (1€), 2-Soda (2€), 3-Jus (1.5€)
- Demande le choix de boisson
- Demande l'argent inséré
- Affiche si l'achat est possible et la monnaie à rendre

### Difficile 🦊🦊🦊 - Jeu Pierre-Feuille-Ciseaux

**Écrire un programme qui :**

- Demande au joueur 1 de choisir entre "pierre", "feuille" ou "ciseaux"
- Demande au joueur 2 de choisir
- Affiche qui a gagné selon les règles du jeu