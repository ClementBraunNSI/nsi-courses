# Programmation Orientée Objet

## Définition

La Programmation Orientée Objet (POO) est un paradigme de programmation qui permet de structurer le code en regroupant les données et les comportements dans des objets. Cette approche facilite la réutilisation du code, sa maintenance et sa compréhension.

!!! Tip
	La POO est particulièrement adaptée pour modéliser des systèmes complexes où les données et les comportements sont étroitement liés.

## Classes et Objets

Une classe est un modèle qui définit :
- Les attributs (données)
- Les méthodes (comportements)

Un objet est une instance d'une classe, c'est-à-dire une réalisation concrète du modèle défini par la classe.

!!! Danger Important
	En Python, la méthode `__init__` est le constructeur de la classe. Elle est appelée automatiquement lors de la création d'un objet.

Exemple de création d'une classe et d'un objet :

```python
class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.vitesse = 0
    
    def accelerer(self, delta):
        self.vitesse += delta

# Création d'un objet
ma_voiture = Voiture("Renault", "Clio")
ma_voiture.accelerer(50)

# Accès aux attributs
print(f"Ma {ma_voiture.marque} {ma_voiture.modele} roule à {ma_voiture.vitesse} km/h")
```

## Encapsulation

L'encapsulation est un concept fondamental de la POO qui permet de :
- Regrouper les données (attributs) et les méthodes qui les manipulent
- Contrôler l'accès aux données
- Protéger les données de modifications non autorisées

!!! Danger Important
	En Python, il existe différentes conventions pour contrôler l'accès aux attributs :
	- Sans préfixe (public) : accessible partout
	- `_attribut` : protégé (ne pas utiliser hors de la classe)
	- `__attribut` : privé (accès impossible hors de la classe)

!!! Tip
	Il est recommandé d'utiliser des getters et setters pour accéder aux attributs privés d'une classe.

```python
class CompteBancaire:
    def __init__(self, solde_initial):
        self.__solde = solde_initial
        self.__operations = []
    
    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self.__operations.append(("dépôt", montant))
            return True
        return False
    
    def retirer(self, montant):
        if montant > 0 and self.__solde >= montant:
            self.__solde -= montant
            self.__operations.append(("retrait", montant))
            return True
        return False
    
    def get_solde(self):
        return self.__solde
    
    def get_operations(self):
        return self.__operations.copy()

# Exemple d'utilisation
compte = CompteBancaire(1000)
compte.deposer(500)  # True
compte.retirer(200)  # True
print(f"Solde actuel : {compte.get_solde()} €")  # 1300 €
print("Opérations :", compte.get_operations())
```

## Héritage

L'héritage est un mécanisme qui permet de créer une nouvelle classe à partir d'une classe existante :
- La nouvelle classe (classe fille) hérite des attributs et méthodes de la classe parent
- On peut ajouter de nouveaux attributs et méthodes
- On peut modifier (redéfinir) les comportements existants

!!! Tip
	L'héritage permet de créer une hiérarchie de classes et de réutiliser du code existant.

!!! Danger Important
	En Python, toutes les méthodes sont virtuelles, c'est-à-dire qu'elles peuvent être redéfinies dans les classes filles.

```python
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def faire_bruit(self):
        pass
    
    def description(self):
        return f"{self.nom} ({self.age} ans)"

class Chat(Animal):
    def __init__(self, nom, age, couleur):
        super().__init__(nom, age)  # Appel du constructeur parent
        self.couleur = couleur
    
    def faire_bruit(self):
        return "Miaou!"
    
    def description(self):
        return f"Chat {self.couleur} : {super().description()}"

class Chien(Animal):
    def __init__(self, nom, age, race):
        super().__init__(nom, age)
        self.race = race
    
    def faire_bruit(self):
        return "Wouf!"
    
    def description(self):
        return f"Chien {self.race} : {super().description()}"

# Exemple d'utilisation
chat = Chat("Felix", 3, "noir")
chien = Chien("Rex", 5, "Berger Allemand")

print(chat.description())  # Chat noir : Felix (3 ans)
print(chien.description())  # Chien Berger Allemand : Rex (5 ans)
```

### Polymorphisme

Le polymorphisme permet d'utiliser des objets de classes différentes de manière uniforme :
- Même interface (mêmes noms de méthodes)
- Comportements différents

```python
animaux = [Chat("Felix"), Chien("Rex")]
for animal in animaux:
    print(animal.faire_bruit())  # Appelle la bonne méthode selon la classe
```

## Exercices

### Exercice 1 : Création d'une classe
Créer une classe `Rectangle` avec :
- Attributs : longueur, largeur
- Méthodes : calcul_perimetre(), calcul_aire()

### Exercice 2 : Héritage
Créer une classe `Carre` qui hérite de `Rectangle`

### Exercice 3 : Encapsulation
Modifier la classe `CompteBancaire` pour :
- Empêcher les retraits qui mettraient le compte à découvert
- Ajouter des frais de gestion mensuels

### Exercice 4 : Polymorphisme
Créer une hiérarchie de classes pour différentes formes géométriques avec une méthode commune `calcul_aire()`


