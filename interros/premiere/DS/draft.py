def est_divisible(a,b):
    return a%b == 0

def tous_les_diviseurs(a):
    l = []
    for i in range(1,a):
        if est_divisible(a,i):
            l.append(i)
    return l

def somme_elements_listes(l):
    return sum(l)

def est_parfait(a):
    return somme_elements_listes(tous_les_diviseurs(a)) == a

def liste_parfaits(n):
    l = []
    for i in range(n):
        if est_parfait(i):
            l.append(i)
    return l

print(liste_parfaits(3000))