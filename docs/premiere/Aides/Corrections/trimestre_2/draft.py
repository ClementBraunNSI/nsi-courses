def fusionner_dico(dico1, dico2):
    fusion = dico1
    for clef in dico2:
        fusion[clef] = dico2[clef]
    return fusion

def fusionner_dico2(dico1, dico2):
    fusion = {}
    for i in dico1:
        for j in dico2:
            print(i,j)
            if i==j:
                fusion[i] = dico2[i]
            elif i in dico1 and not i in dico2:
                fusion[i] = dico1[i]
            elif j in dico2 and not j in dico1:
                fusion[j] = dico2[j]
    return fusion
print(fusionner_dico2({"a": 1, "b": 2}, {"b": 3, "c": 4}))