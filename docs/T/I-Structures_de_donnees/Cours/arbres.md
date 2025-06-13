# Arbres

## Introduction

Les **arbres** sont des structures de données hiérarchiques composées de **nœuds** reliés par des **arêtes**. Ils sont fondamentaux en informatique pour organiser et rechercher efficacement des données.

**Analogie :** Un arbre généalogique où chaque personne (nœud) a des parents et des enfants.

## I. Concepts fondamentaux

### 1. Terminologie

- **Nœud** : élément de l'arbre contenant une valeur
- **Racine** : nœud au sommet de l'arbre (sans parent)
- **Feuille** : nœud sans enfants
- **Nœud interne** : nœud avec au moins un enfant
- **Parent** : nœud ayant des enfants
- **Enfant** : nœud ayant un parent
- **Frères/Sœurs** : nœuds ayant le même parent
- **Ancêtre** : nœud sur le chemin de la racine à un nœud donné
- **Descendant** : nœud accessible depuis un nœud donné

### 2. Propriétés importantes

- **Hauteur** : longueur du plus long chemin de la racine à une feuille
- **Profondeur** d'un nœud : longueur du chemin de la racine à ce nœud
- **Degré** d'un nœud : nombre d'enfants de ce nœud
- **Taille** : nombre total de nœuds dans l'arbre

```
        A (racine, profondeur 0)
       / \
      B   C (profondeur 1)
     /   / \
    D   E   F (profondeur 2, feuilles)

Hauteur de l'arbre : 2
Degré de A : 2, degré de B : 1, degré de D : 0
```

## II. Implémentation des arbres

### 1. Représentation par nœuds et pointeurs

```python
class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfants = []  # Liste des enfants
        self.parent = None
    
    def ajouter_enfant(self, enfant):
        """Ajoute un enfant à ce nœud"""
        self.enfants.append(enfant)
        enfant.parent = self
    
    def supprimer_enfant(self, enfant):
        """Supprime un enfant de ce nœud"""
        if enfant in self.enfants:
            self.enfants.remove(enfant)
            enfant.parent = None
    
    def est_feuille(self):
        """Vérifie si le nœud est une feuille"""
        return len(self.enfants) == 0
    
    def est_racine(self):
        """Vérifie si le nœud est la racine"""
        return self.parent is None
    
    def profondeur(self):
        """Calcule la profondeur du nœud"""
        if self.est_racine():
            return 0
        return 1 + self.parent.profondeur()
    
    def __str__(self):
        return str(self.valeur)

class Arbre:
    def __init__(self, racine=None):
        self.racine = racine
    
    def est_vide(self):
        """Vérifie si l'arbre est vide"""
        return self.racine is None
    
    def taille(self):
        """Calcule le nombre de nœuds dans l'arbre"""
        if self.est_vide():
            return 0
        return self._taille_recursive(self.racine)
    
    def _taille_recursive(self, noeud):
        """Calcule récursivement la taille"""
        if noeud is None:
            return 0
        taille = 1  # Le nœud actuel
        for enfant in noeud.enfants:
            taille += self._taille_recursive(enfant)
        return taille
    
    def hauteur(self):
        """Calcule la hauteur de l'arbre"""
        if self.est_vide():
            return -1
        return self._hauteur_recursive(self.racine)
    
    def _hauteur_recursive(self, noeud):
        """Calcule récursivement la hauteur"""
        if noeud.est_feuille():
            return 0
        hauteurs_enfants = [self._hauteur_recursive(enfant) 
                           for enfant in noeud.enfants]
        return 1 + max(hauteurs_enfants)

# Exemple de création d'un arbre
racine = Noeud("A")
arbre = Arbre(racine)

# Ajout de nœuds
noeud_b = Noeud("B")
noeud_c = Noeud("C")
racine.ajouter_enfant(noeud_b)
racine.ajouter_enfant(noeud_c)

noeud_d = Noeud("D")
noeud_e = Noeud("E")
noeud_f = Noeud("F")
noeud_b.ajouter_enfant(noeud_d)
noeud_c.ajouter_enfant(noeud_e)
noeud_c.ajouter_enfant(noeud_f)

print(f"Taille de l'arbre : {arbre.taille()}")    # 6
print(f"Hauteur de l'arbre : {arbre.hauteur()}")  # 2
```

### 2. Représentation par listes

```python
class ArbreListe:
    def __init__(self, valeur_racine):
        self.arbre = [valeur_racine]  # [racine, enfant1, enfant2, ...]
    
    def ajouter_enfant(self, valeur_parent, valeur_enfant):
        """Ajoute un enfant à un parent donné"""
        # Trouve l'index du parent
        try:
            index_parent = self.arbre.index(valeur_parent)
        except ValueError:
            print(f"Parent {valeur_parent} non trouvé")
            return
        
        # Ajoute l'enfant après le parent
        self.arbre.insert(index_parent + 1, valeur_enfant)
    
    def afficher(self):
        """Affiche l'arbre sous forme de liste"""
        return self.arbre

# Exemple
arbre_liste = ArbreListe("A")
arbre_liste.ajouter_enfant("A", "B")
arbre_liste.ajouter_enfant("A", "C")
print(arbre_liste.afficher())  # ['A', 'B', 'C']
```

## III. Parcours d'arbres

### 1. Parcours en profondeur (DFS)

#### Parcours préfixe (pré-ordre)
Visite : nœud → enfants gauche à droite

```python
def parcours_prefixe(noeud, visite=[]):
    """Parcours préfixe récursif"""
    if noeud is not None:
        visite.append(noeud.valeur)  # Visite le nœud
        for enfant in noeud.enfants:  # Puis ses enfants
            parcours_prefixe(enfant, visite)
    return visite

def parcours_prefixe_iteratif(racine):
    """Parcours préfixe itératif avec une pile"""
    if racine is None:
        return []
    
    pile = [racine]
    visite = []
    
    while pile:
        noeud = pile.pop()
        visite.append(noeud.valeur)
        
        # Ajouter les enfants en ordre inverse pour maintenir l'ordre
        for enfant in reversed(noeud.enfants):
            pile.append(enfant)
    
    return visite
```

#### Parcours postfixe (post-ordre)
Visite : enfants gauche à droite → nœud

```python
def parcours_postfixe(noeud, visite=[]):
    """Parcours postfixe récursif"""
    if noeud is not None:
        for enfant in noeud.enfants:  # D'abord les enfants
            parcours_postfixe(enfant, visite)
        visite.append(noeud.valeur)  # Puis le nœud
    return visite
```

### 2. Parcours en largeur (BFS)

```python
from collections import deque

def parcours_largeur(racine):
    """Parcours en largeur avec une file"""
    if racine is None:
        return []
    
    file = deque([racine])
    visite = []
    
    while file:
        noeud = file.popleft()
        visite.append(noeud.valeur)
        
        # Ajouter tous les enfants à la file
        for enfant in noeud.enfants:
            file.append(enfant)
    
    return visite

def parcours_par_niveau(racine):
    """Parcours niveau par niveau"""
    if racine is None:
        return []
    
    niveaux = []
    niveau_actuel = [racine]
    
    while niveau_actuel:
        niveau_valeurs = []
        niveau_suivant = []
        
        for noeud in niveau_actuel:
            niveau_valeurs.append(noeud.valeur)
            niveau_suivant.extend(noeud.enfants)
        
        niveaux.append(niveau_valeurs)
        niveau_actuel = niveau_suivant
    
    return niveaux

# Exemple avec l'arbre précédent
print("Préfixe :", parcours_prefixe(racine, []))     # ['A', 'B', 'D', 'C', 'E', 'F']
print("Postfixe :", parcours_postfixe(racine, []))   # ['D', 'B', 'E', 'F', 'C', 'A']
print("Largeur :", parcours_largeur(racine))         # ['A', 'B', 'C', 'D', 'E', 'F']
print("Par niveau :", parcours_par_niveau(racine))   # [['A'], ['B', 'C'], ['D', 'E', 'F']]
```

## IV. Arbres binaires

### 1. Définition et propriétés

Un **arbre binaire** est un arbre où chaque nœud a au maximum **deux enfants** : un enfant gauche et un enfant droit.

```python
class NoeudBinaire:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None
    
    def est_feuille(self):
        """Vérifie si le nœud est une feuille"""
        return self.gauche is None and self.droit is None
    
    def __str__(self):
        return str(self.valeur)

class ArbreBinaire:
    def __init__(self, racine=None):
        self.racine = racine
    
    def est_vide(self):
        return self.racine is None
    
    def taille(self):
        """Calcule le nombre de nœuds"""
        return self._taille_recursive(self.racine)
    
    def _taille_recursive(self, noeud):
        if noeud is None:
            return 0
        return 1 + self._taille_recursive(noeud.gauche) + self._taille_recursive(noeud.droit)
    
    def hauteur(self):
        """Calcule la hauteur de l'arbre"""
        return self._hauteur_recursive(self.racine)
    
    def _hauteur_recursive(self, noeud):
        if noeud is None:
            return -1
        return 1 + max(self._hauteur_recursive(noeud.gauche),
                      self._hauteur_recursive(noeud.droit))
```

### 2. Parcours d'arbres binaires

```python
def parcours_infixe(noeud, visite=[]):
    """Parcours infixe : gauche → nœud → droit"""
    if noeud is not None:
        parcours_infixe(noeud.gauche, visite)
        visite.append(noeud.valeur)
        parcours_infixe(noeud.droit, visite)
    return visite

def parcours_prefixe_binaire(noeud, visite=[]):
    """Parcours préfixe : nœud → gauche → droit"""
    if noeud is not None:
        visite.append(noeud.valeur)
        parcours_prefixe_binaire(noeud.gauche, visite)
        parcours_prefixe_binaire(noeud.droit, visite)
    return visite

def parcours_postfixe_binaire(noeud, visite=[]):
    """Parcours postfixe : gauche → droit → nœud"""
    if noeud is not None:
        parcours_postfixe_binaire(noeud.gauche, visite)
        parcours_postfixe_binaire(noeud.droit, visite)
        visite.append(noeud.valeur)
    return visite

# Création d'un arbre binaire exemple
#       1
#      / \
#     2   3
#    / \
#   4   5

racine_bin = NoeudBinaire(1)
racine_bin.gauche = NoeudBinaire(2)
racine_bin.droit = NoeudBinaire(3)
racine_bin.gauche.gauche = NoeudBinaire(4)
racine_bin.gauche.droit = NoeudBinaire(5)

print("Infixe :", parcours_infixe(racine_bin, []))      # [4, 2, 5, 1, 3]
print("Préfixe :", parcours_prefixe_binaire(racine_bin, []))  # [1, 2, 4, 5, 3]
print("Postfixe :", parcours_postfixe_binaire(racine_bin, [])) # [4, 5, 2, 3, 1]
```

## V. Arbres binaires de recherche (ABR)

### 1. Définition et propriété

Un **arbre binaire de recherche** est un arbre binaire où :
- Toutes les valeurs du sous-arbre gauche < valeur du nœud
- Toutes les valeurs du sous-arbre droit > valeur du nœud
- Cette propriété est vraie pour tous les nœuds

```python
class ABR:
    def __init__(self):
        self.racine = None
    
    def inserer(self, valeur):
        """Insère une valeur dans l'ABR"""
        self.racine = self._inserer_recursive(self.racine, valeur)
    
    def _inserer_recursive(self, noeud, valeur):
        # Cas de base : position trouvée
        if noeud is None:
            return NoeudBinaire(valeur)
        
        # Insertion récursive
        if valeur < noeud.valeur:
            noeud.gauche = self._inserer_recursive(noeud.gauche, valeur)
        elif valeur > noeud.valeur:
            noeud.droit = self._inserer_recursive(noeud.droit, valeur)
        # Si valeur == noeud.valeur, on ne fait rien (pas de doublons)
        
        return noeud
    
    def rechercher(self, valeur):
        """Recherche une valeur dans l'ABR"""
        return self._rechercher_recursive(self.racine, valeur)
    
    def _rechercher_recursive(self, noeud, valeur):
        # Cas de base
        if noeud is None or noeud.valeur == valeur:
            return noeud
        
        # Recherche récursive
        if valeur < noeud.valeur:
            return self._rechercher_recursive(noeud.gauche, valeur)
        else:
            return self._rechercher_recursive(noeud.droit, valeur)
    
    def minimum(self, noeud=None):
        """Trouve la valeur minimale"""
        if noeud is None:
            noeud = self.racine
        
        while noeud.gauche is not None:
            noeud = noeud.gauche
        return noeud
    
    def maximum(self, noeud=None):
        """Trouve la valeur maximale"""
        if noeud is None:
            noeud = self.racine
        
        while noeud.droit is not None:
            noeud = noeud.droit
        return noeud
    
    def supprimer(self, valeur):
        """Supprime une valeur de l'ABR"""
        self.racine = self._supprimer_recursive(self.racine, valeur)
    
    def _supprimer_recursive(self, noeud, valeur):
        if noeud is None:
            return noeud
        
        # Trouver le nœud à supprimer
        if valeur < noeud.valeur:
            noeud.gauche = self._supprimer_recursive(noeud.gauche, valeur)
        elif valeur > noeud.valeur:
            noeud.droit = self._supprimer_recursive(noeud.droit, valeur)
        else:
            # Nœud trouvé, cas de suppression
            
            # Cas 1 : nœud sans enfant (feuille)
            if noeud.gauche is None and noeud.droit is None:
                return None
            
            # Cas 2 : nœud avec un seul enfant
            elif noeud.gauche is None:
                return noeud.droit
            elif noeud.droit is None:
                return noeud.gauche
            
            # Cas 3 : nœud avec deux enfants
            else:
                # Trouver le successeur (minimum du sous-arbre droit)
                successeur = self.minimum(noeud.droit)
                # Remplacer la valeur du nœud par celle du successeur
                noeud.valeur = successeur.valeur
                # Supprimer le successeur
                noeud.droit = self._supprimer_recursive(noeud.droit, successeur.valeur)
        
        return noeud
    
    def parcours_ordonne(self):
        """Retourne les valeurs triées (parcours infixe)"""
        return parcours_infixe(self.racine, [])

# Exemple d'utilisation
abr = ABR()
valeurs = [50, 30, 70, 20, 40, 60, 80]
for val in valeurs:
    abr.inserer(val)

print("Valeurs triées :", abr.parcours_ordonne())  # [20, 30, 40, 50, 60, 70, 80]
print("Recherche 40 :", abr.rechercher(40) is not None)  # True
print("Recherche 25 :", abr.rechercher(25) is not None)  # False

abr.supprimer(30)
print("Après suppression de 30 :", abr.parcours_ordonne())  # [20, 40, 50, 60, 70, 80]
```

### 2. Complexité des opérations

| Opération | Cas moyen | Pire cas |
|-----------|-----------|----------|
| Recherche | O(log n) | O(n) |
| Insertion | O(log n) | O(n) |
| Suppression | O(log n) | O(n) |

Le pire cas se produit quand l'arbre est dégénéré (linéaire).

## VI. Applications pratiques

### 1. Système de fichiers

```python
class Fichier:
    def __init__(self, nom, taille=0):
        self.nom = nom
        self.taille = taille
        self.est_dossier = taille == 0
        self.enfants = [] if self.est_dossier else None
    
    def ajouter_fichier(self, fichier):
        """Ajoute un fichier/dossier"""
        if self.est_dossier:
            self.enfants.append(fichier)
        else:
            raise ValueError("Impossible d'ajouter un fichier à un fichier")
    
    def taille_totale(self):
        """Calcule la taille totale récursivement"""
        if not self.est_dossier:
            return self.taille
        
        taille = 0
        for enfant in self.enfants:
            taille += enfant.taille_totale()
        return taille
    
    def afficher_arborescence(self, niveau=0):
        """Affiche l'arborescence"""
        indent = "  " * niveau
        if self.est_dossier:
            print(f"{indent}{self.nom}/")
            for enfant in self.enfants:
                enfant.afficher_arborescence(niveau + 1)
        else:
            print(f"{indent}{self.nom} ({self.taille} octets)")
    
    def rechercher(self, nom):
        """Recherche un fichier/dossier par nom"""
        if self.nom == nom:
            return self
        
        if self.est_dossier:
            for enfant in self.enfants:
                resultat = enfant.rechercher(nom)
                if resultat:
                    return resultat
        
        return None

# Création d'un système de fichiers
racine = Fichier("racine")
documents = Fichier("Documents")
images = Fichier("Images")

racine.ajouter_fichier(documents)
racine.ajouter_fichier(images)

documents.ajouter_fichier(Fichier("rapport.pdf", 1024))
documents.ajouter_fichier(Fichier("notes.txt", 512))
images.ajouter_fichier(Fichier("photo1.jpg", 2048))
images.ajouter_fichier(Fichier("photo2.jpg", 1536))

racine.afficher_arborescence()
print(f"Taille totale : {racine.taille_totale()} octets")
```

### 2. Arbre d'expression mathématique

```python
class NoeudExpression:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
    
    def est_operateur(self):
        """Vérifie si le nœud est un opérateur"""
        return self.valeur in ['+', '-', '*', '/', '^']
    
    def evaluer(self):
        """Évalue l'expression représentée par l'arbre"""
        if not self.est_operateur():
            return float(self.valeur)
        
        gauche_val = self.gauche.evaluer()
        droit_val = self.droit.evaluer()
        
        if self.valeur == '+':
            return gauche_val + droit_val
        elif self.valeur == '-':
            return gauche_val - droit_val
        elif self.valeur == '*':
            return gauche_val * droit_val
        elif self.valeur == '/':
            return gauche_val / droit_val
        elif self.valeur == '^':
            return gauche_val ** droit_val
    
    def vers_infixe(self):
        """Convertit l'arbre en notation infixe"""
        if not self.est_operateur():
            return str(self.valeur)
        
        gauche_expr = self.gauche.vers_infixe()
        droit_expr = self.droit.vers_infixe()
        
        return f"({gauche_expr} {self.valeur} {droit_expr})"
    
    def vers_postfixe(self):
        """Convertit l'arbre en notation postfixe"""
        if not self.est_operateur():
            return str(self.valeur)
        
        gauche_expr = self.gauche.vers_postfixe()
        droit_expr = self.droit.vers_postfixe()
        
        return f"{gauche_expr} {droit_expr} {self.valeur}"

# Création de l'arbre pour l'expression : (3 + 4) * 2
#       *
#      / \
#     +   2
#    / \
#   3   4

racine_expr = NoeudExpression('*',
    NoeudExpression('+',
        NoeudExpression('3'),
        NoeudExpression('4')
    ),
    NoeudExpression('2')
)

print(f"Expression infixe : {racine_expr.vers_infixe()}")      # ((3 + 4) * 2)
print(f"Expression postfixe : {racine_expr.vers_postfixe()}")  # 3 4 + 2 *
print(f"Résultat : {racine_expr.evaluer()}")                   # 14.0
```

## VII. Exercices d'application

### Exercice 1 : Arbre généalogique

```python
class Personne:
    def __init__(self, nom, naissance=None):
        self.nom = nom
        self.naissance = naissance
        self.enfants = []
        self.parents = []
    
    def ajouter_enfant(self, enfant):
        """Ajoute un enfant"""
        self.enfants.append(enfant)
        enfant.parents.append(self)
    
    def ancetres(self):
        """Retourne tous les ancêtres"""
        ancetres = set()
        for parent in self.parents:
            ancetres.add(parent)
            ancetres.update(parent.ancetres())
        return ancetres
    
    def descendants(self):
        """Retourne tous les descendants"""
        descendants = set()
        for enfant in self.enfants:
            descendants.add(enfant)
            descendants.update(enfant.descendants())
        return descendants
    
    def generation(self, niveau=0):
        """Affiche la génération à un niveau donné"""
        if niveau == 0:
            return [self]
        
        generation_suivante = []
        for enfant in self.enfants:
            generation_suivante.extend(enfant.generation(niveau - 1))
        return generation_suivante
```

### Exercice 2 : Validation d'ABR

```python
def est_abr_valide(noeud, min_val=float('-inf'), max_val=float('inf')):
    """Vérifie si un arbre binaire est un ABR valide"""
    if noeud is None:
        return True
    
    # Vérifier la contrainte de l'ABR
    if noeud.valeur <= min_val or noeud.valeur >= max_val:
        return False
    
    # Vérifier récursivement les sous-arbres
    return (est_abr_valide(noeud.gauche, min_val, noeud.valeur) and
            est_abr_valide(noeud.droit, noeud.valeur, max_val))

def trouver_kieme_element(racine, k):
    """Trouve le k-ième plus petit élément dans un ABR"""
    def parcours_infixe_avec_compteur(noeud, compteur, k):
        if noeud is None:
            return None, compteur
        
        # Parcourir le sous-arbre gauche
        resultat, compteur = parcours_infixe_avec_compteur(noeud.gauche, compteur, k)
        if resultat is not None:
            return resultat, compteur
        
        # Visiter le nœud actuel
        compteur += 1
        if compteur == k:
            return noeud.valeur, compteur
        
        # Parcourir le sous-arbre droit
        return parcours_infixe_avec_compteur(noeud.droit, compteur, k)
    
    resultat, _ = parcours_infixe_avec_compteur(racine, 0, k)
    return resultat
```

## Conclusion

Les arbres sont des structures de données fondamentales qui offrent :

**Avantages :**
- Organisation hiérarchique naturelle
- Recherche efficace (ABR)
- Parcours flexibles
- Applications nombreuses

**Types d'arbres importants :**
- Arbres généraux : pour les hiérarchies
- Arbres binaires : pour les expressions et structures simples
- ABR : pour la recherche efficace
- Arbres équilibrés : pour garantir les performances

Les arbres sont essentiels pour de nombreux algorithmes et applications en informatique, des systèmes de fichiers aux bases de données en passant par les compilateurs.