# Fiche d'Exercices : TP Concessionnaire Automobile


## Objectif

L'objectif de ce TP est de mettre en pratique les concepts de base de la Programmation Orientée Objet (POO) en Python. Vous allez modéliser un système simple de gestion de voitures dans un concessionnaire.

## Exercices d'introduction

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
    *   Repeindre une de vos voitures et l'afficher à nouveau pour vérifier le changement de couleur.

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

---

# Exercices d'application

!!! danger "⚠️ Attention"
      Ces exercices sont indépendants du TP Concessionnaire Automobile et permettent de pratiquer d'autres aspects de la Programmation Orientée Objet.

## 🎯 Exercices d'introduction

1. **Créer une classe `Personne` avec les attributs `nom`, `prenom` et `age`. Ajouter une méthode `se_presenter` qui affiche "Je m'appelle [prenom] [nom] et j'ai [age] ans".** ⭐

??? fox_correction "✅ Correction"

      ```python
      class Personne:
          def __init__(self, nom, prenom, age):
              self.nom = nom
              self.prenom = prenom
              self.age = age
          
          def se_presenter(self):
              print(f"Je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans")
      ```

2. **Créer deux objets de la classe `Personne` et appeler leur méthode `se_presenter`.** ⭐

3. **Ajouter une méthode `est_majeur` à la classe `Personne` qui renvoie `True` si la personne a 18 ans ou plus, et `False` sinon.** ⭐

---

## 🌟 Niveau Facile

!!! fox_exercice "💻 Compte bancaire simple ⭐"
      **Écrire une classe `CompteBancaire` avec les attributs `titulaire` (chaîne de caractères), `solde` (nombre) et les méthodes `deposer(montant)`, `retirer(montant)` et `afficher_solde()`.**  
      *Exemple :*  
      ```python
      compte = CompteBancaire("Jean Dupont", 1000)
      compte.deposer(500)  # Le solde est maintenant de 1500
      compte.retirer(200)  # Le solde est maintenant de 1300
      compte.afficher_solde()  # Affiche "Solde du compte de Jean Dupont : 1300 euros"
      ```


---

!!! fox_exercice "Rectangle et calculs ⭐"
    **Écrire une classe `Rectangle` avec les attributs `longueur` et `largeur` et les méthodes `calculer_aire()`, `calculer_perimetre()` et `est_carre()`.**  
    *Exemple :*
    ```python
    rect = Rectangle(5, 3)
    print(rect.calculer_aire())  # Affiche 15
    print(rect.calculer_perimetre())  # Affiche 16
    print(rect.est_carre())  # Affiche False
    ```

!!! fox_exercice "Livre et bibliothèque ⭐"
    **Écrire une classe `Livre` avec les attributs `titre`, `auteur` et `annee_publication`. Puis créer une classe `Bibliotheque` qui peut stocker des livres et offre des méthodes pour ajouter un livre, afficher tous les livres et rechercher un livre par titre.**  
    *Exemple :*
    ```python
    livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
    livre2 = Livre("1984", "George Orwell", 1949)
    
    biblio = Bibliotheque()
    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)
    biblio.afficher_livres()  # Affiche les informations des deux livres
    livre_trouve = biblio.rechercher_livre("1984")
    print(livre_trouve.auteur)  # Affiche "George Orwell"
    ```

## Niveau Intermédiaire

!!! fox_exercice "Héritage simple ⭐⭐"
    **Créer une classe `Animal` avec les attributs `nom` et `age` et une méthode `faire_bruit()` qui affiche "L'animal fait un bruit". Ensuite, créer deux classes dérivées `Chien` et `Chat` qui héritent d'`Animal` et qui redéfinissent la méthode `faire_bruit()` pour afficher respectivement "Le chien aboie" et "Le chat miaule".**  
    *Exemple :*
    ```python
    animal = Animal("Bestiole", 5)
    animal.faire_bruit()  # Affiche "L'animal fait un bruit"
    
    chien = Chien("Rex", 3)
    chien.faire_bruit()  # Affiche "Le chien aboie"
    
    chat = Chat("Félix", 2)
    chat.faire_bruit()  # Affiche "Le chat miaule"
    ```

---

!!! fox_exercice "Encapsulation et propriétés ⭐⭐"
    **Créer une classe `Etudiant` avec un attribut privé `__notes` (liste) et des méthodes pour ajouter une note, calculer la moyenne et obtenir la note maximale. Utiliser des propriétés pour accéder de manière contrôlée aux attributs privés.**  
    *Exemple :*
    ```python
    etudiant = Etudiant("Jean Dupont")
    etudiant.ajouter_note(15)
    etudiant.ajouter_note(18)
    etudiant.ajouter_note(12)
    print(etudiant.moyenne)  # Utilise la propriété pour calculer et afficher 15.0
    print(etudiant.note_max)  # Utilise la propriété pour trouver et afficher 18
    ```

---

!!! fox_exercice "Forme géométrique et polymorphisme ⭐⭐"
    **Créer une classe abstraite `Forme` avec une méthode abstraite `calculer_aire()`. Ensuite, créer des classes dérivées `Cercle` et `Triangle` qui implémentent cette méthode. Créer une fonction `afficher_aire(forme)` qui prend n'importe quelle forme en paramètre et affiche son aire.**  
    *Exemple :*
    ```python
    cercle = Cercle(5)  # rayon = 5
    triangle = Triangle(4, 3)  # base = 4, hauteur = 3
    
    afficher_aire(cercle)  # Affiche "L'aire du cercle est de 78.54 unités carrées"
    afficher_aire(triangle)  # Affiche "L'aire du triangle est de 6.0 unités carrées"
    ```



## Niveau Difficile

!!! fox_exercice "Système de gestion d'employés ⭐⭐⭐"
    **Créer un système de gestion d'employés avec une classe de base `Employe` et des classes dérivées `Manager`, `Technicien` et `Commercial`. Chaque type d'employé a une méthode différente pour calculer son salaire. Implémenter une classe `Entreprise` qui gère une liste d'employés et peut calculer la masse salariale totale.**  
    *Exemple :*
    ```python
    entreprise = Entreprise("TechCorp")
    
    manager = Manager("Alice Dupont", 5)  # 5 ans d'expérience
    technicien = Technicien("Bob Martin", 35)  # 35 heures par semaine
    commercial = Commercial("Charlie Durand", 50000)  # 50000€ de ventes
    
    entreprise.ajouter_employe(manager)
    entreprise.ajouter_employe(technicien)
    entreprise.ajouter_employe(commercial)
    
    print(f"Masse salariale de {entreprise.nom}: {entreprise.calculer_masse_salariale()}€")
    ```

---

!!! fox_exercice "Jeu de cartes ⭐⭐⭐"
    **Implémenter un système de jeu de cartes avec des classes `Carte`, `Paquet`, et `Joueur`. La classe `Carte` a des attributs `valeur` et `couleur`. La classe `Paquet` contient une liste de cartes et des méthodes pour mélanger et distribuer. La classe `Joueur` a une main de cartes et peut jouer des cartes.**  
    *Exemple :*
    ```python
    paquet = Paquet()  # Crée un paquet standard de 52 cartes
    paquet.melanger()
    
    joueur1 = Joueur("Alice")
    joueur2 = Joueur("Bob")
    
    paquet.distribuer([joueur1, joueur2], 5)  # Distribue 5 cartes à chaque joueur
    
    joueur1.afficher_main()
    carte_jouee = joueur1.jouer_carte(0)  # Joue la première carte de sa main
    print(f"{joueur1.nom} joue {carte_jouee}")
    ```

---

!!! fox_exercice "Système de réservation ⭐⭐⭐"
    **Créer un système de réservation pour un hôtel avec des classes `Client`, `Chambre`, `Reservation` et `Hotel`. Implémenter des fonctionnalités pour vérifier la disponibilité des chambres, effectuer des réservations et calculer le coût total d'un séjour.**  
    *Exemple :*
    ```python
    hotel = Hotel("Grand Hôtel")
    
    # Ajouter des chambres à l'hôtel
    hotel.ajouter_chambre(Chambre(101, "Simple", 80))
    hotel.ajouter_chambre(Chambre(102, "Double", 120))
    hotel.ajouter_chambre(Chambre(103, "Suite", 200))
    
    # Créer un client
    client = Client("Alice Dupont", "alice@example.com")
    
    # Vérifier la disponibilité et faire une réservation
    chambres_disponibles = hotel.verifier_disponibilite("2023-07-01", "2023-07-05")
    if chambres_disponibles:
        reservation = hotel.reserver_chambre(client, 102, "2023-07-01", "2023-07-05")
        print(f"Réservation confirmée: {reservation}")
        print(f"Coût total: {reservation.calculer_cout()}€")
    ```