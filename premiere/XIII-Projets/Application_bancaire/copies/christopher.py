
comptes = {}
def creer_compte(numero_compte: str, nom: str, solde_initial: float = 0.0):
    if numero_compte in comptes:
        print("Ce compte existe déjà.")
    else:
        comptes[numero_compte] = {"nom": nom, "solde": solde_initial, "transactions": []}
        print("Compte ", numero_compte, " créé avec succès pour ", nom, ".")

def deposer(numero_compte: str, montant: float):
    if numero_compte not in comptes:
        print("Le compte n'existe pas.")
    else:
        comptes[numero_compte]["solde"] += montant
        comptes[numero_compte]["transactions"].append("Dépôt de " + str(montant) + "€")
        print(montant, "€ déposés sur le compte ", numero_compte, ". Nouveau solde: ", comptes[numero_compte]['solde'], "€")

def retirer(numero_compte: str, montant: float):
    if numero_compte not in comptes:
        print("Le compte n'existe pas.")
    elif comptes[numero_compte]["solde"] < montant:
        print("Fonds insuffisants.")
    else:
        comptes[numero_compte]["solde"] -= montant
        comptes[numero_compte]["transactions"].append("Retrait de " + str(montant) + "€")
        print(montant, "€ retirés du compte ", numero_compte, ". Nouveau solde: ", comptes[numero_compte]['solde'], "€")

def verifier_solde(numero_compte: str):
    if numero_compte not in comptes:
        print("Le compte n'existe pas.")
    else:
        print("Solde du compte ", numero_compte, ": ", comptes[numero_compte]['solde'], "€")

def voir_transactions(numero_compte: str):
    if numero_compte not in comptes:
        print("Le compte n'existe pas.")
    else:
        print("Historique des transactions du compte ", numero_compte, ":")
        for transaction in comptes[numero_compte]["transactions"]:
            print(transaction)

def afficher_menu():
    print("#######LOGICIEL DE ROUSSEAU LAGRANGRE CHRISTOPHER#########")
    print("#Menu Principal#")
    print("1. Créer un compte")
    print("2. Faire un dépôt")
    print("3. Faire un retrait")
    print("4. Vérifier le solde")
    print("5. Voir les transactions")
    print("6. Quitter")

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option: ")
        
        if choix == "1":
            numero = input("entrez le numéro de compte: ")
            nom = input("entrez le nom du titulaire: ")
            solde = float(input("entrez le solde initial: "))
            creer_compte(numero, nom, solde)
        
        elif choix == "2":
            numero = input("entrez le numéro de compte: ")
            montant = float(input("entrez le montant à déposer: "))
            deposer(numero, montant)
        
        elif choix == "3":
            numero = input("entrez le numéro de compte: ")
            montant = float(input("entrez le montant à retirer: "))
            retirer(numero, montant)
        
        elif choix == "4":
            numero = input("entrez le numéro de compte: ")
            verifier_solde(numero)
        
        elif choix == "5":
            numero = input("entrez le numéro de compte: ")
            voir_transactions(numero)
        
        elif choix == "6":
            print("merci d'avoir utilisé l'application bancaire. À bientôt!")
        
        else:
            print("option invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()
