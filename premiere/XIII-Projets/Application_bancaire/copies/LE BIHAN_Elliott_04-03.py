comptes = {}

def creer_compte():
    numero = input("Numéro du compte : ")
    if numero in comptes:
        print("Ce compte existe déjà.")
        return
    nom = input("Nom du titulaire : ")
    solde = float(input("Solde initial : "))
    comptes[numero] = {"nom": nom, "solde": solde, "transactions": []}
    print("Compte créé.")

def deposer():
    numero = input("Numéro du compte : ")
    if numero not in comptes:
        print("Compte introuvable.")
        return
    montant = float(input("Montant à déposer : "))
    if montant > 0:
        comptes[numero]["solde"] += montant
        comptes[numero]["transactions"].append("Dépôt: " + str(montant) + "€")
        print("Dépôt réussi.")
    else:
        print("Montant invalide.")

def retirer():
    numero = input("Numéro du compte : ")
    if numero not in comptes:
        print("Compte introuvable.")
        return
    montant = float(input("Montant à retirer : "))
    if 0 < montant <= comptes[numero]["solde"]:
        comptes[numero]["solde"] -= montant
        comptes[numero]["transactions"].append("Retrait: " + str(montant) + "€")
        print("Retrait réussi.")
    else:
        print("Montant invalide ou solde insuffisant.")

def verifier_solde():
    numero = input("Numéro du compte : ")
    if numero in comptes:
        print("Solde : " + str(comptes[numero]['solde']) + "€")
    else:
        print("Compte introuvable.")

def voir_transactions():
    numero = input("Numéro du compte : ")
    if numero in comptes:
        print("Historique :", *comptes[numero]['transactions'], sep="\n-")
    else:
        print("Compte introuvable.")

def main():
    fin = True
    while fin:
        print("1. Créer un compte")
        print("2. Déposer")
        print("3. Retirer")
        print("4. Vérifier solde")
        print("5. Voir transactions")
        print("6. Quitter")
        choix = input("Choisissez : ")
        if choix == "1":
            creer_compte()
        elif choix == "2":
            deposer()
        elif choix == "3":
            retirer()
        elif choix == "4":
            verifier_solde()
        elif choix == "5":
            voir_transactions()
        elif choix == "6":
            fin = False
            print("Impossible de quitter, vous restez dans le programme.")
        else:
            print("Choix invalide.")