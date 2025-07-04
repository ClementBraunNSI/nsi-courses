import random
comptes={}
def creer_compte(numero_compte:str,nom:str,solde_initial:float,transactions:list):
    if numero_compte in comptes:
        print('Erreur: Le compte existe deja')
        return None
    comptes[numero_compte]={'nom':nom,
                             'solde': solde_initial,
                             'transactions': transactions
                             }
    return comptes
comptes=creer_compte('4','ewan',0.0,[])
print(comptes)
def deposer(numero_compte:str,montant:float):
    if numero_compte not in comptes:
        print("ce compte n'existe pas")
        return None
    comptes[numero_compte]['solde']+=montant
    comptes[numero_compte]['transactions'].append('+'+str(montant))
    return comptes
def retirer(numero_compte:str,montant:float):
    if numero_compte not in comptes:
        print("ce compte n'existe pas")
        return None
    if comptes[numero_compte]['solde']<montant:
        print("vous n'avez pas assez d'argent sur votre compte")
        return None
    comptes[numero_compte]['solde']-=montant
    comptes[numero_compte]['transactions'].append('-'+str(montant))
    return comptes
def verifier_solde(numero_compte):
    return comptes[numero_compte]['solde']
def voir_transactions(numero_compte):
    return comptes[numero_compte]['transactions']
def afficher_menu():
    print('1. Créer un compte')
    print('2. Faire un dépôt')
    print('3. Faire un retrait')
    print('4. Vérifier le solde')
    print('5. Voir les transactions')
    print('6. Quitter')
    a=int(input("choisissez un nombre correspondant a l'action que vous voulez faire: "))
    if a==1:
        print('vous avez choisis de creer un compte:')
        numero_compte=random.randint(1,99999999999)
        if numero_compte in comptes:
            while numero_compte in comptes:
                numero_compte=random.randint(1,99999999999)
        nom=input('saisissez votre nom: ')
        print('voici votre compte: ',creer_compte(numero_compte,nom,0.0,[]))
    elif a==2:
        print("vous avez choisis de deposer de l'argent:")
        numero_compte=input('saisissez votre numero de compte: ')
        if numero_compte not in comptes:
            print("aucun compte n'est associé avec votre numero")
            return None
        montant=float(input('choisissez le montant que vous voulez deposer: '))
        deposer(numero_compte,montant)
        print('vous avez maintenant',comptes[numero_compte]['solde'],'euros sur votre compte')
    elif a==3:
        print('vous avez choisis de faire un retrait:')
        numero_compte=input('saisissez votre numero de compte: ')
        if numero_compte not in comptes:
            print("aucun compte n'est associé avec votre numero")
            return None
        montant=float(input('choisissez le montant que vous voulez retirer: '))
        retirer(numero_compte,montant)
        print('vous avez maintenant',comptes[numero_compte]['solde'],'euros sur votre compte')
    elif a==4:
        print('vous avez choisis de verifier votre solde: ')
        numero_compte=input('saisissez votre numero de compte: ')
        if numero_compte not in comptes:
            print("aucun compte n'est associé avec votre numero")
            return None
        print('vous avez',verifier_solde(numero_compte),'euros sur votre compte')
    elif a==5:
        print('vous avez choisis de verifier vos transactions: ')
        numero_compte=input('saisissez votre numero de compte: ')
        if numero_compte not in comptes:
            print("aucun compte n'est associé avec votre numero")
        print('voici toutes vos transaction',voir_transactions(numero_compte))
    elif a==6:
        print('vous avez choisis de quitter: ')
    else:
        print('ERREUR! veuillez choisir un chiffre entre 1 et 6')
def main():
    numero_compte=input("bienvenue, veuillez saisir votre numero de compte pour pouvoir accéder a votre compte, si vous n'avez pas encore de compte ecrivez 0: ")
    if numero_compte=='0':
        print('vous avez choisis de creer un compte:')
        numero_compte=random.randint(1,99999999999)
        if numero_compte in comptes:
            while numero_compte in comptes:
                numero_compte=random.randint(1,99999999999)
        nom=input('saisissez votre nom: ')
        print('voici votre compte: ',creer_compte(numero_compte,nom,0.0,[]))
    elif numero_compte not in comptes:
        print("aucun compte n'est associé avec votre numero")
        return None
    while True :
        print('bonjour',comptes[numero_compte]['nom'])
        print('1-Gerer votre compte')
        print("2-Quitter")
        a=int(input('que souhaitez vous faire: '))
        if a==2:
            print("merci d'avoir utiliser notre apllication. Au revoir!")
            return None
        elif a==1:
            afficher_menu()
    
    
    
    
    