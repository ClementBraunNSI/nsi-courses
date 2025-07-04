# Structures conditionnelles et boucles

## Objectifs
Rappeler les structures de contrôle fondamentales : conditions et boucles.

## Structures conditionnelles

### Instruction if simple
```python
age = int(input("Quel est votre âge ? "))

if age >= 18:
    print("Vous êtes majeur")
```

### Instruction if...else
```python
note = float(input("Entrez votre note : "))

if note >= 10:
    print("Admis")
else:
    print("Refusé")
```

### Instruction if...elif...else
```python
note = float(input("Entrez votre note : "))

if note >= 16:
    print("Très bien")
elif note >= 14:
    print("Bien")
elif note >= 12:
    print("Assez bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")
```

### Conditions composées
```python
age = 17
a_permis = True

if age >= 18 and a_permis:
    print("Peut conduire seul")
elif age >= 16 and a_permis:
    print("Peut conduire accompagné")
else:
    print("Ne peut pas conduire")
```

## Boucles

### Boucle for avec range()
```python
# Afficher les nombres de 0 à 4
for i in range(5):
    print(i)

# Afficher les nombres de 1 à 10
for i in range(1, 11):
    print(i)

# Afficher les nombres pairs de 0 à 20
for i in range(0, 21, 2):
    print(i)
```

### Boucle for avec des séquences
```python
# Parcourir une chaîne
mot = "Python"
for lettre in mot:
    print(lettre)

# Parcourir une liste
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)
```

### Boucle while
```python
# Boucle while simple
compteur = 0
while compteur < 5:
    print(f"Compteur : {compteur}")
    compteur += 1

# Boucle de saisie
nombre = 0
while nombre <= 0:
    nombre = int(input("Entrez un nombre positif : "))
print(f"Vous avez saisi : {nombre}")
```

### Instructions break et continue
```python
# break : sortir de la boucle
for i in range(10):
    if i == 5:
        break
    print(i)  # Affiche 0, 1, 2, 3, 4

# continue : passer à l'itération suivante
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Affiche 1, 3, 5, 7, 9
```

## Boucles imbriquées
```python
# Table de multiplication
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print()  # Ligne vide

# Motif d'étoiles
for ligne in range(5):
    for colonne in range(ligne + 1):
        print("*", end="")
    print()  # Nouvelle ligne
```

## Exercices de révision

### Exercice 1 : Calculatrice simple
Écrire un programme qui :
1. Demande deux nombres et une opération (+, -, *, /)
2. Effectue le calcul selon l'opération choisie
3. Gère le cas de la division par zéro
4. Propose de recommencer

### Exercice 2 : Jeu de devinette
Écrire un programme qui :
1. Génère un nombre aléatoire entre 1 et 100
2. Demande à l'utilisateur de deviner
3. Indique si le nombre est trop grand ou trop petit
4. Compte le nombre d'essais
5. Félicite quand le nombre est trouvé

### Exercice 3 : Validation de saisie
Écrire un programme qui :
1. Demande une note entre 0 et 20
2. Redemande tant que la note n'est pas valide
3. Affiche la mention correspondante
4. Propose de saisir une nouvelle note

### Exercice 4 : Motifs géométriques
Écrire des programmes qui affichent :
1. Un triangle d'étoiles
2. Un carré creux
3. Un losange
4. Une pyramide inversée