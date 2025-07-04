# Interrogation Première NSI - Programmation Orientée Objet (25 min)
**Nom :** _________________ **Prénom :** _________________ **Classe :** _______

## Exercice 1 : Questions de cours (5 points)

**1.1** Définir les termes suivants :
- Classe : ___________
- Objet : ___________
- Attribut : ___________
- Méthode : ___________

**1.2** À quoi sert la méthode `__init__` dans une classe Python ?

**1.3** Quelle est la différence entre un attribut d'instance et un attribut de classe ?

**1.4** Que représente le paramètre `self` dans une méthode de classe ?

## Exercice 2 : Analyse de code (6 points)

Soit la classe suivante :

```python
class Voiture:
    nb_voitures = 0
    
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = 0
        Voiture.nb_voitures += 1
    
    def rouler(self, distance):
        self.kilometrage += distance
    
    def age(self):
        return 2025 - self.annee
    
    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee})"
```

**2.1** Que fait le code suivant ?
```python
voiture1 = Voiture("Toyota", "Corolla", 2020)
voiture2 = Voiture("Honda", "Civic", 2018)
voiture1.rouler(15000)
print(voiture1.age())
print(Voiture.nb_voitures)
```

**2.2** Quelle est la valeur de `voiture1.kilometrage` après l'exécution du code ci-dessus ?

**2.3** Que renvoie `str(voiture2)` ?

## Exercice 3 : Programmation (9 points)

**3.1** Créer une classe `Rectangle` avec :
- Un constructeur qui prend la largeur et la hauteur
- Une méthode `aire()` qui calcule l'aire
- Une méthode `perimetre()` qui calcule le périmètre
- Une méthode `est_carre()` qui renvoie `True` si c'est un carré

```python
class Rectangle:
    # À compléter
    pass

# Exemple d'utilisation
>>> rect = Rectangle(5, 3)
>>> rect.aire()
15
>>> rect.perimetre()
16
>>> rect.est_carre()
False
```

**3.2** Créer une classe `CompteBancaire` avec :
- Un constructeur qui prend le nom du titulaire et le solde initial (0 par défaut)
- Une méthode `deposer(montant)` qui ajoute de l'argent
- Une méthode `retirer(montant)` qui retire de l'argent (si le solde est suffisant)
- Une méthode `consulter_solde()` qui renvoie le solde actuel
- Une méthode `__str__()` qui affiche les informations du compte

```python
class CompteBancaire:
    # À compléter
    pass

# Exemple d'utilisation
>>> compte = CompteBancaire("Alice", 100)
>>> compte.deposer(50)
>>> compte.retirer(30)
>>> compte.consulter_solde()
120
>>> print(compte)
Compte de Alice : 120€
```

**3.3** Créer une classe `Bibliotheque` qui gère une collection de livres :
- Un constructeur qui initialise une liste vide de livres
- Une méthode `ajouter_livre(titre, auteur)` qui ajoute un livre (dictionnaire)
- Une méthode `rechercher_par_auteur(auteur)` qui renvoie tous les livres d'un auteur
- Une méthode `nombre_livres()` qui renvoie le nombre total de livres

```python
class Bibliotheque:
    # À compléter
    pass

# Exemple d'utilisation
>>> biblio = Bibliotheque()
>>> biblio.ajouter_livre("1984", "George Orwell")
>>> biblio.ajouter_livre("Animal Farm", "George Orwell")
>>> biblio.rechercher_par_auteur("George Orwell")
[{'titre': '1984', 'auteur': 'George Orwell'}, 
 {'titre': 'Animal Farm', 'auteur': 'George Orwell'}]
>>> biblio.nombre_livres()
2
```