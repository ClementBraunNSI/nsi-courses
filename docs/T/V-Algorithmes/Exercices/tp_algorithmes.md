# TP Algorithmes avancés

## Objectifs

- Maîtriser la programmation dynamique et les algorithmes gloutons
- Implémenter des algorithmes sur les graphes
- Analyser la complexité et comparer les performances
- Résoudre des problèmes d'optimisation concrets

---

## Partie 1 : Programmation dynamique

### Exercice 1.1 : Plus longue sous-séquence croissante

**Objectif :** Implémenter l'algorithme de recherche de la plus longue sous-séquence strictement croissante.

```python
def plus_longue_sous_sequence_croissante(sequence):
    """
    Trouve la longueur de la plus longue sous-séquence strictement croissante
    
    Args:
        sequence: liste d'entiers
    
    Returns:
        int: longueur de la PLSC
    
    Exemple:
        >>> plus_longue_sous_sequence_croissante([10, 9, 2, 5, 3, 7, 101, 18])
        4  # [2, 3, 7, 18] ou [2, 3, 7, 101]
    """
    # TODO: Implémenter l'algorithme O(n²)
    pass

def plus_longue_sous_sequence_croissante_optimise(sequence):
    """
    Version optimisée en O(n log n) avec recherche binaire
    """
    # TODO: Implémenter la version optimisée
    pass

def reconstruction_plsc(sequence):
    """
    Reconstruit la sous-séquence croissante maximale
    
    Returns:
        tuple: (longueur, sous_sequence)
    """
    # TODO: Implémenter la reconstruction
    pass

# Tests
if __name__ == "__main__":
    sequences_test = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7, 7, 7],
        [1, 3, 6, 7, 9, 4, 10, 5, 6]
    ]
    
    for seq in sequences_test:
        longueur = plus_longue_sous_sequence_croissante(seq)
        print(f"Séquence: {seq}")
        print(f"Longueur PLSC: {longueur}")
        print()
```

### Exercice 1.2 : Problème de découpe de barres

**Objectif :** Maximiser le profit en découpant une barre de longueur donnée.

```python
def decoupe_barre(longueur, prix):
    """
    Trouve le profit maximal en découpant une barre
    
    Args:
        longueur: longueur de la barre
        prix: liste des prix pour chaque longueur (prix[i] = prix pour longueur i+1)
    
    Returns:
        int: profit maximal
    
    Exemple:
        >>> prix = [1, 5, 8, 9, 10, 17, 17, 20]
        >>> decoupe_barre(8, prix)
        22  # Découpe en 2+6 ou 6+2
    """
    # TODO: Implémenter avec programmation dynamique
    pass

def decoupe_barre_avec_solution(longueur, prix):
    """
    Version qui retourne aussi la découpe optimale
    
    Returns:
        tuple: (profit_max, liste_decoupes)
    """
    # TODO: Implémenter avec reconstruction
    pass

# Tests
prix_exemple = [1, 5, 8, 9, 10, 17, 17, 20]
for n in range(1, 9):
    profit = decoupe_barre(n, prix_exemple)
    print(f"Barre de longueur {n}: profit maximal = {profit}")
```

### Exercice 1.3 : Problème de partition équilibrée

**Objectif :** Déterminer si un ensemble peut être partitionné en deux sous-ensembles de somme égale.

```python
def partition_equilibree(ensemble):
    """
    Détermine si l'ensemble peut être partitionné en deux sous-ensembles de somme égale
    
    Args:
        ensemble: liste d'entiers positifs
    
    Returns:
        bool: True si partition possible, False sinon
    
    Exemple:
        >>> partition_equilibree([1, 5, 11, 5])
        True  # {1, 5, 5} et {11}
        >>> partition_equilibree([1, 5, 3])
        False
    """
    # TODO: Implémenter avec programmation dynamique
    pass

def partition_avec_solution(ensemble):
    """
    Version qui retourne les deux partitions si possible
    
    Returns:
        tuple: (bool, partition1, partition2) ou (False, None, None)
    """
    # TODO: Implémenter avec reconstruction
    pass

# Tests
ensembles_test = [
    [1, 5, 11, 5],
    [1, 5, 3],
    [1, 1, 3, 5],
    [2, 3, 4, 6]
]

for ens in ensembles_test:
    resultat = partition_equilibree(ens)
    print(f"Ensemble {ens}: partition possible = {resultat}")
```

---

## Partie 2 : Algorithmes gloutons

### Exercice 2.1 : Problème de sélection d'activités

**Objectif :** Sélectionner le maximum d'activités non-conflictuelles.

```python
def selection_activites(activites):
    """
    Sélectionne le maximum d'activités non-conflictuelles
    
    Args:
        activites: liste de tuples (nom, heure_debut, heure_fin)
    
    Returns:
        list: liste des activités sélectionnées
    
    Exemple:
        >>> activites = [('A', 1, 4), ('B', 3, 5), ('C', 0, 6), ('D', 5, 7)]
        >>> selection_activites(activites)
        [('A', 1, 4), ('D', 5, 7)]
    """
    # TODO: Implémenter l'algorithme glouton
    pass

def selection_activites_poids(activites):
    """
    Version avec poids (maximiser la somme des poids)
    activites: liste de tuples (nom, heure_debut, heure_fin, poids)
    """
    # TODO: Implémenter (attention: plus complexe, peut nécessiter DP)
    pass

# Tests
activites_exemple = [
    ('Cours Math', 8, 10),
    ('Cours Info', 9, 11),
    ('TP Physique', 10, 12),
    ('Cours Anglais', 11, 13),
    ('Sport', 14, 16),
    ('Étude', 15, 17)
]

selection = selection_activites(activites_exemple)
print("Activités sélectionnées:")
for nom, debut, fin in selection:
    print(f"  {nom}: {debut}h-{fin}h")
print(f"Nombre total: {len(selection)}")
```

### Exercice 2.2 : Problème du sac à dos fractionnaire

**Objectif :** Maximiser la valeur dans un sac à dos en autorisant les fractions.

```python
def sac_a_dos_fractionnaire(objets, capacite):
    """
    Résout le problème du sac à dos fractionnaire
    
    Args:
        objets: liste de tuples (nom, poids, valeur)
        capacite: capacité maximale du sac
    
    Returns:
        tuple: (valeur_totale, liste_selections)
        où liste_selections contient (nom, fraction_prise)
    
    Exemple:
        >>> objets = [('A', 10, 60), ('B', 20, 100), ('C', 30, 120)]
        >>> sac_a_dos_fractionnaire(objets, 50)
        (240.0, [('A', 1.0), ('B', 1.0), ('C', 0.667)])
    """
    # TODO: Implémenter l'algorithme glouton
    pass

def comparer_sac_01_vs_fractionnaire(objets, capacite):
    """
    Compare les résultats du sac 0-1 et fractionnaire
    """
    # TODO: Implémenter la comparaison
    pass

# Tests
objets_exemple = [
    ('Ordinateur', 10, 60),
    ('Livre', 20, 100),
    ('Appareil photo', 30, 120)
]

valeur, selections = sac_a_dos_fractionnaire(objets_exemple, 50)
print(f"Valeur maximale: {valeur}")
print("Sélections:")
for nom, fraction in selections:
    if fraction > 0:
        print(f"  {nom}: {fraction:.1%}")
```

### Exercice 2.3 : Algorithme de Huffman

**Objectif :** Construire un code de Huffman optimal pour la compression.

```python
import heapq
from collections import defaultdict, Counter

class NoeudHuffman:
    def __init__(self, caractere=None, frequence=0, gauche=None, droite=None):
        self.caractere = caractere
        self.frequence = frequence
        self.gauche = gauche
        self.droite = droite
    
    def __lt__(self, autre):
        return self.frequence < autre.frequence

def construire_arbre_huffman(texte):
    """
    Construit l'arbre de Huffman pour un texte donné
    
    Args:
        texte: chaîne de caractères
    
    Returns:
        NoeudHuffman: racine de l'arbre de Huffman
    """
    # TODO: Implémenter l'algorithme de Huffman
    pass

def generer_codes_huffman(racine):
    """
    Génère les codes de Huffman à partir de l'arbre
    
    Returns:
        dict: mapping caractère -> code binaire
    """
    # TODO: Implémenter la génération des codes
    pass

def encoder_huffman(texte, codes):
    """
    Encode un texte avec les codes de Huffman
    """
    # TODO: Implémenter l'encodage
    pass

def decoder_huffman(code_binaire, racine):
    """
    Décode un code binaire avec l'arbre de Huffman
    """
    # TODO: Implémenter le décodage
    pass

def analyser_compression(texte):
    """
    Analyse le taux de compression obtenu
    """
    # TODO: Implémenter l'analyse
    pass

# Tests
texte_exemple = "hello world"
print(f"Texte original: '{texte_exemple}'")
print(f"Taille originale: {len(texte_exemple) * 8} bits")

# Construction et analyse
racine = construire_arbre_huffman(texte_exemple)
codes = generer_codes_huffman(racine)
code_encode = encoder_huffman(texte_exemple, codes)
texte_decode = decoder_huffman(code_encode, racine)

print(f"Codes de Huffman: {codes}")
print(f"Texte encodé: {code_encode}")
print(f"Taille compressée: {len(code_encode)} bits")
print(f"Texte décodé: '{texte_decode}'")
print(f"Taux de compression: {len(code_encode) / (len(texte_exemple) * 8):.2%}")
```

---

## Partie 3 : Algorithmes sur les graphes

### Exercice 3.1 : Détection de cycles dans un graphe orienté

**Objectif :** Implémenter la détection de cycles avec DFS et coloration.

```python
from enum import Enum

class Couleur(Enum):
    BLANC = 1  # Non visité
    GRIS = 2   # En cours de visite
    NOIR = 3   # Visite terminée

def detection_cycle_oriente(graphe):
    """
    Détecte un cycle dans un graphe orienté
    
    Returns:
        tuple: (bool, cycle) où cycle est la liste des sommets du cycle
    """
    # TODO: Implémenter avec coloration DFS
    pass

def tri_topologique(graphe):
    """
    Effectue un tri topologique du graphe (si acyclique)
    
    Returns:
        list: ordre topologique ou None si cycle détecté
    """
    # TODO: Implémenter le tri topologique
    pass

def tri_topologique_kahn(graphe):
    """
    Tri topologique avec l'algorithme de Kahn
    """
    # TODO: Implémenter l'algorithme de Kahn
    pass

# Tests
from collections import defaultdict

class GrapheOriente:
    def __init__(self):
        self.adjacence = defaultdict(list)
        self.sommets = set()
    
    def ajouter_arete(self, u, v):
        self.adjacence[u].append(v)
        self.sommets.add(u)
        self.sommets.add(v)

# Graphe acyclique
graphe_acyclique = GrapheOriente()
aretes_acyclique = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
for u, v in aretes_acyclique:
    graphe_acyclique.ajouter_arete(u, v)

# Graphe avec cycle
graphe_cyclique = GrapheOriente()
aretes_cyclique = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'D')]
for u, v in aretes_cyclique:
    graphe_cyclique.ajouter_arete(u, v)

print("Test graphe acyclique:")
cycle_detecte, cycle = detection_cycle_oriente(graphe_acyclique)
print(f"Cycle détecté: {cycle_detecte}")
if not cycle_detecte:
    ordre = tri_topologique(graphe_acyclique)
    print(f"Ordre topologique: {ordre}")

print("\nTest graphe cyclique:")
cycle_detecte, cycle = detection_cycle_oriente(graphe_cyclique)
print(f"Cycle détecté: {cycle_detecte}")
if cycle_detecte:
    print(f"Cycle: {cycle}")
```

### Exercice 3.2 : Algorithme de Bellman-Ford

**Objectif :** Implémenter l'algorithme de Bellman-Ford pour détecter les cycles négatifs.

```python
def bellman_ford(graphe, sommet_depart):
    """
    Algorithme de Bellman-Ford pour les plus courts chemins
    
    Args:
        graphe: graphe avec arêtes pondérées (peut avoir des poids négatifs)
        sommet_depart: sommet de départ
    
    Returns:
        tuple: (distances, predecesseurs, cycle_negatif)
        où cycle_negatif est True s'il y a un cycle de poids négatif
    """
    # TODO: Implémenter Bellman-Ford
    pass

def detecter_cycle_negatif(graphe):
    """
    Détecte s'il existe un cycle de poids négatif dans le graphe
    """
    # TODO: Implémenter la détection
    pass

def plus_courts_chemins_tous_sommets(graphe):
    """
    Calcule les plus courts chemins entre tous les sommets
    Utilise Bellman-Ford depuis chaque sommet
    """
    # TODO: Implémenter
    pass

# Tests
class GraphePondere:
    def __init__(self, oriente=True):
        self.aretes = []  # Liste de (u, v, poids)
        self.sommets = set()
        self.oriente = oriente
    
    def ajouter_arete(self, u, v, poids):
        self.aretes.append((u, v, poids))
        self.sommets.add(u)
        self.sommets.add(v)
        if not self.oriente:
            self.aretes.append((v, u, poids))

# Graphe sans cycle négatif
graphe_normal = GraphePondere()
aretes_normal = [('A', 'B', -1), ('A', 'C', 4), ('B', 'C', 3), 
                ('B', 'D', 2), ('D', 'B', 1), ('D', 'C', 5)]
for u, v, p in aretes_normal:
    graphe_normal.ajouter_arete(u, v, p)

# Graphe avec cycle négatif
graphe_negatif = GraphePondere()
aretes_negatif = [('A', 'B', 1), ('B', 'C', -3), ('C', 'D', 2), ('D', 'B', -1)]
for u, v, p in aretes_negatif:
    graphe_negatif.ajouter_arete(u, v, p)

print("Test Bellman-Ford - Graphe normal:")
distances, predecesseurs, cycle_negatif = bellman_ford(graphe_normal, 'A')
print(f"Cycle négatif détecté: {cycle_negatif}")
if not cycle_negatif:
    for sommet, dist in sorted(distances.items()):
        print(f"  Distance A -> {sommet}: {dist}")

print("\nTest Bellman-Ford - Graphe avec cycle négatif:")
distances, predecesseurs, cycle_negatif = bellman_ford(graphe_negatif, 'A')
print(f"Cycle négatif détecté: {cycle_negatif}")
```

### Exercice 3.3 : Algorithmes d'arbre couvrant minimal

**Objectif :** Implémenter les algorithmes de Kruskal et Prim.

```python
class UnionFind:
    """Structure Union-Find pour l'algorithme de Kruskal"""
    
    def __init__(self, elements):
        # TODO: Initialiser la structure
        pass
    
    def find(self, x):
        """Trouve le représentant de x avec compression de chemin"""
        # TODO: Implémenter
        pass
    
    def union(self, x, y):
        """Unit les ensembles contenant x et y"""
        # TODO: Implémenter
        pass
    
    def connected(self, x, y):
        """Vérifie si x et y sont dans le même ensemble"""
        return self.find(x) == self.find(y)

def kruskal(graphe):
    """
    Algorithme de Kruskal pour l'arbre couvrant minimal
    
    Returns:
        tuple: (poids_total, aretes_acm)
    """
    # TODO: Implémenter Kruskal
    pass

def prim(graphe, sommet_depart):
    """
    Algorithme de Prim pour l'arbre couvrant minimal
    
    Returns:
        tuple: (poids_total, aretes_acm)
    """
    # TODO: Implémenter Prim
    pass

def comparer_acm(graphe):
    """
    Compare les résultats de Kruskal et Prim
    """
    # TODO: Implémenter la comparaison
    pass

# Tests
graphe_acm = GraphePondere(oriente=False)
aretes_acm = [
    ('A', 'B', 4), ('A', 'H', 8), ('B', 'C', 8), ('B', 'H', 11),
    ('C', 'D', 7), ('C', 'F', 4), ('C', 'I', 2), ('D', 'E', 9),
    ('D', 'F', 14), ('E', 'F', 10), ('F', 'G', 2), ('G', 'H', 1),
    ('G', 'I', 6), ('H', 'I', 7)
]

for u, v, p in aretes_acm:
    graphe_acm.ajouter_arete(u, v, p)

print("Arbre couvrant minimal:")
poids_kruskal, aretes_kruskal = kruskal(graphe_acm)
print(f"Kruskal - Poids total: {poids_kruskal}")
print(f"Arêtes: {aretes_kruskal}")

poids_prim, aretes_prim = prim(graphe_acm, 'A')
print(f"\nPrim - Poids total: {poids_prim}")
print(f"Arêtes: {aretes_prim}")
```

---

## Partie 4 : Projet intégrateur

### Exercice 4.1 : Système de navigation GPS

**Objectif :** Créer un système de navigation complet.

```python
class SystemeNavigation:
    """
    Système de navigation GPS avec différents algorithmes
    """
    
    def __init__(self):
        self.graphe_routes = GraphePondere(oriente=False)
        self.points_interet = {}  # nom -> coordonnées
        self.restrictions = {}    # limitations de vitesse, etc.
    
    def charger_carte(self, fichier_routes):
        """
        Charge une carte depuis un fichier
        Format: point1,point2,distance,vitesse_max
        """
        # TODO: Implémenter le chargement
        pass
    
    def ajouter_point_interet(self, nom, coordonnees):
        """
        Ajoute un point d'intérêt
        """
        # TODO: Implémenter
        pass
    
    def plus_court_chemin(self, depart, arrivee, critere='distance'):
        """
        Calcule le plus court chemin selon différents critères
        critere: 'distance', 'temps', 'economie'
        """
        # TODO: Implémenter avec Dijkstra adapté
        pass
    
    def itineraire_multi_points(self, points):
        """
        Calcule un itinéraire passant par plusieurs points
        (problème du voyageur de commerce simplifié)
        """
        # TODO: Implémenter avec heuristiques
        pass
    
    def eviter_embouteillages(self, depart, arrivee, embouteillages):
        """
        Recalcule l'itinéraire en évitant les embouteillages
        """
        # TODO: Implémenter
        pass
    
    def analyser_connectivite(self):
        """
        Analyse la connectivité du réseau routier
        """
        # TODO: Implémenter avec DFS/BFS
        pass

# Tests du système
navigation = SystemeNavigation()

# Simulation d'une petite ville
routes = [
    ('Centre', 'Nord', 5, 50),
    ('Centre', 'Sud', 7, 60),
    ('Centre', 'Est', 4, 40),
    ('Centre', 'Ouest', 6, 50),
    ('Nord', 'Est', 8, 45),
    ('Sud', 'Ouest', 9, 55)
]

for depart, arrivee, distance, vitesse in routes:
    navigation.graphe_routes.ajouter_arete(depart, arrivee, distance)

# Points d'intérêt
navigation.ajouter_point_interet('Hôpital', 'Nord')
navigation.ajouter_point_interet('École', 'Est')
navigation.ajouter_point_interet('Supermarché', 'Sud')

# Tests
print("Plus court chemin Centre -> Nord:")
chemin, distance = navigation.plus_court_chemin('Centre', 'Nord')
print(f"Chemin: {chemin}, Distance: {distance}")

print("\nItinéraire multi-points:")
points_visite = ['Centre', 'Nord', 'Est', 'Sud']
itineraire = navigation.itineraire_multi_points(points_visite)
print(f"Itinéraire: {itineraire}")
```

### Exercice 4.2 : Optimisation de planning

**Objectif :** Créer un système d'optimisation de planning scolaire.

```python
class OptimisateurPlanning:
    """
    Optimisateur de planning scolaire
    """
    
    def __init__(self):
        self.cours = []           # (nom, duree, professeur, salle_requise)
        self.contraintes = []     # Contraintes diverses
        self.salles = []          # Salles disponibles
        self.creneaux = []        # Créneaux horaires
    
    def ajouter_cours(self, nom, duree, professeur, salle_requise=None):
        # TODO: Implémenter
        pass
    
    def ajouter_contrainte(self, type_contrainte, **params):
        """
        Types: 'professeur_indisponible', 'salle_occupee', 'cours_consecutifs'
        """
        # TODO: Implémenter
        pass
    
    def generer_planning_glouton(self):
        """
        Génère un planning avec algorithme glouton
        """
        # TODO: Implémenter
        pass
    
    def optimiser_planning_dp(self):
        """
        Optimise le planning avec programmation dynamique
        """
        # TODO: Implémenter
        pass
    
    def verifier_contraintes(self, planning):
        """
        Vérifie si un planning respecte toutes les contraintes
        """
        # TODO: Implémenter
        pass
    
    def calculer_score_planning(self, planning):
        """
        Calcule un score de qualité pour un planning
        """
        # TODO: Implémenter
        pass

# Tests
optimisateur = OptimisateurPlanning()

# Configuration
optimisateur.salles = ['A101', 'A102', 'B201', 'Labo']
optimisateur.creneaux = ['8h-9h', '9h-10h', '10h-11h', '11h-12h', '14h-15h', '15h-16h']

# Cours
cours_liste = [
    ('Mathématiques', 2, 'Prof_Math', 'A101'),
    ('Informatique', 2, 'Prof_Info', 'Labo'),
    ('Physique', 1, 'Prof_Physique', 'A102'),
    ('Anglais', 1, 'Prof_Anglais', None)
]

for cours in cours_liste:
    optimisateur.ajouter_cours(*cours)

# Contraintes
optimisateur.ajouter_contrainte('professeur_indisponible', 
                               professeur='Prof_Math', 
                               creneaux=['14h-15h'])

print("Génération du planning...")
planning = optimisateur.generer_planning_glouton()
print(f"Planning généré: {planning}")
print(f"Score: {optimisateur.calculer_score_planning(planning)}")
```

---

## Partie 5 : Analyse et comparaison

### Exercice 5.1 : Benchmark des algorithmes

```python
import time
import random
import matplotlib.pyplot as plt

def benchmark_fibonacci(max_n=35):
    """
    Compare les performances des différentes implémentations de Fibonacci
    """
    # TODO: Implémenter le benchmark
    pass

def benchmark_tri(tailles=[100, 500, 1000, 5000]):
    """
    Compare les algorithmes de tri
    """
    # TODO: Implémenter le benchmark
    pass

def benchmark_graphes(nb_sommets_max=1000):
    """
    Compare les algorithmes sur graphes
    """
    # TODO: Implémenter le benchmark
    pass

def analyser_complexite_empirique(algorithme, generateur_donnees, tailles):
    """
    Analyse empirique de la complexité d'un algorithme
    """
    # TODO: Implémenter l'analyse
    pass

# Exécution des benchmarks
if __name__ == "__main__":
    print("Benchmark Fibonacci...")
    benchmark_fibonacci()
    
    print("\nBenchmark Tri...")
    benchmark_tri()
    
    print("\nBenchmark Graphes...")
    benchmark_graphes()
```

---

## Critères d'évaluation

### Fonctionnalité (40%)
- Implémentation correcte des algorithmes
- Gestion des cas particuliers
- Respect des spécifications

### Qualité du code (30%)
- Lisibilité et documentation
- Structure et organisation
- Gestion d'erreurs

### Analyse et optimisation (20%)
- Analyse de complexité
- Optimisations pertinentes
- Comparaisons d'algorithmes

### Innovation et extensions (10%)
- Améliorations proposées
- Fonctionnalités supplémentaires
- Créativité dans les solutions

---

## Ressources

### Documentation
- [Algorithmes de graphes](https://fr.wikipedia.org/wiki/Algorithme_de_graphe)
- [Programmation dynamique](https://fr.wikipedia.org/wiki/Programmation_dynamique)
- [Algorithmes gloutons](https://fr.wikipedia.org/wiki/Algorithme_glouton)

### Outils
- `networkx` : Bibliothèque Python pour les graphes
- `matplotlib` : Visualisation des résultats
- `time` et `cProfile` : Mesure de performances

### Extensions possibles
- Interface graphique pour la visualisation
- Implémentation en C++ pour les performances
- Algorithmes parallèles
- Applications à l'intelligence artificielle

---

## Conseils

1. **Commencez simple** : Implémentez d'abord les versions de base
2. **Testez régulièrement** : Vérifiez chaque fonction avec des exemples
3. **Documentez** : Expliquez vos choix d'implémentation
4. **Optimisez progressivement** : Améliorez après avoir une version fonctionnelle
5. **Visualisez** : Utilisez des graphiques pour comprendre les performances

Bon travail !