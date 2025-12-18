# Logique booléenne

## Introduction

La logique booléenne est un système mathématique qui ne manipule que deux valeurs : **VRAI** (True) ou **FAUX** (False). Elle est au cœur du fonctionnement des ordinateurs et permet de prendre des décisions dans les programmes informatiques.

## Les valeurs booléennes

En informatique, on utilise deux valeurs :
- **VRAI** (True, 1, ou Oui)
- **FAUX** (False, 0, ou Non)

### Exemples de la vie quotidienne
- "La lumière est allumée" → VRAI ou FAUX
- "Il pleut aujourd'hui" → VRAI ou FAUX
- "J'ai 15 ans" → VRAI ou FAUX

## Les opérateurs booléens

### 1. L'opérateur ET (AND)

L'opérateur **ET** renvoie VRAI seulement si **les deux** conditions sont vraies.

**Table de vérité du ET :**

| A     | B     | A ET B |
|-------|-------|--------|
| FAUX  | FAUX  | FAUX   |
| FAUX  | VRAI  | FAUX   |
| VRAI  | FAUX  | FAUX   |
| VRAI  | VRAI  | VRAI   |

**Exemple :**

- "J'ai mon téléphone ET j'ai du réseau" → Je peux appeler
- Si j'ai mon téléphone mais pas de réseau : FAUX
- Si j'ai du réseau mais pas mon téléphone : FAUX
- Si j'ai les deux : VRAI

**En Python :**
```python
a = True
b = False
resultat = a and b  # Résultat : False
```

### 2. L'opérateur OU (OR)

L'opérateur **OU** renvoie VRAI si **au moins une** des conditions est vraie.

**Table de vérité du OU :**

| A     | B     | A OU B |
|-------|-------|--------|
| FAUX  | FAUX  | FAUX   |
| FAUX  | VRAI  | VRAI   |
| VRAI  | FAUX  | VRAI   |
| VRAI  | VRAI  | VRAI   |

**Exemple :**
- "Je vais au cinéma OU je reste à la maison" → Une des deux actions sera vraie
- Si je vais au cinéma : VRAI
- Si je reste à la maison : VRAI
- Si je fais les deux ou aucun des deux, c'est selon le contexte

**En Python :**
```python
a = True
b = False
resultat = a or b  # Résultat : True
```

### 3. L'opérateur NON (NOT)

L'opérateur **NON** inverse la valeur : il transforme VRAI en FAUX et FAUX en VRAI.

**Table de vérité du NON :**

| A     | NON A |
|-------|-------|
| FAUX  | VRAI  |
| VRAI  | FAUX  |

**Exemple :**
- "Il ne pleut pas" = NON "Il pleut"
- Si "Il pleut" est VRAI, alors "Il ne pleut pas" est FAUX
- Si "Il pleut" est FAUX, alors "Il ne pleut pas" est VRAI

**En Python :**
```python
a = True
resultat = not a  # Résultat : False
```

## L'opérateur OU EXCLUSIF (XOR)

Le **OU EXCLUSIF** renvoie VRAI si **une seule** des deux conditions est vraie (mais pas les deux en même temps).

**Table de vérité du OU EXCLUSIF :**

| A     | B     | A XOR B |
|-------|-------|---------|
| FAUX  | FAUX  | FAUX    |
| FAUX  | VRAI  | VRAI    |
| VRAI  | FAUX  | VRAI    |
| VRAI  | VRAI  | FAUX    |

**Exemple :**

- "Je prends le bus XOR je prends le vélo" → Je prends l'un OU l'autre, mais pas les deux
- Si je prends le bus et le vélo : FAUX (ce n'est pas logique)
- Si je prends seulement l'un des deux : VRAI

**En Python :**
```python
a = True
b = False
resultat = a ^ b  # Résultat : True (opérateur ^ pour XOR)
```

## Exercices pratiques

### Exercice 1 : Compléter les tables de vérité

Complétez les tables suivantes :

**1. (A ET B) OU (NON A)**

| A     | B     | A ET B | NON A | Résultat |
|-------|-------|--------|-------|----------|
| FAUX  | FAUX  |        |       |          |
| FAUX  | VRAI  |        |       |          |
| VRAI  | FAUX  |        |       |          |
| VRAI  | VRAI  |        |       |          |

### Exercice 2 : Questions de compréhension

1. J'ai 15 ans (VRAI) ET j'ai mon permis de conduire (FAUX). Puis-je conduire ? Réponse : ___________

2. Il fait beau (VRAI) OU il pleut (FAUX). Je sors ? Réponse : ___________

3. Je n'ai PAS faim (si j'ai faim = VRAI). Vais-je manger ? Réponse : ___________

## Applications concrètes

### Dans un moteur de recherche

Lorsque vous recherchez "chat ET vidéo", le moteur cherche des pages contenant les deux mots.
Lorsque vous recherchez "chat OU chien", le moteur cherche des pages contenant au moins un des deux mots.

### Dans un jeu vidéo

```python
# Le personnage peut sauter si :
# - Il est sur le sol ET il appuie sur espace
sur_le_sol = True
touche_espace = True

peut_sauter = sur_le_sol and touche_espace
```

### Dans un système d'alarme

```python
# L'alarme se déclenche si :
# - Une porte est ouverte OU une fenêtre est ouverte
# ET l'alarme est activée

porte_ouverte = False
fenetre_ouverte = True
alarme_activee = True

alarme_sonne = (porte_ouverte or fenetre_ouverte) and alarme_activee
# Résultat : True (l'alarme sonne)
```

### Combinaisons complexes

On peut combiner plusieurs opérateurs :

```python
age = 14
a_carte = True
accompagne = False

# Peut entrer au cinéma si :
# - (a plus de 12 ans ET a sa carte) OU (est accompagné)
peut_entrer = (age > 12 and a_carte) or accompagne
print(peut_entrer)  # True
```
