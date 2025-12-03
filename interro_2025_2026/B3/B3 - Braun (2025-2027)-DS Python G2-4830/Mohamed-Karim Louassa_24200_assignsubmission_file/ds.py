#PARTIE A
print("____PARTIE A____")


def nb_occurrences(texte: str, lettre: str) -> int:
	compteur = 0
	for c in texte:
		if lettre in c:
			compteur = compteur+1
	return compteur
	
print(nb_occurrences("BQ","B"))

print(nb_occurrences("BBQ","B"))

print("------------------")

def contient_majuscule(nom: str) -> bool:
	maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for c in nom:
		if c in maj:
			return True
	return False

print(contient_majuscule("arrah"))

print(contient_majuscule("Arrah"))

print("------------------")

def contient_separateur(code: str) -> bool:
	seps = "-_"
	for c in code:
		if c in seps:
			return True
	return False

print(contient_separateur("mohamed-karim"))

print(contient_separateur("mohamedkarim"))

print("------------------")

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

print(contient_deux_types("Fortinte"))

print("-----------------")
	
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
	
print(identifiant_renard_valide("Fortnite2"))
print("------------------")
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
print(score_renard("FortniteR-6"))

print("------------------------------------")


#PARTIE B
print("____PARTIE B____")
print("B1:")
def repeter_hurlement(c: str, n: int) -> int:
	rep=0
	for rep in range(rep,n):
		print(c)
print(repeter_hurlement("Je suis Iron Man",8))

print("------------------")
print("B2:")
def compter_voyelles(nom: str) -> int:
	compteur=0
	voyelles = "aeiouyAEIOUY"
	for c in nom:
		if c in voyelles:
			compteur= compteur +1 
	return compteur
print(compter_voyelles("Monsieur Braun c'est le meilleur des profs)"))

print("------------------")

print("B3:")

def categorie_age_renard(age:int) -> str:
	if age>6:
		return "Senior"
	elif age>=2 and age<=6:
		return "Adulte"
	else:
		return "Junior"

print(categorie_age_renard(7))

print("------------------")
print("B4:")

def identifiant_suivi(nom:str, annee:int) ->str:
	a="RX"+"-"+str(annee)+"-"+nom
	return a
print(identifiant_suivi("KingVon",2021))

print("------------------")
print("B5:")

def inverser_chaine(chaine):
	superchaine=""
	for caractere in chaine:
		superchaine= caractere + superchaine
	return superchaine
print(inverser_chaine("fortnite"))









