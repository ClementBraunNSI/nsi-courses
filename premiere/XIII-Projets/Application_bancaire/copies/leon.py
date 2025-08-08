comptes={}
def creer_compte(num:str,nom:str,soldi:float,liste_transac:list)->dict:
    if num not in comptes:
        nv={}
        nv={"nom":nom,
             "sold":float(soldi),
             "liste":[]}
        comptes[num]=nv
    return comptes
def deposer(num:str,montant:float)->dict:
    if num in comptes:
        comptes[num]["sold"]+=float(montant)
        comptes[num]["liste"]+=["+"+str(montant)]
    else:
        print("comptes inexistant")
    return comptes

def retirer(num:str,montant:str)->dict:
    if num in comptes:
        if comptes[num]["sold"]>=float(montant):
            comptes[num]["sold"]-=float(montant)
            comptes[num]["liste"]+=["-"+str(montant)]
        else :
            print("montant insufisant")
    else:
        print("comptes inexistant")
    return comptes

def verifier_solde(num:str)->None:
    if num in comptes :
        print(comptes[num]["sold"])
    else:
        print('compte inexistant')
def verifier_transac(num:str)->None:
    if num in comptes:
        print(comptes[num]["liste"])
    else:
        print('compte inexistant')
def afficher_menue():
    print("option: 1. Créer un compte 2. Faire un dépôt 3. Faire un retrait 4. Vérifier le solde 5. Voir les transactions 6. Quitter")
def main():
    while True :
        afficher_menue()
        a=input("num option choisie:",)
        if a=="1":
            numero=input('num de compte:',)
            nomu=input('nom:',)
            solde=float(input('solde initiale:',))
            listee=list(input("liste_transaction:",))
            creer_compte(numero,nomu,solde,listee)
        elif a=="2":
            numero=input("num du compte:",)
            montan=input("montant verser:",)
            deposer(numero,montan)
        elif a=="3":
            numero=input("num du compte",)
            montan= float(input("montant a volee:",))
            retirer(numero,montan)
        elif a=="4":
            numero=input("num compte",)
            verifier_solde(numero)
        elif a=="5":
            numero=input("num compte",)
            verifier_transac(numero)
        elif a=="6":
            return "au revoir"
        else :
            return "non"
