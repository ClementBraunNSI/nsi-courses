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

f(10)
