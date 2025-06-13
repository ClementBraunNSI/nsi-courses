# TP Récursivité - Exercices pratiques

## Objectifs

- Maîtriser les concepts de récursivité
- Implémenter des algorithmes récursifs classiques
- Analyser la complexité des solutions récursives
- Optimiser les algorithmes récursifs
- Résoudre des problèmes complexes par décomposition récursive

---

## Exercice 1 : Récursivité de base

### 1.1 Fonctions mathématiques

**Consigne :** Implémentez les fonctions suivantes de manière récursive.

```python
# À compléter
def puissance(base, exposant):
    """
    Calcule base^exposant de manière récursive
    Précondition: exposant >= 0
    """
    pass

def somme_entiers(n):
    """
    Calcule la somme des entiers de 1 à n
    Formule: 1 + 2 + ... + n
    """
    pass

def pgcd(a, b):
    """
    Calcule le PGCD de deux nombres (algorithme d'Euclide)
    """
    pass

def coefficient_binomial(n, k):
    """
    Calcule le coefficient binomial C(n,k) = n! / (k! * (n-k)!)
    Utilise la relation: C(n,k) = C(n-1,k-1) + C(n-1,k)
    """
    pass
```

**Tests :**
```python
# Tests à exécuter
print(f"2^10 = {puissance(2, 10)}")  # Attendu: 1024
print(f"Somme 1 à 10 = {somme_entiers(10)}")  # Attendu: 55
print(f"PGCD(48, 18) = {pgcd(48, 18)}")  # Attendu: 6
print(f"C(5,2) = {coefficient_binomial(5, 2)}")  # Attendu: 10
```

### 1.2 Manipulation de chaînes

**Consigne :** Implémentez ces fonctions récursives sur les chaînes.

```python
def inverser_chaine(chaine):
    """
    Inverse une chaîne de caractères
    """
    pass

def compter_voyelles(chaine):
    """
    Compte le nombre de voyelles dans une chaîne
    """
    pass

def est_palindrome_recursif(chaine):
    """
    Vérifie si une chaîne est un palindrome (ignore la casse)
    """
    pass

def remplacer_caractere_recursif(chaine, ancien, nouveau):
    """
    Remplace toutes les occurrences d'un caractère par un autre
    """
    pass
```

---

## Exercice 2 : Récursivité sur les listes

### 2.1 Opérations de base

```python
def maximum_liste_recursif(liste):
    """
    Trouve le maximum d'une liste non vide
    """
    pass

def filtrer_pairs(liste):
    """
    Retourne une nouvelle liste contenant seulement les nombres pairs
    """
    pass

def aplatir_liste(liste_imbriquee):
    """
    Aplatit une liste de listes
    Exemple: [[1, 2], [3, 4, 5], [6]] -> [1, 2, 3, 4, 5, 6]
    """
    pass

def inserer_trie(liste_triee, element):
    """
    Insère un élément dans une liste triée en maintenant l'ordre
    """
    pass
```

### 2.2 Tri récursif

```python
def tri_rapide(liste):
    """
    Implémente le tri rapide (quicksort)
    """
    pass

def tri_insertion_recursif(liste):
    """
    Implémente le tri par insertion de manière récursive
    """
    pass
```

---

## Exercice 3 : Arbres binaires

### 3.1 Structure d'arbre

```python
class Noeud:
    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite

class ArbreBinaire:
    def __init__(self, racine=None):
        self.racine = racine
    
    def inserer(self, valeur):
        """
        Insère une valeur dans l'arbre binaire de recherche
        """
        pass
    
    def rechercher(self, valeur):
        """
        Recherche une valeur dans l'arbre
        """
        pass
    
    def supprimer(self, valeur):
        """
        Supprime une valeur de l'arbre
        """
        pass
    
    def hauteur(self):
        """
        Calcule la hauteur de l'arbre
        """
        pass
    
    def est_equilibre(self):
        """
        Vérifie si l'arbre est équilibré
        """
        pass
    
    def parcours_largeur(self):
        """
        Parcours en largeur (BFS) - peut utiliser une file
        """
        pass
    
    def serialiser(self):
        """
        Sérialise l'arbre en chaîne de caractères
        """
        pass
    
    @classmethod
    def deserialiser(cls, chaine):
        """
        Reconstruit un arbre à partir de sa sérialisation
        """
        pass
```

### 3.2 Tests pour l'arbre

```python
# Créer et tester l'arbre
arbre = ArbreBinaire()
valeurs = [50, 30, 70, 20, 40, 60, 80]

for valeur in valeurs:
    arbre.inserer(valeur)

print(f"Hauteur: {arbre.hauteur()}")
print(f"Recherche 40: {arbre.rechercher(40)}")
print(f"Recherche 90: {arbre.rechercher(90)}")
print(f"Est équilibré: {arbre.est_equilibre()}")
print(f"Parcours largeur: {arbre.parcours_largeur()}")
```

---

## Exercice 4 : Problèmes de backtracking

### 4.1 Génération de combinaisons

```python
def generer_combinaisons(elements, k):
    """
    Génère toutes les combinaisons de k éléments
    """
    pass

def generer_sous_ensembles(ensemble):
    """
    Génère tous les sous-ensembles d'un ensemble
    """
    pass

def partitions_entier(n, max_val=None):
    """
    Génère toutes les partitions d'un entier n
    Exemple: partitions(4) = [[4], [3,1], [2,2], [2,1,1], [1,1,1,1]]
    """
    pass
```

### 4.2 Sudoku

```python
def resoudre_sudoku(grille):
    """
    Résout une grille de Sudoku 9x9
    0 représente une case vide
    """
    def est_valide(grille, ligne, colonne, nombre):
        # Vérifier la ligne
        pass
        
        # Vérifier la colonne
        pass
        
        # Vérifier le carré 3x3
        pass
    
    def resoudre_recursif(grille):
        pass
    
    return resoudre_recursif(grille)

# Grille de test
grille_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
```

---

## Exercice 5 : Fractales et géométrie

### 5.1 Triangle de Sierpinski

```python
import turtle

def triangle_sierpinski(t, ordre, taille):
    """
    Dessine le triangle de Sierpinski avec turtle
    t: objet turtle
    ordre: niveau de récursion
    taille: taille du triangle
    """
    pass

def dessiner_triangle(t, taille):
    """
    Dessine un triangle équilatéral
    """
    pass

# Code pour tester
# screen = turtle.Screen()
# t = turtle.Turtle()
# triangle_sierpinski(t, 4, 200)
# screen.exitonclick()
```

### 5.2 Courbe de Koch

```python
def courbe_koch(t, ordre, taille):
    """
    Dessine la courbe de Koch
    """
    pass

def flocon_koch(t, ordre, taille):
    """
    Dessine le flocon de Koch (3 courbes de Koch)
    """
    pass
```

---

## Exercice 6 : Optimisation et mémoïsation

### 6.1 Problème du sac à dos

```python
def sac_a_dos_recursif(objets, capacite):
    """
    Résout le problème du sac à dos 0-1
    objets: liste de tuples (poids, valeur)
    capacite: capacité maximale du sac
    """
    pass

def sac_a_dos_memo(objets, capacite, memo=None):
    """
    Version avec mémoïsation
    """
    pass
```

### 6.2 Plus longue sous-séquence commune

```python
def lcs_recursif(seq1, seq2):
    """
    Trouve la longueur de la plus longue sous-séquence commune
    """
    pass

def lcs_memo(seq1, seq2, memo=None):
    """
    Version avec mémoïsation
    """
    pass

def lcs_reconstruction(seq1, seq2):
    """
    Reconstruit la sous-séquence commune
    """
    pass
```

---

## Exercice 7 : Analyse de performance

### 7.1 Comparaison d'algorithmes

```python
import time
import sys

def mesurer_performance():
    """
    Compare les performances de différentes implémentations
    """
    # Fibonacci
    def fibonacci_naif(n):
        pass
    
    def fibonacci_memo(n, memo={}):
        pass
    
    def fibonacci_iteratif(n):
        pass
    
    # Tests de performance
    for n in [10, 20, 30, 35]:
        print(f"\nFibonacci({n}):")
        
        # Mesurer chaque version
        pass

def analyser_pile_recursion():
    """
    Analyse l'utilisation de la pile de récursion
    """
    def profondeur_max_recursion():
        try:
            return 1 + profondeur_max_recursion()
        except RecursionError:
            return 0
    
    print(f"Limite de récursion système: {sys.getrecursionlimit()}")
    # Tester différentes fonctions récursives
```

---

## Exercice 8 : Projet - Interpréteur d'expressions

### 8.1 Analyseur syntaxique récursif

```python
class Noeud:
    pass

class Nombre(Noeud):
    def __init__(self, valeur):
        self.valeur = valeur

class Operation(Noeud):
    def __init__(self, operateur, gauche, droite):
        self.operateur = operateur
        self.gauche = gauche
        self.droite = droite

class AnalyseurExpression:
    """
    Analyseur récursif descendant pour expressions arithmétiques
    Grammaire:
    expression := terme (('+' | '-') terme)*
    terme := facteur (('*' | '/') facteur)*
    facteur := nombre | '(' expression ')'
    """
    
    def __init__(self, expression):
        self.expression = expression.replace(' ', '')
        self.position = 0
    
    def analyser(self):
        """
        Analyse l'expression et retourne l'arbre syntaxique
        """
        pass
    
    def expression(self):
        pass
    
    def terme(self):
        pass
    
    def facteur(self):
        pass
    
    def evaluer(self, noeud):
        """
        Évalue récursivement l'arbre syntaxique
        """
        pass

# Tests
expression = "3 + 4 * (2 - 1)"
analyseur = AnalyseurExpression(expression)
arbre = analyseur.analyser()
resultat = analyseur.evaluer(arbre)
print(f"{expression} = {resultat}")
```

---

## Critères d'évaluation

### Fonctionnalité (40%)
- [ ] Toutes les fonctions sont implémentées
- [ ] Les cas de base sont correctement définis
- [ ] Les appels récursifs sont appropriés
- [ ] Les résultats sont corrects

### Qualité du code (30%)
- [ ] Code lisible et bien structuré
- [ ] Commentaires appropriés
- [ ] Gestion des cas d'erreur
- [ ] Respect des conventions Python

### Optimisation (20%)
- [ ] Utilisation de la mémoïsation quand approprié
- [ ] Analyse de la complexité
- [ ] Comparaison avec les versions itératives
- [ ] Optimisations pertinentes

### Tests et validation (10%)
- [ ] Tests complets des fonctions
- [ ] Cas limites testés
- [ ] Validation des résultats
- [ ] Documentation des tests

---

## Ressources

### Concepts clés
- Cas de base et cas récursif
- Pile d'appels et gestion mémoire
- Complexité temporelle et spatiale
- Mémoïsation et programmation dynamique
- Backtracking et exploration exhaustive

### Algorithmes à maîtriser
- Tri fusion et tri rapide
- Parcours d'arbres
- Recherche avec backtracking
- Diviser pour régner
- Analyse syntaxique récursive

### Outils de débogage
- Affichage des appels récursifs
- Limitation de la profondeur
- Mesure de performance
- Visualisation des structures

---

## Extensions possibles

1. **Parallélisation** : Adapter certains algorithmes pour le calcul parallèle
2. **Récursivité mutuelle** : Implémenter des automates à états
3. **Optimisation avancée** : Récursivité terminale et trampolines
4. **Applications graphiques** : Fractales interactives
5. **Structures avancées** : Arbres B, arbres rouge-noir

---

## Conseils

1. **Commencez simple** : Maîtrisez les cas de base avant les cas complexes
2. **Visualisez** : Dessinez les arbres d'appels pour comprendre
3. **Testez progressivement** : Validez chaque fonction avant de passer à la suivante
4. **Optimisez intelligemment** : Identifiez les goulots d'étranglement
5. **Documentez** : Expliquez la logique récursive dans vos commentaires

Bonne chance dans votre exploration de la récursivité !