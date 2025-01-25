ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def lettres_majuscules(message):
    resultat = ""
    for lettre in message:
        if lettre.upper() in ALPHABET:
            resultat += lettre.upper()
        elif lettre == " ":
            resultat += " "
    return resultat

def dechiffrer_cesar(message, decalage):
    message_res = ''
    for lettre in message:
        if lettre in ALPHABET:
            message_res+=ALPHABET[(ALPHABET.index(lettre)-decalage)%26]
        elif lettre == " ":
            message_res += " "
    return message_res

def chiffrer_cesar(message, decalage):
    message_res = ''
    for lettre in message:
        if lettre in ALPHABET:
            message_res+=ALPHABET[(ALPHABET.index(lettre)+decalage)%26]
        elif lettre == " ":
            message_res += " "
    return message_res
