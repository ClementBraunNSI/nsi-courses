def indice_dans_alphabet(lettre, alphabet):
    return alphabet.index(lettre) if lettre in alphabet else -1

def chiffrer_cesar(lettre,clef,alphabet):
    ind_lettre = indice_dans_alphabet(lettre, alphabet)
    if ind_lettre == -1:  # Si ce n'est pas une lettre
        return lettre
    else:  # Si c'est une lettre
        n_ind = (ind_lettre + clef) % 26
        return alphabet[n_ind]

def chiffrer_mot_cesar(mot,clef,alphabet):
    res = ""
    for lettre in mot:
        res += chiffrer_cesar(lettre,clef,alphabet)
    return res

def dechiffrer_mot_cesar(mot,clef,alphabet):
    res = ""
    for lettre in mot:
        res += chiffrer_cesar(lettre,-clef,alphabet)
    return res

def bruteforce_dechiffrer(mot,alphabet):
    for clef in range(len(alphabet)):
        print(chiffrer_mot_cesar(mot,-clef,alphabet))

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(indice_dans_alphabet("A",ALPHABET))
print(chiffrer_cesar("B",3,ALPHABET))
print(chiffrer_mot_cesar("ALPHA",3,ALPHABET))
print(dechiffrer_mot_cesar("DOSKD",3,ALPHABET))
#bruteforce_dechiffrer("ERQMRXU",ALPHABET)