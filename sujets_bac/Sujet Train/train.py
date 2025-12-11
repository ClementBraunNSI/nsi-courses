"""Gestion simplifiée d’un emploi du temps ferroviaire"""

def vers_minutes(horaire: str) -> int:
    """Convertit un horaire au format 'hh:mm' en minutes depuis minuit.
       Il y aura toujours deux valeurs pour les hh et les minutes.
       Si il est une heure 40 du matin on écrira 01h40
    """
    heures, minutes = map(int, horaire.split(':')) # il sont pas obligé de faire un split, un parcours est possible
    return heures * 60 + minutes


def chevauchement(train1: tuple, train2: tuple) -> bool:
    """Vérifie si deux trains se chevauchent dans le temps."""
    return not(train1[2] <= train2[1] or train2[2] <= train1[1])
    # Deux trains se chevauchent si les intervalles de temps se recoupent

def test_chevauchement():
    """Teste la fonction chevauchement avec des cas simples."""
    assert chevauchement(("TGV 8437", "08:30", "09:45"), ("TER 9321", "09:00", "09:50")) == True
    assert chevauchement(("TGV 8437", "08:30", "09:45"), ("Intercités 4102", "10:15", "12:00")) == False
    assert chevauchement(("TER 9321", "09:00", "09:50"), ("Intercités 4102", "9:10", "9:40")) == True

def exporter_planning(trains: list, nom_fichier: str) -> None:
    """Crée un fichier texte contenant la liste triée des trains par heure de départ."""
    trains_tries = sorted(trains, key=lambda t: vers_minutes(t[1]))
    lignes = []
    for train in trains_tries:
        nom, dep, arr = train
        lignes.append(f"{nom} – Départ : {dep} – Arrivée : {arr}")
    with open(nom_fichier, 'a', encoding='utf-8') as f:
        f.write('\n'.join(lignes))


if __name__ == "__main__":
    trains = [
        ("TGV 8437", "08:30", "09:45"),
        ("TER 9321", "09:00", "09:50"),
        ("Intercités 4102", "10:15", "12:00")
    ]

    print("Chevauchement entre TGV 8437 et TER 9321 :", chevauchement(trains[0], trains[1]))
    exporter_planning(trains, "planning_trains.txt")
    print("Fichier planning_trains.txt généré.")
