# DS — Python pratique (BTS SIO 1re année, Bloc B3)

**Durée**: 2 heures  
**Thème**: Centre de sauvegarde des renards (FoxShelter) — conditions, boucles, fonctions  
**Contraintes**: Ne pas utiliser les listes ni les tuples. Utiliser uniquement chaînes, nombres, conditions, boucles, fonctions.

La rigueur, la rédaction et le soin sont évalués sur 2 points.

---

## Rappels autorisés

- `int(...)`, `str(...)`, `input(...)`, `print(...)`  
- Concaténation de chaînes: `"bonjour" + " monde"` → `"bonjour monde"`, `"A" + "B"` → `"AB"`, `"B" + "A"` → `"BA"`  
- Pour obtenir la taille d'une chaîne de caractères, on peut utiliser `len(chaine)`  
- Pour tester qu’un caractère appartient à un ensemble (chiffres, lettres, spéciaux), parcourir une **chaîne de référence** avec une boucle et comparer les caractères (sans listes).

## Partie A — Code à compléter (50 min)

### Exercice A1

**Compléter la fonction `nb_occurrences(texte, lettre)` qui prend une chaîne `texte` et un caractère `lettre`, et renvoie le nombre d’occurrences de `lettre` dans `texte`.**  
Entête typée obligatoire.

```python
def nb_occurrences(texte: str, lettre: str) -> int:
    compteur = 0
    for c in texte:
        # Compléter la condition d'égalité
        if ...:
            compteur = compteur + 1
    return ...
```

### Exercice A2

**Compléter la fonction `nb_chiffres(code_cage)` qui prend une chaîne `code_cage` (ex: "R-23-A") et renvoie le nombre de chiffres présents.**  
Entête typée obligatoire.

```python
def nb_chiffres(code_cage: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in code_cage:
        i = 0
        trouve = False
        while i < len(digits):
            if ...:
                trouve = True
            i = i + 1
        if ...:
            compteur = compteur + 1
    return ...
```

### Exercice A3

**Compléter `contient_majuscule(nom)` qui renvoie `True` si `nom` contient au moins une majuscule (A–Z), `False` sinon.**  
Entête typée obligatoire.

```python
def contient_majuscule(nom: str) -> bool:
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in nom:
        k = 0
        while k < len(maj):
            if ...:
                return True
            k = k + 1
    return ...
```

### Exercice A4

**Compléter `contient_symbole(identifiant)` qui renvoie `True` si `identifiant` contient au moins un symbole parmi `-` et `_`, sinon `False`.**  
Entête typée obligatoire.

```python
def contient_symbole(identifiant: str) -> bool:
    specials = "-_"
    for c in identifiant:
        i = 0
        while i < len(specials):
            if ...:
                return True
            i = i + 1
    return ...
```

### Exercice A5

**Compléter `contient_deux_types(identifiant)` qui renvoie `True` si `identifiant` contient au moins deux catégories différentes parmi: lettre, chiffre, symbole; sinon `False`, en utilisant les fonctions précédentes (`nb_occurrences` pour une lettre, `nb_chiffres`, `contient_symbole`) et une chaîne de l'alphabet.**  
Entête typée obligatoire.

```python
def contient_deux_types(identifiant: str) -> bool:
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # au moins une lettre ?
    a_lettre = False
    j = 0
    while j < len(alphabet):
        if nb_occurrences(identifiant, alphabet[j]) > ...:
            a_lettre = True
        j = j + 1
    a_chiffre = nb_chiffres(identifiant) > ...
    a_symbole = contient_symbole(...)
    if (a_lettre and a_chiffre) or (a_lettre and a_symbole) or (a_chiffre and a_symbole):
        return True
    return ...
```

### Exercice A6

**Compléter `score_identifiant(identifiant)` qui calcule un score simple:**  
- +2 si longueur ≥ 6  
- +2 si `contient_deux_types` est vrai  
- +2 si `contient_majuscule` est vrai  
- +2 si `contient_symbole` est vrai  
- +2 si `nb_chiffres(identifiant) ≥ 1`

Entête typée obligatoire.

```python
def score_identifiant(identifiant: str) -> int:
    score = 0
    if len(identifiant) >= ...:
        score = score + ...
    if contient_deux_types(...):
        score = score + ...
    if contient_majuscule(...):
        score = score + ...
    if contient_symbole(...):
        score = score + ...
    if nb_chiffres(...) >= ...:
        score = score + ...
    return ...
```

---

## Partie B — Fonctions à écrire (1h10)

### Exercice B1

**Écrire une fonction `repeter_caractere(c, n)` qui prend en paramètre un caractère `c` et un entier `n`, et qui renvoie une chaîne contenant `c` répété `n` fois (sans listes ni `*`).**

Exemple: `repeter_caractere('X', 5)` → `'XXXXX'`

### Exercice B2

**Écrire une fonction `masquer_nom(nom)` qui renvoie une nouvelle chaîne où seules la première et la dernière lettre restent visibles et où toutes les autres positions sont remplacées par `*`.**  
Si la longueur est ≤ 2, renvoyer la chaîne telle quelle.

Exemple: `masquer_nom("Renard")` → `R*****d`

### Exercice B3

**Écrire une fonction `contient_trois_identiques(chaine)` qui prend en paramètre une chaîne `chaine` et renvoie `True` si la chaîne contient au moins 3 fois le même caractère d'affilée (ex: `aaa`, `111`, `@@@`), sinon `False`.**  
Contraintes: utiliser une boucle, comparer chaque caractère au précédent, compter les répétitions consécutives, réinitialiser quand le caractère change, retourner `True` dès que le compteur atteint 3.

### Exercice B4

**Écrire une fonction `calcul_ration(age, poids)` qui prend en paramètre l’`age` (entier, années) et le `poids` (flottant, kilogrammes) et renvoie la ration journalière (entier, grammes) selon:**  
- Si `age <= 1`: `poids * 6`  
- Si `2 <= age <= 6`: `poids * 5`  
- Si `age >= 7`: `poids * 4`

Ne pas utiliser de listes. Arrondir à l’entier inférieur en convertissant simplement le résultat avec `int(...)`.

### Exercice B5

**Écrire une fonction `conseil_identifiant(identifiant)` qui renvoie une chaîne explicative avec 2 à 3 conseils personnalisés (simples phrases concaténées) si `score_identifiant(identifiant) < 6`.**  
Exemples de conseils: « ajouter une majuscule », « allonger à 6+ », « mettre un chiffre », « ajouter un symbole - ou _ ».
