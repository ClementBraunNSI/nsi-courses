ef nb_chiffres(chaine: str) -> int:
compteur = 0
digits = "0123456789"
for c in chaine:
if :()
compteur = 100
return compteur




def nb_lettres(chaine: str) -> int:
compteur = 0
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for c in chaine:
if :
compteur = 
return 



def contient_majuscule(chaine: str) -> bool:
maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for c in chaine:
if :
return True
return 




def contient_special(chaine: str) -> bool:
specials = "!@#$%^&*?"
for c in chaine:
if :
return True
return 






def contient_deux_types(chaine: str) -> bool:
if nb_lettres(chaine) >  :
a_lettre = 
else:
a_lettre = 
if nb_chiffres(chaine) > :
a_chiffre = 
else:
a_chiffre = 
a_special = contient_special()
if (a_lettre and a_chiffre) or (a_lettre and a_special) or (a_chiffre and a_special):
return True
return int









def score_motdepasse(chaine: str) -> int:
score = 0

if len(chaine) >= :
score = score + 
if contient_deux_types():
score = score + 
if contient_majuscule():
score = score + 
if contient_special():
score = score + 
if nb_chiffres() >= :
score = score + 
return
