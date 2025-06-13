# Algorithmes avancés

## Introduction

Ce cours présente des algorithmes avancés essentiels en informatique, couvrant la programmation dynamique, les algorithmes gloutons, et les algorithmes sur les graphes. Ces techniques permettent de résoudre efficacement des problèmes complexes d'optimisation et de recherche.

---

## Programmation dynamique

### Principe général

**Définition :** La programmation dynamique résout des problèmes en les décomposant en sous-problèmes plus simples, en stockant les résultats pour éviter les recalculs.

**Conditions d'application :**
1. **Sous-structure optimale** : La solution optimale contient des solutions optimales aux sous-problèmes
2. **Chevauchement de sous-problèmes** : Les mêmes sous-problèmes apparaissent plusieurs fois

**Approches :**
- **Top-down** (mémoïsation) : Récursion + cache
- **Bottom-up** (tabulaire) : Construction itérative de la solution

### Exemple classique : Suite de Fibonacci

```python
# Approche naïve (exponentielle)
def fibonacci_naif(n):
    if n <= 1:
        return n
    return fibonacci_naif(n-1) + fibonacci_naif(n-2)

# Approche top-down (mémoïsation)
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Approche bottom-up (tabulaire)
def fibonacci_dp(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Optimisation mémoire
def fibonacci_optimise(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Comparaison des performances
import time

def comparer_fibonacci(n):
    print(f"Calcul de Fibonacci({n}):")
    
    # Version naïve (seulement pour petites valeurs)
    if n <= 35:
        start = time.time()
        result_naif = fibonacci_naif(n)
        time_naif = time.time() - start
        print(f"  Naïf: {result_naif} (temps: {time_naif:.4f}s)")
    
    # Version mémoïsation
    start = time.time()
    result_memo = fibonacci_memo(n, {})
    time_memo = time.time() - start
    print(f"  Mémoïsation: {result_memo} (temps: {time_memo:.6f}s)")
    
    # Version tabulaire
    start = time.time()
    result_dp = fibonacci_dp(n)
    time_dp = time.time() - start
    print(f"  Tabulaire: {result_dp} (temps: {time_dp:.6f}s)")
    
    # Version optimisée
    start = time.time()
    result_opt = fibonacci_optimise(n)
    time_opt = time.time() - start
    print(f"  Optimisée: {result_opt} (temps: {time_opt:.6f}s)")

# Test
comparer_fibonacci(30)
```

### Problème du sac à dos 0-1

```python
def sac_a_dos_01(objets, capacite):
    """
    Résout le problème du sac à dos 0-1 avec programmation dynamique
    objets: liste de tuples (poids, valeur)
    capacite: capacité maximale du sac
    """
    n = len(objets)
    
    # dp[i][w] = valeur maximale avec les i premiers objets et capacité w
    dp = [[0 for _ in range(capacite + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        poids, valeur = objets[i-1]
        
        for w in range(capacite + 1):
            # Option 1: ne pas prendre l'objet i
            dp[i][w] = dp[i-1][w]
            
            # Option 2: prendre l'objet i (si possible)
            if poids <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-poids] + valeur)
    
    return dp[n][capacite]

def sac_a_dos_reconstruction(objets, capacite):
    """
    Version qui reconstruit la solution optimale
    """
    n = len(objets)
    dp = [[0 for _ in range(capacite + 1)] for _ in range(n + 1)]
    
    # Remplir la table DP
    for i in range(1, n + 1):
        poids, valeur = objets[i-1]
        for w in range(capacite + 1):
            dp[i][w] = dp[i-1][w]
            if poids <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-poids] + valeur)
    
    # Reconstruction de la solution
    w = capacite
    solution = []
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            solution.append(i-1)  # Indice de l'objet
            w -= objets[i-1][0]   # Réduire la capacité
    
    return dp[n][capacite], solution[::-1]

# Version optimisée en mémoire
def sac_a_dos_optimise(objets, capacite):
    """
    Version avec optimisation mémoire O(capacite)
    """
    dp = [0] * (capacite + 1)
    
    for poids, valeur in objets:
        # Parcourir de droite à gauche pour éviter les conflits
        for w in range(capacite, poids - 1, -1):
            dp[w] = max(dp[w], dp[w - poids] + valeur)
    
    return dp[capacite]

# Test
objets = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (poids, valeur)
capacite = 8

valeur_max = sac_a_dos_01(objets, capacite)
print(f"Valeur maximale: {valeur_max}")

valeur_max, solution = sac_a_dos_reconstruction(objets, capacite)
print(f"Valeur maximale: {valeur_max}")
print(f"Objets sélectionnés: {[objets[i] for i in solution]}")

valeur_opt = sac_a_dos_optimise(objets, capacite)
print(f"Valeur optimisée: {valeur_opt}")
```

### Plus longue sous-séquence commune (LCS)

```python
def lcs_longueur(seq1, seq2):
    """
    Calcule la longueur de la plus longue sous-séquence commune
    """
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def lcs_reconstruction(seq1, seq2):
    """
    Reconstruit la LCS
    """
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Remplir la table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruction
    lcs = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if seq1[i-1] == seq2[j-1]:
            lcs.append(seq1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

# Test
seq1 = "ABCDGH"
seq2 = "AEDFHR"

print(f"Séquence 1: {seq1}")
print(f"Séquence 2: {seq2}")
print(f"Longueur LCS: {lcs_longueur(seq1, seq2)}")
print(f"LCS: {lcs_reconstruction(seq1, seq2)}")
```

### Distance d'édition (Levenshtein)

```python
def distance_edition(mot1, mot2):
    """
    Calcule la distance d'édition entre deux mots
    """
    m, n = len(mot1), len(mot2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialisation
    for i in range(m + 1):
        dp[i][0] = i  # Suppression
    for j in range(n + 1):
        dp[0][j] = j  # Insertion
    
    # Remplissage
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if mot1[i-1] == mot2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # Pas de changement
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Suppression
                    dp[i][j-1],    # Insertion
                    dp[i-1][j-1]   # Substitution
                )
    
    return dp[m][n]

def distance_edition_operations(mot1, mot2):
    """
    Retourne la distance et les opérations nécessaires
    """
    m, n = len(mot1), len(mot2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialisation
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Remplissage
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if mot1[i-1] == mot2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    # Reconstruction des opérations
    operations = []
    i, j = m, n
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and mot1[i-1] == mot2[j-1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + 1:
            operations.append(f"Substituer '{mot1[i-1]}' par '{mot2[j-1]}' à la position {i}")
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            operations.append(f"Supprimer '{mot1[i-1]}' à la position {i}")
            i -= 1
        else:
            operations.append(f"Insérer '{mot2[j-1]}' à la position {i+1}")
            j -= 1
    
    return dp[m][n], operations[::-1]

# Test
mot1 = "kitten"
mot2 = "sitting"

distance = distance_edition(mot1, mot2)
print(f"Distance d'édition entre '{mot1}' et '{mot2}': {distance}")

distance, operations = distance_edition_operations(mot1, mot2)
print(f"Opérations nécessaires:")
for op in operations:
    print(f"  {op}")
```

---

## Algorithmes gloutons

### Principe général

**Définition :** Un algorithme glouton fait toujours le choix localement optimal, en espérant aboutir à un optimum global.

**Propriétés requises :**
1. **Choix glouton** : Un choix localement optimal mène à une solution globalement optimale
2. **Sous-structure optimale** : Une solution optimale contient des solutions optimales aux sous-problèmes

### Problème de rendu de monnaie

```python
def rendu_monnaie_glouton(montant, pieces):
    """
    Algorithme glouton pour le rendu de monnaie
    ATTENTION: Ne fonctionne que pour certains systèmes de pièces
    """
    pieces_triees = sorted(pieces, reverse=True)
    rendu = []
    
    for piece in pieces_triees:
        while montant >= piece:
            rendu.append(piece)
            montant -= piece
    
    return rendu if montant == 0 else None

def rendu_monnaie_dp(montant, pieces):
    """
    Version programmation dynamique (solution optimale garantie)
    """
    dp = [float('inf')] * (montant + 1)
    dp[0] = 0
    parent = [-1] * (montant + 1)
    
    for i in range(1, montant + 1):
        for piece in pieces:
            if piece <= i and dp[i - piece] + 1 < dp[i]:
                dp[i] = dp[i - piece] + 1
                parent[i] = piece
    
    if dp[montant] == float('inf'):
        return None
    
    # Reconstruction
    rendu = []
    m = montant
    while m > 0:
        piece = parent[m]
        rendu.append(piece)
        m -= piece
    
    return rendu

# Test avec différents systèmes
print("Système européen (glouton optimal):")
pieces_euro = [1, 2, 5, 10, 20, 50, 100, 200]
montant = 67
rendu_glouton = rendu_monnaie_glouton(montant, pieces_euro)
rendu_dp = rendu_monnaie_dp(montant, pieces_euro)
print(f"Montant: {montant}")
print(f"Glouton: {rendu_glouton} ({len(rendu_glouton)} pièces)")
print(f"DP: {rendu_dp} ({len(rendu_dp)} pièces)")

print("\nSystème non-optimal pour glouton:")
pieces_special = [1, 3, 4]
montant = 6
rendu_glouton = rendu_monnaie_glouton(montant, pieces_special)
rendu_dp = rendu_monnaie_dp(montant, pieces_special)
print(f"Montant: {montant}")
print(f"Glouton: {rendu_glouton} ({len(rendu_glouton) if rendu_glouton else 'N/A'} pièces)")
print(f"DP: {rendu_dp} ({len(rendu_dp)} pièces)")
```

### Problème de l'ordonnancement

```python
def ordonnancement_glouton(taches):
    """
    Ordonnancement de tâches pour minimiser le temps d'attente moyen
    taches: liste de tuples (nom, duree)
    """
    # Trier par durée croissante (algorithme glouton optimal)
    taches_triees = sorted(taches, key=lambda x: x[1])
    
    temps_actuel = 0
    temps_attente_total = 0
    planning = []
    
    for nom, duree in taches_triees:
        planning.append((nom, temps_actuel, temps_actuel + duree))
        temps_attente_total += temps_actuel
        temps_actuel += duree
    
    temps_attente_moyen = temps_attente_total / len(taches)
    
    return planning, temps_attente_moyen

def ordonnancement_avec_echeances(taches):
    """
    Ordonnancement avec échéances (algorithme de Jackson)
    taches: liste de tuples (nom, duree, echeance)
    """
    # Trier par échéance croissante
    taches_triees = sorted(taches, key=lambda x: x[2])
    
    temps_actuel = 0
    planning = []
    retards = []
    
    for nom, duree, echeance in taches_triees:
        debut = temps_actuel
        fin = temps_actuel + duree
        retard = max(0, fin - echeance)
        
        planning.append((nom, debut, fin, echeance, retard))
        if retard > 0:
            retards.append((nom, retard))
        
        temps_actuel = fin
    
    return planning, retards

# Test
taches = [
    ("Tâche A", 3),
    ("Tâche B", 1),
    ("Tâche C", 4),
    ("Tâche D", 2)
]

planning, temps_moyen = ordonnancement_glouton(taches)
print("Ordonnancement optimal (temps d'attente minimum):")
for nom, debut, fin in planning:
    print(f"  {nom}: {debut} -> {fin}")
print(f"Temps d'attente moyen: {temps_moyen:.2f}")

# Avec échéances
taches_echeances = [
    ("Tâche A", 3, 5),
    ("Tâche B", 1, 2),
    ("Tâche C", 4, 8),
    ("Tâche D", 2, 4)
]

planning, retards = ordonnancement_avec_echeances(taches_echeances)
print("\nOrdonnancement avec échéances:")
for nom, debut, fin, echeance, retard in planning:
    status = f"(retard: {retard})" if retard > 0 else "(à temps)"
    print(f"  {nom}: {debut} -> {fin} (échéance: {echeance}) {status}")
```

### Problème de la couverture d'intervalles

```python
def couverture_intervalles(intervalles):
    """
    Sélectionne le minimum d'intervalles pour couvrir tous les points
    intervalles: liste de tuples (debut, fin)
    """
    if not intervalles:
        return []
    
    # Trier par fin croissante
    intervalles_tries = sorted(intervalles, key=lambda x: x[1])
    
    selection = [intervalles_tries[0]]
    derniere_fin = intervalles_tries[0][1]
    
    for debut, fin in intervalles_tries[1:]:
        if debut > derniere_fin:
            selection.append((debut, fin))
            derniere_fin = fin
    
    return selection

def points_couverts(intervalles):
    """
    Calcule tous les points couverts par une liste d'intervalles
    """
    points = set()
    for debut, fin in intervalles:
        points.update(range(debut, fin + 1))
    return sorted(points)

# Test
intervalles = [(1, 3), (2, 5), (4, 6), (7, 9), (8, 10)]
selection = couverture_intervalles(intervalles)

print(f"Intervalles: {intervalles}")
print(f"Sélection optimale: {selection}")
print(f"Points couverts par tous: {points_couverts(intervalles)}")
print(f"Points couverts par sélection: {points_couverts(selection)}")
```

---

## Algorithmes sur les graphes

### Représentation des graphes

```python
from collections import defaultdict, deque
import heapq

class Graphe:
    """Représentation d'un graphe avec listes d'adjacence"""
    
    def __init__(self, oriente=False):
        self.adjacence = defaultdict(list)
        self.oriente = oriente
        self.sommets = set()
    
    def ajouter_arete(self, u, v, poids=1):
        """Ajoute une arête entre u et v"""
        self.adjacence[u].append((v, poids))
        self.sommets.add(u)
        self.sommets.add(v)
        
        if not self.oriente:
            self.adjacence[v].append((u, poids))
    
    def voisins(self, sommet):
        """Retourne les voisins d'un sommet"""
        return self.adjacence[sommet]
    
    def afficher(self):
        """Affiche le graphe"""
        for sommet in sorted(self.sommets):
            voisins = [f"{v}({p})" for v, p in self.adjacence[sommet]]
            print(f"{sommet}: {', '.join(voisins)}")
```

### Parcours en profondeur (DFS)

```python
def dfs_recursif(graphe, sommet_depart, visite=None):
    """Parcours en profondeur récursif"""
    if visite is None:
        visite = set()
    
    visite.add(sommet_depart)
    parcours = [sommet_depart]
    
    for voisin, _ in graphe.voisins(sommet_depart):
        if voisin not in visite:
            parcours.extend(dfs_recursif(graphe, voisin, visite))
    
    return parcours

def dfs_iteratif(graphe, sommet_depart):
    """Parcours en profondeur itératif"""
    visite = set()
    pile = [sommet_depart]
    parcours = []
    
    while pile:
        sommet = pile.pop()
        
        if sommet not in visite:
            visite.add(sommet)
            parcours.append(sommet)
            
            # Ajouter les voisins à la pile (ordre inverse pour cohérence)
            for voisin, _ in reversed(graphe.voisins(sommet)):
                if voisin not in visite:
                    pile.append(voisin)
    
    return parcours

def composantes_connexes(graphe):
    """Trouve toutes les composantes connexes"""
    visite = set()
    composantes = []
    
    for sommet in graphe.sommets:
        if sommet not in visite:
            composante = dfs_recursif(graphe, sommet, visite)
            composantes.append(composante)
    
    return composantes

def detection_cycle_non_oriente(graphe):
    """Détecte un cycle dans un graphe non orienté"""
    visite = set()
    
    def dfs_cycle(sommet, parent):
        visite.add(sommet)
        
        for voisin, _ in graphe.voisins(sommet):
            if voisin not in visite:
                if dfs_cycle(voisin, sommet):
                    return True
            elif voisin != parent:
                return True  # Cycle détecté
        
        return False
    
    for sommet in graphe.sommets:
        if sommet not in visite:
            if dfs_cycle(sommet, None):
                return True
    
    return False
```

### Parcours en largeur (BFS)

```python
def bfs(graphe, sommet_depart):
    """Parcours en largeur"""
    visite = set([sommet_depart])
    file = deque([sommet_depart])
    parcours = []
    
    while file:
        sommet = file.popleft()
        parcours.append(sommet)
        
        for voisin, _ in graphe.voisins(sommet):
            if voisin not in visite:
                visite.add(voisin)
                file.append(voisin)
    
    return parcours

def plus_court_chemin_bfs(graphe, depart, arrivee):
    """Plus court chemin (nombre d'arêtes) avec BFS"""
    if depart == arrivee:
        return [depart]
    
    visite = set([depart])
    file = deque([(depart, [depart])])
    
    while file:
        sommet, chemin = file.popleft()
        
        for voisin, _ in graphe.voisins(sommet):
            if voisin == arrivee:
                return chemin + [voisin]
            
            if voisin not in visite:
                visite.add(voisin)
                file.append((voisin, chemin + [voisin]))
    
    return None  # Pas de chemin

def distances_bfs(graphe, sommet_depart):
    """Calcule les distances depuis un sommet"""
    distances = {sommet_depart: 0}
    file = deque([sommet_depart])
    
    while file:
        sommet = file.popleft()
        
        for voisin, _ in graphe.voisins(sommet):
            if voisin not in distances:
                distances[voisin] = distances[sommet] + 1
                file.append(voisin)
    
    return distances
```

### Algorithme de Dijkstra

```python
def dijkstra(graphe, sommet_depart):
    """Algorithme de Dijkstra pour les plus courts chemins"""
    distances = {sommet: float('inf') for sommet in graphe.sommets}
    distances[sommet_depart] = 0
    predecesseurs = {}
    
    # File de priorité : (distance, sommet)
    heap = [(0, sommet_depart)]
    visite = set()
    
    while heap:
        dist_courante, sommet = heapq.heappop(heap)
        
        if sommet in visite:
            continue
        
        visite.add(sommet)
        
        for voisin, poids in graphe.voisins(sommet):
            if voisin not in visite:
                nouvelle_distance = dist_courante + poids
                
                if nouvelle_distance < distances[voisin]:
                    distances[voisin] = nouvelle_distance
                    predecesseurs[voisin] = sommet
                    heapq.heappush(heap, (nouvelle_distance, voisin))
    
    return distances, predecesseurs

def reconstruire_chemin(predecesseurs, depart, arrivee):
    """Reconstruit le chemin depuis les prédécesseurs"""
    if arrivee not in predecesseurs and arrivee != depart:
        return None
    
    chemin = []
    sommet = arrivee
    
    while sommet is not None:
        chemin.append(sommet)
        sommet = predecesseurs.get(sommet)
    
    return chemin[::-1]

def dijkstra_chemin(graphe, depart, arrivee):
    """Dijkstra avec reconstruction du chemin"""
    distances, predecesseurs = dijkstra(graphe, depart)
    chemin = reconstruire_chemin(predecesseurs, depart, arrivee)
    distance = distances.get(arrivee, float('inf'))
    
    return chemin, distance
```

### Algorithme de Floyd-Warshall

```python
def floyd_warshall(graphe):
    """Algorithme de Floyd-Warshall pour tous les plus courts chemins"""
    sommets = list(graphe.sommets)
    n = len(sommets)
    
    # Initialisation des matrices
    dist = [[float('inf')] * n for _ in range(n)]
    next_sommet = [[None] * n for _ in range(n)]
    
    # Mapping sommet -> indice
    sommet_to_index = {sommet: i for i, sommet in enumerate(sommets)}
    
    # Distance de chaque sommet à lui-même = 0
    for i in range(n):
        dist[i][i] = 0
    
    # Initialiser avec les arêtes directes
    for sommet in sommets:
        i = sommet_to_index[sommet]
        for voisin, poids in graphe.voisins(sommet):
            j = sommet_to_index[voisin]
            dist[i][j] = poids
            next_sommet[i][j] = voisin
    
    # Algorithme principal
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_sommet[i][j] = next_sommet[i][k]
    
    return dist, next_sommet, sommets, sommet_to_index

def reconstruire_chemin_floyd(next_sommet, sommets, sommet_to_index, depart, arrivee):
    """Reconstruit un chemin avec Floyd-Warshall"""
    i = sommet_to_index[depart]
    j = sommet_to_index[arrivee]
    
    if next_sommet[i][j] is None:
        return None
    
    chemin = [depart]
    while depart != arrivee:
        depart = next_sommet[sommet_to_index[depart]][sommet_to_index[arrivee]]
        chemin.append(depart)
    
    return chemin
```

### Tests des algorithmes sur graphes

```python
# Création d'un graphe de test
graphe = Graphe(oriente=False)
aretes = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'C', 1), ('B', 'D', 5),
    ('C', 'D', 8), ('C', 'E', 10),
    ('D', 'E', 2)
]

for u, v, p in aretes:
    graphe.ajouter_arete(u, v, p)

print("Graphe:")
graphe.afficher()

print("\nParcours DFS depuis A:")
print(dfs_recursif(graphe, 'A'))

print("\nParcours BFS depuis A:")
print(bfs(graphe, 'A'))

print("\nPlus court chemin A -> E (BFS):")
chemin_bfs = plus_court_chemin_bfs(graphe, 'A', 'E')
print(chemin_bfs)

print("\nPlus court chemin A -> E (Dijkstra):")
chemin_dijkstra, distance = dijkstra_chemin(graphe, 'A', 'E')
print(f"Chemin: {chemin_dijkstra}, Distance: {distance}")

print("\nDistances depuis A (Dijkstra):")
distances, _ = dijkstra(graphe, 'A')
for sommet, dist in sorted(distances.items()):
    print(f"  A -> {sommet}: {dist}")

print("\nComposantes connexes:")
composantes = composantes_connexes(graphe)
for i, comp in enumerate(composantes, 1):
    print(f"  Composante {i}: {comp}")

print(f"\nCycle détecté: {detection_cycle_non_oriente(graphe)}")
```

---

## Analyse de complexité

### Complexité des algorithmes étudiés

```python
class AnalyseurComplexite:
    """Analyse la complexité des algorithmes"""
    
    @staticmethod
    def analyser_programmation_dynamique():
        print("Complexité - Programmation Dynamique:")
        print("  Fibonacci naïf: O(2^n) temps, O(n) espace (pile)")
        print("  Fibonacci mémoïsation: O(n) temps, O(n) espace")
        print("  Fibonacci tabulaire: O(n) temps, O(n) espace")
        print("  Fibonacci optimisé: O(n) temps, O(1) espace")
        print("  Sac à dos 0-1: O(n*W) temps, O(n*W) espace")
        print("  LCS: O(m*n) temps, O(m*n) espace")
        print("  Distance d'édition: O(m*n) temps, O(m*n) espace")
    
    @staticmethod
    def analyser_algorithmes_gloutons():
        print("\nComplexité - Algorithmes Gloutons:")
        print("  Rendu monnaie: O(n) temps, O(1) espace")
        print("  Ordonnancement: O(n log n) temps (tri), O(1) espace")
        print("  Couverture intervalles: O(n log n) temps, O(1) espace")
    
    @staticmethod
    def analyser_algorithmes_graphes():
        print("\nComplexité - Algorithmes sur Graphes:")
        print("  DFS: O(V + E) temps, O(V) espace")
        print("  BFS: O(V + E) temps, O(V) espace")
        print("  Dijkstra: O((V + E) log V) temps, O(V) espace")
        print("  Floyd-Warshall: O(V^3) temps, O(V^2) espace")
        print("  où V = nombre de sommets, E = nombre d'arêtes")

# Affichage de l'analyse
analyseur = AnalyseurComplexite()
analyseur.analyser_programmation_dynamique()
analyseur.analyser_algorithmes_gloutons()
analyseur.analyser_algorithmes_graphes()
```

---

## Exercices pratiques

### Exercice 1 : Problème de la sous-séquence croissante maximale

```python
def plus_longue_sous_sequence_croissante(sequence):
    """
    Trouve la longueur de la plus longue sous-séquence strictement croissante
    """
    # À implémenter
    pass

def reconstruction_sous_sequence_croissante(sequence):
    """
    Reconstruit la sous-séquence croissante maximale
    """
    # À implémenter
    pass
```

### Exercice 2 : Problème du voyageur de commerce (approximation)

```python
def tsp_plus_proche_voisin(distances):
    """
    Heuristique du plus proche voisin pour TSP
    """
    # À implémenter
    pass

def tsp_2_opt(distances, circuit_initial):
    """
    Amélioration 2-opt d'un circuit TSP
    """
    # À implémenter
    pass
```

### Exercice 3 : Arbre couvrant minimal

```python
def kruskal(graphe):
    """
    Algorithme de Kruskal pour l'arbre couvrant minimal
    """
    # À implémenter
    pass

def prim(graphe, sommet_depart):
    """
    Algorithme de Prim pour l'arbre couvrant minimal
    """
    # À implémenter
    pass
```

---

## Conclusion

Les algorithmes avancés présentés dans ce cours constituent des outils fondamentaux pour résoudre efficacement des problèmes complexes :

**Programmation dynamique :**
- Technique puissante pour les problèmes d'optimisation
- Évite les recalculs grâce à la mémoïsation
- Applications : bioinformatique, économie, intelligence artificielle

**Algorithmes gloutons :**
- Solutions simples et efficaces pour certains problèmes
- Attention aux conditions d'optimalité
- Applications : ordonnancement, compression, réseaux

**Algorithmes sur graphes :**
- Modélisation de nombreux problèmes réels
- Parcours et recherche de chemins optimaux
- Applications : réseaux, transport, réseaux sociaux

**Importance de l'analyse de complexité :**
- Choix de l'algorithme approprié selon les contraintes
- Optimisation des performances
- Compréhension des limites théoriques

Ces algorithmes forment la base de nombreuses applications modernes en informatique et constituent des outils essentiels pour tout informaticien.