def nb_occurrences(texte:str, lettre: str)-> int:
    compteur = 0
    for c in texte:
        if c in lettre:
            compteur= compteur + 1

    return compteur



def contient_majuscule(nom:str)->bool:
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in nom :
        if c in maj:
            return True
    return False


def contient_separateur(code:str)->bool:
    seps= "-_"
    for c in code:
        if c in seps:
            return True
    return False

def contient_deux_types(chaine:str)->bool:
    a_lettre=False
    a_chiffre=False
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits="0123456789"
    a_sep=False
    for lettre in chaine:
        if lettre in digits:
            a_chiffre = True
        elif lettre in alphabet:
            a_lettre = True
    if contient_separateur(chaine):
        a_sep=True
        
    return(a_lettre and a_sep) or (a_lettre and a_chiffre) or (a_chiffre and a_sep)



def identifiant_renard_valid(code:str)->bool:
    if len(code) < 6:
        return False
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


def score_renard(code:str)->int:
    score = 0
    if len(code) >= 6:
        score = score + 2
    if contient_separateur(code):
        score = score + 2
    if contient_majuscule(code):
        score = score + 2
    if contient_deux_types(code):
        score = score + 2
    if nb_occurrences(code,'R') >=1:
        score = score + 2
    return score


def repeter_hurlement(c:str,n:int)->str:
    rep = 0
    for repe in range(rep,n):
        print(c)

def compter_voyelles(nom:str)->int:
    v = "aeiouyAEIOUY"
    occu = 0
    for c in nom:
        if c in v:
            occu = occu + 1
    return occu

def categorie_age_renard(age:int)->str:
    if age <= 1 :
        print("Jeune")
    if 2 <= age and age <= 6 :
        print("Adulte")
    else:
        print("Senior")

def identifiant_suivi(nom:str,annee:str)->str:
    res = "RX-" + nom + "-" + annee
    print(res)

#def inverser_chaine(chaine:str)->str:
    
        
        



print(nb_occurrences("test","e"))
print(contient_majuscule("Test"))
print(contient_separateur("test-"))
print(contient_deux_types("Renard1"))
print(identifiant_renard_valid("Renard1-"))
print(score_renard("Renardlemeilleur1"))
print(repeter_hurlement("test",5))
print(compter_voyelles("aeiouy"))
print(categorie_age_renard(5))
print(identifiant_suivi("Renard","2020"))
print(inverser_chaine("Renard"))






