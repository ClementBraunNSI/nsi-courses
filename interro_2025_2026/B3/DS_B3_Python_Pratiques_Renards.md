# Devoir Surveillé – Python pratique (B3)

## Contexte: Centre de sauvegarde des renards « FoxShelter »

**Durée totale : 2 heures**  
**Contraintes :** sans listes ni tuples. Utiliser variables, `input()`, conversions, conditions, fonctions, boucles et chaînes.

La justification, la rigueur, la rédaction et le soin du code entrent dans la notation sur 2 points. Un manquement de ces 4 critères entraîne une perte de 2 points.

---

## Rappels autorisés

- `print(...)`, `input(...)`, `int(...)`, `float(...)`, `str(...)`  
- Conditions `if`, `elif`, `else` et opérateurs `>`, `<`, `>=`, `<=`, `==`, `!=`, `and`, `or`, `not`  
- Fonctions `def`, paramètres, `return`  
- Boucles `for` avec `range(...)`, boucles `while`  
- Méthodes de chaînes (`lower`, `upper`, `isdigit`, `isalpha`, `replace`)

---

## Exercice 1 — Fiche d’accueil (2 points)

Écrire un programme qui:

1. Demande le **nom** du renard et son **âge** (entier) en années.  
2. Affiche:  
   `Renard NOM — Âge: X an(s)`  
3. Affiche la **catégorie d’âge**: 0–1: « Jeune », 2–6: « Adulte », 7+: « Senior ».

---

## Exercice 2 — Ration quotidienne (3 points)

Écrire une fonction `ration_journaliere(age, poids)` qui **retourne** en grammes la ration recommandée selon:

- S'il a moins d'un an compris: `poids * 6`  
- S'il a entre 2 et 6 ans compris': `poids * 5`  
- S'il a plus de 7 ans compris: `poids * 4`  

Tester la fonction en demandant un age et un poids à l'utilisateur. Afficher la ration recommandée.

---

## Exercice 3 — Identifiant de suivi (3 points)

Écrire une fonction `identifiant(nom, annee)` qui retourne une chaîne normalisée:

- Forme: `RX-ANNEE-nom`, avec `NOM` en majuscules sans espaces ni accents.  
- Remplacer les espaces par `-` et retirer les caractères non alphabétiques.

Afficher l’identifiant pour un renard saisi par l’utilisateur.

---

## Exercice 4 — Réhabilitation (3 points)

Le renard suit un programme avec un **score bien‑être** initial `s` sur 0–100. Chaque jour, le score augmente de `+3`. Écrire une fonction `jours_jusqua_palier(s, palier)` qui calcule le **nombre de jours** nécessaires pour atteindre `palier` en utilisant une boucle `while`. Afficher le résultat pour une saisie utilisateur.

---

## Exercice 5 — Analyse du nom (2 points)

Écrire une fonction `compter_voyelles(nom)` qui retourne le **nombre de voyelles** dans `nom`. Afficher:  
`NOM contient N voyelle(s)`.

---

## Exercice 6 — Planning d’alimentation (3 points)

Écrire une fonction `planning_ration(age, poids, jours)` qui retourne **une chaîne** contenant, pour `jours` de 1 à `jours`:  
`Jour i : NN g`  
La ration de base est celle de l’exercice 2. Utiliser une boucle `for` et construire la chaîne sans liste.

---

## Exercice 7 — Suivi de poids (2 points)

À chaque visite, le poids diminue de 10% jusqu’à passer sous un **seuil** `t`. Écrire une fonction `nb_visites(poids_initial, t)` qui retourne le **nombre de visites** nécessaires. Utiliser une boucle `while` et des flottants. Afficher le résultat pour une saisie utilisateur.

---
