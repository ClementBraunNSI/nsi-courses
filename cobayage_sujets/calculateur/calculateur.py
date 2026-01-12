map = [["RPM", "Load 20%" , "Load 40%", "Load 60%", "Load 80%"], [1000,10,12,14,15], [2000,12,14,16,17], [3000,14,18,20,22]]


def flat_map(map2D):
    """ Renvoie la map en liste 1D """
    res = []
    for liste in map2D:
        for elt in liste:
            res.append(elt)
    return res


def rebuild_map(flat, width):
    """ Renvoie une map 2D à partir d'une liste 1D et de la longueur d'une ligne """
    res = []
    temp = []
    for i in range(0,len(flat),width):
        for j in range(i, i+width):
            temp.append(flat[j])
        res.append(temp)
        temp = []
    return res


def moyenne_par_ligne(map2D):
    """ Renvoie la liste des moyennes des valeurs par ligne """
    moyennes = []
    for i in range(1,len(map2D)):
        total_values = 0
        for j in range(1,len(map2D[i])):
            total_values += int(map2D[i][j])
        moyennes.append(int(total_values/len(map2D[i])-1))
    return moyennes

def calcul_delta(map):
    """Renvoie le delta"""
    return max(moyenne_par_ligne(map)) - min(moyenne_par_ligne(map))

def zones_risque(map2D, seuil):
    """ Renvoie la liste des coordonnées où la valeur dépasse le seuil """
    L = []
    for i in range(1,len(map2D)):
        for j in range(1,len(map2D[i])):
            if int(map2D[i][j]) > seuil:
                L.append((i, j, map2D[i][j]))
    return L

def comparaison(mapA, mapB):
    res = []
    for i in range(len(mapA)):
        for j in range(len(mapA[i])):
            if int(mapA[i][j] != mapB[i][j]):
                res.append((i,j,mapA[i][j],mapB[i][j]))
    return res


def corriger_map(map2D, seuil, delta):
    """ Renvoie une nouvelle liste corrigée """
    nouvelle = []
    nouvelle.append(map2D[0])
    for i in range(1, len(map2D)):
        ligne = []
        for j in range(1, len(map2D[i])):
            if int(map2D[i][j]) > seuil:
                ligne.append(int(map2D[i][j]) - delta)
            else:
                ligne.append(int(map2D[i][j]) )
        nouvelle.append([map2D[i][0]] + ligne)
    return nouvelle

print("map 2D aplatie en 1D :")
flat = flat_map(map)
print(flat)
remap = rebuild_map(flat, 5)
print("map 2D à partir de map en 1D :")
print(remap)
print("coordonnée des zones à risque (>18°) :")
print(zones_risque(map, 18))
print("moyenne_par_ligne(map2D)")
print(moyenne_par_ligne(map))

newmap = corriger_map(map, 18, calcul_delta(map))
print(newmap)