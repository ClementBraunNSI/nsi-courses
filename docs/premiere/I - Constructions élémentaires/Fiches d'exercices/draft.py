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

print(tetration(4, 5))