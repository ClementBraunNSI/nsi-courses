# Les Arbres

## Introduction

Un **arbre** est une structure de données hiérarchique composée de nœuds reliés par des arêtes, sans cycle. C'est un cas particulier de graphe connexe et acyclique.

### Vocabulaire

- **Nœud** (ou sommet) : élément de l'arbre
- **Racine** : nœud au sommet de l'arbre (pas de parent)
- **Feuille** : nœud sans enfants
- **Parent** : nœud directement au-dessus
- **Enfant** : nœud directement en-dessous
- **Frères** : nœuds ayant le même parent
- **Ancêtre** : nœud sur le chemin vers la racine
- **Descendant** : nœud accessible en descendant
- **Sous-arbre** : arbre formé par un nœud et ses descendants

```
       A (racine)
      / \
     B   C
    /   / \
   D   E   F (feuilles)
```

### Propriétés importantes

- **Hauteur** : longueur du plus long chemin de la racine à une feuille
- **Profondeur** d'un nœud : distance de la racine à ce nœud
- **Degré** d'un nœud : nombre d'enfants
- **Taille** : nombre total de nœuds

## Arbres binaires

Un **arbre binaire** est un arbre où chaque nœud a **au maximum 2 enfants** : un enfant gauche et un enfant droit.

### Implémentation en Python

```python
class NoeudBinaire:
    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite
    
    def est_feuille(self):
        return self.gauche is None and self.droite is None
    
    def __str__(self):
        return str(self.valeur)

class ArbreBinaire:
    def __init__(self, racine=None):
        self.racine = racine
    
    def est_vide(self):
        return self.racine is None
    
    def hauteur(self, noeud=None):
        """Calcule la hauteur de l'arbre"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return -1
        
        if noeud.est_feuille():
            return 0
        
        hauteur_gauche = self.hauteur(noeud.gauche) if noeud.gauche else -1
        hauteur_droite = self.hauteur(noeud.droite) if noeud.droite else -1
        
        return 1 + max(hauteur_gauche, hauteur_droite)
    
    def taille(self, noeud=None):
        """Calcule le nombre de nœuds"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return 0
        
        return 1 + self.taille(noeud.gauche) + self.taille(noeud.droite)
    
    def rechercher(self, valeur, noeud=None):
        """Recherche une valeur dans l'arbre"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return False
        
        if noeud.valeur == valeur:
            return True
        
        return (self.rechercher(valeur, noeud.gauche) or 
                self.rechercher(valeur, noeud.droite))
```

### Exemple de création

```python
# Création manuelle d'un arbre
#       1
#      / \
#     2   3
#    /   / \
#   4   5   6

racine = NoeudBinaire(1)
racine.gauche = NoeudBinaire(2)
racine.droite = NoeudBinaire(3)
racine.gauche.gauche = NoeudBinaire(4)
racine.droite.gauche = NoeudBinaire(5)
racine.droite.droite = NoeudBinaire(6)

arbre = ArbreBinaire(racine)
print(f"Hauteur: {arbre.hauteur()}")  # 2
print(f"Taille: {arbre.taille()}")    # 6
```

## Parcours d'arbres

Il existe plusieurs façons de parcourir un arbre binaire :

### 1. Parcours en profondeur (DFS)

#### Parcours préfixe (préordre)
Racine → Gauche → Droite

```python
def parcours_prefixe(self, noeud=None, resultat=None):
    """Parcours préfixe : racine, gauche, droite"""
    if resultat is None:
        resultat = []
    if noeud is None:
        noeud = self.racine
    
    if noeud is not None:
        resultat.append(noeud.valeur)  # Visiter la racine
        self.parcours_prefixe(noeud.gauche, resultat)   # Sous-arbre gauche
        self.parcours_prefixe(noeud.droite, resultat)   # Sous-arbre droit
    
    return resultat
```

#### Parcours infixe (en ordre)
Gauche → Racine → Droite

```python
def parcours_infixe(self, noeud=None, resultat=None):
    """Parcours infixe : gauche, racine, droite"""
    if resultat is None:
        resultat = []
    if noeud is None:
        noeud = self.racine
    
    if noeud is not None:
        self.parcours_infixe(noeud.gauche, resultat)    # Sous-arbre gauche
        resultat.append(noeud.valeur)   # Visiter la racine
        self.parcours_infixe(noeud.droite, resultat)    # Sous-arbre droit
    
    return resultat
```

#### Parcours postfixe (postordre)
Gauche → Droite → Racine

```python
def parcours_postfixe(self, noeud=None, resultat=None):
    """Parcours postfixe : gauche, droite, racine"""
    if resultat is None:
        resultat = []
    if noeud is None:
        noeud = self.racine
    
    if noeud is not None:
        self.parcours_postfixe(noeud.gauche, resultat)  # Sous-arbre gauche
        self.parcours_postfixe(noeud.droite, resultat)  # Sous-arbre droit
        resultat.append(noeud.valeur)  # Visiter la racine
    
    return resultat
```

### 2. Parcours en largeur (BFS)

Parcourt niveau par niveau.

```python
from collections import deque

def parcours_largeur(self):
    """Parcours en largeur (niveau par niveau)"""
    if self.racine is None:
        return []
    
    resultat = []
    file = deque([self.racine])
    
    while file:
        noeud = file.popleft()
        resultat.append(noeud.valeur)
        
        if noeud.gauche:
            file.append(noeud.gauche)
        if noeud.droite:
            file.append(noeud.droite)
    
    return resultat
```

### Exemple de parcours

```python
# Pour l'arbre :
#       1
#      / \
#     2   3
#    /   / \
#   4   5   6

print("Préfixe:", arbre.parcours_prefixe())   # [1, 2, 4, 3, 5, 6]
print("Infixe:", arbre.parcours_infixe())     # [4, 2, 1, 5, 3, 6]
print("Postfixe:", arbre.parcours_postfixe()) # [4, 2, 5, 6, 3, 1]
print("Largeur:", arbre.parcours_largeur())   # [1, 2, 3, 4, 5, 6]
```

## Arbres binaires de recherche (ABR)

Un **ABR** est un arbre binaire où :
- Tous les nœuds du sous-arbre gauche < racine
- Tous les nœuds du sous-arbre droit > racine
- Cette propriété s'applique récursivement

### Implémentation

```python
class ABR(ArbreBinaire):
    def inserer(self, valeur):
        """Insère une valeur dans l'ABR"""
        self.racine = self._inserer_recursif(self.racine, valeur)
    
    def _inserer_recursif(self, noeud, valeur):
        # Cas de base : position trouvée
        if noeud is None:
            return NoeudBinaire(valeur)
        
        # Insertion récursive
        if valeur < noeud.valeur:
            noeud.gauche = self._inserer_recursif(noeud.gauche, valeur)
        elif valeur > noeud.valeur:
            noeud.droite = self._inserer_recursif(noeud.droite, valeur)
        # Si valeur == noeud.valeur, on ne fait rien (pas de doublons)
        
        return noeud
    
    def rechercher(self, valeur):
        """Recherche efficace dans un ABR"""
        return self._rechercher_recursif(self.racine, valeur)
    
    def _rechercher_recursif(self, noeud, valeur):
        if noeud is None:
            return False
        
        if valeur == noeud.valeur:
            return True
        elif valeur < noeud.valeur:
            return self._rechercher_recursif(noeud.gauche, valeur)
        else:
            return self._rechercher_recursif(noeud.droite, valeur)
    
    def minimum(self, noeud=None):
        """Trouve la valeur minimale"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return None
        
        while noeud.gauche is not None:
            noeud = noeud.gauche
        
        return noeud.valeur
    
    def maximum(self, noeud=None):
        """Trouve la valeur maximale"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return None
        
        while noeud.droite is not None:
            noeud = noeud.droite
        
        return noeud.valeur
    
    def supprimer(self, valeur):
        """Supprime une valeur de l'ABR"""
        self.racine = self._supprimer_recursif(self.racine, valeur)
    
    def _supprimer_recursif(self, noeud, valeur):
        if noeud is None:
            return noeud
        
        # Recherche du nœud à supprimer
        if valeur < noeud.valeur:
            noeud.gauche = self._supprimer_recursif(noeud.gauche, valeur)
        elif valeur > noeud.valeur:
            noeud.droite = self._supprimer_recursif(noeud.droite, valeur)
        else:
            # Nœud trouvé, 3 cas :
            
            # Cas 1 : nœud feuille ou avec un seul enfant
            if noeud.gauche is None:
                return noeud.droite
            elif noeud.droite is None:
                return noeud.gauche
            
            # Cas 2 : nœud avec deux enfants
            # Remplacer par le successeur (minimum du sous-arbre droit)
            successeur = self._trouver_minimum(noeud.droite)
            noeud.valeur = successeur.valeur
            noeud.droite = self._supprimer_recursif(noeud.droite, successeur.valeur)
        
        return noeud
    
    def _trouver_minimum(self, noeud):
        while noeud.gauche is not None:
            noeud = noeud.gauche
        return noeud
```

### Exemple d'utilisation

```python
# Création d'un ABR
abr = ABR()
valeurs = [50, 30, 70, 20, 40, 60, 80]

for val in valeurs:
    abr.inserer(val)

# L'arbre ressemble à :
#       50
#      /  \
#    30    70
#   / \   / \
#  20 40 60 80

print("Parcours infixe (trié):", abr.parcours_infixe())  # [20, 30, 40, 50, 60, 70, 80]
print("Recherche 40:", abr.rechercher(40))  # True
print("Minimum:", abr.minimum())  # 20
print("Maximum:", abr.maximum())  # 80

abr.supprimer(30)
print("Après suppression de 30:", abr.parcours_infixe())  # [20, 40, 50, 60, 70, 80]
```

## Arbres équilibrés

Un ABR peut devenir déséquilibré (ressembler à une liste), ce qui dégrade les performances.

### Arbre AVL (aperçu)

Un arbre AVL maintient l'équilibre en s'assurant que la différence de hauteur entre les sous-arbres gauche et droit ne dépasse jamais 1.

```python
class NoeudAVL(NoeudBinaire):
    def __init__(self, valeur):
        super().__init__(valeur)
        self.hauteur = 1  # Hauteur du nœud
    
    def facteur_equilibre(self):
        """Calcule le facteur d'équilibre"""
        hauteur_gauche = self.gauche.hauteur if self.gauche else 0
        hauteur_droite = self.droite.hauteur if self.droite else 0
        return hauteur_gauche - hauteur_droite
    
    def mettre_a_jour_hauteur(self):
        """Met à jour la hauteur du nœud"""
        hauteur_gauche = self.gauche.hauteur if self.gauche else 0
        hauteur_droite = self.droite.hauteur if self.droite else 0
        self.hauteur = 1 + max(hauteur_gauche, hauteur_droite)
```

## Applications des arbres

### 1. Système de fichiers

```python
class Fichier:
    def __init__(self, nom, taille=0):
        self.nom = nom
        self.taille = taille
        self.enfants = []  # Pour les dossiers
        self.est_dossier = False
    
    def ajouter_enfant(self, enfant):
        if self.est_dossier:
            self.enfants.append(enfant)
    
    def taille_totale(self):
        if not self.est_dossier:
            return self.taille
        
        return sum(enfant.taille_totale() for enfant in self.enfants)
    
    def afficher(self, niveau=0):
        indent = "  " * niveau
        print(f"{indent}{self.nom} ({'dossier' if self.est_dossier else f'{self.taille} octets'})")
        
        for enfant in self.enfants:
            enfant.afficher(niveau + 1)
```

### 2. Arbre d'expression

```python
class ArbreExpression:
    def __init__(self, expression_postfixe):
        self.racine = self._construire_arbre(expression_postfixe)
    
    def _construire_arbre(self, expression):
        pile = []
        operateurs = {'+', '-', '*', '/', '^'}
        
        for token in expression.split():
            if token in operateurs:
                # Opérateur : créer un nœud avec deux enfants
                droite = pile.pop()
                gauche = pile.pop()
                noeud = NoeudBinaire(token, gauche, droite)
                pile.append(noeud)
            else:
                # Opérande : créer une feuille
                pile.append(NoeudBinaire(float(token)))
        
        return pile[0] if pile else None
    
    def evaluer(self, noeud=None):
        if noeud is None:
            noeud = self.racine
        
        if noeud.est_feuille():
            return noeud.valeur
        
        gauche = self.evaluer(noeud.gauche)
        droite = self.evaluer(noeud.droite)
        
        if noeud.valeur == '+':
            return gauche + droite
        elif noeud.valeur == '-':
            return gauche - droite
        elif noeud.valeur == '*':
            return gauche * droite
        elif noeud.valeur == '/':
            return gauche / droite
        elif noeud.valeur == '^':
            return gauche ** droite

# Exemple : (3 + 4) * 2 en postfixe : "3 4 + 2 *"
arbre_expr = ArbreExpression("3 4 + 2 *")
print(f"Résultat: {arbre_expr.evaluer()}")  # 14.0
```

## Complexités

### Arbre binaire général
- **Recherche** : O(n) dans le pire cas (arbre dégénéré)
- **Insertion** : O(n) dans le pire cas
- **Suppression** : O(n) dans le pire cas

### ABR équilibré
- **Recherche** : O(log n)
- **Insertion** : O(log n)
- **Suppression** : O(log n)
- **Parcours** : O(n)

### Espace
- **Mémoire** : O(n) pour n nœuds

## Conclusion

Les arbres sont des structures fondamentales en informatique :

**Avantages :**
- Structure hiérarchique naturelle
- Recherche efficace (ABR équilibrés)
- Parcours systématiques
- Nombreuses applications

**Points clés :**
- Arbre = graphe connexe acyclique
- Arbres binaires : au plus 2 enfants par nœud
- ABR : propriété d'ordre pour une recherche efficace
- Équilibrage nécessaire pour maintenir les performances
- Applications : systèmes de fichiers, expressions, bases de données

**Types de parcours :**
- **Profondeur** : préfixe, infixe, postfixe
- **Largeur** : niveau par niveau

Le choix du type d'arbre dépend des opérations les plus fréquentes et des contraintes de performance.