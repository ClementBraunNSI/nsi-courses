from Objet3D import Objet3D

#############################################################################
# Variable et fonction fournies pour la question 3                          #
#############################################################################
parametres_imprimante = {'remplissage' : 20, 'vitesse_extrusion' : 8}   #8mm3 / seconde

def volume_cube(cube):
    a, b = cube.sommets_adjacents() 
    taille_cote = a.distance(b)
    return taille_cote ** 3

def estimation_impression(elt_3D, parametres_imprimante):
    return ((volume_cube(elt_3D)*parametres_imprimante['remplissage']/100)/parametres_imprimante['vitesse_extrusion'])/60


#############################################################################
# Écrire le code de la methode estimation_impression de la question 3       #
#############################################################################

#############################################################################
# Programme à modifier de la question 4 et 5                                #
#############################################################################
objet = Objet3D()
objet.ajouter_sommet(0, 0, 0)
objet.ajouter_sommet(0, 1, 0)
objet.ajouter_sommet(1, 1, 0)
objet.ajouter_sommet(1, 0, 0)
objet.ajouter_sommet(0.5,0.5,1)
objet.ajouter_face([1, 2, 3, 4])
objet.ajouter_face([1,2,5])
objet.ajouter_face([2,3,5])
objet.ajouter_face([3,4,5])
objet.ajouter_face([1,4,5])



#objet.afficher()

nouv_obj = objet.transformer(2)
nouv_obj.afficher()