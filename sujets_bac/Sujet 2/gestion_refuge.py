import csv
# Le module csv est inclus ici, mais une lecture simple par ligne est aussi possible.

class Renard:
    """
    Classe représentant un renard dans le refuge.
    Attributs : identifiant, nom, poids, date_arrivee.
    À compléter (Question 1)
    """
    def __init__(self, identifiant, nom, poids, date_arrivee):
        '''
        Constructeur de la classe Renard qui permet de créer une instance de Renard
        
        entrée:
            - identifiant : entier représentant l'identifiant unique du renard.
            - nom  : str représentant le nom du renard.
            - poids  : flottant représentant le poids du renard en kg.
            - date_arrivee : str représentant la date d'arrivée du renard au refuge au format 'YYYY-MM-DD'.
        '''
        self.id = identifiant
        self.nom = nom
        self.poids = poids
        self.date_arrivee = date_arrivee

    def __str__(self):
        """
        Méthode d'affichage de la classe Renard.
        sortie : 
            - str : représentation sous forme de chaîne de caractères du renard.
        """

class Refuge:
    """
    Classe représentant le refuge contenant la liste des renards.
    À compléter (Question 2)
    """
    def __init__(self, nom, adresse):
        '''
        Constructeur de la classe Refuge qui permet de créer une instance de Refuge.
        
        entrée:
            - nom : str représentant le nom du refuge.
            - adresse : str représentant l'adresse du refuge.
        '''
        # Q2.a : Compléter le constructeur
        self.nom = ...
        self.adresse = ...
        self.liste_renards = ...
        
    def recueillir(self, un_renard):
        """
        Méthode d'ajout d'un renard au refuge.
        entrée : 
            - un_renard : instance de la classe Renard représentant le renard à ajouter.
        """
        # Q2.b : Compléter la méthode d'ajout
        pass

    def lister_peu_corpulents(self):
        """
        Méthode qui renvoie une liste des Renards dont le poids est < 6.0 kg.
        sortie : 
            - list[Renard] : liste des renards peu corpulents.
        """
        return [renard for renard in self.liste_renards if renard.poids < 6]

    def pourcentage_peu_corpulents(self):
        """
        Méthode qui renvoie le pourcentage des renards peu corpulents.
        sortie : 
            - float : pourcentage des renards peu corpulents.
        """
        return len(self.lister_peu_corpulents()) / len(self.liste_renards) * 100


    def importer_donnees(self, nom_fichier):
        """
        Fonction qui importe les données des renards à partir d'un fichier CSV et les ajoute au refuge.
        entrée : 
            - nom_fichier : str représentant le nom du fichier CSV à importer.
            - refuge : instance de la classe Refuge représentant le refuge où ajouter les renards.
        """
        print(f"Tentative d'importation depuis {nom_fichier}...")
        with open(nom_fichier, 'r', encoding='utf-8') as f:
                lignes = csv.DictReader(f, delimiter=';')
                for ligne in lignes:
                    renard = Renard((ligne['id']), ligne['nom'], (ligne['poids']), ligne['date_arrivee'])
                    self.recueillir(renard)
