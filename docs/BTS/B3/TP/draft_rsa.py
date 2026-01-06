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

def est_premier(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def diviseurs(n):
    div = []
    for i in range(1, n+1):
        if n % i == 0:
            div.append(i)
    return div

def pgcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def inverse_modulaire(e, phi):
    for i in range(2, phi):
        if (e * i) % phi == 1:
            return i
    return None

def generer_clef_rsa(p,q):
    n = p * q
    print("n",n)
    phi = (p-1) * (q-1)
    print("phi",phi)
    e = 0
    for i in range(2, phi):
        if pgcd(i, phi) == 1:
            e = i
            break
    print("e",e)
    d = inverse_modulaire(e, phi)
    print("d",d)
    return ((e,n),(d,n))

def chiffrer_message_texte_rsa(message, clef):
    l = []
    for lettre in message:
        ind_lettre = indice_dans_alphabet(lettre)
        if ind_lettre == -1:  # Si ce n'est pas une lettre
            l.append("")
        else:  # Si c'est une lettre
            chiffre = pow(ind_lettre, clef[0], clef[1])
            l.append(chiffre)
    return l

def dechiffrer_message_texte_rsa(message, clef):
    l = ""
    for chiffre in message:
        if chiffre == "":  # Si ce n'est pas une lettre
            l += ""
        else:  # Si c'est un chiffre
            lettre = ALPHABET[pow(chiffre, clef[0], clef[1])]
            l += lettre
    return l


cle_pub, cle_priv = generer_clef_rsa(61, 53)
print(cle_pub)
print(cle_priv)

a_chiffrer = 100
chiffre = pow(a_chiffrer, cle_pub[0], cle_pub[1])
print(chiffre)

dechiffre = pow(chiffre, cle_priv[0], cle_priv[1])
print(dechiffre)

msg = "HELLO WORLD"
message_chiffre = chiffrer_message_texte_rsa(msg, cle_pub)
print(message_chiffre)
message_clair = dechiffrer_message_texte_rsa(message_chiffre, cle_priv)
print(message_clair)