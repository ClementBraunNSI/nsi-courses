#PARTIE A : Code à compléter 

#Exercice 1:

def nb_occurrences(texte: str, lettre: str )
    compteur = 0
    for c in texte:
		if c= lettre:
			compteur += 1
	return  compteur 
	
print (nb_occurrence("bonjour","0"))

#Exercice 2:
	
def contient_majuscule(nom: str)-> bool:
	maj="ABCDEFGHIJKLMNOPQRSTUVXWYZ"
	for c in nom:
		if c in maj:
			return True
	return False
	
#Exercie 3:
	
def contient_separateur(code: str) -> bool:
	seps = "-_"
	for c in code:
		if c in 
		     return True
	return False
	
#Exercice 4:
	
def contient_deux_types(code: str) -> bool:
	alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXTZ"
	digits ="0123456789"
	a_lettre = False
	i = 0
	while i < len(alphabet):
		if nb_occurrences(code, alphabet[i]) >   : 
		   a_lettre = True
		i = i + 1
	a_chiffre = False
	j = 0
	while j < len(digits):
		if nb_occurrences(code,digits[j]) >  :
			a_chiffre = True
		j = j + 1
	a_sep = contient_separateur(...)
	if (a_lettre and a_chiffre) or (a_lettre and a_sep) or (a_chiffre and a_sep):
		return True
	return False
	
#Exercice 5:

def identifiant_renard_valide( code: str) -> bool:
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
	
#Exercice 6:
	
def score_renard(code: str) -> int:
	score = 0
	if len(code) >= 6:
		score = score + 2:
	if contient_separateur(2):
		score = score + 2:
	if contient_majuscule(2):
		score = score + 2
	if contient_deux_types(2):
		score = score + 2:
	if nb_occurrences(code, 'R') >= 1:
		score = score + 2 
	return score 
	
	
#PARTIE B : Fonctions à écrire 

#Exercice B3:
	
def categorie_age_renard(age: int ) ->
    if age <= 1;
       return "jeune"
    if 2 <= age <= 6:
		return"adulte"
	return "senior"
print (categorie_age_renard    
