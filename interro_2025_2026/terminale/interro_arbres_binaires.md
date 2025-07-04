# Interrogation Terminale NSI - Arbres binaires (25 min)
**Nom :** _________________ **Prénom :** _________________ **Classe :** _______

## Exercice 1 : Questions de cours (5 points)

**1.1** Définir ce qu'est un arbre binaire. Quelle est la différence avec un arbre binaire de recherche ?

**1.2** Pour un arbre binaire de hauteur h :
- Nombre minimum de nœuds : ___________
- Nombre maximum de nœuds : ___________

**1.3** Donner l'ordre de visite des nœuds pour les parcours suivants de l'arbre ci-dessous :

```
       A
      / \
     B   C
    / \   \
   D   E   F
```

- Parcours préfixe : ___________
- Parcours infixe : ___________
- Parcours postfixe : ___________
- Parcours en largeur : ___________

**1.4** Quelle est la complexité de la recherche dans un arbre binaire de recherche équilibré ? Et dans le pire des cas ?

## Exercice 2 : Analyse de code (6 points)

Soit la classe suivante :

```python
class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

def mystere(racine):
    if racine is None:
        return 0
    return 1 + max(mystere(racine.gauche), mystere(racine.droit))
```

**2.1** Que calcule la fonction `mystere` ?

**2.2** Quelle est la complexité temporelle de cette fonction ?

**2.3** Tracer l'exécution de `mystere(racine)` sur l'arbre de l'exercice 1.

## Exercice 3 : Programmation (9 points)

**3.1** Écrire une fonction `compter_noeuds(racine)` qui compte le nombre total de nœuds dans un arbre binaire.

```python
def compter_noeuds(racine):
    """
    Compte le nombre de nœuds dans l'arbre
    """
    # À compléter
```

**3.2** Écrire une fonction `rechercher(racine, valeur)` qui recherche une valeur dans un arbre binaire de recherche.

```python
def rechercher(racine, valeur):
    """
    Recherche une valeur dans un ABR
    Renvoie True si trouvée, False sinon
    """
    # À compléter
```

**3.3** Écrire une fonction `inserer(racine, valeur)` qui insère une nouvelle valeur dans un arbre binaire de recherche.

```python
def inserer(racine, valeur):
    """
    Insère une valeur dans un ABR
    Renvoie la racine de l'arbre modifié
    """
    # À compléter
```

**3.4** Écrire une fonction `parcours_largeur(racine)` qui effectue un parcours en largeur et renvoie la liste des valeurs dans l'ordre de visite.

```python
def parcours_largeur(racine):
    """
    Parcours en largeur d'un arbre binaire
    Renvoie la liste des valeurs
    """
    # À compléter (utiliser une file)
```

**3.5** Bonus : Écrire une fonction `est_equilibre(racine)` qui détermine si un arbre binaire est équilibré (la différence de hauteur entre les sous-arbres gauche et droit de chaque nœud est au plus 1).

```python
def est_equilibre(racine):
    """
    Vérifie si l'arbre est équilibré
    """
    # À compléter

def hauteur(racine):
    """
    Calcule la hauteur d'un arbre
    """
    # À compléter
```