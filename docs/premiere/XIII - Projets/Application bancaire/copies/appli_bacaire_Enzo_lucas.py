# Dictionnaire pour stocker les comptes bancaires
comptes = {}

def creer_compte(ndc: str, nom: str, solde_ini: float = 0.0) -> None:
    """
    Crée un nouveau compte bancaire avec un numéro de compte unique.
    """
    if ndc in comptes:
        print(f"Le compte numéro {ndc} existe déjà.")
    else:
        comptes[ndc] = {'nom': nom, 'solde': solde_ini, 'transactions': []}
        print(f"Compte créé pour {nom} avec le numéro {ndc} et un solde initial de {solde_ini}€.")

def deposer(ndc: str, mad: float) -> None:
    """
    Dépose un montant sur le compte spécifié.
    """
    if ndc in comptes:
        if mad > 0:
            comptes[ndc]['solde'] += mad
            comptes[ndc]['transactions'].append(f"Dépôt de {mad}€")
            print(f"{mad}€ déposés sur le compte numéro {ndc}.")
        else:
            print("Le montant à déposer doit être positif.")
    else:
        print(f"Le compte numéro {ndc} n'existe pas.")

def retirer(ndc: str, mar: float) -> None:
    """
    Retire un montant du compte spécifié si le solde est suffisant.
    """
    if ndc in comptes:
        if mar > 0:
            if comptes[ndc]['solde'] >= mar:
                comptes[ndc]['solde'] -= mar
                comptes[ndc]['transactions'].append(f"Retrait de {mar}€")
                print(f"{mar}€ retirés du compte numéro {ndc}.")
            else:
                print("Solde insuffisant pour effectuer ce retrait.")
        else:
            print("Le montant à retirer doit être positif.")
    else:
        print(f"Le compte numéro {ndc} n'existe pas.")

def verifier_solde(ndc: str) -> None:
    """
    Affiche le solde actuel du compte spécifié.
    """
    if ndc in comptes:
        print(f"Le solde du compte numéro {ndc} est de {comptes[ndc]['solde']}€.")
    else:
        print(f"Le compte numéro {ndc} n'existe pas.")

def voir_transactions(ndc: str) -> None:
    """
    Affiche l'historique des transactions du compte spécifié.
    """
    if ndc in comptes:
        if comptes[ndc]['transactions']:
            print(f"Historique des transactions pour le compte numéro {ndc} :")
            for transaction in comptes[ndc]['transactions']:
                print(f" - {transaction}")
        else:
            print("Aucune transaction pour ce compte.")
    else:
        print(f"Le compte numéro {ndc} n'existe pas.")

def afficher_menu() -> None:
    """
    Affiche le menu principal avec les options disponibles.
    """
    print("\nMenu principal :")
    print("1. Créer un compte")
    print("2. Faire un dépôt")
    print("3. Faire un retrait")
    print("4. Vérifier le solde")
    print("5. Voir les transactions")
    print("6. Quitter")

def main() -> None:
    """
    Gère l'interaction avec l'utilisateur.
    """
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-6) : ")
        if choix == '1':
            ndc = input("Entrez le numéro de compte : ")
            nom = input("Entrez le nom du titulaire : ")
            try:
                solde_ini = float(input("Entrez le solde initial (optionnel, défaut 0) : ") or 0)
            except ValueError:
                print("Le solde initial doit être un nombre.")
                continue
            creer_compte(ndc, nom, solde_ini)
        elif choix == '2':
            ndc = input("Entrez le numéro de compte : ")
            try:
                mad = float(input("Entrez le montant à déposer : "))
            except ValueError:
                print("Le montant doit être un nombre.")
                continue
            deposer(ndc, mad)
        elif choix == '3':
            ndc = input("Entrez le numéro de compte : ")
            try:
                mar = float(input("Entrez le montant à retirer : "))
            except ValueError:
                print("Le montant doit être un nombre.")
                continue
            retirer(ndc, mar)
        elif choix == '4':
            ndc = input("Entrez le numéro de compte : ")
            verifier_solde(ndc)
        elif choix == '5':
            ndc = input("Entrez le numéro de compte : ")
            voir_transactions(ndc)
        elif choix == '6':
            print("Merci d'avoir utilisé l'application bancaire. Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 6.")

