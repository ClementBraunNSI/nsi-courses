from Sommet import Sommet
from Face import Face
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Objet3D:

    """
    Représente un objet 3D composé de sommets, de faces et d'un nom.
    """

    def __init__(self):
        """
        Initialise un objet 3D vide.
        """
        self.sommets = []
        self.faces = []
        self.nom = ""
        
    def ajouter_sommet(self, x, y, z):
        """
        Ajoute un sommet à l'objet 3D.
        """
        self.sommets.append(Sommet(x, y, z))
        
    def ajouter_face(self, liste_sommets):
        """
        Ajoute une face à l'objet 3D.
        """
        self.faces.append(Face(liste_sommets))
                    
    def __str__(self):       
        """
        Renvoie une représentation textuelle de l'objet 3D.
        """     
        return str({'nom':self.nom, 'sommets':len(self.sommets), 'faces':len(self.faces)})
    
    def afficher(self):
        """
        Affiche l'objet 3D à l'aide de matplotlib.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        f = []
        for face in self.faces:
            print(face.sommets)
            x = [ (self.sommets[s-1].x, self.sommets[s-1].y, self.sommets[s-1].z) for s in face.sommets]
            f.append(x)
        mesh = Poly3DCollection(f, alpha=0.4, edgecolor='black')
        ax.add_collection3d(mesh)
        plt.show()
        
#############################################################################
# Méthode à modifier de la question 5                                       #
#############################################################################
    def transformer(self, rapport):
        o = Objet3D()
        for sommet in self.sommets:
            o.ajouter_sommet(sommet.x*rapport, sommet.y*rapport, sommet.z*rapport)
        for face in self.faces:
            o.ajouter_face(face.sommets)
        o.nom = self.nom
        return o
        
        
        
    def exporter(self, nom_fichier):
        """
        Exporte l'objet 3D dans un fichier texte au format OBJ.
        """
        with open(nom_fichier, 'w') as file:
            file.write("o " + str(self.nom) + "\n")
            for s in self.sommets :
                file.write("v " + str(s.x) + ' ' + str(s.y) + ' ' + str(s.z) + "\n")
            
            for f in self.faces :
                file.write("f ")
                for p in f.sommets:
                    file.write(str(p) + " ")
                file.write("\n")               

#############################################################################
# Écrire le code de la methode trouver_sommets_adjacents de la question 2   #
#############################################################################
    def trouver_sommets_adjacents(self):
        for som1 in self.sommets:
            for som2 in self.sommets[0:]:
                if som1.est_adjacent(som2):
                    return(som1, som2)
        return None
                    
                    
        

#############################################################################
# Programme votre méthode de la question 2                                  #
#############################################################################
objet = Objet3D()
objet.ajouter_sommet(0, 0, 0)  # s1
objet.ajouter_sommet(1, 0, 0)  # s2 
objet.ajouter_sommet(0, 1, 0)  # s3
objet.ajouter_sommet(0, 0, 1)  # s4
