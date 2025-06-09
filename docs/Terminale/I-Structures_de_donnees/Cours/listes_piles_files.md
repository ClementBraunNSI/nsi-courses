# Listes, piles et files

## Introduction

Les **structures de données** sont des façons d'organiser et de stocker des données pour permettre un accès et une modification efficaces. En terminale NSI, nous étudions trois structures fondamentales :

- **Listes** : structures séquentielles permettant l'accès par index
- **Piles** (Stack) : structures LIFO (Last In, First Out)
- **Files** (Queue) : structures FIFO (First In, First Out)

## I. Les listes

### 1. Définition et propriétés

Une **liste** est une structure de données séquentielle où chaque élément est accessible par son **index** (position).

**Propriétés principales :**
- Accès direct aux éléments par index
- Taille variable
- Éléments ordonnés
- Possibilité d'insertion/suppression à n'importe quelle position

### 2. Implémentation en Python

#### Listes Python natives

```python
# Création d'une liste
ma_liste = [1, 2, 3, 4, 5]

# Accès par index
print(ma_liste[0])  # Premier élément : 1
print(ma_liste[-1]) # Dernier élément : 5

# Modification
ma_liste[2] = 10    # [1, 2, 10, 4, 5]

# Ajout d'éléments
ma_liste.append(6)      # Ajout à la fin
ma_liste.insert(1, 15)  # Insertion à l'index 1

# Suppression
ma_liste.remove(10)     # Supprime la première occurrence
del ma_liste[0]         # Supprime l'élément à l'index 0
element = ma_liste.pop() # Supprime et retourne le dernier élément
```

#### Implémentation avec une classe

```python
class Liste:
    def __init__(self):
        self.elements = []
    
    def ajouter(self, element):
        """Ajoute un élément à la fin de la liste"""
        self.elements.append(element)
    
    def inserer(self, index, element):
        """Insère un élément à l'index donné"""
        self.elements.insert(index, element)
    
    def supprimer(self, index):
        """Supprime l'élément à l'index donné"""
        if 0 <= index < len(self.elements):
            return self.elements.pop(index)
        raise IndexError("Index hors limites")
    
    def obtenir(self, index):
        """Retourne l'élément à l'index donné"""
        if 0 <= index < len(self.elements):
            return self.elements[index]
        raise IndexError("Index hors limites")
    
    def taille(self):
        """Retourne la taille de la liste"""
        return len(self.elements)
    
    def est_vide(self):
        """Vérifie si la liste est vide"""
        return len(self.elements) == 0
```

### 3. Complexité des opérations

| Opération | Complexité |
|-----------|------------|
| Accès par index | O(1) |
| Insertion en fin | O(1) amortie |
| Insertion au début | O(n) |
| Suppression en fin | O(1) |
| Suppression au début | O(n) |
| Recherche | O(n) |

## II. Les piles (Stack)

### 1. Définition et principe LIFO

Une **pile** est une structure de données qui suit le principe **LIFO** (Last In, First Out) : le dernier élément ajouté est le premier à être retiré.

**Analogie :** Une pile d'assiettes - on ne peut ajouter ou retirer des assiettes que sur le dessus.

### 2. Opérations principales

- **push(element)** : ajouter un élément au sommet
- **pop()** : retirer et retourner l'élément du sommet
- **top()** ou **peek()** : consulter l'élément du sommet sans le retirer
- **is_empty()** : vérifier si la pile est vide
- **size()** : obtenir le nombre d'éléments

### 3. Implémentation en Python

#### Avec une liste Python

```python
class Pile:
    def __init__(self):
        self.elements = []
    
    def push(self, element):
        """Ajoute un élément au sommet de la pile"""
        self.elements.append(element)
    
    def pop(self):
        """Retire et retourne l'élément du sommet"""
        if self.est_vide():
            raise IndexError("Pile vide")
        return self.elements.pop()
    
    def top(self):
        """Retourne l'élément du sommet sans le retirer"""
        if self.est_vide():
            raise IndexError("Pile vide")
        return self.elements[-1]
    
    def est_vide(self):
        """Vérifie si la pile est vide"""
        return len(self.elements) == 0
    
    def taille(self):
        """Retourne la taille de la pile"""
        return len(self.elements)
    
    def __str__(self):
        return f"Pile: {self.elements}"

# Exemple d'utilisation
pile = Pile()
pile.push(1)
pile.push(2)
pile.push(3)
print(pile)  # Pile: [1, 2, 3]
print(pile.pop())  # 3
print(pile.top())  # 2
```

### 4. Applications des piles

#### Vérification de parenthèses équilibrées

```python
def parentheses_equilibrees(expression):
    """Vérifie si les parenthèses sont équilibrées"""
    pile = Pile()
    correspondances = {'(': ')', '[': ']', '{': '}'}
    
    for caractere in expression:
        if caractere in correspondances:  # Parenthèse ouvrante
            pile.push(caractere)
        elif caractere in correspondances.values():  # Parenthèse fermante
            if pile.est_vide():
                return False
            if correspondances[pile.pop()] != caractere:
                return False
    
    return pile.est_vide()

# Tests
print(parentheses_equilibrees("(a + b) * [c - d]"))  # True
print(parentheses_equilibrees("(a + b] * [c - d)"))  # False
```

#### Évaluation d'expressions postfixées

```python
def evaluer_postfixe(expression):
    """Évalue une expression en notation postfixée"""
    pile = Pile()
    operateurs = {'+', '-', '*', '/'}
    
    for token in expression.split():
        if token not in operateurs:
            pile.push(float(token))
        else:
            b = pile.pop()
            a = pile.pop()
            if token == '+':
                pile.push(a + b)
            elif token == '-':
                pile.push(a - b)
            elif token == '*':
                pile.push(a * b)
            elif token == '/':
                pile.push(a / b)
    
    return pile.pop()

# Exemple : "3 4 + 2 *" = (3 + 4) * 2 = 14
print(evaluer_postfixe("3 4 + 2 *"))  # 14.0
```

## III. Les files (Queue)

### 1. Définition et principe FIFO

Une **file** est une structure de données qui suit le principe **FIFO** (First In, First Out) : le premier élément ajouté est le premier à être retiré.

**Analogie :** Une file d'attente - les personnes sont servies dans l'ordre d'arrivée.

### 2. Opérations principales

- **enqueue(element)** : ajouter un élément à la fin de la file
- **dequeue()** : retirer et retourner l'élément du début de la file
- **front()** : consulter l'élément du début sans le retirer
- **is_empty()** : vérifier si la file est vide
- **size()** : obtenir le nombre d'éléments

### 3. Implémentation en Python

#### Implémentation simple avec une liste

```python
class File:
    def __init__(self):
        self.elements = []
    
    def enqueue(self, element):
        """Ajoute un élément à la fin de la file"""
        self.elements.append(element)
    
    def dequeue(self):
        """Retire et retourne l'élément du début de la file"""
        if self.est_vide():
            raise IndexError("File vide")
        return self.elements.pop(0)
    
    def front(self):
        """Retourne l'élément du début sans le retirer"""
        if self.est_vide():
            raise IndexError("File vide")
        return self.elements[0]
    
    def est_vide(self):
        """Vérifie si la file est vide"""
        return len(self.elements) == 0
    
    def taille(self):
        """Retourne la taille de la file"""
        return len(self.elements)
    
    def __str__(self):
        return f"File: {self.elements}"
```

#### Implémentation optimisée avec collections.deque

```python
from collections import deque

class FileOptimisee:
    def __init__(self):
        self.elements = deque()
    
    def enqueue(self, element):
        """Ajoute un élément à la fin de la file"""
        self.elements.append(element)
    
    def dequeue(self):
        """Retire et retourne l'élément du début de la file"""
        if self.est_vide():
            raise IndexError("File vide")
        return self.elements.popleft()
    
    def front(self):
        """Retourne l'élément du début sans le retirer"""
        if self.est_vide():
            raise IndexError("File vide")
        return self.elements[0]
    
    def est_vide(self):
        """Vérifie si la file est vide"""
        return len(self.elements) == 0
    
    def taille(self):
        """Retourne la taille de la file"""
        return len(self.elements)
```

### 4. Applications des files

#### Simulation d'une file d'attente

```python
class FileAttente:
    def __init__(self):
        self.file = File()
        self.numero_ticket = 1
    
    def arriver(self, nom):
        """Une personne arrive et prend un ticket"""
        ticket = self.numero_ticket
        self.file.enqueue((ticket, nom))
        self.numero_ticket += 1
        print(f"{nom} a pris le ticket n°{ticket}")
        return ticket
    
    def servir(self):
        """Sert la prochaine personne dans la file"""
        if not self.file.est_vide():
            ticket, nom = self.file.dequeue()
            print(f"Ticket n°{ticket} - {nom} est servi(e)")
            return ticket, nom
        else:
            print("Aucune personne en attente")
            return None
    
    def prochain(self):
        """Affiche qui sera servi en prochain"""
        if not self.file.est_vide():
            ticket, nom = self.file.front()
            print(f"Prochain : Ticket n°{ticket} - {nom}")
        else:
            print("Aucune personne en attente")

# Simulation
file_attente = FileAttente()
file_attente.arriver("Alice")
file_attente.arriver("Bob")
file_attente.arriver("Charlie")
file_attente.prochain()
file_attente.servir()
file_attente.servir()
```

## IV. Comparaison des structures

| Structure | Principe | Ajout | Suppression | Accès |
|-----------|----------|-------|-------------|-------|
| **Liste** | Accès indexé | Partout | Partout | Par index |
| **Pile** | LIFO | Sommet | Sommet | Sommet uniquement |
| **File** | FIFO | Fin | Début | Début uniquement |

### Complexités temporelles

| Opération | Liste | Pile | File (liste) | File (deque) |
|-----------|-------|------|--------------|-------------|
| Insertion | O(n) | O(1) | O(1) | O(1) |
| Suppression | O(n) | O(1) | O(n) | O(1) |
| Accès | O(1) | O(1) | O(1) | O(1) |

## V. Exercices d'application

### Exercice 1 : Pile d'historique

Implémentez une classe `HistoriqueNavigation` qui utilise une pile pour gérer l'historique de navigation d'un navigateur web.

```python
class HistoriqueNavigation:
    def __init__(self):
        self.historique = Pile()
    
    def visiter_page(self, url):
        """Visite une nouvelle page"""
        self.historique.push(url)
        print(f"Page visitée : {url}")
    
    def page_precedente(self):
        """Retourne à la page précédente"""
        if self.historique.taille() > 1:
            self.historique.pop()  # Retire la page actuelle
            page = self.historique.top()  # Page précédente
            print(f"Retour à : {page}")
            return page
        else:
            print("Aucune page précédente")
            return None
    
    def page_actuelle(self):
        """Retourne la page actuelle"""
        if not self.historique.est_vide():
            return self.historique.top()
        return None
```

### Exercice 2 : File de tâches

Implémentez un système de gestion de tâches avec priorités en utilisant plusieurs files.

```python
class GestionnaireTaches:
    def __init__(self):
        self.taches_haute = File()
        self.taches_normale = File()
        self.taches_basse = File()
    
    def ajouter_tache(self, tache, priorite="normale"):
        """Ajoute une tâche selon sa priorité"""
        if priorite == "haute":
            self.taches_haute.enqueue(tache)
        elif priorite == "basse":
            self.taches_basse.enqueue(tache)
        else:
            self.taches_normale.enqueue(tache)
        print(f"Tâche ajoutée : {tache} (priorité {priorite})")
    
    def executer_tache(self):
        """Exécute la prochaine tâche selon les priorités"""
        if not self.taches_haute.est_vide():
            tache = self.taches_haute.dequeue()
        elif not self.taches_normale.est_vide():
            tache = self.taches_normale.dequeue()
        elif not self.taches_basse.est_vide():
            tache = self.taches_basse.dequeue()
        else:
            print("Aucune tâche à exécuter")
            return None
        
        print(f"Exécution de : {tache}")
        return tache
```

## Conclusion

Les listes, piles et files sont des structures de données fondamentales qui répondent à différents besoins :

- **Listes** : pour un accès flexible aux données
- **Piles** : pour gérer des données selon le principe LIFO
- **Files** : pour gérer des données selon le principe FIFO

Le choix de la structure dépend du problème à résoudre et des opérations les plus fréquentes à effectuer.