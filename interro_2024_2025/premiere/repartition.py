import random

eleves = ['Osama','Mathis','Lucas','Hugo','Leon','Liam','Nathan','Ewan','Lois','Maxime','Elliott','Ethan','Nolann','Terry','Lino','Lowen','Enzo','Christopher']

sujet_1 = random.sample(eleves,9)
sujet_2 = [eleve for eleve in eleves if eleve not in sujet_1]


eleve = {eleve:0 for eleve in eleves}
def ajouter_point():
    while True:
        eleve_a_rajouter = input("Nom eleve")
        if eleve_a_rajouter == "break":
            break
        points_a_rajouter = int(input("nb points"))
        eleve[eleve_a_rajouter] += points_a_rajouter

ajouter_point()
print(eleve)