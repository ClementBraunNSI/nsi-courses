def cercle(n):
    return 2 * 3.14 * n

def carre(n):
    return 4 * n

def triangle_equilateral(n):
    return 3 * n

def pentagone_regulier(n):
    return 5 * n

def perimetre(forme,n):
    return forme(n)

liste_formes = [cercle,carre,triangle_equilateral,pentagone_regulier]

for forme in liste_formes:
    print(perimetre(forme,5))