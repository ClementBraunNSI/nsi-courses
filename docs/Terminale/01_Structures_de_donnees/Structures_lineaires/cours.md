# Structures de données linéaires

## Listes chaînées

### Concept

Une liste chaînée est une structure de données composée de nœuds reliés entre eux :
- Chaque nœud contient une donnée et une référence vers le nœud suivant
- Le dernier nœud pointe vers None
- L'accès se fait séquentiellement

### Implémentation en Python

```python
class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None

class ListeChainee:
    def __init__(self):
        self.tete = None
    
    def ajouter_debut(self, valeur):
        nouveau = Noeud(valeur)
        nouveau.suivant = self.tete
        self.tete = nouveau
    
    def afficher(self):
        courant = self.tete
        while courant:
            print(courant.valeur, end=' → ')
            courant = courant.suivant
        print('None')
```

## Piles (LIFO - Last In First Out)

### Concept

Une pile est une structure de données qui suit le principe LIFO :
- On empile les éléments au sommet
- On dépile toujours l'élément du sommet
- Analogie : pile d'assiettes

### Opérations principales

- push : ajouter un élément
- pop : retirer et renvoyer l'élément du sommet
- peek/top : consulter l'élément du sommet
- is_empty : vérifier si la pile est vide

### Implémentation en Python

```python
class Pile:
    def __init__(self):
        self.elements = []
    
    def push(self, element):
        self.elements.append(element)
    
    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        raise IndexError("Pile vide")
    
    def peek(self):
        if not self.is_empty():
            return self.elements[-1]
        raise IndexError("Pile vide")
    
    def is_empty(self):
        return len(self.elements) == 0
```

## Files (FIFO - First In First Out)

### Concept

Une file est une structure de données qui suit le principe FIFO :
- On ajoute les éléments à la fin
- On retire les éléments au début
- Analogie : file d'attente

### Opérations principales

- enqueue : ajouter un élément à la fin
- dequeue : retirer et renvoyer l'élément du début
- front : consulter l'élément du début
- is_empty : vérifier si la file est vide

### Implémentation en Python

```python
from collections import deque

class File:
    def __init__(self):
        self.elements = deque()
    
    def enqueue(self, element):
        self.elements.append(element)
    
    def dequeue(self):
        if not self.is_empty():
            return self.elements.popleft()
        raise IndexError("File vide")
    
    def front(self):
        if not self.is_empty():
            return self.elements[0]
        raise IndexError("File vide")
    
    def is_empty(self):
        return len(self.elements) == 0
```

## Exercices

### Exercice 1 : Manipulation de liste chaînée
Implémentez les méthodes suivantes pour la classe ListeChainee :
- ajouter_fin(valeur)
- supprimer(valeur)
- rechercher(valeur)

### Exercice 2 : Applications des piles
Utilisez une pile pour :
- Vérifier si une expression avec parenthèses est bien équilibrée
- Convertir une expression infixe en notation polonaise inverse

### Exercice 3 : Simulation de file d'attente
Créez un programme qui simule une file d'attente de clients dans un magasin :
- Arrivée aléatoire de clients
- Temps de service variable
- Statistiques sur le temps d'attente

### Exercice 4 : Liste chaînée circulaire
Modifiez la classe ListeChainee pour créer une liste chaînée circulaire où le dernier élément pointe vers le premier

## Applications pratiques

### Piles
- Gestion des appels de fonctions
- Évaluation d'expressions
- Algorithmes de backtracking

### Files
- Gestion des processus dans un OS
- Tampons de données
- Algorithmes de parcours en largeur

### Listes chaînées
- Gestion de mémoire dynamique
- Implémentation de structures de données complexes
- Optimisation de certains algorithmes