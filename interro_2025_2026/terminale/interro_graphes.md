# Interrogation Terminale NSI - Graphes (25 min)
**Nom :** _________________ **Prénom :** _________________ **Classe :** _______

## Exercice 1 : Questions de cours (6 points)

**1.1** Définir :
- Graphe orienté : ___________
- Graphe non orienté : ___________
- Degré d'un sommet : ___________
- Chemin : ___________

**1.2** Donner deux façons de représenter un graphe en informatique et leurs avantages respectifs.

**1.3** Quelle est la complexité temporelle du parcours en profondeur et du parcours en largeur pour un graphe avec V sommets et E arêtes ?

**1.4** Dans quel cas utilise-t-on l'algorithme de Dijkstra ? Quelle est sa limitation principale ?

## Exercice 2 : Analyse de graphe (5 points)

Soit le graphe suivant :

```
    A ----5---- B
    |\          |
    | \         |
   3|  \2       |4
    |   \       |
    |    \      |
    C ----1---- D
         6
```

**2.1** Ce graphe est-il orienté ? Justifier.

**2.2** Donner le degré de chaque sommet.

**2.3** Représenter ce graphe sous forme de matrice d'adjacence.

**2.4** Représenter ce graphe sous forme de liste d'adjacence.

**2.5** Appliquer l'algorithme de Dijkstra pour trouver le plus court chemin de A vers D. Détailler les étapes.

## Exercice 3 : Programmation (9 points)

**3.1** Implémenter un parcours en profondeur :

```python
def parcours_profondeur(graphe, sommet_depart, visites=None):
    """
    Parcours en profondeur d'un graphe
    graphe : dictionnaire d'adjacence
    sommet_depart : sommet de départ
    visites : ensemble des sommets déjà visités
    Renvoie : liste des sommets dans l'ordre de visite
    """
    # À compléter
```

**3.2** Implémenter un parcours en largeur :

```python
def parcours_largeur(graphe, sommet_depart):
    """
    Parcours en largeur d'un graphe
    Renvoie : liste des sommets dans l'ordre de visite
    """
    # À compléter (utiliser une file)
```

**3.3** Implémenter une fonction de détection de cycle :

```python
def detecter_cycle(graphe):
    """
    Détecte s'il existe un cycle dans un graphe non orienté
    Renvoie : True s'il y a un cycle, False sinon
    """
    # À compléter
```

**3.4** Implémenter l'algorithme de Dijkstra :

```python
def dijkstra(graphe, depart):
    """
    Algorithme de Dijkstra pour les plus courts chemins
    graphe : dictionnaire {sommet: [(voisin, poids), ...]}
    depart : sommet de départ
    Renvoie : dictionnaire {sommet: distance_minimale}
    """
    # À compléter
```

**3.5** Bonus : Implémenter une fonction qui trouve le chemin le plus court entre deux sommets en utilisant Dijkstra :

```python
def chemin_plus_court(graphe, depart, arrivee):
    """
    Trouve le chemin le plus court entre deux sommets
    Renvoie : (distance, chemin) ou (float('inf'), []) si pas de chemin
    """
    # À compléter
```

## Exercice 4 : Application (Bonus)

Un réseau social peut être modélisé comme un graphe où les sommets représentent les utilisateurs et les arêtes représentent les relations d'amitié.

**4.1** Écrire une fonction `amis_communs(graphe, utilisateur1, utilisateur2)` qui renvoie la liste des amis communs entre deux utilisateurs.

**4.2** Écrire une fonction `degre_separation(graphe, utilisateur1, utilisateur2)` qui calcule le degré de séparation entre deux utilisateurs (nombre minimum d'intermédiaires).

```python
# Exemple de graphe de réseau social
reseau = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'David', 'Eve'],
    'Charlie': ['Alice', 'Frank'],
    'David': ['Bob'],
    'Eve': ['Bob', 'Frank'],
    'Frank': ['Charlie', 'Eve']
}

# Utilisation
>>> amis_communs(reseau, 'Alice', 'Eve')
['Bob']
>>> degre_separation(reseau, 'Alice', 'Frank')
2  # Alice -> Charlie -> Frank
```