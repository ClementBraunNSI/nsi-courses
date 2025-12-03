#partie a 
#exercice 1
def nb_occurrence (texte: str, lettre: str) -> int:
	compteur = 0
	for c in texte:
		if c == lettre: 
			compteur += 1
	return compteur 


#exercice 2
def contient_majuscule (nom: str) -> bool:
	maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for c in nom: 
		if c in maj:
			return True
	return False

#exercice 3
def contient_separateur(code: str) -> bool:
	seps = "-_"
	for c in code: 
		if c in seps:
			return True
	return False

#exercice 4
def contient_deux_types(code: str) -> bool:
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	digits = "012345689"
	a_lettre = False
	i = 0
	while i < len(alphabet):
		if nb_occurrence(code, alphabet[i]) > 0:
			a_lettre = True
		i = i + 1
	a_chiffre = False
	j = 0 
	while j < len(digits):
		if nb_occurrence(code, digits[j]) > 0:
			a_chiffre = True
		j = j + 1
	a_sep = contient_separateur(code)
	if (a_lettre and a_chiffre) or (a_lettre and a_sep) or (a_chiffre and a_sep):
		return True
	return False

#exercice 5:
def identifiant_renard_valide(code: str) -> bool:
	if len(code) < 6:
		return False
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	digits = "012345689"
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

#exercice 6:
def score_renard(code: str) -> int:
	score = 0
	if len(code) >= 6:
		score = score + 2
	if contient_separateur(code):
		score = score + 2
	if contient_majuscule(code):
		score = score + 2
	if contient_deux_types(code):
		score = score + 2
	if nb_occurrence(code, 'R') >= 1:
		score = score + 2
	return score

#parie B
#exercice 1
def repeter_hurlement(c: str, n: int) -> str:
	hurlement = c * n
	return hurlement

print (repeter_hurlement("s", 7))

#exercice 2
def compter_voyelles(nom: str) -> int:
	nb = 0 
	voyelles = "aeiouyAEIOUY"
	for c in nom: 
		if c in voyelles: 
			nb += 1 
	return nb 

print (compter_voyelles("bonjour"))

#exercice 3:
def categorie_age_renard(age: int) -> str:
	if age <= 1:
		return "jeune"
	if 2 <= age <= 6:
		return "adulte"
	return "Senior"

print (categorie_age_renard(1))

#exercice 4:
def identifiant_suivi(nom: str, annee: int) -> str:
	return "RX-" + str(annee) + "-" + nom 

print (identifiant_suivi("Milo", 2025))

#exercice 5:
def inverser_chaine(chaine: str) -> str:
	nv = ""
	for i in range (len(chaine)-1,-1, -1):
		nv += chaine[i] 
	return nv
	
print (inverser_chaine("bonjour"))
	
