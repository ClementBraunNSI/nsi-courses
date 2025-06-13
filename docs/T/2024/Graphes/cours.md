# Graphes

## Introduction aux graphes

### Définitions

Un graphe est une structure composée de :
- Sommets (ou nœuds)
- Arêtes (graphe non orienté) ou arcs (graphe orienté) reliant les sommets

Types de graphes :
- Non orienté : les arêtes n'ont pas de direction
- Orienté : les arcs ont une direction
- Pondéré : les arêtes/arcs ont un poids

### Vocabulaire

- Degré d'un sommet : nombre d'arêtes incidentes
- Chemin : suite d'arêtes reliant deux sommets
- Cycle : chemin dont les extrémités coïncident
- Graphe connexe : il existe un chemin entre toute paire de sommets

## Représentations informatiques

### Matrice d'adjacence

```python
class GrapheMatrice:
    def __init__(self, n):
        self.n = n  # nombre de sommets
        self.matrice = [[0] * n for _ in range(n)]
    
    def ajouter_arete(self, u, v):
        self.matrice[u][v] = 1
        self.matrice[v][u] = 1  # pour un graphe non orienté
    
    def sont_adjacents(self, u, v):
        return self.matrice[u][v] == 1
```

### Liste d'adjacence

```python
class GrapheListe:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
    
    def ajouter_arete(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # pour un graphe non orienté
    
    def voisins(self, u):
        return self.adj[u]
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
    distances[depart] = 0
    visites = set()
    
    while len(visites) < n:
        # Trouver le sommet non visité le plus proche
        u = min((v for v in range(n) if v not in visites),
                key=lambda x: distances[x])
        
        visites.add(u)
        
        for v, poids in graphe.voisins_ponderes(u):
            if distances[u] + poids < distances[v]:
                distances[v] = distances[u] + poids
    
    return distances
```

### Détection de cycles

```python
def a_cycle(graphe, sommet, visites=None, parent=None):
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            if a_cycle(graphe, voisin, visites, sommet):
                return True
        elif parent != voisin:
            return True
    
    return False
```

## Exercices

### Exercice 1 : Implémentation
Implémentez une classe Graphe avec les deux représentations (matrice et liste) et des méthodes pour :
- Ajouter/supprimer des arêtes
- Calculer le degré d'un sommet
- Vérifier si le graphe est connexe

### Exercice 2 : Parcours
Écrivez un programme qui :
- Crée un graphe à partir d'un fichier
- Effectue un parcours en profondeur
- Effectue un parcours en largeur
- Compare les résultats

### Exercice 3 : Plus court chemin
Implémentez l'algorithme de Dijkstra pour :
- Trouver le plus court chemin entre deux villes
- Afficher le chemin et la distance totale

### Exercice 4 : Applications
Résolvez les problèmes suivants avec des graphes :
- Labyrinthe (chemin de sortie)
- Coloration de carte
- Réseau social (composantes connexes)

## Applications pratiques

- GPS et calcul d'itinéraires
- Réseaux sociaux
- Réseaux de transport
- Internet et routage
- Planification de tâches