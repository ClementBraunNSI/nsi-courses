#exo 1
def nb_chiffres(chaine: str) -> int:

	compteur = 0
	
	digits = "012456789"
	
	for c in chaine:
	
		if c in digits:
			compteur = compteur +1 
	return compteur

print(nb_chiffres ("odfh12"))

#exo 2 
def nb_lettres(chaine: str) -> int:
	
	compteur = 0
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	for c in chaine:
		if c in alphabet:
			compteur = compteur +1
	return compteur
	
print(nb_lettres("sggsgssg"))

#exo 3 

def contient_majuscule(chaine: str) -> bool:
	
	maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	for c in chaine:
		if c in maj:
		
			return True
		else :
			return False
	return chaine
	
print(contient_majuscule("ODGO"))

#exo4
def contient_special(chaine: str) -> bool:
	
	specials = "!@#$%^&*?"
	
	for c in chaine:
		if c in specials:
			return True
		else :
			return False
	return chaine
	
#print(contient_special("GG"))

#exo5 
def contient_deux_types(chaine: str) -> bool: 
	if nb_lettres(chaine) > 0:
		a_lettre = True
	else:
		a_lettre = False
	if nb_chiffres(chaine) > 0 :
		a_chiffre = True
	else:
		a_chiffre = False
	a_special = contient_special(chaine)
	if (a_lettre and a_chiffre) or (a_lettre and a_special) or (a_chiffre and a_special):
		return True
	else : 
		return 	False
	return chaine

print(contient_deux_types("@!AS"))

#exo6 
def score_motdepasse(chaine: str) -> int:
	score = 0
	
	if len(chaine) >= 8:
		score = score + 2
		
	if contient_deux_types(chaine):
		score = score + 2
		
	if contient_majuscule(chaine):
		score = score + 2
		
	if contient_special(chaine):
		score = score + 2
		
	if nb_chiffres(chaine) >= 2:
		score = score + 2
	return score
	
print(score_motdepasse("azertyOP8*"))
