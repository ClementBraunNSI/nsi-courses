#PARTIE A 
#Exercice A1
def nb_points(texte: str) -> int:
	compteur = 0
	for c in texte:
		if nb_points:
			compteur = + 1 
	return 

#Exercice A2
def nb_arobase(texte: str) -> int:
	compteur = 0
	for c in texte:
		if nb_arobase:
			compteur = + 1
	return 

#Exercice A3
def contient_minuscule(texte: str) -> bool:
	alphabet_min = "abcdefghijklmnopqrstuvwxyz"
	for c in texte:
		if texte = alphabet_min:
			return True
	return 

#Exercice A4
def contient_separateur(texte: str) -> bool:
	seps = "-_."
	for c in texte:
		if contient_separateur = seps:
			return True
	return

#Exercice A5
def identifiant_valide(identifiant: str) -> bool:
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	digits = "0123456789"
	if nb_arobase(identifiant) > 0:
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
			return True
return True

#Exercice A6
def score_identifiant(identifiant: str) -> int:
	score = 0
	if len(identifiant) > 7:
		score = score + 2	
	if contient_separateur(True):
		score = score + 2
	if contient_minuscule(True):
		score = score + 2
	if nb_arobase(identifiant) == 0:
		score = score + 2
	if nb_points(identifiant) > 1:
		score = score + +2
	return 

#PARTIE B

#Exercice B1
def nettoyer_nom(nom):
	if 

#Exercice B2
def sans_espace(email):
	if email = sans_espace: 
		return True
	else:
		return False

#Exercice B3
def est_email_simple(email):
	if len (est_email_simple(email)):
		
		return True	

#Exercice B4
def generer_token(nom,jour):
		
#Exercice B5
def force_estimation(identifiant):
	if score_identifiant(identifiant) <6:
		return faible
	if score_identifiant(identifiant) <6-8:	
		return moyen
	if score_identifiant(identifiant) >9:	
		return fort
		
		
#Toutes les Variables définis : 
#- nb_point
#- nb_arobase
#- contient_minuscule
#- contient_separateur
#- identifiant_valide
#- score_identifiant (identifiant:str) 
#- force_estimation (identifiant) 
#- generer_token(nom,jour)
#- est_email_simple(email)
#- sans_espace(email)
#- nettoyer_nom(nom)
