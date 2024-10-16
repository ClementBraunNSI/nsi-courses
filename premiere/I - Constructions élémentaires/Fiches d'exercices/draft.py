import sys
sys.set_int_max_str_digits(10000)

def tetration(nombre, tetre):
    if tetre == 1:
        return nombre
    else:
        cpt = 2
        puissance = nombre
        while cpt < tetre:
            puissance = puissance ** nombre
            print(puissance)
            cpt += 1
        return nombre**puissance
    
def tetration_2(n,tetre):
    puissance = n
    if tetre == 0:
        return 1
    elif tetre == 1:
         return n
    else:
        for i in range(2,tetre):
            puissance = puissance ** n
    return n**puissance

print(tetration(3,4))
print(tetration_2(3,4))
    
def est_premier(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def somme_premiers(n):
    somme = 0
    for i in range(1, n+1):
        if est_premier(i):
            somme += i
    return somme

def f(n):
        x = 0
        y = 1
        chaine = ''
        for i in range(n):
            print(x)
            y = x + y
            x = y - x

def multiplication_par_addition(nombre : int, multiple : int)-> int:
        resultat = 0
        for i in range(multiple):
            resultat = resultat + nombre
        return resultat

def compter_voyelles(chaine : str)-> int:
        voyelles = 0
        for lettre in chaine:
            if lettre in 'aeiouAEIOU' :
                voyelles = voyelles + 1
        return voyelles

def puissance(nombre_1 : int, nombre_2 : int)-> int:
        resultat = 1
        for i in range(nombre_2):
            resultat = resultat * nombre_1
        return resultat

def est_premier(nombre : int)-> bool:
        diviseurs = 0
        for i in range(1,nombre+1):
            if nombre%i == 0:
                diviseurs = diviseurs + 1
        if diviseurs == 2 :
            return True
        else:
            return False
        
def somme_chiffres(nombre : int)-> int:
        somme = 0
        str_nombre = str(nombre)
        for chiffre in str_nombre:
            somme = somme + int(chiffre)
        return somme

def nombre_parfait(nombre : int)-> int:
        somme = 0
        for i in range(1,nombre):
            if nombre % i == 0:
                somme = somme + i
        print(somme)
        if somme == nombre:
            return True
        else:
            return False

def fibonacci(borne : int)-> None:
            x = 0
            y = 1
            for i in range(borne):
                print(x)
                y = x + y
                x = y - x

def nombre_armstrong(nombre : int)-> bool:
            str_nombre = str(nombre)
            somme = 0
            taille = len(str_nombre)
            for chiffre in str_nombre:
                carre = int(chiffre)**taille
                somme = somme + carre
            if somme == nombre:
                return True
            else:
                return False
            
def somme_premiers(borne : int)-> int:
            somme = 0
            for i in range(borne+1):
                if est_premier(i):
                    somme = somme + i
            return somme

def compter_occurences(chaine : str, caractere : str)-> int:
            compteur = 0
            for carac in chaine:
                if carac == caractere:
                    compteur = compteur + 1
            return compteur


