from random import *
comptes = {}
transactions = []

def creer_compte(nmr_compte:str,nom:str,solde_initial:float,transactions:list):
    if nmr_compte in comptes:
        print("Le compte exitse déjà ! ")
        return None
    comptes[nmr_compte] = {"nom" : nom, "solde" : solde_initial, "transactions" : []}
    print("Le compte", {nmr_compte}," a été créé avec succès")
    return comptes

def deposer(nmr_compte:str,montant:float):
    if nmr_compte not in comptes:
        print("Le compte n'exitse pas !")
        return None
    comptes[nmr_compte]["solde"] += montant
    comptes[nmr_compte]["transactions"].append({"type":"dépot","montant":montant})
    print("Le dépot de ",montant," a bien été effectué sur le compte",nmr_compte)
    return comptes

def retirer(nmr_compte:str,montant:float):
    if nmr_compte not in comptes:
        print("Le compte n'exitse pas !")
        return None
    if comptes[nmr_compte]["solde"] < montant:
        print("Vous ne pouvez pas faire cela, le compte n'a pas un solde suffisant ! ")
        return None
    if comptes[nmr_compte]["solde"] > montant:
        comptes[nmr_compte]["solde"] -= montant
    comptes[nmr_compte]["transactions"].append({"type":"retrait","montant":montant})
    print("Le retrait de ",montant," a bien été effectué sur le compte",nmr_compte)
    return comptes

def verifier_solde(nmr_compte:str):
    if nmr_compte not in comptes:
        print("Le compte n'existe pas !")
        return None
    solde = comptes[nmr_compte]["solde"]
    print("Le solde actuel du compte", nmr_compte,"est de",solde)

def voir_transactions(nmr_compte:str):
    if nmr_compte not in comptes:
        print("Le compte n'existe pas !")
        return None
    transac = comptes[nmr_compte]["transactions"]
    print("Le compte", nmr_compte,"a subit ces transactions : ",transac)

def afficher_menu():
    print("1. Créer un compte")
    print("2. Faire un dépôt")
    print("3. Faire un retrait")
    print("4. Vérifier le solde")
    print("5. Voir les transactions")
    print("6. Quitter")

def emain():
    print("Bienvenue sur l'application bancaire OuraMost créée par Nolann Le Pavec ! ")
    appli = True
    while appli == True:
        print("Que souhaitez-vous effectuer ? ")
        afficher_menu()
        a = int(input("Veuillez indiquer le numéro de l'action que vous souhaitez effectuer  : "))
        match a:
            case 1:
                nom = input("Veuillez rentrer le nom du compte : ")
                solde_initial = int(input("Quel est votre solde initial ? "))
                nmr_compte = str(randint(1,561691))
                creer_compte(nmr_compte,nom,solde_initial,transactions)
            case 2:
                depot = input("Sur quel compte voulez vous déposer de l'argent ? Veuillez indiquer le numéro de compte : ")
                montant = int(input("Quel montant voulez vous déposer ? "))
                deposer(depot,montant)
            case 3:
                retrait = input("Depuis quel compte voulez vous retirer de l'argent ? Veuillez indiquer le numéro de compte : ")
                montant = int(input("Quel montant voulez vous retirer ? "))
                retirer(retrait,montant)
            case 4:
                solde = input("De quel compte voulez vous vérifier le solde ? Veuillez indiquer le numéro du compte : ")
                verifier_solde(solde)
            case 5:
                transac = input("De quel compte voulez vous voir les transactions ? Veuillez indiquer le numéro de compte : ")
                voir_transactions(transac)
            case 6:
                print("Vous avez bien quitté l'application bancaire")
                appli = False
            
            
    