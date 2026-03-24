#Compétences
# 33% prog / 33% compréhension / 18% autonomie / 16% oral

from math import *
from random import *
from donnees_habitats import zones_connues

nouveau = {'vegetation': 5, 'proximite_eau': 2, 'densite_urbaine': 4, 'disponibilite_proies': 6}

def distance(habitat_1:dict, habitat_2:dict)->float:
    d = 0
    for key in habitat_1:
        if key != 'presence_renard':
            d += (habitat_1[key] - habitat_2[key])**2
    return sqrt(d)

def distance_d_un_habitat(habitat:dict, habitats:list )->list  :
    distances = []
    for hab in habitats:
        distances.append((distance(habitat, hab), hab))
    return distances


def k_plus_proches(k:int, habitat:dict, habitats:list )->list  :
    distances = distance_d_un_habitat(habitat, habitats)
    distances.sort(key = lambda x: x[0])
    return distances[:k]

def presence_renard(k:int, habitat:dict, habitats:list )->bool:
    habitats = k_plus_proches(k, habitat, habitats)
    n_renards = 0
    for habitat in habitats:
        if habitat[1]['presence_renard']:
            n_renards += 1
    return n_renards > k/2

print(distance_d_un_habitat(nouveau, zones_connues)[:3])

print(presence_renard(10, nouveau, zones_connues)) #True
print(presence_renard(50, nouveau, zones_connues)) #True
print(presence_renard(100, nouveau, zones_connues)) #False
print(presence_renard(500, nouveau, zones_connues)) #False
print(presence_renard(600, nouveau, zones_connues)) #True
print(presence_renard(800, nouveau, zones_connues)) #False
print(presence_renard(900, nouveau, zones_connues)) #False


#Q3 : On utilise le mauvais élément du tuple (dist au lieu de caractéristique), l'élément 0 correspond à la distance et 
# l'élément 1 correspond à l'habitat (au dict) en lui même 

#Q4 : En regardant avec k = 10 ou k = 50, la présence semble confirmée. En regardant au plus grand jusque 900 la presence ne semble pas
# confirmée hormis pour 600. Cela montre que cette méthode des k plus proches voisins peut être fiable (avec quelques exceptions)
# Mais le renard ne semble pas habiter dans cet habitat précis.