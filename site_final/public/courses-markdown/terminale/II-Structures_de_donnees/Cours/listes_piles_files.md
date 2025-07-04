# Listes, Piles et Files

## Introduction

Les **structures de données linéaires** sont des collections d'éléments organisés de manière séquentielle. En terminale NSI, nous approfondissons l'étude de trois structures fondamentales : les listes, les piles et les files. Ces structures constituent la base de nombreux algorithmes et sont essentielles pour comprendre l'organisation des données en informatique.

!!! info "Rappel de première"
    En première, nous avons étudié les listes Python et les tuples. En terminale, nous nous concentrons sur l'**interface** et l'**implémentation** de ces structures de données abstraites.

## Types abstraits de données (TAD)

**Définition :** Un **type abstrait de données** (TAD) est une spécification qui définit :
- Les **données** que peut contenir la structure
- Les **opérations** possibles sur ces données
- Le **comportement** attendu de ces opérations

Un TAD sépare l'**interface** (ce que fait la structure) de l'**implémentation** (comment elle le fait).

### Interface vs Implémentation

- **Interface** : Ensemble des opérations disponibles et leur spécification
- **Implémentation** : Façon concrète de réaliser ces opérations en mémoire

!!! example "Analogie"
    Une voiture a une interface (volant, pédales, levier de vitesse) qui reste la même, mais l'implémentation peut varier (moteur essence, électrique, hybride).

## Les Listes

### Définition et interface

Une **liste** est une structure de données linéaire qui permet de stocker une séquence d'éléments accessibles par leur position (indice).

**Interface d'une liste :**
- `creer_liste()` : créer une liste vide
- `est_vide(liste)` : tester si la liste est vide
- `taille(liste)` : obtenir le nombre d'éléments
- `acceder(liste, i)` : accéder à l'élément d'indice i
- `modifier(liste, i, element)` : modifier l'élément d'indice i
- `inserer(liste, i, element)` : insérer un élément à la position i
- `supprimer(liste, i)` : supprimer l'élément à la position i

### Implémentations possibles

#### 1. Tableau dynamique (comme les listes Python)

```python
class ListeTableau:
    def __init__(self):
        self.elements = []
    
    def est_vide(self):
        return len(self.elements) == 0
    
    def taille(self):
        return len(self.elements)
    
    def acceder(self, i):
        if 0 <= i < len(self.elements):
            return self.elements[i]
        raise IndexError("Indice hors limites")
    
    def modifier(self, i, element):
        if 0 <= i < len(self.elements):
            self.elements[i] = element
        else:
            raise IndexError("Indice hors limites")
    
    def inserer(self, i, element):
        self.elements.insert(i, element)
    
    def supprimer(self, i):
        if 0 <= i < len(self.elements):
            return self.elements.pop(i)
        raise IndexError("Indice hors limites")
```

#### 2. Liste chaînée

```python
class Noeud:
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

class ListeChainee:
    def __init__(self):
        self.tete = None
        self._taille = 0
    
    def est_vide(self):
        return self.tete is None
    
    def taille(self):
        return self._taille
    
    def acceder(self, i):
        if i < 0 or i >= self._taille:
            raise IndexError("Indice hors limites")
        
        noeud_courant = self.tete
        for _ in range(i):
            noeud_courant = noeud_courant.suivant
        return noeud_courant.valeur
    
    def inserer(self, i, element):
        if i < 0 or i > self._taille:
            raise IndexError("Indice hors limites")
        
        nouveau_noeud = Noeud(element)
        
        if i == 0:
            nouveau_noeud.suivant = self.tete
            self.tete = nouveau_noeud
        else:
            noeud_courant = self.tete
            for _ in range(i - 1):
                noeud_courant = noeud_courant.suivant
            nouveau_noeud.suivant = noeud_courant.suivant
            noeud_courant.suivant = nouveau_noeud
        
        self._taille += 1
```

## Les Piles (Stack)

### Définition et principe LIFO

Une **pile** est une structure de données qui suit le principe **LIFO** (Last In, First Out) : le dernier élément ajouté est le premier à être retiré.

!!! example "Analogie"
    Une pile d'assiettes : on ne peut ajouter ou retirer des assiettes que par le dessus.

### Interface d'une pile

- `creer_pile()` : créer une pile vide
- `est_vide(pile)` : tester si la pile est vide
- `empiler(pile, element)` : ajouter un élément au sommet (push)
- `depiler(pile)` : retirer et retourner l'élément du sommet (pop)
- `sommet(pile)` : consulter l'élément du sommet sans le retirer (peek)

### Implémentation avec une liste Python

```python
class Pile:
    def __init__(self):
        self.elements = []
    
    def est_vide(self):
        return len(self.elements) == 0
    
    def empiler(self, element):
        self.elements.append(element)
    
    def depiler(self):
        if self.est_vide():
            raise IndexError("Pile vide")
        return self.elements.pop()
    
    def sommet(self):
        if self.est_vide():
            raise IndexError("Pile vide")
        return self.elements[-1]
    
    def taille(self):
        return len(self.elements)
```

### Applications des piles

1. **Gestion des appels de fonctions** : pile d'exécution
2. **Évaluation d'expressions** : notation polonaise inverse
3. **Parcours en profondeur** dans les graphes
4. **Annulation d'opérations** (Ctrl+Z)
5. **Vérification de parenthésage**

```python
def parentheses_equilibrees(expression):
    """Vérifie si les parenthèses sont équilibrées dans une expression"""
    pile = Pile()
    
    for caractere in expression:
        if caractere in "([{":
            pile.empiler(caractere)
        elif caractere in ")]}":
            if pile.est_vide():
                return False
            ouvrante = pile.depiler()
            if not correspond(ouvrante, caractere):
                return False
    
    return pile.est_vide()

def correspond(ouvrante, fermante):
    """Vérifie si une parenthèse ouvrante correspond à une fermante"""
    couples = {'(': ')', '[': ']', '{': '}'}
    return couples.get(ouvrante) == fermante
```

## Les Files (Queue)

### Définition et principe FIFO

Une **file** est une structure de données qui suit le principe **FIFO** (First In, First Out) : le premier élément ajouté est le premier à être retiré.

!!! example "Analogie"
    Une file d'attente : les personnes sont servies dans l'ordre d'arrivée.

### Interface d'une file

- `creer_file()` : créer une file vide
- `est_vide(file)` : tester si la file est vide
- `enfiler(file, element)` : ajouter un élément à la fin (enqueue)
- `defiler(file)` : retirer et retourner l'élément du début (dequeue)
- `premier(file)` : consulter l'élément du début sans le retirer

### Implémentation avec une liste Python

```python
class File:
    def __init__(self):
        self.elements = []
    
    def est_vide(self):
        return len(self.elements) == 0
    
    def enfiler(self, element):
        self.elements.append(element)
    
    def defiler(self):
        if self.est_vide():
            raise IndexError("File vide")
        return self.elements.pop(0)  # Attention : coût O(n)
    
    def premier(self):
        if self.est_vide():
            raise IndexError("File vide")
        return self.elements[0]
    
    def taille(self):
        return len(self.elements)
```

!!! warning "Complexité"
    L'implémentation ci-dessus a un coût O(n) pour `defiler()` car il faut décaler tous les éléments. Une implémentation plus efficace utiliserait deux indices ou une liste chaînée.

### Implémentation optimisée avec deux indices

```python
class FileOptimisee:
    def __init__(self):
        self.elements = []
        self.debut = 0
    
    def est_vide(self):
        return self.debut >= len(self.elements)
    
    def enfiler(self, element):
        self.elements.append(element)
    
    def defiler(self):
        if self.est_vide():
            raise IndexError("File vide")
        element = self.elements[self.debut]
        self.debut += 1
        
        # Réorganiser périodiquement pour éviter la croissance infinie
        if self.debut > len(self.elements) // 2:
            self.elements = self.elements[self.debut:]
            self.debut = 0
        
        return element
    
    def premier(self):
        if self.est_vide():
            raise IndexError("File vide")
        return self.elements[self.debut]
```

### Applications des files

1. **Gestion des processus** dans les systèmes d'exploitation
2. **Parcours en largeur** dans les graphes
3. **Gestion des requêtes** dans les serveurs web
4. **Simulation de files d'attente**
5. **Algorithmes de planification**

## Comparaison des structures

| Structure | Principe | Ajout | Suppression | Accès |
|-----------|----------|-------|-------------|-------|
| **Liste** | Accès indexé | Partout | Partout | Par indice |
| **Pile** | LIFO | Sommet | Sommet | Sommet uniquement |
| **File** | FIFO | Fin | Début | Début uniquement |

## Complexité temporelle

### Tableau dynamique (liste Python)
- Accès : O(1)
- Insertion/suppression en fin : O(1) amorti
- Insertion/suppression au milieu : O(n)

### Liste chaînée
- Accès : O(n)
- Insertion/suppression en tête : O(1)
- Insertion/suppression au milieu : O(n) pour trouver + O(1) pour modifier

### Pile (avec liste Python)
- Empiler : O(1)
- Dépiler : O(1)
- Consulter le sommet : O(1)

### File (avec liste Python naïve)
- Enfiler : O(1)
- Défiler : O(n)
- Consulter le premier : O(1)

### File (avec implémentation optimisée)
- Enfiler : O(1)
- Défiler : O(1) amorti
- Consulter le premier : O(1)

## Conclusion

Les structures de données linéaires sont fondamentales en informatique. Le choix entre liste, pile ou file dépend du problème à résoudre :

- **Liste** : quand on a besoin d'un accès aléatoire aux éléments
- **Pile** : pour gérer des éléments dans l'ordre inverse d'arrivée
- **File** : pour traiter des éléments dans l'ordre d'arrivée

La compréhension de ces structures et de leurs implémentations est essentielle pour concevoir des algorithmes efficaces et comprendre le fonctionnement des systèmes informatiques.