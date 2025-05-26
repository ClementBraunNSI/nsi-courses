# Fiche de Cours : Introduction à la Programmation Orientée Objet (POO)

## 1. Qu'est-ce que la Programmation Orientée Objet ?

La Programmation Orientée Objet (POO) est une manière de concevoir et d'écrire des programmes informatiques. Au lieu de penser en termes de fonctions et de procédures, on pense en termes d'**objets**.

Un **objet** est une entité qui possède des **attributs** (des données qui le caractérisent) et des **méthodes** (des actions qu'il peut effectuer).

## 2. Les Classes : Modèles pour les Objets

En POO, on utilise des **classes** pour créer des objets. Une classe est comme un plan ou un moule qui définit comment les objets de ce type seront structurés et comment ils se comporteront.

### Exemple : La classe `Voiture`

Regardons un exemple concret avec une classe `Voiture`. Imaginons que nous voulons représenter des voitures dans notre programme.

```python
class Voiture:
    # C'est le "constructeur". Il est appelé quand on crée un nouvel objet Voiture.
    def __init__(self, immatriculation, marque, modele, annee, couleur):
        # Ce sont les attributs de notre voiture
        self.immatriculation = immatriculation
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleur = couleur
        self.est_demarre = False # Par défaut, une voiture est arrêtée

    # C'est une méthode spéciale qui définit comment l'objet doit être affiché
    # quand on utilise print()
    def __str__(self):
        return f"Voiture {self.immatriculation} de marque {self.marque} et de modèle {self.modele}."

    # Voici une méthode pour démarrer la voiture
    def demarrer(self):
        self.est_demarre = True
        print(f"La voiture {self.immatriculation} démarre.")

    # Et une méthode pour l'arrêter
    def arreter(self):S
        self.est_demarre = False
        print(f"La voiture {self.immatriculation} s'arrête.")
```

**Explications :**

*   **`class Voiture:`** : Définit une nouvelle classe nommée `Voiture`.
*   **`__init__(self, ...)`** : C'est le **constructeur**. Il est appelé automatiquement lorsqu'on crée une nouvelle instance (un nouvel objet) de la classe `Voiture`. Le mot-clé `self` fait référence à l'instance de l'objet qui est en train d'être créé. Les autres paramètres (`immatriculation`, `marque`, etc.) sont les valeurs que l'on fournira pour initialiser les attributs de la voiture.
*   **`self.immatriculation = immatriculation`** : Crée un **attribut** `immatriculation` pour l'objet `self` et lui assigne la valeur passée en paramètre.
*   **`__str__(self)`** : C'est une **méthode spéciale**. Python l'appelle quand on essaie de convertir un objet `Voiture` en chaîne de caractères (par exemple, avec `print(ma_voiture)`).
*   **`demarrer(self)`** et **`arreter(self)`** : Ce sont des **méthodes** que les objets `Voiture` peuvent exécuter. Elles modifient l'attribut `est_demarre` et affichent un message.

## 3. Créer et Utiliser des Objets (Instances)

Une fois la classe définie, on peut créer des **instances** (des objets spécifiques) de cette classe.

```python
# Création d'un objet (une instance) de la classe Voiture
ma_voiture_bleue = Voiture("AB-123-CD", "Renault", "Clio", 2020, "bleu")
une_autre_voiture = Voiture("XY-789-ZW", "Peugeot", "3008", 2022, "gris")

# Accéder aux attributs
print(f"La couleur de ma première voiture est : {ma_voiture_bleue.couleur}") # Affiche: bleu
print(f"L'année de l'autre voiture est : {une_autre_voiture.annee}") # Affiche: 2022

# Utiliser les méthodes
print(ma_voiture_bleue) # Appelle la méthode __str__
ma_voiture_bleue.demarrer() # Affiche: La voiture AB-123-CD démarre.
print(f"Ma voiture bleue est démarrée : {ma_voiture_bleue.est_demarre}") # Affiche: True

une_autre_voiture.arreter() # La méthode arreter n'affiche rien par défaut dans notre exemple, mais modifie self.est_demarre
print(f"L'autre voiture est démarrée : {une_autre_voiture.est_demarre}") # Affiche: False
```

## 4. Pourquoi utiliser la POO ?

*   **Organisation** : La POO aide à structurer le code de manière plus logique, en regroupant les données et les fonctions qui les manipulent.
*   **Réutilisabilité** : Les classes peuvent être réutilisées pour créer de nombreux objets.
*   **Modularité** : Chaque objet est une entité indépendante, ce qui facilite la modification et la maintenance du code.
*   **Abstraction** : On peut utiliser un objet sans avoir besoin de connaître tous les détails de son fonctionnement interne.