# Graphes

## Introduction

Les **graphes** sont des structures de données composées de **sommets** (ou nœuds) reliés par des **arêtes**. Ils permettent de modéliser des relations complexes entre des entités et sont fondamentaux pour résoudre de nombreux problèmes algorithmiques.

**Exemples concrets :** réseaux sociaux, cartes routières, réseaux informatiques, circuits électroniques, dépendances entre tâches.

## I. Concepts fondamentaux

### 1. Définitions de base

- **Sommet (vertex)** : nœud du graphe représentant une entité
- **Arête (edge)** : lien entre deux sommets
- **Graphe orienté** : les arêtes ont une direction (A → B ≠ B → A)
- **Graphe non orienté** : les arêtes sont bidirectionnelles (A — B = B — A)
- **Boucle** : arête reliant un sommet à lui-même
- **Graphe simple** : sans boucles ni arêtes multiples
- **Graphe pondéré** : chaque arête a un poids (coût, distance, etc.)

### 2. Propriétés importantes

- **Degré** d'un sommet : nombre d'arêtes incidentes
  - Graphe orienté : degré entrant + degré sortant
- **Chemin** : séquence de sommets reliés par des arêtes
- **Cycle** : chemin fermé (premier et dernier sommet identiques)
- **Graphe connexe** : il existe un chemin entre toute paire de sommets
- **Composante connexe** : sous-graphe connexe maximal

```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```
Exemple de graphe non orienté :
    A ——— B
    |     |
    |     |
    C ——— D

Degré de A : 2 (relié à B et C)
Chemin de A à D : A → C → D
Cycle : A → B → D → C → A
```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```

## II. Représentations des graphes

### 1. Matrice d'adjacence

Tableau 2D où `matrice[i][j] = 1` si une arête existe entre les sommets i et j.

```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```python
class GrapheMatrice:
    def __init__(self, nb_sommets, oriente=False):
        self.nb_sommets = nb_sommets
        self.oriente = oriente
        self.matrice = [[0] * nb_sommets for _ in range(nb_sommets)]
        self.sommets = {}  # Mapping nom -> index
        self.noms = {}     # Mapping index -> nom
    
    def ajouter_sommet(self, nom, index):
        """Ajoute un sommet avec son nom"""
        if 0 <= index < self.nb_sommets:
            self.sommets[nom] = index
            self.noms[index] = nom
    
    def ajouter_arete(self, sommet1, sommet2, poids=1):
        """Ajoute une arête entre deux sommets"""
        if sommet1 in self.sommets and sommet2 in self.sommets:
            i, j = self.sommets[sommet1], self.sommets[sommet2]
            self.matrice[i][j] = poids
            if not self.oriente:
                self.matrice[j][i] = poids
    
    def supprimer_arete(self, sommet1, sommet2):
        """Supprime une arête"""
        if sommet1 in self.sommets and sommet2 in self.sommets:
            i, j = self.sommets[sommet1], self.sommets[sommet2]
            self.matrice[i][j] = 0
            if not self.oriente:
                self.matrice[j][i] = 0
    
    def sont_adjacents(self, sommet1, sommet2):
        """Vérifie si deux sommets sont adjacents"""
        if sommet1 in self.sommets and sommet2 in self.sommets:
            i, j = self.sommets[sommet1], self.sommets[sommet2]
            return self.matrice[i][j] != 0
        return False
    
    def voisins(self, sommet):
        """Retourne les voisins d'un sommet"""
        if sommet not in self.sommets:
            return []
        
        index = self.sommets[sommet]
        voisins = []
        for j in range(self.nb_sommets):
            if self.matrice[index][j] != 0:
                voisins.append(self.noms[j])
        return voisins
    
    def degre(self, sommet):
        """Calcule le degré d'un sommet"""
        if sommet not in self.sommets:
            return 0
        
        index = self.sommets[sommet]
        if self.oriente:
            degre_sortant = sum(1 for j in range(self.nb_sommets) if self.matrice[index][j] != 0)
            degre_entrant = sum(1 for i in range(self.nb_sommets) if self.matrice[i][index] != 0)
            return degre_entrant, degre_sortant
        else:
            return sum(1 for j in range(self.nb_sommets) if self.matrice[index][j] != 0)
    
    def afficher_matrice(self):
        """Affiche la matrice d'adjacence"""
        print("   ", end="")
        for i in range(self.nb_sommets):
            print(f"{self.noms.get(i, i):3}", end="")
        print()
        
        for i in range(self.nb_sommets):
            print(f"{self.noms.get(i, i):3}", end="")
            for j in range(self.nb_sommets):
                print(f"{self.matrice[i][j]:3}", end="")
            print()

# Exemple d'utilisation
graphe_mat = GrapheMatrice(4, oriente=False)
graphe_mat.ajouter_sommet("A", 0)
graphe_mat.ajouter_sommet("B", 1)
graphe_mat.ajouter_sommet("C", 2)
graphe_mat.ajouter_sommet("D", 3)

graphe_mat.ajouter_arete("A", "B")
graphe_mat.ajouter_arete("A", "C")
graphe_mat.ajouter_arete("B", "D")
graphe_mat.ajouter_arete("C", "D")

graphe_mat.afficher_matrice()
print(f"Voisins de A : {graphe_mat.voisins('A')}")
print(f"Degré de A : {graphe_mat.degre('A')}")
```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```

### 2. Liste d'adjacence

Chaque sommet maintient une liste de ses voisins.

```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```python
class GrapheListe:
    def __init__(self, oriente=False):
        self.oriente = oriente
        self.adjacence = {}  # sommet -> liste des voisins
    
    def ajouter_sommet(self, sommet):
        """Ajoute un sommet"""
        if sommet not in self.adjacence:
            self.adjacence[sommet] = []
    
    def ajouter_arete(self, sommet1, sommet2, poids=1):
        """Ajoute une arête entre deux sommets"""
        # S'assurer que les sommets existent
        self.ajouter_sommet(sommet1)
        self.ajouter_sommet(sommet2)
        
        # Ajouter l'arête
        if isinstance(poids, (int, float)) and poids != 1:
            self.adjacence[sommet1].append((sommet2, poids))
            if not self.oriente:
                self.adjacence[sommet2].append((sommet1, poids))
        else:
            self.adjacence[sommet1].append(sommet2)
            if not self.oriente:
                self.adjacence[sommet2].append(sommet1)
    
    def supprimer_arete(self, sommet1, sommet2):
        """Supprime une arête"""
        if sommet1 in self.adjacence:
            # Gérer les arêtes avec ou sans poids
            self.adjacence[sommet1] = [
                voisin for voisin in self.adjacence[sommet1]
                if (isinstance(voisin, tuple) and voisin[0] != sommet2) or
                   (not isinstance(voisin, tuple) and voisin != sommet2)
            ]
        
        if not self.oriente and sommet2 in self.adjacence:
            self.adjacence[sommet2] = [
                voisin for voisin in self.adjacence[sommet2]
                if (isinstance(voisin, tuple) and voisin[0] != sommet1) or
                   (not isinstance(voisin, tuple) and voisin != sommet1)
            ]
    
    def sont_adjacents(self, sommet1, sommet2):
        """Vérifie si deux sommets sont adjacents"""
        if sommet1 not in self.adjacence:
            return False
        
        for voisin in self.adjacence[sommet1]:
            if isinstance(voisin, tuple):
                if voisin[0] == sommet2:
                    return True
            else:
                if voisin == sommet2:
                    return True
        return False
    
    def voisins(self, sommet):
        """Retourne les voisins d'un sommet"""
        if sommet not in self.adjacence:
            return []
        
        voisins = []
        for voisin in self.adjacence[sommet]:
            if isinstance(voisin, tuple):
                voisins.append(voisin[0])
            else:
                voisins.append(voisin)
        return voisins
    
    def degre(self, sommet):
        """Calcule le degré d'un sommet"""
        if sommet not in self.adjacence:
            return 0
        
        if self.oriente:
            degre_sortant = len(self.adjacence[sommet])
            degre_entrant = sum(1 for s in self.adjacence 
                              for v in self.adjacence[s]
                              if (isinstance(v, tuple) and v[0] == sommet) or
                                 (not isinstance(v, tuple) and v == sommet))
            return degre_entrant, degre_sortant
        else:
            return len(self.adjacence[sommet])
    
    def sommets(self):
        """Retourne tous les sommets"""
        return list(self.adjacence.keys())
    
    def nb_sommets(self):
        """Retourne le nombre de sommets"""
        return len(self.adjacence)
    
    def nb_aretes(self):
        """Retourne le nombre d'arêtes"""
        total = sum(len(voisins) for voisins in self.adjacence.values())
        return total if self.oriente else total // 2
    
    def afficher(self):
        """Affiche le graphe"""
        for sommet, voisins in self.adjacence.items():
            print(f"{sommet}: {voisins}")

# Exemple d'utilisation
graphe_liste = GrapheListe(oriente=False)
graphe_liste.ajouter_arete("A", "B")
graphe_liste.ajouter_arete("A", "C")
graphe_liste.ajouter_arete("B", "D")
graphe_liste.ajouter_arete("C", "D")

graphe_liste.afficher()
print(f"Nombre de sommets : {graphe_liste.nb_sommets()}")
print(f"Nombre d'arêtes : {graphe_liste.nb_aretes()}")
```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```

### 3. Comparaison des représentations

| Aspect | Matrice d'adjacence | Liste d'adjacence |
|--------|--------------------|-----------------|
| **Espace** | O(V²) | O(V + E) |
| **Vérifier arête** | O(1) | O(degré) |
| **Ajouter arête** | O(1) | O(1) |
| **Parcourir voisins** | O(V) | O(degré) |
| **Meilleur pour** | Graphes denses | Graphes creux |

## III. Parcours de graphes

### 1. Parcours en profondeur (DFS)

Explore le graphe en allant le plus loin possible avant de revenir en arrière.

```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```python
def dfs_recursif(graphe, sommet_depart, visites=None):
    """Parcours en profondeur récursif"""
    if visites is None:
        visites = set()
    
    visites.add(sommet_depart)
    print(f"Visite : {sommet_depart}")
    
    for voisin in graphe.voisins(sommet_depart):
        if voisin not in visites:
            dfs_recursif(graphe, voisin, visites)
    
    return visites

def dfs_iteratif(graphe, sommet_depart):
    """Parcours en profondeur itératif avec une pile"""
    visites = set()
    pile = [sommet_depart]
    
    while pile:
        sommet = pile.pop()
        if sommet not in visites:
            visites.add(sommet)
            print(f"Visite : {sommet}")
            
            # Ajouter les voisins non visités à la pile
            for voisin in graphe.voisins(sommet):
                if voisin not in visites:
                    pile.append(voisin)
    
    return visites

def composantes_connexes(graphe):
    """Trouve toutes les composantes connexes"""
    visites = set()
    composantes = []
    
    for sommet in graphe.sommets():
        if sommet not in visites:
            composante = set()
            dfs_composante(graphe, sommet, visites, composante)
            composantes.append(composante)
    
    return composantes

def dfs_composante(graphe, sommet, visites, composante):
    """DFS pour une composante connexe"""
    visites.add(sommet)
    composante.add(sommet)
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs_composante(graphe, voisin, visites, composante)
```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```

### 2. Parcours en largeur (BFS)

Explore le graphe niveau par niveau.

```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```python
from collections import deque

def bfs(graphe, sommet_depart):
    """Parcours en largeur"""
    visites = set()
    file = deque([sommet_depart])
    visites.add(sommet_depart)
    
    while file:
        sommet = file.popleft()
        print(f"Visite : {sommet}")
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
    
    return visites

def plus_court_chemin_bfs(graphe, depart, arrivee):
    """Trouve le plus court chemin (en nombre d'arêtes) avec BFS"""
    if depart == arrivee:
        return [depart]
    
    visites = set([depart])
    file = deque([(depart, [depart])])
    
    while file:
        sommet, chemin = file.popleft()
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                nouveau_chemin = chemin + [voisin]
                
                if voisin == arrivee:
                    return nouveau_chemin
                
                visites.add(voisin)
                file.append((voisin, nouveau_chemin))
    
    return None  # Pas de chemin trouvé

def distance_bfs(graphe, sommet_depart):
    """Calcule les distances depuis un sommet de départ"""
    distances = {sommet_depart: 0}
    file = deque([sommet_depart])
    
    while file:
        sommet = file.popleft()
        
        for voisin in graphe.voisins(sommet):
            if voisin not in distances:
                distances[voisin] = distances[sommet] + 1
                file.append(voisin)
    
    return distances
```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```

## IV. Algorithmes sur les graphes

### 1. Détection de cycles

```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```python
def a_cycle_non_oriente(graphe):
    """Détecte un cycle dans un graphe non orienté"""
    visites = set()
    
    def dfs_cycle(sommet, parent):
        visites.add(sommet)
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                if dfs_cycle(voisin, sommet):
                    return True
            elif voisin != parent:  # Cycle détecté
                return True
        
        return False
    
    for sommet in graphe.sommets():
        if sommet not in visites:
            if dfs_cycle(sommet, None):
                return True
    
    return False

def a_cycle_oriente(graphe):
    """Détecte un cycle dans un graphe orienté"""
    BLANC, GRIS, NOIR = 0, 1, 2
    couleurs = {sommet: BLANC for sommet in graphe.sommets()}
    
    def dfs_cycle(sommet):
        couleurs[sommet] = GRIS
        
        for voisin in graphe.voisins(sommet):
            if couleurs[voisin] == GRIS:  # Arête arrière = cycle
                return True
            elif couleurs[voisin] == BLANC and dfs_cycle(voisin):
                return True
        
        couleurs[sommet] = NOIR
        return False
    
    for sommet in graphe.sommets():
        if couleurs[sommet] == BLANC:
            if dfs_cycle(sommet):
                return True
    
    return False
```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```

### 2. Tri topologique

```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```python
def tri_topologique(graphe):
    """Tri topologique d'un graphe orienté acyclique (DAG)"""
    if a_cycle_oriente(graphe):
        return None  # Impossible si le graphe a des cycles
    
    visites = set()
    pile = []
    
    def dfs_topo(sommet):
        visites.add(sommet)
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                dfs_topo(voisin)
        
        pile.append(sommet)  # Ajouter après avoir visité tous les descendants
    
    for sommet in graphe.sommets():
        if sommet not in visites:
            dfs_topo(sommet)
    
    return pile[::-1]  # Inverser pour obtenir l'ordre topologique

def tri_topologique_kahn(graphe):
    """Tri topologique avec l'algorithme de Kahn"""
    # Calculer les degrés entrants
    degres_entrants = {sommet: 0 for sommet in graphe.sommets()}
    for sommet in graphe.sommets():
        for voisin in graphe.voisins(sommet):
            degres_entrants[voisin] += 1
    
    # File des sommets sans prédécesseurs
    file = deque([sommet for sommet, degre in degres_entrants.items() if degre == 0])
    resultat = []
    
    while file:
        sommet = file.popleft()
        resultat.append(sommet)
        
        # Supprimer les arêtes sortantes
        for voisin in graphe.voisins(sommet):
            degres_entrants[voisin] -= 1
            if degres_entrants[voisin] == 0:
                file.append(voisin)
    
    # Vérifier s'il y a un cycle
    if len(resultat) != graphe.nb_sommets():
        return None  # Cycle détecté
    
    return resultat
```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```

## V. Graphes pondérés et plus courts chemins

### 1. Algorithme de Dijkstra

```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```python
import heapq

def dijkstra(graphe, sommet_depart):
    """Algorithme de Dijkstra pour les plus courts chemins"""
    distances = {sommet: float('inf') for sommet in graphe.sommets()}
    distances[sommet_depart] = 0
    predecesseurs = {sommet: None for sommet in graphe.sommets()}
    
    # File de priorité : (distance, sommet)
    tas = [(0, sommet_depart)]
    visites = set()
    
    while tas:
        distance_actuelle, sommet_actuel = heapq.heappop(tas)
        
        if sommet_actuel in visites:
            continue
        
        visites.add(sommet_actuel)
        
        # Examiner tous les voisins
        for voisin_info in graphe.adjacence[sommet_actuel]:
            if isinstance(voisin_info, tuple):
                voisin, poids = voisin_info
            else:
                voisin, poids = voisin_info, 1
            
            if voisin not in visites:
                nouvelle_distance = distance_actuelle + poids
                
                if nouvelle_distance < distances[voisin]:
                    distances[voisin] = nouvelle_distance
                    predecesseurs[voisin] = sommet_actuel
                    heapq.heappush(tas, (nouvelle_distance, voisin))
    
    return distances, predecesseurs

def reconstruire_chemin(predecesseurs, depart, arrivee):
    """Reconstruit le chemin à partir des prédécesseurs"""
    chemin = []
    sommet_actuel = arrivee
    
    while sommet_actuel is not None:
        chemin.append(sommet_actuel)
        sommet_actuel = predecesseurs[sommet_actuel]
    
    chemin.reverse()
    
    # Vérifier si un chemin existe
    if chemin[0] != depart:
        return None
    
    return chemin

# Exemple d'utilisation
graphe_pondere = GrapheListe(oriente=True)
graphe_pondere.ajouter_arete("A", "B", 4)
graphe_pondere.ajouter_arete("A", "C", 2)
graphe_pondere.ajouter_arete("B", "C", 1)
graphe_pondere.ajouter_arete("B", "D", 5)
graphe_pondere.ajouter_arete("C", "D", 8)
graphe_pondere.ajouter_arete("C", "E", 10)
graphe_pondere.ajouter_arete("D", "E", 2)

distances, predecesseurs = dijkstra(graphe_pondere, "A")
print(f"Distances depuis A : {distances}")
print(f"Chemin A → E : {reconstruire_chemin(predecesseurs, 'A', 'E')}")
```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```

### 2. Algorithme de Floyd-Warshall

```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```python
def floyd_warshall(graphe):
    """Algorithme de Floyd-Warshall pour tous les plus courts chemins"""
    sommets = list(graphe.sommets())
    n = len(sommets)
    
    # Initialiser les matrices de distances et de prédécesseurs
    distances = [[float('inf')] * n for _ in range(n)]
    predecesseurs = [[None] * n for _ in range(n)]
    
    # Mapping sommet -> index
    index_sommet = {sommet: i for i, sommet in enumerate(sommets)}
    
    # Initialiser les distances
    for i in range(n):
        distances[i][i] = 0
    
    for sommet in sommets:
        i = index_sommet[sommet]
        for voisin_info in graphe.adjacence[sommet]:
            if isinstance(voisin_info, tuple):
                voisin, poids = voisin_info
            else:
                voisin, poids = voisin_info, 1
            
            j = index_sommet[voisin]
            distances[i][j] = poids
            predecesseurs[i][j] = i
    
    # Algorithme principal
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    predecesseurs[i][j] = predecesseurs[k][j]
    
    return distances, predecesseurs, sommets

def afficher_matrice_distances(distances, sommets):
    """Affiche la matrice des distances"""
    print("Matrice des plus courtes distances :")
    print("     ", end="")
    for sommet in sommets:
        print(f"{sommet:6}", end="")
    print()
    
    for i, sommet in enumerate(sommets):
        print(f"{sommet:4} ", end="")
        for j in range(len(sommets)):
            if distances[i][j] == float('inf'):
                print("   ∞  ", end="")
            else:
                print(f"{distances[i][j]:6.1f}", end="")
        print()
```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```

## VI. Applications pratiques

### 1. Réseau social

```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```python
class ReseauSocial:
    def __init__(self):
        self.graphe = GrapheListe(oriente=False)
        self.utilisateurs = {}  # nom -> informations
    
    def ajouter_utilisateur(self, nom, age=None, ville=None):
        """Ajoute un utilisateur"""
        self.graphe.ajouter_sommet(nom)
        self.utilisateurs[nom] = {'age': age, 'ville': ville}
    
    def ajouter_amitie(self, utilisateur1, utilisateur2):
        """Ajoute une relation d'amitié"""
        self.graphe.ajouter_arete(utilisateur1, utilisateur2)
    
    def amis_communs(self, utilisateur1, utilisateur2):
        """Trouve les amis communs entre deux utilisateurs"""
        amis1 = set(self.graphe.voisins(utilisateur1))
        amis2 = set(self.graphe.voisins(utilisateur2))
        return amis1.intersection(amis2)
    
    def suggestions_amis(self, utilisateur):
        """Suggère des amis (amis d'amis)"""
        amis = set(self.graphe.voisins(utilisateur))
        suggestions = set()
        
        for ami in amis:
            amis_de_ami = set(self.graphe.voisins(ami))
            suggestions.update(amis_de_ami)
        
        # Exclure l'utilisateur lui-même et ses amis actuels
        suggestions.discard(utilisateur)
        suggestions -= amis
        
        return list(suggestions)
    
    def distance_sociale(self, utilisateur1, utilisateur2):
        """Calcule la distance sociale (degrés de séparation)"""
        distances = distance_bfs(self.graphe, utilisateur1)
        return distances.get(utilisateur2, float('inf'))
    
    def influenceurs(self, top_n=5):
        """Trouve les utilisateurs les plus connectés"""
        degres = [(utilisateur, self.graphe.degre(utilisateur)) 
                 for utilisateur in self.graphe.sommets()]
        return sorted(degres, key=lambda x: x[1], reverse=True)[:top_n]

# Exemple d'utilisation
reseau = ReseauSocial()
reseau.ajouter_utilisateur("Alice", 25, "Paris")
reseau.ajouter_utilisateur("Bob", 30, "Lyon")
reseau.ajouter_utilisateur("Charlie", 28, "Paris")
reseau.ajouter_utilisateur("Diana", 22, "Marseille")
reseau.ajouter_utilisateur("Eve", 35, "Paris")

reseau.ajouter_amitie("Alice", "Bob")
reseau.ajouter_amitie("Alice", "Charlie")
reseau.ajouter_amitie("Bob", "Diana")
reseau.ajouter_amitie("Charlie", "Eve")
reseau.ajouter_amitie("Diana", "Eve")

print(f"Amis communs Alice-Diana : {reseau.amis_communs('Alice', 'Diana')}")
print(f"Suggestions pour Alice : {reseau.suggestions_amis('Alice')}")
print(f"Distance Alice-Eve : {reseau.distance_sociale('Alice', 'Eve')}")
print(f"Influenceurs : {reseau.influenceurs(3)}")
```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```

### 2. Système de navigation GPS

```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```python
class CarteRoutiere:
    def __init__(self):
        self.graphe = GrapheListe(oriente=False)
        self.coordonnees = {}  # ville -> (latitude, longitude)
    
    def ajouter_ville(self, nom, latitude, longitude):
        """Ajoute une ville avec ses coordonnées"""
        self.graphe.ajouter_sommet(nom)
        self.coordonnees[nom] = (latitude, longitude)
    
    def ajouter_route(self, ville1, ville2, distance):
        """Ajoute une route entre deux villes"""
        self.graphe.ajouter_arete(ville1, ville2, distance)
    
    def plus_court_chemin(self, depart, arrivee):
        """Trouve le plus court chemin entre deux villes"""
        distances, predecesseurs = dijkstra(self.graphe, depart)
        
        if distances[arrivee] == float('inf'):
            return None, float('inf')
        
        chemin = reconstruire_chemin(predecesseurs, depart, arrivee)
        return chemin, distances[arrivee]
    
    def villes_accessibles(self, depart, distance_max):
        """Trouve toutes les villes accessibles dans une distance donnée"""
        distances, _ = dijkstra(self.graphe, depart)
        return [ville for ville, dist in distances.items() 
                if dist <= distance_max and ville != depart]
    
    def itineraire_detaille(self, chemin):
        """Affiche un itinéraire détaillé"""
        if not chemin or len(chemin) < 2:
            return
        
        distance_totale = 0
        print(f"Itinéraire de {chemin[0]} à {chemin[-1]} :")
        
        for i in range(len(chemin) - 1):
            ville_actuelle = chemin[i]
            ville_suivante = chemin[i + 1]
            
            # Trouver la distance entre les deux villes
            for voisin_info in self.graphe.adjacence[ville_actuelle]:
                if isinstance(voisin_info, tuple):
                    voisin, distance = voisin_info
                    if voisin == ville_suivante:
                        distance_totale += distance
                        print(f"{i+1}. {ville_actuelle} → {ville_suivante} ({distance} km)")
                        break
        
        print(f"Distance totale : {distance_totale} km")

# Exemple d'utilisation
carte = CarteRoutiere()
carte.ajouter_ville("Paris", 48.8566, 2.3522)
carte.ajouter_ville("Lyon", 45.7640, 4.8357)
carte.ajouter_ville("Marseille", 43.2965, 5.3698)
carte.ajouter_ville("Toulouse", 43.6047, 1.4442)
carte.ajouter_ville("Bordeaux", 44.8378, -0.5792)

carte.ajouter_route("Paris", "Lyon", 462)
carte.ajouter_route("Lyon", "Marseille", 314)
carte.ajouter_route("Paris", "Bordeaux", 579)
carte.ajouter_route("Bordeaux", "Toulouse", 244)
carte.ajouter_route("Toulouse", "Marseille", 405)

chemin, distance = carte.plus_court_chemin("Paris", "Marseille")
print(f"Plus court chemin : {chemin} ({distance} km)")
carte.itineraire_detaille(chemin)
```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```

## VII. Exercices d'application

### Exercice 1 : Planification de tâches

```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```python
class PlanificateurTaches:
    def __init__(self):
        self.graphe = GrapheListe(oriente=True)
        self.durees = {}  # tâche -> durée
    
    def ajouter_tache(self, nom, duree):
        """Ajoute une tâche avec sa durée"""
        self.graphe.ajouter_sommet(nom)
        self.durees[nom] = duree
    
    def ajouter_dependance(self, tache_prerequis, tache_dependante):
        """Ajoute une dépendance entre tâches"""
        self.graphe.ajouter_arete(tache_prerequis, tache_dependante)
    
    def ordre_execution(self):
        """Détermine l'ordre d'exécution des tâches"""
        return tri_topologique(self.graphe)
    
    def chemin_critique(self):
        """Calcule le chemin critique (plus long chemin)"""
        ordre = self.ordre_execution()
        if not ordre:
            return None
        
        # Calculer les temps de début au plus tôt
        temps_debut = {tache: 0 for tache in self.graphe.sommets()}
        
        for tache in ordre:
            for successeur in self.graphe.voisins(tache):
                temps_debut[successeur] = max(
                    temps_debut[successeur],
                    temps_debut[tache] + self.durees[tache]
                )
        
        # Trouver la tâche avec le temps de fin le plus tardif
        temps_fin_max = 0
        tache_finale = None
        
        for tache in self.graphe.sommets():
            temps_fin = temps_debut[tache] + self.durees[tache]
            if temps_fin > temps_fin_max:
                temps_fin_max = temps_fin
                tache_finale = tache
        
        return temps_fin_max, self.reconstruire_chemin_critique(tache_finale, temps_debut)
```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```

### Exercice 2 : Détection de communautés

```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```python
def detecter_communautes_simples(graphe):
    """Détection simple de communautés basée sur la connectivité"""
    communautes = []
    visites = set()
    
    for sommet in graphe.sommets():
        if sommet not in visites:
            communaute = set()
            dfs_communaute(graphe, sommet, visites, communaute)
            communautes.append(communaute)
    
    return communautes

def coefficient_clustering(graphe, sommet):
    """Calcule le coefficient de clustering d'un sommet"""
    voisins = set(graphe.voisins(sommet))
    n = len(voisins)
    
    if n < 2:
        return 0
    
    # Compter les arêtes entre voisins
    aretes_voisins = 0
    for v1 in voisins:
        for v2 in voisins:
            if v1 != v2 and graphe.sont_adjacents(v1, v2):
                aretes_voisins += 1
    
    # Diviser par 2 car chaque arête est comptée deux fois
    aretes_voisins //= 2
    
    # Coefficient = arêtes réelles / arêtes possibles
    return aretes_voisins / (n * (n - 1) / 2)
```

## Parcours de graphes

### Parcours en profondeur (DFS)

```python
def dfs(graphe, sommet, visites=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            dfs(graphe, voisin, visites)
```

### Parcours en largeur (BFS)

```python
from collections import deque

def bfs(graphe, depart):
    visites = set([depart])
    file = deque([depart])
    
    while file:
        sommet = file.popleft()
        print(sommet, end=' ')
        
        for voisin in graphe.voisins(sommet):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
```

## Algorithmes sur les graphes

### Plus court chemin (Dijkstra)

```python
def dijkstra(graphe, depart):
    n = graphe.n
    distances = [float('inf')] * n
    # ... (le reste de la fonction Dijkstra et autres algorithmes potentiels)
```

## Conclusion

Les graphes sont des structures de données fondamentales qui permettent de :

**Modéliser des relations complexes :**
- Réseaux sociaux, transport, communication
- Dépendances, hiérarchies, flux

**Résoudre des problèmes algorithmiques :**
- Plus courts chemins
- Détection de cycles
- Tri topologique
- Connectivité

**Choisir la bonne représentation :**
- Matrice d'adjacence : graphes denses, vérifications rapides
- Liste d'adjacence : graphes creux, parcours efficaces

Les algorithmes sur les graphes sont essentiels dans de nombreux domaines : intelligence artificielle, optimisation, analyse de réseaux, bioinformatique, etc.