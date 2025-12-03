
'''Exercice A1
'''
def nb_occurrences(texte: str, lettre: str) -> int:
	compteur = 0
	for c in texte:
		if lettre in texte:
			compteur = c + 1
	return compteur

'''Exercice A2

'''
def contient_majuscule(nom: str) -> bool:
	maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for c in nom:
		if c == maj:
			return True
	return False

'''Exercice A3

'''
def contient_separateur(code: str) -> bool:
	seps = "-_"
	for c in code:
		if c == seps:
			return True
	return False	

'''Exercice A4

'''
def contient_deux_types(code: str) -> bool:
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	digits = "0123456789"
	a_lettre = False
	# au moins une lettre ?
	i = 0
	while i < len(alphabet):
		if nb_occurrences(code, alphabet[i]) > 1:
			a_lettre = True
		i = i + 1
	a_chiffre = False
	j = 0
	while j < len(digits):
		if nb_occurrences(code, digits[j]) > 1:
			a_chiffre = True
		j = j + 1
	a_sep = contient_separateur(True)
	if (a_lettre and a_chiffre) or (a_lettre and a_sep) or (a_chiffre and a_sep):
		return True
	return False
	
	
''' Exercice A5	

'''
def identifiant_renard_valide(code: str) -> bool:
	if len(code) < 6 :
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


''' Exercice A6
'''
def score_renard(code: str) -> int:
	score = 0
	if len(code) >= 6:
		score = score + 2
	if contient_separateur(True):
		score = score + 2
	if contient_majuscule(True):
		score = score + 2
	if contient_deux_types(True):
		score = score + 2
	if nb_occurrences(code,'R' ) >= 1:
		score = score + 2
	return score





