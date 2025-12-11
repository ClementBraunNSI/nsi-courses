ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def indice_dans_alphabet(lettre):
    if lettre in ALPHABET:
        return ALPHABET.index(lettre)
    else:
        return -1

def chiffrer_vigenere(message, clef):
    res = ""
    i_clef = 0
    for lettre in message:
        ind_lettre = indice_dans_alphabet(lettre)
        
        if ind_lettre == -1:  # Si ce n'est pas une lettre
            res += lettre
        else:  # Si c'est une lettre
            ind_clef = indice_dans_alphabet(clef[i_clef])
            n_ind = (ind_lettre + ind_clef) % 26
            res += ALPHABET[n_ind]
            i_clef = (i_clef + 1) % len(clef)
    
    return res

print(chiffrer_vigenere("BONJOUR", "CLE"))  # Attendu : DZRLZYT
print(chiffrer_vigenere("HELLO WORLD","KEY"))