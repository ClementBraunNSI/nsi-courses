# Fiche d'exercices : La Programmation Orientée Objet en Python

## Gestion d'une bibliothèque

Nous allons créer un système de gestion de bibliothèque en utilisant la POO.

!!! fox_exercice "Création de la classe Livre"
    Créer une classe `Livre` avec :
    - Des attributs : titre, auteur, année, disponible (booléen)
    - Une méthode `__init__` pour initialiser ces attributs
    - Une méthode `afficher_infos()` qui renvoie une chaîne formatée avec les informations du livre
    - Des méthodes `emprunter()` et `rendre()` qui modifient l'état de disponibilité

??? fox_correction "Correction"
    ```python
    class Livre:
        def __init__(self, titre, auteur, annee):
            self.titre = titre
            self.auteur = auteur
            self.annee = annee
            self.disponible = True
        
        def afficher_infos(self):
            statut = "disponible" if self.disponible else "emprunté"
            return f"{self.titre} par {self.auteur} ({self.annee}) - {statut}"
        
        def emprunter(self):
            if self.disponible:
                self.disponible = False
                return True
            return False
        
        def rendre(self):
            if not self.disponible:
                self.disponible = True
                return True
            return False
    ```

!!! fox_exercice "Création de la classe Bibliothèque"
    Créer une classe `Bibliotheque` qui gère une collection de livres :
    - Un attribut privé `__livres` (liste de livres)
    - Des méthodes pour ajouter et retirer des livres
    - Une méthode pour afficher tous les livres
    - Une méthode pour rechercher des livres par auteur

??? fox_correction "Correction"
    ```python
    class Bibliotheque:
        def __init__(self):
            self.__livres = []
        
        def ajouter_livre(self, livre):
            self.__livres.append(livre)
        
        def retirer_livre(self, titre):
            for livre in self.__livres:
                if livre.titre == titre:
                    self.__livres.remove(livre)
                    return True
            return False
        
        def afficher_livres(self):
            for livre in self.__livres:
                print(livre.afficher_infos())
        
        def rechercher_par_auteur(self, auteur):
            return [livre for livre in self.__livres if livre.auteur == auteur]
    ```

## Système de gestion d'école

!!! fox_exercice "Création de la classe Personne"
    Créer une classe de base `Personne` avec :
    - Attributs : nom, prénom, age
    - Une méthode `se_presenter()` qui renvoie une présentation de la personne

??? fox_correction "Correction"
    ```python
    class Personne:
        def __init__(self, nom, prenom, age):
            self.nom = nom
            self.prenom = prenom
            self.age = age
        
        def se_presenter(self):
            return f"Je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans."
    ```

!!! fox_exercice "Héritage : Élève et Professeur"
    Créer deux classes `Eleve` et `Professeur` qui héritent de `Personne` :
    - Pour `Eleve` : ajouter un attribut `classe` et une liste de `notes`
    - Pour `Professeur` : ajouter un attribut `matiere` et une liste de `classes`
    - Redéfinir la méthode `se_presenter()` pour chaque classe

??? fox_correction "Correction"
    ```python
    class Eleve(Personne):
        def __init__(self, nom, prenom, age, classe):
            super().__init__(nom, prenom, age)
            self.classe = classe
            self.notes = []
        
        def ajouter_note(self, note):
            self.notes.append(note)
        
        def calculer_moyenne(self):
            return sum(self.notes) / len(self.notes) if self.notes else 0
        
        def se_presenter(self):
            return f"{super().se_presenter()} Je suis en {self.classe}."

    class Professeur(Personne):
        def __init__(self, nom, prenom, age, matiere):
            super().__init__(nom, prenom, age)
            self.matiere = matiere
            self.classes = []
        
        def ajouter_classe(self, classe):
            self.classes.append(classe)
        
        def se_presenter(self):
            return f"{super().se_presenter()} J'enseigne {self.matiere}."
    ```

## Jeu de cartes

!!! fox_exercice "Création des classes Carte et Paquet"
    Créer un système de jeu de cartes avec :
    1. Une classe `Carte` :
       - Attributs : valeur, couleur
       - Méthode pour afficher la carte
    2. Une classe `Paquet` :
       - Une liste privée de cartes
       - Méthodes pour mélanger et tirer une carte

??? fox_correction "Correction"
    ```python
    import random

    class Carte:
        def __init__(self, valeur, couleur):
            self.valeur = valeur
            self.couleur = couleur
        
        def afficher(self):
            return f"{self.valeur} de {self.couleur}"

    class Paquet:
        def __init__(self):
            self.__cartes = []
            couleurs = ['Cœur', 'Carreau', 'Pique', 'Trèfle']
            valeurs = ['As'] + [str(i) for i in range(2, 11)] + ['Valet', 'Dame', 'Roi']
            
            for couleur in couleurs:
                for valeur in valeurs:
                    self.__cartes.append(Carte(valeur, couleur))
        
        def melanger(self):
            random.shuffle(self.__cartes)
        
        def tirer_carte(self):
            if len(self.__cartes) > 0:
                return self.__cartes.pop()
            return None
        
        def nombre_cartes(self):
            return len(self.__cartes)
    ```

!!! fox_exercice "Création d'un jeu de bataille"
    Utiliser les classes précédentes pour créer une classe `JeuBataille` qui :
    - Distribue les cartes à deux joueurs
    - Implémente une méthode `jouer_tour()` qui compare les cartes
    - Garde le score de chaque joueur

??? fox_correction "Correction"
    ```python
    class JeuBataille:
        def __init__(self):
            self.paquet = Paquet()
            self.paquet.melanger()
            self.cartes_j1 = []
            self.cartes_j2 = []
            self.score_j1 = 0
            self.score_j2 = 0
            
            # Distribution des cartes
            while self.paquet.nombre_cartes() >= 2:
                self.cartes_j1.append(self.paquet.tirer_carte())
                self.cartes_j2.append(self.paquet.tirer_carte())
        
        def valeur_carte(self, carte):
            valeurs = {'As': 14, 'Roi': 13, 'Dame': 12, 'Valet': 11}
            return valeurs.get(carte.valeur, int(carte.valeur))
        
        def jouer_tour(self):
            if not self.cartes_j1 or not self.cartes_j2:
                return "Partie terminée"
            
            carte1 = self.cartes_j1.pop()
            carte2 = self.cartes_j2.pop()
            
            val1 = self.valeur_carte(carte1)
            val2 = self.valeur_carte(carte2)
            
            if val1 > val2:
                self.score_j1 += 1
                return f"Joueur 1 gagne avec {carte1.afficher()} contre {carte2.afficher()}"
            elif val2 > val1:
                self.score_j2 += 1
                return f"Joueur 2 gagne avec {carte2.afficher()} contre {carte1.afficher()}"
            else:
                return f"Égalité avec {carte1.afficher()} et {carte2.afficher()}"
    ```

## Formes géométriques

!!! fox_exercice "Hiérarchie de formes"
    Créer une hiérarchie de classes pour représenter différentes formes géométriques :
    1. Une classe abstraite `Forme` avec une méthode `aire()`
    2. Des classes `Cercle`, `Rectangle`, et `Triangle` qui héritent de `Forme`
    3. Implémenter le calcul d'aire pour chaque forme
    4. Ajouter une méthode `perimetre()` pour chaque forme

??? fox_correction "Correction"
    ```python
    from math import pi, sqrt

    class Forme:
        def aire(self):
            pass
        
        def perimetre(self):
            pass

    class Cercle(Forme):
        def __init__(self, rayon):
            self.rayon = rayon
        
        def aire(self):
            return pi * self.rayon ** 2
        
        def perimetre(self):
            return 2 * pi * self.rayon

    class Rectangle(Forme):
        def __init__(self, longueur, largeur):
            self.longueur = longueur
            self.largeur = largeur
        
        def aire(self):
            return self.longueur * self.largeur
        
        def perimetre(self):
            return 2 * (self.longueur + self.largeur)

    class Triangle(Forme):
        def __init__(self, a, b, c):
            self.a = a  # côtés du triangle
            self.b = b
            self.c = c
        
        def perimetre(self):
            return self.a + self.b + self.c
        
        def aire(self):
            # Formule de Héron
            p = self.perimetre() / 2
            return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    ```

!!! fox_exercice "Utilisation du polymorphisme"
    Créer une fonction `afficher_infos_formes` qui prend une liste de formes en paramètre et affiche pour chaque forme :
    - Son type
    - Son aire
    - Son périmètre

??? fox_correction "Correction"
    ```python
    def afficher_infos_formes(formes):
        for forme in formes:
            nom_classe = forme.__class__.__name__
            aire = forme.aire()
            perimetre = forme.perimetre()
            print(f"Forme : {nom_classe}")
            print(f"Aire : {aire:.2f}")
            print(f"Périmètre : {perimetre:.2f}\n")

    # Exemple d'utilisation
    formes = [
        Cercle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5)
    ]
    afficher_infos_formes(formes)
    ```