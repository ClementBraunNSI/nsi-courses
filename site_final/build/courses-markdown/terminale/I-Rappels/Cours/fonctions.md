# Fonctions

## Objectifs
Rappeler la définition, l'utilisation et l'importance des fonctions en programmation.

## Définition d'une fonction

### Syntaxe de base
```python
def nom_fonction(parametre1, parametre2):
    """Documentation de la fonction"""
    # Corps de la fonction
    resultat = parametre1 + parametre2
    return resultat
```

### Fonction simple sans paramètre
```python
def dire_bonjour():
    """Affiche un message de salutation"""
    print("Bonjour !")

# Appel de la fonction
dire_bonjour()  # Affiche : Bonjour !
```

### Fonction avec paramètres
```python
def calculer_aire_rectangle(longueur, largeur):
    """Calcule l'aire d'un rectangle"""
    aire = longueur * largeur
    return aire

# Appel avec arguments
resultat = calculer_aire_rectangle(5, 3)
print(f"Aire : {resultat}")  # Aire : 15
```

## Valeur de retour

### Fonction avec return
```python
def carre(nombre):
    """Retourne le carré d'un nombre"""
    return nombre ** 2

resultat = carre(4)
print(resultat)  # 16
```

### Fonction sans return (procédure)
```python
def afficher_table(nombre, limite=10):
    """Affiche la table de multiplication"""
    for i in range(1, limite + 1):
        print(f"{nombre} x {i} = {nombre * i}")

afficher_table(7, 5)
```

### Retour multiple
```python
def diviser(dividende, diviseur):
    """Retourne le quotient et le reste"""
    quotient = dividende // diviseur
    reste = dividende % diviseur
    return quotient, reste

q, r = diviser(17, 5)
print(f"17 ÷ 5 = {q} reste {r}")  # 17 ÷ 5 = 3 reste 2
```

## Paramètres

### Paramètres obligatoires
```python
def presenter_personne(nom, prenom, age):
    """Présente une personne"""
    print(f"Je m'appelle {prenom} {nom} et j'ai {age} ans.")

presenter_personne("Dupont", "Marie", 17)
```

### Paramètres par défaut
```python
def saluer(nom, formule="Bonjour"):
    """Salue une personne avec une formule personnalisable"""
    print(f"{formule} {nom} !")

saluer("Alice")              # Bonjour Alice !
saluer("Bob", "Bonsoir")     # Bonsoir Bob !
```

### Paramètres nommés
```python
def creer_profil(nom, age, ville="Paris", profession="Étudiant"):
    """Crée un profil utilisateur"""
    return f"{nom}, {age} ans, {profession} à {ville}"

# Appel avec paramètres nommés
profil = creer_profil(nom="Alice", age=17, ville="Lyon")
print(profil)
```

## Portée des variables

### Variables locales
```python
def ma_fonction():
    x = 10  # Variable locale
    print(f"x dans la fonction : {x}")

ma_fonction()
# print(x)  # Erreur : x n'existe pas ici
```

### Variables globales
```python
y = 20  # Variable globale

def afficher_y():
    print(f"y dans la fonction : {y}")

def modifier_y():
    global y
    y = 30
    print(f"y modifié : {y}")

afficher_y()  # y dans la fonction : 20
modifier_y()  # y modifié : 30
print(f"y global : {y}")  # y global : 30
```

## Fonctions utiles

### Fonctions mathématiques
```python
import math

def calculer_distance(x1, y1, x2, y2):
    """Calcule la distance entre deux points"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def factorielle(n):
    """Calcule la factorielle de n"""
    if n <= 1:
        return 1
    else:
        return n * factorielle(n - 1)
```

### Fonctions de validation
```python
def est_pair(nombre):
    """Vérifie si un nombre est pair"""
    return nombre % 2 == 0

def est_majeur(age):
    """Vérifie si une personne est majeure"""
    return age >= 18

def valider_email(email):
    """Validation simple d'un email"""
    return "@" in email and "." in email
```

## Exercices de révision

### Exercice 1 : Fonctions mathématiques
Écrire des fonctions pour :
1. Calculer le périmètre et l'aire d'un cercle
2. Convertir des températures (Celsius ↔ Fahrenheit)
3. Calculer la moyenne de trois notes
4. Déterminer si un nombre est premier

### Exercice 2 : Jeux et divertissement
Écrire des fonctions pour :
1. Générer un mot de passe aléatoire
2. Jouer à pierre-papier-ciseaux
3. Calculer l'âge en jours
4. Convertir un nombre en lettres (1 → "un")

### Exercice 3 : Validation et traitement
Écrire des fonctions pour :
1. Valider un numéro de téléphone
2. Compter les voyelles dans un mot
3. Inverser une chaîne de caractères
4. Vérifier si un mot est un palindrome

### Exercice 4 : Calculatrice avancée
Créer un programme avec des fonctions pour :
1. Addition, soustraction, multiplication, division
2. Puissance et racine carrée
3. Calculs trigonométriques
4. Menu interactif pour choisir l'opération