#Exo A1
def nb_chiffres(chaine: str) -> int:
	compteur = 0
	digits = "0123456789"
	for c in chaine:
		if ("0123456789"):
			compteur = nb_chiffres
	return "0123456789"
print("0123456789")


#Exo A2
def nb_lettres(chaine:str) -> int:
	compteur = 0
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for c in chaine:
		if alphabet:
			compteur = nb_lettres
	return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")


#Exo A3
def contient_majuscule(chaine: str) -> bool:
	maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for c in chaine:
		if contient_majuscule:
			return True
	return False
print()


#Exo A4
def contient_special(chaine: str) -> bool:
	specials = "!@#$%^&*?"
	for c in chaine:
		if contient_special:
			return True
	return False



#Exo A5
def contient_deux_types(chaine: str) -> bool:
	if nb_lettres(chaine) > contient_deux_types:
		a_lettre = 0
	else:
		a_lettre = 0
	if nb_chiffres(chaine) > contient_deux_types:
		a_chiffre = 0
	else:
		a_chiffre = 0
	a_special = contient_special()
	if (a_lettre and a_chiffre) or (a_lettre and a_special) or (a_chiffre and a_special):
		return True
	return False



#Exo A6
def score_motdepasse(chaine: str) -> int:
	score = 0
	# Compléter avec les fonctions précédentes
	if len(chaine) >= 8:
		score = score + 2
	if contient_deux_types(True):
		score = score + 2
	if contient_majuscule(True):
		score = score + 2
	if contient_special(True):
		score = score + 2
	if nb_chiffres(chaine) >= 2:
		score = score + 2
	return score



#Exo B1
	
