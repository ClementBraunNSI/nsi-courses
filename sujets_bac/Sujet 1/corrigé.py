#Compétences
# 33% prog / 33% compréhension / 18% autonomie / 16% oral

from math import *
from random import *
from donnees_habitats import donnees

zones_connues = donnees

nouveau = {'vegetation': 5, 'proximite_eau': 2, 'densite_urbaine': 4, 'disponibilite_proies': 6}

def distance(habitat_1:dict, habitat_2:dict)->float:
    d = 0
    for key in habitat_1:
        if key != 'presence_renard':
            d += (habitat_1[key] - habitat_2[key])**2
    return sqrt(d)

def distance_d_un_habitat(habitat:dict, habitats:list[dict])->list[tuple]:
    distances = []
    for hab in habitats:
        distances.append((distance(habitat, hab), hab))
    return distances


def k_plus_proches(k:int, habitat:dict, habitats:list[dict])->list[tuple]:
    distances = distance_d_un_habitat(habitat, habitats)
    distances.sort(key = lambda x: x[0])
    return distances[:k]

def presence_renard(k:int, habitat:dict, habitats:list[dict])->bool:
    habitats = k_plus_proches(k, habitat, habitats)
    n_renards = 0
    for habitat in habitats:
        distance = habitat[0]
        caracteristiques = habitat[1]
        if caracteristiques['presence_renard']:
            n_renards += 1
    return n_renards > k/2


print(presence_renard(10, nouveau, zones_connues)) #True
print(presence_renard(50, nouveau, zones_connues)) #True
print(presence_renard(100, nouveau, zones_connues)) #False
print(presence_renard(500, nouveau, zones_connues)) #False
print(presence_renard(700, nouveau, zones_connues)) #True