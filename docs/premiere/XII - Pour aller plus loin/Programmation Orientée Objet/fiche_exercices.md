# Fiche d'Exercices : TP Concessionnaire Automobile

## Objectif

L'objectif de ce TP est de mettre en pratique les concepts de base de la Programmation Orientée Objet (POO) en Python. Vous allez modéliser un système simple de gestion de voitures dans un concessionnaire.

## Prérequis

*   Avoir lu la fiche de cours sur l'introduction à la POO.
*   Avoir un environnement Python fonctionnel.

## Partie 1 : La Classe `Voiture` (Rappel et Compléments)

Nous allons réutiliser et compléter la classe `Voiture` vue en cours.

```python
class Voiture:
    def __init__(self, immatriculation, marque, modele, annee, couleur):
        self.immatriculation = immatriculation
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleur = couleur
        self.est_demarre = False

    def __str__(self):
        # TODO 1: Améliorer cette méthode pour qu'elle affiche aussi si la voiture est démarrée ou non.
        # Exemple de retour attendu: "Voiture AA-123-BB de marque Renault et de modèle Clio (Démarrée)"
        # ou "Voiture CC-456-DD de marque Peugeot et de modèle 208 (Arrêtée)"
        return f"Voiture {self.immatriculation} de marque {self.marque} et de modèle {self.modele}."

    def demarrer(self):
        if not self.est_demarre:
            self.est_demarre = True
            print(f"La voiture {self.immatriculation} démarre.")
        else:
            print(f"La voiture {self.immatriculation} est déjà démarrée.")

    def arreter(self):
        if self.est_demarre:
            self.est_demarre = False
            print(f"La voiture {self.immatriculation} s'arrête.")
        else:
            print(f"La voiture {self.immatriculation} est déjà arrêtée.")

    # TODO 2: Ajouter une méthode repeindre(self, nouvelle_couleur)
    # Cette méthode doit changer la couleur de la voiture et afficher un message
    # indiquant l'ancienne et la nouvelle couleur.
    # Exemple: "La voiture AB-123-CD passe de la couleur bleu à rouge."

```

**Exercices sur la classe `Voiture` :**

1.  **Compléter `__str__`** : Modifier la méthode `__str__` pour qu'elle indique également l'état (démarrée ou arrêtée) de la voiture, comme indiqué dans le commentaire `TODO 1`.
2.  **Méthode `repeindre`** : Ajouter une nouvelle méthode `repeindre(self, nouvelle_couleur)` à la classe `Voiture` comme décrit dans le `TODO 2`.
3.  **Tester la classe `Voiture`** :
    *   Créer au moins deux objets `Voiture` différents.
    *   Afficher ces voitures en utilisant `print()`.
    *   Essayer de démarrer une voiture déjà démarrée.
    *   Essayer d'arrêter une voiture déjà arrêtée.
    *   Repeindre une de vos voitures et afficher-la à nouveau pour vérifier le changement de couleur.

## Partie 2 : La Classe `Concessionnaire`

Maintenant, nous allons créer une classe `Concessionnaire` qui pourra gérer un ensemble de voitures.

```python
class Concessionnaire:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.voitures_en_stock = [] # Une liste pour stocker les objets Voiture

    def __str__(self):
        # TODO 3: Améliorer cette méthode pour qu'elle affiche le nom du concessionnaire
        # et le nombre de voitures en stock.
        # Exemple: "Concessionnaire 'SuperAutos' situé à '123 Rue de la Paix' (Stock: 5 voitures)"
        return f"Concessionnaire {self.nom} à l'adresse {self.adresse}."

    def ajouter_voiture(self, voiture):
        # TODO 4: Implémenter cette méthode.
        # Elle doit ajouter l'objet 'voiture' (qui est une instance de la classe Voiture)
        # à la liste self.voitures_en_stock.
        # Afficher un message confirmant l'ajout.
        # Exemple: "La voiture XY-789-ZW a été ajoutée au stock de SuperAutos."
        pass

    def afficher_stock(self):
        # TODO 5: Implémenter cette méthode.
        # Si le stock est vide, afficher "Le stock de [nom du concessionnaire] est actuellement vide."
        # Sinon, afficher "Voici les voitures en stock chez [nom du concessionnaire]:"
        # puis, pour chaque voiture dans self.voitures_en_stock, afficher ses informations
        # en utilisant sa méthode __str__().
        pass

    def rechercher_voiture(self, immatriculation):
        # TODO 6: Implémenter cette méthode.
        # Elle doit parcourir self.voitures_en_stock.
        # Si une voiture avec l'immatriculation donnée est trouvée, la retourner.
        # Sinon, retourner None et afficher "Aucune voiture avec l'immatriculation [immatriculation] trouvée."
        pass

    def vendre_voiture(self, immatriculation):
        # TODO 7: Implémenter cette méthode.
        # 1. Utiliser rechercher_voiture pour trouver la voiture.
        # 2. Si la voiture est trouvée:
        #    a. La retirer de self.voitures_en_stock.
        #    b. Afficher un message: "La voiture [immatriculation] a été vendue par [nom du concessionnaire] !"
        #    c. Retourner l'objet voiture vendu.
        # 3. Si la voiture n'est pas trouvée, afficher un message approprié et ne rien retourner.
        pass

```

**Exercices sur la classe `Concessionnaire` :**

1.  **Compléter `__str__`** (TODO 3) : Modifier la méthode `__str__` de `Concessionnaire`.
2.  **Implémenter `ajouter_voiture`** (TODO 4).
3.  **Implémenter `afficher_stock`** (TODO 5).
4.  **Implémenter `rechercher_voiture`** (TODO 6).
5.  **Implémenter `vendre_voiture`** (TODO 7).

## Partie 3 : Interaction et Scénario Complet

1.  **Créer un Concessionnaire** : Instancier un objet de la classe `Concessionnaire`.
2.  **Créer des Voitures** : Instancier au moins 3 objets `Voiture` différents.
3.  **Ajouter les Voitures au Concessionnaire** : Utiliser la méthode `ajouter_voiture` de votre concessionnaire.
4.  **Afficher le Stock** : Utiliser `afficher_stock`.
5.  **Tester la Recherche** :
    *   Rechercher une voiture existante par son immatriculation et afficher ses informations si elle est trouvée.
    *   Rechercher une voiture non existante.
6.  **Tester la Vente** :
    *   Vender une voiture existante. Afficher le stock après la vente pour vérifier.
    *   Essayer de vendre une voiture déjà vendue ou non existante.
7.  **Interactions supplémentaires** :
    *   Prendre une voiture du stock (par exemple, en la recherchant), démarrer-la, repeigner-la, puis afficher à nouveau le stock du concessionnaire (la voiture dans le stock devrait refléter ces changements si vous avez bien manipulé les objets).

## Pour aller plus loin (Optionnel)

*   Ajouter une méthode `valeur_stock(self)` à `Concessionnaire` qui calcule la valeur totale des voitures en stock (devrer ajouter un attribut `prix` à la classe `Voiture`).
*   Permettre à un concessionnaire d'avoir une liste de voitures d'occasion et une liste de voitures neuves.
*   Ajouter d'autres attributs ou méthodes qui pourraient être utiles pour `Voiture` ou `Concessionnaire`.