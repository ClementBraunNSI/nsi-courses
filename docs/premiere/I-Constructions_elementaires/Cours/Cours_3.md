# 📚 Les listes en Python

## 📖 Définition et création

Une liste en Python est une structure de données ordonnée et modifiable qui peut contenir des éléments de différents types. Les listes sont définies en utilisant des crochets `[]` et les éléments sont séparés par des virgules.

```python
# Liste vide
ma_liste = []

# Liste avec des entiers
nombres = [1, 2, 3, 4, 5]

# Liste avec différents types
mixte = [1, "hello", 3.14, True]

# Liste de chaînes de caractères
prénoms = ["Alice", "Bob", "Charlie"]
```

## 📖 Accès aux éléments

On peut accéder aux éléments d'une liste en utilisant leur index (position). Les indices commencent à 0 pour le premier élément.

```python
nombres = [10, 20, 30, 40, 50]

# Accès par index positif
print(nombres[0])    # Affiche 10 (premier élément)
print(nombres[2])    # Affiche 30 (troisième élément)

# Accès par index négatif (depuis la fin)
print(nombres[-1])   # Affiche 50 (dernier élément)
print(nombres[-2])   # Affiche 40 (avant-dernier élément)
```

## 📖 Modification des listes

Les listes sont modifiables (mutables), ce qui signifie qu'on peut changer leurs éléments après leur création.

```python
fruits = ["pomme", "banane", "orange"]

# Modifier un élément
fruits[1] = "poire"
print(fruits)  # Affiche ["pomme", "poire", "orange"]

# Ajouter un élément à la fin
fruits.append("kiwi")
print(fruits)  # Affiche ["pomme", "poire", "orange", "kiwi"]

# Insérer un élément à une position spécifique
fruits.insert(1, "mangue")
print(fruits)  # Affiche ["pomme", "mangue", "poire", "orange", "kiwi"]

# Supprimer un élément
fruits.remove("poire")
print(fruits)  # Affiche ["pomme", "mangue", "orange", "kiwi"]
```

## 📖 Opérations sur les listes

### Longueur d'une liste

```python
nombres = [1, 2, 3, 4, 5]
longueur = len(nombres)
print(longueur)  # Affiche 5
```

### Concaténation de listes

```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste_concatenee = liste1 + liste2
print(liste_concatenee)  # Affiche [1, 2, 3, 4, 5, 6]
```

### Répétition d'une liste

```python
liste = [1, 2]
liste_repetee = liste * 3
print(liste_repetee)  # Affiche [1, 2, 1, 2, 1, 2]
```

### Vérifier la présence d'un élément

```python
fruits = ["pomme", "banane", "orange"]

if "pomme" in fruits:
    print("La pomme est dans la liste")

if "kiwi" not in fruits:
    print("Le kiwi n'est pas dans la liste")
```

## 💡 Parcours d'une liste

Il existe plusieurs façons de parcourir une liste :

### Parcours simple

```python
fruits = ["pomme", "banane", "orange"]

# Parcours des éléments
for fruit in fruits:
    print(fruit)
```

### Parcours avec indices

```python
fruits = ["pomme", "banane", "orange"]

# Parcours avec indices
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
```

### Parcours avec enumerate

```python
fruits = ["pomme", "banane", "orange"]

# Parcours avec enumerate (plus pythonique)
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")
```