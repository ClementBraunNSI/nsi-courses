from math import *
from random import *
from donnees_habitats import donnees

zones_connues = donnees

nouveau = {'vegetation': 5, 'proximite_eau': 2, 'densite_urbaine': 4, 'disponibilite_proies': 6}


def distance(habitat_1, habitat_2):
    '''
    Calcule la distance euclidienne entre deux habitats.
    entrée : 
        - habitat_1 : dictionnaire représentant un habitat.
        - habitat_2 : dictionnaire représentant un autre habitat.
    sortie : 
        - float : distance euclidienne entre habitat_1 et habitat_2.
    '''
    d = 0
    for key in habitat_1:
        if key != 'presence_renard':
            d += (habitat_1[...] - ... )** ...
    return ...

def distance_d_un_habitat(habitat, habitats):
    '''
    Calcule la distance euclidienne entre un habitat et chaque habitat de la liste.
    entrée : 
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - list[tuple] : liste de tuples (distance, habitat) où distance est la distance euclidienne entre habitat et chaque habitat de la liste.
    '''
    return [] #modifier le renvoi.

#Si une ligne est soulignée de rouge, ceci est normal, il faut d'abord compléter la fonction distance.
def k_plus_proches(k, habitat, habitats):
    '''
    Calcule les k habitats les plus proches de l'habitat donné.
    entrée : 
        - k : entier représentant le nombre d'habitats à retourner.
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - list[tuple] : liste de tuples (distance, habitat) où distance est la distance euclidienne entre habitat et chaque habitat de la liste.
    '''
    distances = distance_d_un_habitat(habitat, habitats)
    distances.sort(key = lambda x: x[0])
    return distances[:k]

def presence_renard(k, habitat, habitats):
    '''
    Vérifie si l'habitat donné a plus de k/2 voisins avec des renards.
    entrée : 
        - k : entier représentant le nombre d'habitats à considérer.
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - bool : True si l'habitat a plus de k/2 voisins avec des renards, False sinon.
    '''
    voisins = k_plus_proches(k, habitat, habitats)
    n_renards = 0
    for voisin in voisins:
        if voisin[1]['presence_renard'] == True:
            n_renards += 1
    return n_renards > k/2