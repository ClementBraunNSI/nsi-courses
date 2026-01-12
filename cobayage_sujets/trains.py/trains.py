def vers_minutes(horaire: str) -> int:
    """
    Convertit un horaire au format "hh:mm" en nombre total de minutes depuis minuit.
    
    Paramètres
    ----------
    horaire : str
        Chaîne représentant l'heure au format "hh:mm"
        (exemples : "00:00", "01:30", "23:59")
    
    Retour
    ------
    int
        Le nombre total de minutes écoulées depuis minuit.
    
    Exemples
    --------
    >>> vers_minutes("00:00")
    0
    >>> vers_minutes("01:30")
    90
    >>> vers_minutes("23:59")
    1439
    """
    heures, minutes = horaire.split(":")
    heures = int(heures)
    minutes = int(minutes)
    return heures * 60 + minutes
    


def chevauchement(train1: tuple, train2: tuple) -> bool:
    """
    Vérifie si deux trains se chevauchent dans le temps.

    Deux trains se chevauchent si leurs périodes horaires se croisent,
    c’est-à-dire si le départ de l’un a lieu avant la fin de l’autre
    et sa fin après le départ de l’autre.

    Paramètres
    ----------
    train1 : tuple
        (nom, heure_depart, heure_arrivee) du premier train.
    train2 : tuple
        (nom, heure_depart, heure_arrivee) du second train.

    Retour
    ------
    bool
        True si les trains se chevauchent, False sinon.

    Exemples
    --------
    >>> t1 = ("TGV 8437", "08:00", "09:00")
    >>> t2 = ("TER 1203", "08:30", "09:15")
    >>> chevauchement(t1, t2)
    True

    >>> t3 = ("TGV 8437", "10:00", "11:00")
    >>> t4 = ("TER 1203", "11:00", "12:00")
    >>> chevauchement(t3, t4)
    False
    """
    depart1 = vers_minutes(train1[1])
    arrivee1 = vers_minutes(train1[2])
    depart2 = vers_minutes(train2[1])
    arrivee2 = vers_minutes(train2[2])

    return depart1 < arrivee2 and depart2 < arrivee1

def test_chevauchement():
    """
    Effectue trois tests unitaires sur la fonction chevauchement().

    Cas testés :
    1. Deux trains qui se suivent sans chevauchement.
    2. Deux trains qui se chevauchent partiellement.
    3. Un train entièrement inclus dans un autre.

    Chaque cas utilise une assertion.
    """
    # Cas 1 : pas de chevauchement
    t1 = ("TGV 1001", "08:00", "09:00")
    t2 = ("TER 1203", "09:00", "10:00")
    assert not chevauchement(t1, t2), "Erreur : les trains ne devraient pas se chevaucher."

    # Cas 2 : chevauchement partiel
    t3 = ("TGV 2002", "08:00", "09:30")
    t4 = ("TER 1500", "09:00", "10:00")
    assert chevauchement(t3, t4), "Erreur : les trains devraient se chevaucher."
    # Cas 3 : un train inclus dans un autre
    t5 = ("TGV 3003", "07:00", "10:00")
    t6 = ("TER 1800", "08:00", "09:00")
    assert chevauchement(t5, t6), "Erreur : le train court est inclus dans le long."
    print("Tous les tests de chevauchement sont réussis.")

def affichage_planning(trains: list) -> None:
    """
    Affiche à l'écran le planning quotidien des trains trié par heure de départ.

    Chaque ligne affichée est de la forme :
        Nom – Départ : hh:mm – Arrivée : hh:mm

    Paramètres
    ----------
    trains : list
        Liste de tuples représentant les trains sous la forme :
        (nom, heure_depart, heure_arrivee)

    Retour
    ------
    None
        La fonction affiche directement dans la console.

    Exemple
    -------
    >>> trains = [
    ...     ("TGV 8437", "08:30", "09:30"),
    ...     ("TER 1203", "07:45", "08:15")
    ... ]
    >>> affichage_planning(trains)
    TER 1203 – Départ : 07:45 – Arrivée : 08:15
    TGV 8437 – Départ : 08:30 – Arrivée : 09:30
    """
    # Tri manuel par heure de départ
    for i in range(len(trains)):
        for j in range(i + 1, len(trains)):
            if vers_minutes(trains[...][1]) < vers_minutes(trains[i][...]):
                trains[...], trains[...] = trains[...], trains[...]

    
    # Affichage du planning
    print("=== PLANNING QUOTIDIEN ===")
    for nom, depart, arrivee in trains:
        print(nom + " – Départ : " + depart + " – Arrivée : " + arrivee)
    print("===========================")
    pass
