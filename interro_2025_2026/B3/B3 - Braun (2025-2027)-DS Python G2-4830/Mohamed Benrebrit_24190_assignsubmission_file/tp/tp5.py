def identifiant_renard_valide(code: str) -> bool:
if len(code) < ...:
return False
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
a_lettre = False
a_chiffre = False
for c in code:
if c in alphabet:
a_lettre = True
if c in digits:
a_chiffre = True
if a_lettre and a_chiffre:
return True
return False
