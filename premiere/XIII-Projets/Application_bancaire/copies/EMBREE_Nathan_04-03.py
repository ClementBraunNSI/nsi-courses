comptes= {}

def creer_compte(num_compte : str, nom :str, solde : float, transactions : list) -> None:
    if num_compte not in comptes:
        dico = { 'nom' : nom,
                 'solde' : solde,
                 'transactions' : transactions
                 }
        comptes[num_compte] = dico

def deposer(num_compte : str, montant : float) -> None:
    if num_compte in comptes:
        comptes[num_compte]['solde'] += montant
        transaction = 'Dépôt de '+str(montant)+'€'
        comptes[num_compte]['transactions'].append(transaction)

def retirer(num_compte : str, montant : float) -> None:
    if num_compte in comptes:
        if comptes[num_compte]['solde'] >= montant:
            comptes[num_compte]['solde'] -= montant
            transaction = 'Retrait de '+str(montant)+'€'
            comptes[num_compte]['transactions'].append(transaction)
        else:
            print("Erreur : solde insuffisant")
        

def verifier_solde(num_compte : str) -> None:
    print(comptes[num_compte]['solde'])

def voir_transaction(num_compte : str) -> None:
    print(comptes[num_compte]['transactions'])
    
def afficher_menu() -> None:
    print('')
    print('1. Créer un compte')
    print('2. Faire un dépôt')
    print('3. Faire un retrait')
    print('4. Vérifier le solde')
    print('5. Voir les transactions')
    print('6. Quitter')
    print('')
    
    
def est_float(valeur):
    try:
        float(valeur)
        return True
    except ValueError:
        return False
    
    
def main() -> None:
    while True:
        afficher_menu()
        choix = input('Votre choix ici : ')
        while choix not in '123456':
            choix = input('Erreur de saisie, réessaye : ')
        choix = int(choix)
        
        if choix == 1:
            num_compte=input('Votre numéro de compte : ')
            nom=input('Votre nom : ')
            solde=input('Votre solde : ')
            while est_float(solde) is False:
                solde=input('Erreur de saisie, votre solde : ')
            solde=float(solde)
            creer_compte(num_compte,nom,solde,[])
            
        if choix == 2:
            num_compte=input('Votre numéro de compte : ')
            while num_compte not in comptes:
                num_compte=input('Erreur de saisie, votre numéro de compte : ')
            montant=input('Quel montant : ')
            while est_float(montant) is False:
                montant=input('Erreur de saisie, votre montant : ')
            montant=float(montant)
            deposer(num_compte,montant)
            
        if choix == 3:
            num_compte=input('Votre numéro de compte : ')
            while num_compte not in comptes:
                num_compte=input('Erreur de saisie, votre numéro de compte : ')
            montant=input('Quel montant : ')
            while est_float(montant) is False:
                montant=input('Erreur de saisie, votre montant : ')
            montant=float(montant)
            while comptes[num_compte]['solde'] < montant :
                montant=input('Saisir un montant plus raisonnable : ')
                while est_float(montant) is False:
                    montant=input('Erreur de saisie, votre montant : ')
                montant=float(montant)
            retirer(num_compte,montant)     
            
        if choix == 4:
            num_compte=input('Votre numéro de compte : ')
            while num_compte not in comptes:
                num_compte=input('Erreur de saisie, votre numéro de compte : ')
            verifier_solde(num_compte)
            
        if choix == 5:
            num_compte=input('Votre numéro de compte : ')
            while num_compte not in comptes:
                num_compte=input('Erreur de saisie, votre numéro de compte : ')
            voir_transaction(num_compte)
            
        if choix == 6:
            print('Merci, à bientôt !')
            return None

    
    
    
    
    
    
    
    
    
    
    