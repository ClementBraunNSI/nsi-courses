# Roadmaps C — Formateur et Cours particuliers

## Roadmap — Se reformer en C (formateur)

### Semaine 1 — Remise à niveau syntaxe et outils
- Installer toolchain: `gcc`, `clang`, `make`; éditeur + extensions C
- Revoir C moderne: C99/C11/C17 (types, en‑têtes standard, `stdint.h`)
- Rappels: compilation/édition de liens; options: `-Wall -Wextra -Wpedantic -std=c17`
- IO: `stdio.h`; formatages (`%d`, `%.2f`, `%-10s`), `scanf` sécurisé
- Débogage: `gdb` basique (breakpoints, step, print), `printf`‑debug

### Semaine 2 — Mémoire, pointeurs, tableaux, chaînes
- Modèle mémoire C: pile vs tas; durée de vie, portée
- Pointeurs: déclaration, adressage `&`, déréférencement `*`, arithmétique contrôlée
- Tableaux: statiques, passage à fonction (`int a[]`, `size_t n`)
- Chaînes C: terminées par `\0`, `strlen`, `strcpy`, `strncpy`, `strcmp`
- Outils qualité: AddressSanitizer (`-fsanitize=address`), UBSan (`-fsanitize=undefined`), Valgrind

### Semaine 3 — Struct, modules, gestion de projet
- `struct` et `typedef`; encapsulation légère d’API
- Découpage: `.h` (interface) / `.c` (implémentation); inclusion gardes `#ifndef/#define` 
- Makefile minimal: cibles `build`, `run`, `clean`; dépendances
- Tests rapides: auto‑tests avec `assert.h` et scripts
- Lecture/écriture fichiers: `fopen/fclose`, `fprintf/fscanf`, formats robustes

### Semaine 4 — Algorithmique appliquée (vers polynômes)
- Horner pour évaluation, dérivée, addition/multiplication de polynômes
- Complexité, bornes, cas limites; robustesse entrées
- Style: naming, const‑correctness, documentation succincte en `.h`

### Références
- K&R « The C Programming Language », ISO C standard (extraits)
- « Modern C » (Jens Gustedt), cppreference section C

---

## Roadmap — Cours particuliers (étudiante)

### Séance 1 (2h) — Bases essentielles
- Affectations et types (`int`, `double`, `char`); `printf`/`scanf`
- Conditions (`if/else`, `switch`) et opérateurs logiques
- Boucles (`for`, `while`, `do...while`); exercices guidés
- Mini‑TP: somme `1..n`, factorielle, Fibonacci itératif
- Devoir: 4 exercices (affectations, max de 3, compteur de chiffres, mentions)

### Séance 2 (2h) — Fonctions et structuration
- Fonctions: prototypes, retour, paramètres, portée
- Découpage en fichiers: `main.c` + `utils.c` + `utils.h` (aperçu)
- Exercices: `est_pair`, `max2`, `puissance`, `factorielle`
- Mini‑projet: moyenne de `n` valeurs via fonction; tests
- Pré‑lecture: introduction aux tableaux et pointeurs (sans implémentation)

### Séances suivantes (progresser vers polynômes)
- Tableaux: itérations, passage à fonctions (`size_t`), cas limites
- Pointeurs: adresse/déréférencement; `const` correctness
- Allocation dynamique: `malloc/free`, vérification, gestion d’erreurs
- `struct` polynôme: degré + tableau de coefficients; API de base
- Algorithmes: Horner, dérivée, addition, multiplication; tests unitaires
- Fichiers: sauvegarde/chargement de polynômes

### Évaluation continue
- Petits quiz (10 min) sur notions vues
- Revues de code: lisibilité, robustesse, absence d’UB, messages d’erreur

### Matériel & pratiques
- Compiler avec: `-Wall -Wextra -Wpedantic -std=c17`
- Utiliser `assert` pour tests simples; activer `-fsanitize=address,undefined` en développement

---

## Jalons vers le projet « polynômes »
- J1: lecture de `n` + tableau de `double`, affichage formaté
- J2: évaluation par Horner, dérivée, addition; jeux de tests
- J3: persistances (fichiers), cli minimal (`argv/argc`), gestion d’erreurs
- Soutenance: démonstration, validation sur cas bord (degré 0, coefficients nuls)
