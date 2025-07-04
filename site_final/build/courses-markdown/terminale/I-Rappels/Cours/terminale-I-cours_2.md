# Listes et tableaux

## Objectifs
Rappeler les concepts fondamentaux des listes en Python et leur manipulation.

## Création de listes

### Déclaration et initialisation
```python
# Liste vide
liste_vide = []
liste_vide2 = list()

# Liste avec des éléments
nombres = [1, 2, 3, 4, 5]
fruits = ["pomme", "banane", "orange"]
mixte = [1, "hello", 3.14, True]

# Liste avec répétition
zeros = [0] * 5  # [0, 0, 0, 0, 0]
```

### Création avec range()
```python
# Convertir range en liste
nombres = list(range(10))        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pairs = list(range(0, 11, 2))    # [0, 2, 4, 6, 8, 10]
```

## Accès aux éléments

### Indexation
```python
fruits = ["pomme", "banane", "orange", "kiwi"]

# Index positifs
print(fruits[0])   # pomme (premier élément)
print(fruits[1])   # banane
print(fruits[3])   # kiwi (dernier élément)

# Index négatifs
print(fruits[-1])  # kiwi (dernier élément)
print(fruits[-2])  # orange (avant-dernier)
```

### Slicing (tranches)
```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Syntaxe : liste[début:fin:pas]
print(nombres[2:5])      # [2, 3, 4]
print(nombres[:3])       # [0, 1, 2]
print(nombres[7:])       # [7, 8, 9]
print(nombres[::2])      # [0, 2, 4, 6, 8]
print(nombres[::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

## Modification des listes

### Modification d'éléments
```python
fruits = ["pomme", "banane", "orange"]
fruits[1] = "poire"  # Remplace "banane" par "poire"
print(fruits)  # ["pomme", "poire", "orange"]
```

### Ajout d'éléments
```python
fruits = ["pomme", "banane"]

# Ajouter à la fin
fruits.append("orange")
print(fruits)  # ["pomme", "banane", "orange"]

# Insérer à une position
fruits.insert(1, "poire")
print(fruits)  # ["pomme", "poire", "banane", "orange"]

# Étendre avec une autre liste
fruits.extend(["kiwi", "mangue"])
print(fruits)  # ["pomme", "poire", "banane", "orange", "kiwi", "mangue"]
```

### Suppression d'éléments
```python
fruits = ["pomme", "banane", "orange", "kiwi"]

# Supprimer par valeur
fruits.remove("banane")
print(fruits)  # ["pomme", "orange", "kiwi"]

# Supprimer par index
del fruits[1]
print(fruits)  # ["pomme", "kiwi"]

# Supprimer et récupérer le dernier élément
dernier = fruits.pop()
print(dernier)  # kiwi
print(fruits)   # ["pomme"]

# Vider la liste
fruits.clear()
print(fruits)  # []
```

## Parcours de listes

### Parcours simple
```python
fruits = ["pomme", "banane", "orange"]

# Parcours des éléments
for fruit in fruits:
    print(fruit)

# Parcours avec index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Parcours avec enumerate
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

### Parcours avec conditions
```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Afficher les nombres pairs
for nombre in nombres:
    if nombre % 2 == 0:
        print(nombre)

# Compter les éléments > 5
compteur = 0
for nombre in nombres:
    if nombre > 5:
        compteur += 1
print(f"Nombres > 5 : {compteur}")
```

## Méthodes utiles

### Recherche et test
```python
fruits = ["pomme", "banane", "orange", "banane"]

# Vérifier la présence
print("pomme" in fruits)      # True
print("kiwi" not in fruits)   # True

# Trouver l'index
index = fruits.index("banane")  # 1 (première occurrence)
print(index)

# Compter les occurrences
compteur = fruits.count("banane")  # 2
print(compteur)
```

### Tri et organisation
```python
nombres = [3, 1, 4, 1, 5, 9, 2, 6]

# Trier la liste (modifie l'original)
nombres.sort()
print(nombres)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Trier en ordre décroissant
nombres.sort(reverse=True)
print(nombres)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Créer une nouvelle liste triée
originale = [3, 1, 4, 1, 5]
triee = sorted(originale)
print(originale)  # [3, 1, 4, 1, 5] (inchangée)
print(triee)      # [1, 1, 3, 4, 5]

# Inverser l'ordre
nombres.reverse()
print(nombres)
```

## Listes en compréhension

### Syntaxe de base
```python
# Créer une liste des carrés
carres = [x**2 for x in range(10)]
print(carres)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtrer avec condition
pairs = [x for x in range(20) if x % 2 == 0]
print(pairs)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transformer des chaînes
mots = ["python", "java", "javascript"]
majuscules = [mot.upper() for mot in mots]
print(majuscules)  # ["PYTHON", "JAVA", "JAVASCRIPT"]
```

## Tableaux à deux dimensions

### Création et manipulation
```python
# Matrice 3x3
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accès aux éléments
print(matrice[1][2])  # 6 (ligne 1, colonne 2)

# Parcours d'une matrice
for ligne in matrice:
    for element in ligne:
        print(element, end=" ")
    print()  # Nouvelle ligne

# Parcours avec indices
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        print(f"matrice[{i}][{j}] = {matrice[i][j]}")
```

## Exercices de révision

### Exercice 1 : Manipulation de base
Écrire des fonctions pour :
1. Trouver le maximum et minimum d'une liste
2. Calculer la moyenne d'une liste de nombres
3. Supprimer les doublons d'une liste
4. Fusionner deux listes triées

### Exercice 2 : Recherche et tri
Écrire des programmes pour :
1. Recherche linéaire dans une liste
2. Tri par sélection
3. Compter les occurrences de chaque élément
4. Trouver le deuxième plus grand élément

### Exercice 3 : Listes de listes
Travailler avec des matrices pour :
1. Additionner deux matrices
2. Transposer une matrice
3. Trouver la somme de chaque ligne
4. Vérifier si une matrice est symétrique

### Exercice 4 : Applications pratiques
Créer des programmes pour :
1. Gestionnaire de notes d'élèves
2. Inventaire de magasin
3. Carnet d'adresses simple
4. Jeu du pendu avec liste de mots