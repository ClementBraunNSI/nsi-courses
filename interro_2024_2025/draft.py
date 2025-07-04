class Voiture:
    def __init__(self, immatriculation, marque, modele, annee, couleur):
        self.immatriculation = immatriculation
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleur = couleur
        self.est_demarre = False

    def __str__(self):
        return f"Voiture {self.immatriculation} de marque {self.marque} et de modèle {self.modele}."

    def demarrer(self):
        self.est_demarre = True
        print(f"La voiture {self.immatriculation} démarre.")

    def arreter(self):
        self.est_demarre = False
        print(f"La voiture {self.immatriculation} s'arrête.")
    


class Concessionnaire:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.voitures = []

    def __str__(self):
        return f"Concessionnaire {self.nom} à l'adresse {self.adresse}."

    def ajouter_voiture(self, voiture):
        self.voitures.append(voiture)
