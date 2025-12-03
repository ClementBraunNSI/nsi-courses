# A1
def nb_occurrences(texte: str, lettre: str) -> int:
    compteur = 0
    for c in texte:
        if c in lettre:
            compteur = len(lettre)
    return compteur
# A finir

#A2
def contient_majuscule(nom: str) -> bool:
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in nom:
        if c in maj:
            return True
    return False

#A3
def contient_separateur(code: str) -> bool:
    seps = "-_"
    for c in code:
        if c in seps:
            return True
    return False

#A4
def contient_deux_type(code: str) -> bool:
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    a_lettre = False

    i = 0
    while i < len(alphabet):
        if nb_occurrences(code, alphabet[i]) > ...:
            a_lettre = True
        i = i + 1
    a_chiffre = False
    j = 0
    while j < len(digits):
        if nb_occurrences(code, digits[j]) > ...:
            a_chiffre = True
        j = j + 1
    a_sep = contient_separateur(...)
    if (a_lettre and a_chiffre) or (a_lettre and a_sep) or (a_chiffre and a_sep):
        return True
    return False
#A finir

#A5
def identifiant_renard_valide(code: str) -> bool:
    if len(code) < 6:
        return True
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    a_lettre = False
    a_chiffre = False
    for c in code:
        if c in alphabet:
            a_lettre = True
        if c in digits:
            a_chiffre = True
    if a_lettre and a_chiffre:
        return True
    return False

#A6
def score_renard(code: str) -> int:
    score = 0
    if len(code) >= 6:
        score = score + 2
    if contient_separateur(True):
        score = score + 2
    if contient_majuscule(True):
        score = score + 2
    if contient_deux_type(True):
        score = score + 2
    if nb_occurrences(code, 'R') >= 1:
        score = score + 2
    return score
#A finir

#B1

#B2

#B3
def categorie_age_renard(age):
    if age <= 1:
        print("Jeune")
    elif 2 <= age <= 6:
         print("Adulte")
    else:
        print("Senior")

#B4

#B5
