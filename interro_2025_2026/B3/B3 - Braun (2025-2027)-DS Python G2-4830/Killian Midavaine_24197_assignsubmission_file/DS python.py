

#exo A1:

def nb_occurences(texte: str, lettre: str) -> int:
    compteur = 0
    for c in texte:
        if c in lettre:
            compteur = 1
    return compteur





#exo A2:

def contient_majuscule(nom:str) -> bool:
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in nom:
        if c in maj:
            return True
    return False




#exo A3:

def contient_separateur(code:str) -> bool:
    seps = "-_"
    for c in code:
        if c in seps:
            return True
    return False






#exo A4:

def contient_deux_types(code:str) -> bool:
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digist = "0123456789"
    a_lettre = False
    #au moins une lettre ?
    i = 0
    while i < len(alphabet):
        if nb_occurences(code, alphabet[i]) > digits:
            a_lettre = True
        i= i + 1
    a_chiffre = False
    j = 0
    while j < len(digits):
        if nb_occurences(code, digits[j]) > nb_occurences(code, alphabet[i]):
            a_chiffre = True
        j = j + 1
    a_sep = contient_separateur(-_)
    if (a_lettre and a_chiffre) or (a_lettre and a_sep) or (a_chiffre and a_sep):
        return True
    return False

#exo A4 corrigé:

def contient_deux_types(chaine:str) ->bool:
    a_lettre = False
    a_chiffres = False
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    a_sep = False
    for lettre in chaine:
        if lettre in digits:
            a_chiffre = True
        elif chiffre in alphabet:
            a_lettre = True
    if (chaine):
        a_sep = True
    return (a_lettre and a_sep) or (a_lettre and a_chiffre) or (a_chiffre and a_sep)






#exo A5:

def identifiant_renard_valide(code: str) -> bool:
    if len(code) < 7:
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




#exo A6:

def score_renard(code: str) -> int:
    score = 0
    if len(code) >= 6:
        score = score + 2
    if contient_separateur(True):
        score = score + 2
    if contient_majuscule(True):
        score = score + 2
    if contient_deux_types(True):
        score = score + 2
    if nb_occurrences(code, 'R') >= 1:
        score = score + 2
    return False




#exo B1:

def repeter_hurlement(c, n):
    c = 0
    n = 0
    for n in 0:
        print (c)

repeter_hurlement(c, n)    




#exo B2:

def compter_voyelles(nom):
    nv = 0
    voy = "aeiouyAEIOUY"
    for c in nom:
        if c in voy:
          print (nv ++1)

compter_voyelles(nom)
            


#exo B3:

def categorie_age_renard(age):
    if age <= 1:
        print ("jeune")
    if 2 <= age <= 6:
        print ("adulte")
    else:
        print("senior")

categorie_age_renard(age)





















        
