def nb_occurences(texte: str, lettre: str) -> int:
	compteur = 0
	for c in texte:
		if lettre in texte :
			compteur = compteur + 1
		return compteur
		

def contient_majuscule(nom: str) -> bool:
	maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for c in nom:
		if c in maj:
			return True
	return False



def contient_separateur(code: str) -> bool:
	seps = "-_"
	for c in code:
		if c in seps:
			return True
	return False


def contient_deux_types(code: str) -> bool:
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	digits = "0123456789"
	a_lettre = False
	# au moins une lettre ?
	i = 0
	while i < len(alphabet):
		if nb_occurrences(code, alphabet[i]) > 0:
			a_lettre = True
		i = i + 1
	a_chiffre = False
	j = 0
	while j < len(digits):
		if nb_occurrences(code, digits[j]) > 0:
			a_chiffre = True
		j = j + 1
	a_sep = contient_separateur(code)
	if (a_lettre and a_chiffre) or (a_lettre and a_sep) or (a_chiffre and a_sep):
		return True
	return False
	



def identifiant_renard_valide(code: str) -> bool:
	if len(code) < 6:
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
	if nb_occurrences(code, 'R') >= 1:
		score = score + 2
	return score




def repeter_hurlement(c:str, n:int) -> int:
	compteur =0
	for compteur in range(compteur,n):
		print(c)

print(repeter_hurlement("Je suis un renard",2))
		
	
def compter_voyelles(nom: str) -> int:
	x = 0
	voyelles = "aeiouyAEIOUY"
	for c in nom:
		if c in voyelles:
			x = x + 1
	return x

print(compter_voyelles("eau"))

def categorie_age_renard(age:int) -> str:
		if age <= 1:
			print("Jeune")
		elif 2 <= age and age <= 6:
			print("Adulte")
		else:
			print("Senior")

print(categorie_age_renard(5))


def identifiant_suivi(nom:str, annee:int) -> str:
	y = "RX" +"-"+str(annee)+"-"+nom
	return y
	
print(identifiant_suivi("Automoto",1842))


def inverser_chaine(chaine:str) -> str:
	for i in range(chaine)):
		
		
	
print(inverser_chaine(inverse))

	
		
		
	
