from lexique import *
import random
import timeit
import matplotlib.pyplot as plt

EQUIV_SANS_CASSE = {
    "é" : "e", "è" :"e", "ê" : "e", "ë":"e",
    "à" : "a", "â" : "a", "ä" : "a",
    "ö" : "o", "ô" : "o",
    "î" : "i", "ï" : "i", '-' :'', "'" : ''}

def bas_casse_sans_accent(chaine):
    s=""
    for char in chaine:
        if char in EQUIV_SANS_CASSE:
            s+= EQUIV_SANS_CASSE[char]
        else:
            s+= char
    return s

def sort(chaine):
    """
    méthode qui trie les lettres par ordre alphabétique d'un mot
    """
    s = ""
    l = list(bas_casse_sans_accent(chaine))
    l.sort()
    for elt in l:
        s+= str(elt)
    return s


def est_anagramme_1(chaine1, chaine2):
    """
    params:
    chaine1 : chaine de caractère
    chaine2 : chaine de caractère

    Fonction qui renvoie si les mots sont anagrammes en regardant leur lettres triées dans l'ordre alphabetique
    """
    return sort(chaine1) == sort(chaine2)

def anagramme_1(chaine, lexique = LEXIQUE):
    """
    params : 
    chaine : mot sous forme de chaine de caractère dont on cherche les anagrammes
    lexique : liste non exhaustive de mots

    Fonction qui permet de donner les anagrammes d'un mot passé en paramètre en parcourant la liste en utilisant le prédicat est_anagramme_1
    """
    anagrammes = []
    for mot in lexique:
        if est_anagramme_1(mot, chaine):
            anagrammes.append(mot)
    return anagrammes

def anagramme_1_sur_lexique(lexique):
    """
    Fonction qui applique la fonction anagramme sur un lexique de taille variable
    """
    return {mot : anagramme_1(mot, lexique) for mot in lexique}

def clef_mot(mot):
    """
    Renvoie la clef associée au mot, bas_casse et ordre alphabetique
    """
    return sort(mot)

def dict_lexique(lexique):
    """
    associe à chaque clef d'un mot les anagrammes associés
    """
    dictionnary = {}
    for mot in lexique:
        if clef_mot(mot) not in dictionnary:
            dictionnary[clef_mot(mot)] = [mot]
        else:
            dictionnary[clef_mot(mot)].append(mot)
    return dictionnary

def anagramme_2(mot, dictionnaire):
    """
    Renvoie la liste d'anagrammes d'un mot passé en paramètre
    """
    return dictionnaire[clef_mot(mot)]

# prend en paramètre un lexique et renvoie tous les anagrammes du lexique
def mesure_anagramme_clef():
    tab_mesures =[]
    for i in range(0,500):
        s_time = timeit.default_timer()
        anagramme_1_sur_lexique(LEXIQUE[:i])
        #for mot in LEXIQUE[:i]:
        #   anagramme_1(mot, LEXIQUE[:i])
        e_time = timeit.default_timer()
        tab_mesures.append(e_time-s_time)
    print(str(sum(tab_mesures)) + " secondes")
    plt.plot([i for i in range(500)], tab_mesures)
    plt.savefig("fig_clef.png")
    plt.clf()

def mesure_anagramme_dico():
    tab_mesures2 =[]
    for i in range(0,500):
        s_time = timeit.default_timer()
        dico = dict_lexique(LEXIQUE[:i])
        for mot in LEXIQUE[:i]:
            anagramme_2(mot, dico)
        e_time = timeit.default_timer()
        tab_mesures2.append(e_time-s_time)
    print(str(sum(tab_mesures2)) + " secondes" )

    plt.plot([i for i in range(500)], tab_mesures2)
    plt.savefig("fig_dico.png")

