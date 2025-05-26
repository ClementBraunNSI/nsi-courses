def rendu_monnaie(montant:int, systeme:list[int])-> list[int]:
    solution = []
    for billet in systeme:
        while montant - billet >= 0:
            solution.append(billet)
            montant -= billet
    return solution

systeme = [50,20,10,5,2,1]
print(rendu_monnaie(53, systeme)) 