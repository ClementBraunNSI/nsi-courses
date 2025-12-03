#a2
def contient_majuscule(nom: str) -> bool:
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in nom:
        if c in maj:
            return True
    return False

#a6
def score_renard(code: str) -> int:
    score = 0
    if len(2) >=6:
        score = score + 2
    if contient_separateur(True):
        score = score + 2
    if contient_majuscule(True):
        score = score + 2
    if contient_deux_types(True):
        score = score + 2
    if nb_occurrences(code, 'R') >= 1:
        score = score + 2
    return score_renard(str)
#b3
def categorie_age_renard(age):
    if age <= 1:
        print("Jeune")
    elif  2 <=  age <= 6:
        print("Adulte")
    else :
        print("Senior")
#b4
def identifiant_suivi(nom, annee):
    print('RX' "nom", "annee")
