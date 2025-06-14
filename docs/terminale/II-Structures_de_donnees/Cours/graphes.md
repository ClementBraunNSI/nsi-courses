# Les Graphes

## Introduction

Un **graphe** est une structure de données fondamentale qui modélise des relations entre des objets. Il est composé de :
- **Sommets** (ou nœuds) : les objets du graphe
- **Arêtes** (ou arcs) : les relations entre les objets

Les graphes sont omniprésents en informatique : réseaux sociaux, GPS, internet, circuits électroniques, etc.

## Types de graphes

### Graphe orienté vs non orienté

**Graphe non orienté :** Les arêtes n'ont pas de direction. Si A est relié à B, alors B est relié à A.
```
A ---- B
|      |
C ---- D
```

**Graphe orienté :** Les arêtes ont une direction (flèches).
```
A ---> B
^      |
C <--- D
```

### Graphe pondéré

Les arêtes ont un **poids** (coût, distance, temps...).
```
A --5-- B
|       |
3       2
|       |
C --1-- D
```

## Représentations en mémoire

### 1. Matrice d'adjacence

Tableau 2D où `matrice[i][j]` indique s'il y a une arête entre le sommet i et le sommet j.

```python
# Exemple : graphe A-B-C avec A relié à B et C
matrice = [
    [0, 1, 1],  # A : relié à B(1) et C(2)
    [1, 0, 0],  # B : relié à A(0)
    [1, 0, 0]   # C : relié à A(0)
]
```

**Avantages :**
- Vérification d'adjacence en O(1)
- Simple à implémenter

**Inconvénients :**
- Espace O(n²) même pour des graphes peu denses
- Parcours des voisins en O(n)

### 2. Liste d'adjacence

Chaque sommet maintient une liste de ses voisins.

```python
# Même graphe en liste d'adjacence
graphe = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A']
}
```

**Avantages :**
- Espace O(n + m) où m = nombre d'arêtes
- Parcours des voisins efficace

**Inconvénients :**
- Vérification d'adjacence en O(degré)

## Implémentation en Python

### Classe Graphe avec liste d'adjacence

```python
class Graphe:
    def __init__(self, oriente=False):
        self.sommets = {}  # dictionnaire : sommet -> liste des voisins
        self.oriente = oriente
    
    def ajouter_sommet(self, sommet):
        """Ajoute un sommet au graphe"""
        if sommet not in self.sommets:
            self.sommets[sommet] = []
    
    def ajouter_arete(self, sommet1, sommet2, poids=1):
        """Ajoute une arête entre deux sommets"""
        # S'assurer que les sommets existent
        self.ajouter_sommet(sommet1)
        self.ajouter_sommet(sommet2)
        
        # Ajouter l'arête
        self.sommets[sommet1].append((sommet2, poids))
        
        # Si non orienté, ajouter l'arête inverse
        if not self.oriente:
            self.sommets[sommet2].append((sommet1, poids))
    
    def supprimer_arete(self, sommet1, sommet2):
        """Supprime une arête"""
        if sommet1 in self.sommets:
            self.sommets[sommet1] = [(v, p) for v, p in self.sommets[sommet1] if v != sommet2]
        
        if not self.oriente and sommet2 in self.sommets:
            self.sommets[sommet2] = [(v, p) for v, p in self.sommets[sommet2] if v != sommet1]
    
    def voisins(self, sommet):
        """Retourne la liste des voisins d'un sommet"""
        return self.sommets.get(sommet, [])
    
    def est_adjacent(self, sommet1, sommet2):
        """Vérifie si deux sommets sont adjacents"""
        return any(voisin == sommet2 for voisin, _ in self.voisins(sommet1))
    
    def degre(self, sommet):
        """Retourne le degré d'un sommet"""
        return len(self.voisins(sommet))
    
    def afficher(self):
        """Affiche le graphe"""
        for sommet, voisins in self.sommets.items():
            print(f"{sommet}: {[f'{v}({p})' for v, p in voisins]}")
```

### Exemple d'utilisation

```python
# Création d'un graphe non orienté
g = Graphe(oriente=False)

# Ajout des arêtes
g.ajouter_arete('A', 'B', 5)
g.ajouter_arete('A', 'C', 3)
g.ajouter_arete('B', 'D', 2)
g.ajouter_arete('C', 'D', 1)

# Affichage
g.afficher()
# A: ['B(5)', 'C(3)']
# B: ['A(5)', 'D(2)']
# C: ['A(3)', 'D(1)']
# D: ['B(2)', 'C(1)']
```

## Algorithmes de parcours

### Parcours en largeur (BFS)

Explore le graphe niveau par niveau en utilisant une **file**.

```python
from collections import deque

def parcours_largeur(graphe, sommet_depart):
    """Parcours en largeur (BFS)"""
    visites = set()
    file = deque([sommet_depart])
    ordre_visite = []
    
    while file:
        sommet = file.popleft()
        
        if sommet not in visites:
            visites.add(sommet)
            ordre_visite.append(sommet)
            
            # Ajouter les voisins non visités
            for voisin, _ in graphe.voisins(sommet):
                if voisin not in visites:
                    file.append(voisin)
    
    return ordre_visite
```

### Parcours en profondeur (DFS)

Explore le graphe en allant le plus loin possible avant de revenir en arrière. Utilise une **pile** (ou récursion).

```python
def parcours_profondeur_recursif(graphe, sommet, visites=None):
    """Parcours en profondeur récursif (DFS)"""
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin, _ in graphe.voisins(sommet):
        if voisin not in visites:
            parcours_profondeur_recursif(graphe, voisin, visites)

def parcours_profondeur_iteratif(graphe, sommet_depart):
    """Parcours en profondeur itératif (DFS)"""
    visites = set()
    pile = [sommet_depart]
    ordre_visite = []
    
    while pile:
        sommet = pile.pop()
        
        if sommet not in visites:
            visites.add(sommet)
            ordre_visite.append(sommet)
            
            # Ajouter les voisins (en ordre inverse pour respecter l'ordre)
            for voisin, _ in reversed(graphe.voisins(sommet)):
                if voisin not in visites:
                    pile.append(voisin)
    
    return ordre_visite
```

## Algorithmes sur les graphes

### Détection de cycle

```python
def a_un_cycle(graphe):
    """Détecte s'il y a un cycle dans un graphe non orienté"""
    visites = set()
    
    def dfs(sommet, parent):
        visites.add(sommet)
        
        for voisin, _ in graphe.voisins(sommet):
            if voisin not in visites:
                if dfs(voisin, sommet):
                    return True
            elif voisin != parent:  # Cycle détecté
                return True
        
        return False
    
    # Vérifier chaque composante connexe
    for sommet in graphe.sommets:
        if sommet not in visites:
            if dfs(sommet, None):
                return True
    
    return False
```

### Plus court chemin (Dijkstra)

```python
import heapq

def dijkstra(graphe, depart):
    """Algorithme de Dijkstra pour le plus court chemin"""
    distances = {sommet: float('inf') for sommet in graphe.sommets}
    distances[depart] = 0
    predecesseurs = {}
    
    # File de priorité : (distance, sommet)
    file_priorite = [(0, depart)]
    
    while file_priorite:
        distance_actuelle, sommet_actuel = heapq.heappop(file_priorite)
        
        # Si on a déjà trouvé un chemin plus court, ignorer
        if distance_actuelle > distances[sommet_actuel]:
            continue
        
        # Examiner les voisins
        for voisin, poids in graphe.voisins(sommet_actuel):
            nouvelle_distance = distance_actuelle + poids
            
            if nouvelle_distance < distances[voisin]:
                distances[voisin] = nouvelle_distance
                predecesseurs[voisin] = sommet_actuel
                heapq.heappush(file_priorite, (nouvelle_distance, voisin))
    
    return distances, predecesseurs

def reconstruire_chemin(predecesseurs, depart, arrivee):
    """Reconstruit le chemin à partir des prédécesseurs"""
    chemin = []
    sommet = arrivee
    
    while sommet is not None:
        chemin.append(sommet)
        sommet = predecesseurs.get(sommet)
    
    chemin.reverse()
    return chemin if chemin[0] == depart else []
```

## Applications pratiques

### Réseau social

```python
class ReseauSocial:
    def __init__(self):
        self.graphe = Graphe(oriente=False)
    
    def ajouter_personne(self, nom):
        self.graphe.ajouter_sommet(nom)
    
    def ajouter_amitie(self, personne1, personne2):
        self.graphe.ajouter_arete(personne1, personne2)
    
    def amis_communs(self, personne1, personne2):
        """Trouve les amis communs entre deux personnes"""
        amis1 = {voisin for voisin, _ in self.graphe.voisins(personne1)}
        amis2 = {voisin for voisin, _ in self.graphe.voisins(personne2)}
        return amis1.intersection(amis2)
    
    def degre_separation(self, personne1, personne2):
        """Calcule le degré de séparation (distance) entre deux personnes"""
        distances, _ = dijkstra(self.graphe, personne1)
        return distances.get(personne2, float('inf'))
```

### Système de navigation

```python
class CarteRoutiere:
    def __init__(self):
        self.graphe = Graphe(oriente=False)
    
    def ajouter_route(self, ville1, ville2, distance):
        self.graphe.ajouter_arete(ville1, ville2, distance)
    
    def plus_court_chemin(self, depart, arrivee):
        """Trouve le plus court chemin entre deux villes"""
        distances, predecesseurs = dijkstra(self.graphe, depart)
        
        if distances[arrivee] == float('inf'):
            return None, float('inf')
        
        chemin = reconstruire_chemin(predecesseurs, depart, arrivee)
        return chemin, distances[arrivee]
```

## Complexités

| Opération | Matrice d'adjacence | Liste d'adjacence |
|-----------|--------------------|-----------------|
| Ajouter sommet | O(n²) | O(1) |
| Ajouter arête | O(1) | O(1) |
| Supprimer arête | O(1) | O(degré) |
| Vérifier adjacence | O(1) | O(degré) |
| Parcours complet | O(n²) | O(n + m) |

**Où :**
- n = nombre de sommets
- m = nombre d'arêtes
- degré = nombre de voisins d'un sommet

## Conclusion

Les graphes sont une structure de données puissante pour modéliser des relations complexes. Le choix de la représentation (matrice vs liste d'adjacence) dépend de la densité du graphe et des opérations les plus fréquentes.

**Points clés à retenir :**
- Graphe = sommets + arêtes
- Deux représentations principales : matrice et liste d'adjacence
- Algorithmes de parcours : BFS (largeur) et DFS (profondeur)
- Applications : réseaux, navigation, réseaux sociaux, etc.
- Complexité dépend de la représentation choisie