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

print(somme_chiffres(1234))
