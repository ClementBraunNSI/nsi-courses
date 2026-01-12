# Compétences
# Programmation 30% / Compréhension 35% / Autonomie 20% / Oral 15%

import csv
# Le module csv est inclus ici, mais une lecture simple par ligne est aussi possible.

class Renard:
    def __init__(self, identifiant:int, nom:str, poids:float, date_arrivee:str)-> None:
        # Q1.a : Compléter le constructeur
        self.id = identifiant
        self.nom = nom
        self.poids = poids
        self.date_arrivee = date_arrivee

    def __str__(self)->str:
        return f"Renard {self.id} ({self.nom}) : poids {self.poids} kg, arrivé le {self.date_arrivee}"

class Refuge:
    def __init__(self, nom:str, adresse:str)->None:
        # Q2.a : Compléter le constructeur
        self.nom = nom
        self.adresse = adresse
        self.renards = []

    def __repr__(self)->str:
        return f"Refuge {self.nom} ({self.adresse}) : {len(self.renards)} renards"
        
    def recueillir(self, un_renard:Renard)->None:
        self.renards.append(un_renard)

    def lister_sous_poids(self)->list[Renard]:
        liste = []
        for renard in self.renards :
            if renard.poids < 6.0 :
                liste.append(renard)
        return liste

    def pourcentage_sous_poids(self)->float:
        compteur = 0
        for renard in self.renards :
            if renard.poids < 6.0 :
                compteur += 1
        return compteur / len(self.renards) * 100


def importer_donnees(nom_fichier:str, refuge:Refuge)->None:
    print(f"Tentative d'importation depuis {nom_fichier}...")
    with open(nom_fichier, 'r', encoding='utf-8') as f:
            lignes = csv.DictReader(f, delimiter=';')
            for ligne in lignes:
                renard = Renard(int(ligne['id']), ligne['nom'], float(ligne['poids']), ligne['date_arrivee'])
                refuge.recueillir(renard)

oscar = Renard(200, "Oscar", 5.1, "2023-01-01")
refuge = Refuge('SOS Goupil', '123 Rue des Renards 98412 Archipal Crozet')
refuge.recueillir(oscar)
importer_donnees('donnees_renards.csv', refuge)
for renard in refuge.renards :
    print(renard)
print(refuge.pourcentage_sous_poids())


# Q3.a 