def contient_majuscule(nom: str) -> bool:
maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for c in nom:
if c == maj: 
    return True
return maj
