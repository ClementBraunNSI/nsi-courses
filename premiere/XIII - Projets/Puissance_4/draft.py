def creer_grille()->list[list[str]]:
    return [['.' for _ in range(7)] for _ in range(6)]

def afficher_grille(grille:list[list[str]]):
    print("1   2   3   4   5   6   7")
    for ligne in grille:
        s = ""
        for case in ligne:
            s+=case+"   " 
        print(s,"\n")


def colonne_valide(grille:list[list[str]],colonne:int)->bool:
    return colonne < len(grille[0])

def colonne_pleine(grille:list[list[str]],colonne:int)->bool:
    return grille[0][colonne] != '.'

def ajouter_jeton(grille:list[list[str]],colonne:str, jeton:str)->None:
    for i in range(len(grille)-1,-1,-1):
        if grille[i][colonne] == '.':
            print(i)
            grille[i][colonne] = jeton
            break
    afficher_grille(grille)


def verifier_ligne(grille:list[list[str]],joueur:str)->bool:
    for ligne in grille:
        for i in range(0,len(ligne)-3):
            if ligne[i] == joueur and ligne[i+1] == joueur and ligne[i+2] == joueur and ligne[i+3] == joueur:
                return True
    return False

def verifier_colonne(grille:list[list[str]],joueur:str)->bool:
    for i in range(len(grille)):
        for j in range(len(grille[0])-3):
            if grille[i+1][j] == joueur and grille[i+1][j] == joueur and grille[i+1][j] == joueur and grille[i+1][j] == joueur:
                return True
    return False

def verifier_diagonale(grille:list[list[str]],joueur:str)->bool:
    for i in range(len(grille)-3):
        for j in range(len(grille[0])-3):
            if grille[i][j] == joueur and grille[i+1][j+1] == joueur and grille[i+2][j+2] == joueur and grille[i+3][j+3] == joueur:
                return True
    for i in range(3,len(grille)):
        for j in range(len(grille[0])-3):
            if grille[i][j] == joueur and grille[i-1][j+1] == joueur and grille[i-2][j+2] == joueur and grille[i-3][j+3] == joueur:
                return True
    return False

def vainqueur(grille:list[list[str]],joueur:str)->bool:
    return verifier_ligne(grille,joueur) or verifier_colonne(grille,joueur) or verifier_diagonale(grille,joueur)

def match_nul(grille:list[list[str]])->bool:
    return vainqueur(grille,'X') == False and vainqueur(grille,'O') == False

def jouer()->None:
    gagnant = False
    nul = False
    joueur = 'X'
    grille = creer_grille()

    while not gagnant and not nul:
        afficher_grille(grille)
        print("Tour du joueur",joueur)
        colonne = int(input("Entrez une colonne: "))

        while not colonne_valide(grille,colonne) or colonne_pleine(grille,colonne):
            colonne = int(input("Colonne invalide. \nEntrez une colonne: "))

        ajouter_jeton(grille,colonne,joueur)

        print(gagnant)
        if vainqueur(grille,joueur) == True:
            print("Victoire du joueur",joueur)
            gagnant = True
        elif match_nul(grille)== True:
            print("Match nul")
            nul = True

        if joueur == "X":
            joueur = "O"
        else:
            joueur = "X"
        
jouer()



