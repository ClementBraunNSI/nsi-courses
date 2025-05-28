# TP : Implémentation de Piles et Files en Python

## Objectif

Implémenter les structures de données Pile (LIFO) et File (FIFO) en utilisant la Programmation Orientée Objet en Python.

## Partie 1 - La Pile (Stack)

```python
class Pile:
    """
    Classe implémentant une structure de pile (LIFO)
    """
    def __init__(self):
        # À compléter : initialiser la structure de données
        pass

    def empiler(self, element):
        """Ajoute un élément au sommet de la pile"""
        # À compléter
        pass

    def depiler(self):
        """Retire et retourne l'élément du sommet de la pile"""
        # À compléter
        pass

    def est_vide(self):
        """Retourne True si la pile est vide, False sinon"""
        # À compléter
        pass

    def sommet(self):
        """Retourne l'élément du sommet sans le retirer"""
        # À compléter
        pass
```

### Application

```python
def verifier_parentheses(expression):
    """
    Vérifie si une expression parenthésée est valide
    Retourne True si valide, False sinon
    """
    pile = Pile()
    # À compléter
    pass

# Tests
print(verifier_parentheses("((a+b)*(c-d))"))  # Doit afficher True
print(verifier_parentheses("((a+b)*c-d))"))   # Doit afficher False
```

## Partie 2 - La File (Queue)

```python
class File:
    """
    Classe implémentant une structure de file (FIFO)
    """
    def __init__(self):
        # À compléter : initialiser la structure de données
        pass

    def enfiler(self, element):
        """Ajoute un élément à la fin de la file"""
        # À compléter
        pass

    def defiler(self):
        """Retire et retourne l'élément du début de la file"""
        # À compléter
        pass

    def est_vide(self):
        """Retourne True si la file est vide, False sinon"""
        # À compléter
        pass

    def tete(self):
        """Retourne l'élément du début sans le retirer"""
        # À compléter
        pass
```

### Application

```python
def simuler_file_attente():
    """
    Simule une file d'attente avec priorité
    """
    file_normale = File()
    file_prioritaire = File()
    # À compléter
    pass

# Tests
simuler_file_attente()
```
