# Interrogation Terminale NSI - Algorithmes de tri (25 min)
**Nom :** _________________ **Prénom :** _________________ **Classe :** _______

## Exercice 1 : Questions de cours (6 points)

**1.1** Donner la complexité temporelle dans le pire des cas pour :
- Tri par sélection : ___________
- Tri par insertion : ___________
- Tri fusion : ___________
- Tri rapide : ___________

**1.2** Quel est l'avantage principal du tri par insertion par rapport au tri par sélection ?

**1.3** Expliquer le principe du paradigme "diviser pour régner" appliqué au tri fusion.

**1.4** Dans quel cas le tri rapide a-t-il une complexité quadratique ? Comment peut-on l'éviter ?

## Exercice 2 : Analyse d'algorithme (6 points)

Soit l'algorithme suivant :

```python
def tri_mystere(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste
```

**2.1** Quel est le nom de cet algorithme de tri ?

**2.2** Tracer l'exécution de cet algorithme sur la liste `[64, 34, 25, 12]`. Montrer l'état de la liste après chaque passage de la boucle externe.

**2.3** Quelle est la complexité temporelle de cet algorithme dans le meilleur et le pire des cas ?

## Exercice 3 : Implémentation (8 points)

**3.1** Implémenter le tri par sélection :

```python
def tri_selection(liste):
    """
    Trie une liste en utilisant l'algorithme de tri par sélection
    """
    # À compléter
```

**3.2** Implémenter la fonction de fusion pour le tri fusion :

```python
def fusionner(gauche, droite):
    """
    Fusionne deux listes triées en une seule liste triée
    """
    # À compléter
```

**3.3** Implémenter le tri rapide :

```python
def tri_rapide(liste, debut=0, fin=None):
    """
    Trie une liste en utilisant l'algorithme de tri rapide
    """
    if fin is None:
        fin = len(liste) - 1
    
    # À compléter

def partitionner(liste, debut, fin):
    """
    Partitionne la liste autour d'un pivot
    Renvoie l'indice final du pivot
    """
    # À compléter
```

**3.4** Bonus : Implémenter une version optimisée du tri rapide qui utilise le tri par insertion pour les petites sous-listes (taille ≤ 10).

```python
def tri_rapide_optimise(liste, debut=0, fin=None):
    """
    Version optimisée du tri rapide
    """
    # À compléter

def tri_insertion_intervalle(liste, debut, fin):
    """
    Tri par insertion sur un intervalle de la liste
    """
    # À compléter
```