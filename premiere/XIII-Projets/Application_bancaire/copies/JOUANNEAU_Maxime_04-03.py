comptes = {}

def creer_compte(comptes:dict, n_compte:str, nom:str):
    if n_compte not in comptes:
        comptes[n_compte] = {'nom':nom, 'solde':float(0), 'transaction':[]}
    return comptes


def deposer(n_compte:str, montant:float)->dict:
        if n_compte not in comptes:
            print("ce compte n'existe pas")
        else:
            if montant < 0 or montant != round(montant, 2):
                print("ERREUR! La somme d'argent est incorrecte!")
            for i in comptes:
                if i == n_compte:
                    comptes[i]['solde'] += montant
                    s = "+" + str(montant)
                    comptes[i]['transaction'].append(s)
        return comptes
#deposer("0000", 50)
#print(comptes)


def retirer(n_compte:str, montant:float)->dict:
    if n_compte not in comptes:
        print("ERREUR! Ce compte n'existe pas")
    else:
        for i in comptes:
            if i == n_compte:
                if montant > comptes[i]['solde']:
                    print("solde insuffisant pour retirer cete somme!")
                else:
                    comptes[i]['solde'] -= montant
                    s = "-" + str(montant)
                    comptes[i]['transaction'].append(s)
    return comptes
#retirer("0000", 60)
#print(comptes)


def verifier_solde(n_compte:str):
    if n_compte not in comptes:
        print("ce compte n'existe pas")
    else:
        for i in comptes:
            if i == n_compte:
                return comptes[i]['solde']
#verifier_solde(comptes, "0000")


def voir_transactions(n_compte:str):
    if n_compte not in comptes:
        print("ce compte n'existe pas")
    else:
        for i in comptes:
            if i == n_compte:
                return comptes[i]['transaction']
#voir_transactions("0000")


def afficher_menu():
    print("\n1- Creer compte\n2- Faire un depôt\n3- Faire un retrait\n4- Verifier le solde\n5- Voir les transactions\n6- Quitter")
#afficher_menu()


def main():
    fin = False
    while fin == False:
        afficher_menu()
        choix = input("que voulez-vous faire? (tapez le nomero correspondant): ")
        if choix == "1":
            n = input("quel est votre numéro de compte? ")
            nom = input("quel est votre nom? ")
            creer_compte(comptes, n, nom)
        elif choix == "2":
            n = input("quel est votre numéro de compte? ")
            montant = float(input("combien voulez-vous verser? "))
            deposer(n, montant)
        elif choix == "3":
            n = input("quel est votre numéro de compte? ")
            montant = float(input("combien voulez-vous retirer? "))
            retirer(n, montant)
        elif choix == "4":
            n = input("quel est votre numéro de compte? ")
            print("actuellement vous avez, ", verifier_solde(n), "€")
        elif choix == "5":
            n = input("quel est votre numéro de compte? ")
            print("vos transactions sont : ", voir_transactions(n))
        elif choix == "6":
            print("Merci d'utiliser nos service\n a bientôt")
            fin = True
main()