def comp(t1,t2):
    """ Fonction de comparaison qui renvoie True si le ratio (valeur/masse) du tuple 1 est supérieur 
    à celui du ratio (valeur/masse) du tuple 2, False sinon.
    param t1: (tuple) ayant pour données une valeur et une masse
    param t2: (tuple) ayant pour données une valeur et une masse
    """
    if t1[0]/t1[1] > t2[0]/t2[1]:
        bool = True
    else:
        bool = False
    return bool

def tri_decroissant(liste):
    """ Renvoie une liste triée par ratio valeur/masse décroissant sans modifier la liste passée en paramètre. 
    param liste: (list) liste de tuples ayant pour données une valeur et une masse
    return: (list) liste triée par ratio valeur/masse décroissant
    """
    pass

def mystere():
    """ Fonction mystere """
    liste_triee = tri_decroissant([(60, 2),(10, 0.3),(40, 1),(20, 1),(100, 3),(15, 0.3),(50, 1),(120, 4)])
    assert liste_triee == [(15, 0.3), (50, 1), (40, 1), (100, 3), (10, 0.3), (60, 2), (120, 4), (20, 1)], "Assertion déclenchée"
    print("Assertion non déclenchée")

def sac_a_dos_glouton(lObjets, masseM):
    """Fonction qui choisit les objets à mettre dans le sac à dos en utilisant la méthode gloutonne.
    param lObjets: (list) liste de tuples ayant pour données une valeur et une masse
    param masseM: (int) masse maximale autorisée
    return: (list) liste des objets sélectionnés
    """
    # Trier par ratio valeur/masse décroissant
    objets_trie = tri_decroissant(lObjets)
    # Vérifier si on peut ajouter l’objet et mettre à jour le masse total
    selection = []
    masse_totale = 0
    compt = 0
    while ... :
        selection.append(...)
        masse_totale = ...
        compt = compt + 1
    return ...

def sacados_dynamique(lObjets, masseM):
    """Fonction qui choisit les objets à mettre dans le sac à dos en utilisant la programmation dynamique.
    param lObjets: (list) liste de tuples ayant pour données une valeur et une masse
    param masseM: (int) masse maximale autorisée
    return: (list) liste des objets sélectionnés   
    """
    n = len(lObjets)
    # On transforme les masses en entiers pour éviter les problèmes de flottants
    facteur = 10
    pm = int(masseM * facteur)
    # Créer une matrice pour stocker la valeur maximale à chaque étape
    matrice = [[0] * (pm + 1) for i in range(n + 1)]
    # Créer une matrice pour stocker les décisions
    choix = [[False] * (pm + 1) for i in range(n + 1)]
    
    # 
    for i in range(1, n + 1):
        val, masse = lObjets[i-1]
        masse_int = int(masse * facteur)
        for cap in range(masse_int, pm + 1):
            # Cas où l’objet est trop lourd : on ne peut pas le prendre
            if matrice[i-1][cap] >= matrice[i-1][cap - masse_int] + val:
                matrice[i][cap] = matrice[i-1][cap]
            else:
                # Comparaison : prendre ou ne pas prendre l’objet
                matrice[i][cap] = matrice[i-1][cap - masse_int] + val
                choix[i][cap] = True

    # Reconstruire la liste des objets sélectionnés
    selection = []
    cap = pm
    for i in range(n, 0, -1):
        if choix[i][cap] == True:
            val, masse = lObjets[i-1]
            selection.append(lObjets[i-1])
            cap = cap - int(masse * facteur)

    # Remettre les objets dans l’ordre initial
    selection.reverse()
                      
    return selection

# PROGRAMME PRINCIPAL

# Liste d’objets
liste_objets = [
    (60, 2),	# Bouteille d’eau
    (10, 0.3),	# Chocolat
    (40, 1),	# Lampe torche
    (20, 1),	# Livre
    (100, 3),   # Repas
    (15, 0.3),	# Téléphone
    (50, 1),	# Trousse de secours
    (120, 4)	# Vêtements    
]
masseMax = 10  # Masse maximum utilisée

# Tests et affichages:
print("Liste des objets triés par ratio valeur/masse décroissant:", tri_decroissant(liste_objets))
mystere(liste_objets)
print("Liste des objets sélectionnés avec la méthode gloutonne:", sac_a_dos_glouton(liste_objets, poidsMax))
print("Liste des objets sélectionnés avec la méthode dynamique:", sacados_dynamique(liste_objets, poidsMax))