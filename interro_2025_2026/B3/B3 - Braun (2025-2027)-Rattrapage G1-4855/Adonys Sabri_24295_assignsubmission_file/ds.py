def nb_chiffres(chaine: str) -> int:
 compteur = 0
 digits = "0123456789"
 for c in chaine:
   if c in digits:
    compteur = compteur + 1
 return compteur

print (nb_chiffres("abcd"))
print (nb_chiffres("abcdef1"))

#A2


def contient_special(chaine: str) -> bool:
 specials = "!@#$%^&*?"
 for c in chaine:
  if c in specials:
   return True
  return False  

print (contient_special("abc"))
print (contient_special("@"))

#B1


 
def taille_mot_de_passe(chaine: str) -> int: 
 compteur = 0
 élèment = "abcdefj"
 for c in chaine:  
   compteur = compteur + 1
 return compteur
print (taille_mot_de_passe("abcdefj"))

#B2
def est_motdepasse_valide(chaine: str) -> bool:
  lettre = "abcdefghi"
  longueur = > 6
  for c in chaine:
   if c in longueur = > 6:
    return True
   return False
print (est_motdepasse_valide("abc")) 
