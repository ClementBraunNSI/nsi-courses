# Variables et types de données

## Objectifs
Rappeler les notions fondamentales de variables et types de données vues en Première.

## Variables en Python

### Déclaration et affectation
```python
# Déclaration et affectation d'une variable
nom = "Alice"
age = 17
taille = 1.65
est_majeur = False
```

### Règles de nommage
- Commence par une lettre ou un underscore
- Peut contenir des lettres, chiffres et underscores
- Sensible à la casse
- Pas de mots-clés Python

## Types de données de base

### Types numériques
```python
# Entier (int)
nombre_eleves = 25

# Flottant (float)
moyenne = 14.5

# Opérations arithmétiques
resultat = 10 + 3 * 2  # 16
quotient = 15 // 4     # 3 (division entière)
reste = 15 % 4         # 3 (modulo)
puissance = 2 ** 3     # 8
```

### Type chaîne de caractères (str)
```python
# Déclaration
prenom = "Marie"
nom = 'Dupont'
message = """Bonjour,
Comment allez-vous ?"""

# Concaténation
nom_complet = prenom + " " + nom

# Méthodes utiles
print(prenom.upper())     # MARIE
print(nom.lower())        # dupont
print(len(nom_complet))   # 11
```

### Type booléen (bool)
```python
# Valeurs booléennes
vrai = True
faux = False

# Opérateurs de comparaison
resultat1 = 5 > 3      # True
resultat2 = 10 == 10   # True
resultat3 = 7 != 8     # True

# Opérateurs logiques
resultat4 = True and False   # False
resultat5 = True or False    # True
resultat6 = not True         # False
```

## Conversion de types
```python
# Conversion explicite
nombre_str = "42"
nombre_int = int(nombre_str)    # 42
nombre_float = float(nombre_str) # 42.0

# Conversion vers chaîne
age = 17
age_str = str(age)  # "17"

# Attention aux erreurs
# int("3.14")  # ValueError
# int("abc")   # ValueError
```

## Exercices de révision

### Exercice 1 : Variables et calculs
Écrire un programme qui :
1. Demande le nom et l'âge de l'utilisateur
2. Calcule l'année de naissance
3. Affiche un message personnalisé

### Exercice 2 : Manipulation de chaînes
Écrire un programme qui :
1. Demande une phrase à l'utilisateur
2. Affiche la phrase en majuscules
3. Compte le nombre de caractères
4. Vérifie si la phrase contient le mot "Python"

### Exercice 3 : Calculs et conditions
Écrire un programme qui :
1. Demande deux nombres
2. Effectue les quatre opérations de base
3. Vérifie si le premier nombre est pair
4. Détermine le plus grand des deux nombres