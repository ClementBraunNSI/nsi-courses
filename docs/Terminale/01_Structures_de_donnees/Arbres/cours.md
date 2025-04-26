# Arbres

## Introduction aux arbres

### Définitions

Un arbre est une structure de données hiérarchique composée de :
- Nœuds (contenant des données)
- Arêtes reliant les nœuds
- Un nœud racine
- Des nœuds parents et enfants

Terminologie :
- Racine : nœud sans parent
- Feuille : nœud sans enfant
- Hauteur : longueur du plus long chemin de la racine à une feuille
- Profondeur d'un nœud : longueur du chemin de la racine au nœud

## Implémentation en Python

### Arbre binaire

```python
class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

class ArbreBinaire:
    def __init__(self):
        self.racine = None
    
    def inserer(self, valeur):
        if not self.racine:
            self.racine = Noeud(valeur)
        else:
            self._inserer_recursif(self.racine, valeur)
    
    def _inserer_recursif(self, noeud, valeur):
        if valeur < noeud.valeur:
            if noeud.gauche is None:
                noeud.gauche = Noeud(valeur)
            else:
                self._inserer_recursif(noeud.gauche, valeur)
        else:
            if noeud.droit is None:
                noeud.droit = Noeud(valeur)
            else:
                self._inserer_recursif(noeud.droit, valeur)
```

## Parcours d'arbres

### Parcours en profondeur

```python
def parcours_prefixe(noeud):
    if noeud:
        print(noeud.valeur, end=' ')
        parcours_prefixe(noeud.gauche)
        parcours_prefixe(noeud.droit)

def parcours_infixe(noeud):
    if noeud:
        parcours_infixe(noeud.gauche)
        print(noeud.valeur, end=' ')
        parcours_infixe(noeud.droit)

def parcours_postfixe(noeud):
    if noeud:
        parcours_postfixe(noeud.gauche)
        parcours_postfixe(noeud.droit)
        print(noeud.valeur, end=' ')
```

### Parcours en largeur

```python
from collections import deque

def parcours_largeur(racine):
    if not racine:
        return
    
    file = deque([racine])
    while file:
        noeud = file.popleft()
        print(noeud.valeur, end=' ')
        
        if noeud.gauche:
            file.append(noeud.gauche)
        if noeud.droit:
            file.append(noeud.droit)
```

## Types d'arbres particuliers

### Arbre binaire de recherche (ABR)

Propriétés :
- Pour chaque nœud :
  - Valeurs du sous-arbre gauche < valeur du nœud
  - Valeurs du sous-arbre droit > valeur du nœud

```python
def rechercher(racine, valeur):
    if not racine or racine.valeur == valeur:
        return racine
    
    if valeur < racine.valeur:
        return rechercher(racine.gauche, valeur)
    return rechercher(racine.droit, valeur)
```

### Arbre AVL

ABR équilibré où pour chaque nœud :
- La différence de hauteur entre sous-arbres gauche et droit ≤ 1
- Nécessite des rotations pour maintenir l'équilibre

```python
class NoeudAVL(Noeud):
    def __init__(self, valeur):
        super().__init__(valeur)
        self.hauteur = 1

class ArbreAVL:
    def hauteur(self, noeud):
        if not noeud:
            return 0
        return noeud.hauteur
    
    def equilibre(self, noeud):
        if not noeud:
            return 0
        return self.hauteur(noeud.gauche) - self.hauteur(noeud.droit)
    
    def rotation_droite(self, y):
        x = y.gauche
        T2 = x.droit
        
        x.droit = y
        y.gauche = T2
        
        y.hauteur = max(self.hauteur(y.gauche),
                       self.hauteur(y.droit)) + 1
        x.hauteur = max(self.hauteur(x.gauche),
                       self.hauteur(x.droit)) + 1
        
        return x
```

## Exercices

### Exercice 1 : Manipulation d'arbres binaires
Implémentez les méthodes suivantes pour la classe ArbreBinaire :
- calculer_hauteur()
- compter_noeuds()
- est_feuille(noeud)
- afficher_niveau(k)

### Exercice 2 : Arbres binaires de recherche
Créez un programme qui :
- Construit un ABR à partir d'une liste de nombres
- Permet d'insérer/supprimer des valeurs
- Vérifie si c'est un ABR valide

### Exercice 3 : Expressions arithmétiques
Utilisez un arbre binaire pour :
- Représenter une expression arithmétique
- Évaluer l'expression
- Convertir entre notations infixe et postfixe

### Exercice 4 : Arbres AVL
Implémentez un arbre AVL complet avec :
- Insertions et suppressions avec rééquilibrage
- Visualisation de l'arbre
- Comparaison des performances avec un ABR simple

## Applications pratiques

- Structures de données hiérarchiques
- Systèmes de fichiers
- Bases de données indexées
- Compression de données (arbres de Huffman)
- Analyse syntaxique
