#création du dictionnaire de la banque
comptes={}

#fonction pour créer les comptes
def creer_compte(num_compte:str,nom:str,solde:float,liste_transaction:list)->dict:
    if num_compte not in comptes:
        nw_compte={}
        nw_compte["nom"]=nom
        nw_compte["solde"]=solde
        nw_compte["transaction"]=liste_transaction
        comptes[num_compte]=nw_compte
    return comptes
#fonction pour deposer de l'argent sur le compte
def deposer(num_compte:str,depot:float)->dict:
    if num_compte in comptes:
        comptes[num_compte]["solde"]=comptes[num_compte]["solde"]+depot
        comptes[num_compte]["transaction"].append(depot)
    return comptes


#fonction pour retirer de l'argent sur le compte
def retirer(num_compte:str,retrait:float)->dict:
    if num_compte in comptes:
        if comptes[num_compte]["solde"] >= retrait:
            comptes[num_compte]["solde"]=comptes[num_compte]["solde"]-retrait
            comptes[num_compte]["transaction"].append(-retrait)
    return comptes

#fonction qui montre le solde actuel du compte
def verifier_solde(num_compte:str)->None:
    if num_compte in comptes:
        print("le solde du compte de",comptes[num_compte]["nom"],"est de",comptes[num_compte]["solde"],"$")
        
#fonction qui montre les transaction du compte choisie
def voir_transaction(num_compte:str)->None:
    if num_compte in comptes:
        print("voici l'historique du compte de",comptes[num_compte]["nom"],comptes[num_compte]["transaction"])


#fonction pour créer le menu principal
def aff_menu()->None:
    print(" 1. Créer un compte 2. Faire un dépôt 3. Faire un retrait 4. Vérifier le solde 5. Voir les transactions 6. Quitter")

#fonction pour gere les choix de l'utilisateur
def main()->None:
    a = input(aff_menu())
    if a == "1" :
        num_compte = input("qu'elle est votre numéro de comptes")
        nom = input("qu'elle est votre nom")
        solde =input("qu'elle est votre solde")
        creer_compte(num_compte,nom,solde,[])
    elif a == "2":
         num_compte = input("qu'elle est votre numéro de comptes")
         depot = input("combien voullez vous déposer")
         deposer(num_compte,depot)
         
    elif a == "3":
         num_compte = input("qu'elle est votre numéro de comptes")
         retrait = input("combien voullez vous déposer")
         deposer(num_compte,retrait)
    
    elif a == "4":
        num_compte = input("qu'elle est votre numéro de comptes")
        verifier_solde(num_compte)
        
    elif a == "5":
        num_compte = input("qu'elle est votre numéro de comptes")
        voir_transaction(num_compte)
    
    elif a == "6":
        return "merci de votre visite"
    
    else:
        return "imposible"