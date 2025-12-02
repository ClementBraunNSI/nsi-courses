print ("Partie A")

print ("exercice A1")
def nb_chiffres(chaine: str) -> int:
	compteur = 0
	digits = "0123456789"
	for c in chaine:
		if c in digits:
			compteur = compteur + 1 
	return compteur
print (nb_chiffres("azerty1234"))

print ("exercice A2")
def nb_lettres(chaine: str) -> int:
	compteur = 0
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for c in chaine:
		if c in alphabet:
			compteur +=1
	return compteur
	
print (nb_lettres("aZerTY1234"))

print ("exercice A3")
def contient_majuscule(chaine: str) -> bool:
	maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for c in chaine:
		if c in maj:
			return True
	return False
	
print (contient_majuscule("azerty1234A"))
print (contient_majuscule("azerty1234"))

print ("exercice A4")
def contient_special(chaine: str) -> bool: 
	specials = "!@#$%^&*?"
	for c in chaine:
		if c in specials:
			return True
	return False
print (contient_special("bonjour!"))
print (contient_special("bonjour"))

print ("exercice A5")
def contient_deux_types(chaine: str) -> bool:
	if nb_lettres(chaine) > 0:
		a_lettre = True
	else:
		a_lettre = False
	if nb_chiffres(chaine) > 0:
		a_chiffre = True
	else : 
		a_chiffre = False
	a_special = contient_special(chaine)
	if (a_lettre and a_chiffre) or (a_lettre and a_special) or (a_chiffre and a_special):
		return True
	return False
print (contient_deux_types("o2"))
print (contient_deux_types("o!"))
print (contient_deux_types("oO"))

print ("exercice A6")
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
print (score_motdepasse("A!213fel@"))
print (score_motdepasse("A213fe!"))
print (score_motdepasse("A23lllll"))
print (score_motdepasse("a!213fel@"))
print (score_motdepasse("Afel52ll"))
print (score_motdepasse("A!3fel@"))
print (score_motdepasse("1"))

print ("Partie B")

print ("exercice B1")
def repeter_caractere(c: str,n: int) -> str:
	result = ""
	for i in range (n):
		result += c
	return result
print (repeter_caractere("x", 5))

print ("exercice B2") 1/2
def masquer_motdepasse(chaine: str) -> str:
	mdpmasque = ""
	if len (chaine )<= 2:
		return chaine
	else: 
		mdpmasque += chaine[0]
		for i in range(chaine[1], len(chaine)-1): # faux
			mdpmasque += i
		mdpmasque += chaine[-1]
	return mdpmasque
print (masquer_motdepasse("azerty1234"))

print ("exercice B3") 1/2
def contient_trois_identiques(chaine: str) -> bool:
	car_prec = ""
	compteur = 0
	for i in chaine:
		print (car_prec)
		print(compteur)
		if car_prec != i:
			compteur == 0 #
			car_prec == i #
		elif i == car_prec:
			compteur +=1
			if compteur == 3 : 
				return True

	return False
print (contient_trois_identiques("azertyyy"))

print ("exercice B4") 1/2
def est_motdepasse_valide(chaine: str) -> bool:
	if len(chaine) >= 8: a_long = True
	else: a_long = False
	if contient_deux_types(chaine) : a_types = True
	else: a_types = False
	#if contient_trois_identiques(chaine): a_trois = True
	#else: a_trois = False
	for i in chaine: 
		if i == " ": a_espace = False
		else: a_espace = True # pas necessaire
	if contient_majuscule(chaine) = False: a_maj = True # faux ==
	else : a_maj = False
	chiffres = nb_chiffres(chaine)
	if chiffres >= 1: a_chiffres = True
	else: a_chiffres = False
	if a_long and a_types  and a_espace and a_maj and a_chiffres:
		return True
	return False
print (est_motdepasse_valide("L2!fdlfk21"))

print ("exercice B5")
def conseil_motdepasse(chaine: str) -> str:
	if est_motdepasse_valide(chaine): return "Bon MDP"
	else:
		message = ""
		if len(chaine) < 8: message += "rallonger le mot de passe jusqu'au moins 8 caractères."
		if contient_deux_types(chaine) = False: message += "ajouter un type de caractère."  
		if contient_trois_identiques(chaine): message += "Éviter d'utiliser 3 caractères consecutifs." 
		for i in chaine: 
			if i == " ": message += "eviter les espaces"
		if contient_majuscule(chaine) = False: message +="utiliser des majuscules."
		chiffres = nb_chiffres(chaine)
		if chiffres < 1: message +="utiliser au moins deux chiffres"
		return message
print (conseil_motdepasse("1"))
