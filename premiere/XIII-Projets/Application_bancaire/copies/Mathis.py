comptes = {}

def creer_compte(numero_compte: str, nom: str, solde_initial: float = 0, transactions: list = [])->None:
    if numero_compte not in comptes:
        comptes[numero_compte] = {
            'nom': nom,
            'solde': solde_initial,
            'transactions': transactions
        }
    else:
        print('numero de compte déjà existant')
        
#creer_compte('1', 'jsp', 1000.0)
#creer_compte('1', 'Cypher', 1000.0)
#print(comptes)

def deposer(numero_compte: str, montant: float)->None:
    if numero_compte in comptes:
        comptes[numero_compte]['solde'] += montant
        transaction = str(montant)
        comptes[numero_compte]['transactions'] += [f'+{transaction}']
            
#deposer('1', 500)
#print (comptes)

def retirer(numero_compte: str, montant: float)->None:
    if montant<comptes[numero_compte]['solde']:
        if numero_compte in comptes:
            comptes[numero_compte]['solde'] -= montant
            transaction = str(montant)
            comptes[numero_compte]['transactions'] += [f'-{transaction}']
    else:
        print ('vous ne possédez pas ce montant, transaction refusée')
#deposer('1', 700)
#print (comptes)

def verifier_solde(numero_compte: str)->int:
    return comptes[numero_compte]['solde']

#print (verifier_solde('1'))

def voir_transactions(numero_compte: str)->int:
    return comptes[numero_compte]['transactions']

#print (voir_transactions('1'))

def afficher_menu()->None:
    print ('1. Créer un compte')
    print ('2. Faire un dépôt')
    print ('3. Faire un retrait')
    print ('4. Vérifier le solde')
    print ('5. Voir les transactions')
    print ('6. Quitter')
    
def main()->None:
    rester=True
    while rester==True:
        afficher_menu()
        choix=str(input())
        if choix == '1':
            numero_compte = input('numéro de compte: ')
            nom = input('Entrez le nom du titulaire du compte: ')
            solde_initial = float(input('Entrez le solde initial (par défaut 0): ') or 0)
            creer_compte(numero_compte, nom, solde_initial)
            print (comptes)
            main()
       
        elif choix == '2':
            numero_compte = str(input('numéro de compte: '))
            if numero_compte in comptes:
                montant = float(input('montant à déposer: '))
                deposer(numero_compte, montant)
                print (comptes)
                main()
            else:
                print('ce compte ne figure pas ici')
                main()
                
        elif choix == '3':
            numero_compte = str(input('numéro de compte: '))
            if numero_compte in comptes:
                montant = float(input('montant à retirer: '))
                retirer(numero_compte, montant)
                print (comptes)
                main()
            else:
                print('ce compte ne figure pas ici')
                main()
        
        elif choix == '4':
            numero_compte = str(input('numéro de compte: '))
            if numero_compte in comptes:
                print (verifier_solde(numero_compte))
                main()
            else:
                print('ce compte ne figure pas ici')
                main()
        
        elif choix == '5':
            numero_compte = str(input('numéro de compte: '))
            if numero_compte in comptes:
                print (voir_transactions(numero_compte))
                main()
            else:
                print('ce compte ne figure pas ici')
                main()
    
        elif choix == '6':
            rester=False
    
main()