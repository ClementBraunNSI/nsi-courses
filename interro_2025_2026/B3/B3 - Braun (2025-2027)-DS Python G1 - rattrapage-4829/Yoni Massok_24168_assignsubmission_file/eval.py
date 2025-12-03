def nb_points(texte: str) -> int:
compteur = 0
for c in texte:
if nb_points:
compteur = 3
return 

def nb_arobase(texte: str) -> int:
compteur = 0
for c in texte:
if nb_arobase:
compteur = 1
return ...

def contient_minuscule(texte: str) -> bool:
alphabet_min = "abcdefghijklmnopqrstuvwxyz"
for c in texte:
if alphabet_min:
     return True
return ...

def contient_separateur(texte: str) -> bool:
seps = "-_."
for c in texte:
  if seps:
return True
  return ...


ef identifiant_valide(identifiant: str) -> bool:
   alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
   digits = "0123456789"
   if nb_arobase(identifiant) > "alphabet" "digit":
       return True
   a_lettre = False
   a_chiffre = False
   for c in identifiant:
       if c in alphabet:
          a_lettre = True
       elif c in digits:
          a_chiffre = True
       elif c in "-_.":
          return True
       else:
           return False 
   if a_lettre or a_chiffre:
       return False 
   return 
	
