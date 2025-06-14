compte={'1': {'nom': 'thomas', 'solde': 10100000, 'liste': []},
        '2': {'nom': 'léon', 'solde': 270000000, "liste":[]}}
def creer_compte(num:str,nom:str,soldei:float,trans:list):
    if num not in compte:
        nnum={"nom":nom,
             "solde_i":soldei,
             "liste":trans,
             }
        compte[num]=nnum
    return compte
def deposer(num:str,montant:float)->dict:
    if num in compte:
        compte[num]["solde"]+=montant
        compte[num]["liste"]+=["+",montant]
    return compte
def retirer(num:str,montant_re:float)->dict:
    if num in compte:
        if compte[num]["solde"]>=montant_re:
            compte[num]["solde"]-=montant_re
            compte[num]["liste"]+=["-"+str(montant_re)]
        return compte
   
def verifier_solde(num:str)->None:
    print(compte[num]["solde"])

def verifier_trans(num:str)->None:
    print(compte[num]["solde"])

def afficher_menue():
    print("option: 1. Créer un compte 2. Fait un dépôt 3. Fait un retrait 4.Vérifie le solde 5. Vois les trans 6.Quitte")
def main():
    afficher_menue()
    a=input("num option choisie:",)
    print(type(a))
        return "non"
    if a=="1":
        numero=input("num de compte:",)
        nomu=input("nom:",)
        solde=float(input("solde initiale:",))
        liste=list(input("liste_transaction:",))
        creer_compte(numero,nomu,solde,liste)
    elif a=="2":
        numero=input("num du compte",)
        montan=input("montant versé:",)
        deposer(numero,montan)
    elif a=="3":
        numero=input("num du compte",)
        montan=float(input("montant a volée:",))
        retirer(numero,montan)
    elif a=="4":
        numero=input("num compte",)
        verifier_solde(numero)
    elif a=="5":
        numero=float(input("num compte",))
        verifier_trans(numero)
    elif a=="6":
        return "a bientot"
    else:
        return "non"