def renverse(chaine):
    res = ""
    for char in chaine:
        res = char + res
    return res

print(renverse("Mr Braun c'est le meilleur prof de NSI"))