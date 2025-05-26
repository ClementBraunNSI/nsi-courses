paquet_chips_1 = ("Chipeur", 0.150, 1.99)
paquet_chips_2 = ("Frites et Cie", 0.200, 2.49)
paquet_chips_3 = ("Pipoles", 0.200, 2.79)
paquet_chips_4 = ("Tay's", 0.300, 3.19)
paquet_chips_5 = ("Bonne Patate", 0.125, 1.69)
paquet_chips_6 = ("Cuisto's", 0.100, 1.49)
paquet_chips_7 = ("Mik'O Chips", 0.250, 2.59)
        
paquets_de_chips = [paquet_chips_1, paquet_chips_2, paquet_chips_3, paquet_chips_4, paquet_chips_5, paquet_chips_6, paquet_chips_7]

def prix_kilo(paquets:list):
    paquets_chips = []
    for paquet in paquets:
        paquets_chips.append([paquet[0], paquet[1], paquet[2], paquet[2]/paquet[1]])
    return paquets_chips

def afficher_rayon(paquets):
    paquets_prix_kilo = prix_kilo(paquets)
    for paquet in paquets_prix_kilo:
        print(paquet[0], ":", paquet[3], "€/kg")
afficher_rayon(paquets_de_chips)

def paquet_prix_kilo_min(paquets):
    paquets_prix_kilo = prix_kilo(paquets)
    prix_kilo_min = paquets_prix_kilo[0][3]
    for paquet in paquets_prix_kilo:
        if paquet[3] < prix_kilo_min:
            prix_kilo_min = paquet[3]
            paquet_prix_kilo_min = paquet
    return paquet_prix_kilo_min

print(paquet_prix_kilo_min(paquets_de_chips))

def paquet_budget(paquets, budget):
    paquet_min = paquet_prix_kilo_min(paquets)
    nb_paquet = 0
    volume_chips = 0
    while budget >= paquet_min[2]:
        budget -= paquet_min[2]
        nb_paquet += 1
        volume_chips += paquet_min[1]
    return nb_paquet, volume_chips

print(paquet_budget(paquets_de_chips, 25))

'''def paquet_prix_min(paquets:list):
    prix_min = paquets[0][2]
    paquet_prix_min = paquets[0]
    for paquet in paquets:
        if paquet[2] < prix_min:
            prix_min = paquet[2]
            paquet_prix_min = paquet
    return paquet_prix_min

print(paquet_prix_min(paquets_de_chips))

def paquet_budget(paquets:list, budget:float):
    paquet_min = paquet_prix_min(paquets)
    nb_paquet = 0
    volume_chips = 0
    while budget >= paquet_min[2]:
        budget -= paquet_min[2]
        nb_paquet += 1
        volume_chips += paquet_min[1]
    return nb_paquet, volume_chips

print(paquet_budget(paquets_de_chips, 25))'''

        