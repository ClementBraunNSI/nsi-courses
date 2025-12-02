#1
def nb_chiffres(chaine:str) -> int:
	compteur = 0 
	digits= "0123456789"
	for c in chaine:
		if c in digits:
			compteur = compteur +1
	return compteur
	
print("ex1 ",nb_chiffres("12azer43"))

#2
def nb_lettres(chaine: str) -> int:
	compteur = 0
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for c in chaine:
		if c in alphabet:
			compteur = compteur +1
	return compteur
	
print("ex2 ",nb_lettres("lucas"))

#3
def contient_majuscule(chaine: str) -> bool:
	maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for c in chaine:
		if c in maj:
			return True
	return False

print("ex3 ",contient_majuscule("Lucas"))
print("ex3 ",contient_majuscule("nortier"))

#4
def contient_special(chaine: str) -> bool:
	specials = "!@#$%^&*?"
	for c in chaine:
		if c in specials:
			return True
	return False
	
print("ex4" , contient_special("Lucas#"))

#5
def contient_deux_types(chaine: str) -> bool:
	if nb_lettres(chaine) > 0 :
		a_lettre = True
	else:
		a_lettre = False
	if nb_chiffres(chaine) > 0:
		a_chiffre = True
	else:
		a_chiffre = False
	a_special = contient_special(chaine)
	if (a_lettre and a_chiffre) or (a_lettre and a_special) or (a_chiffre and a_special):
		return True
	return False

print("ex5 ",contient_deux_types("Lucas59"))
print("ex5 ",contient_deux_types("Lucas#"))
print("ex5 ",contient_deux_types("Lucas"))

#6
def score_motdepasse(chaine: str) -> int:
	score = 0
	# Compléter avec les fonctions précédentes
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

print("ex6 ",score_motdepasse("Lucas59"))
print("ex6 ",score_motdepasse("Lucas59@@"))
print("ex6 ",score_motdepasse("lucas"))

#PARTIE B
#1
def repeter_caractere(c:str,n:int)->str:
	return c * n

print("b1 ",repeter_caractere("1",3))
print("b1 ",repeter_caractere("Lucas",3))

#2
def masquer_motdepasse(chaine:str)->str:
	chiffrer = ""
	nb_carac = len(chaine)
	if len(chaine) <=2 : 
		return chaine
	for i in range(len(chaine)):
		if i == 0  or i == (len(chaine)-1):
			chiffrer = chiffrer + chaine[i]
		else :
			chiffrer = chiffrer + "*"
	return chiffrer

print("b2 ",masquer_motdepasse("Lucas"))
print("b2 ",masquer_motdepasse("Sécurité"))

#3
def contient_trois_identiques(chaine:str)->bool:
	affilee=0
	for i in range(len(chaine)):
		if chaine[i] == chaine[i-1]:
			affilee=affilee+1
			if affilee == 3 :
				return True
	return False

print("b3 ",contient_trois_identiques("aaa"))
print("b3 ", contient_trois_identiques("abaa"))
print("b3 ", contient_trois_identiques("Aaa"))
print("b3 ", contient_trois_identiques("@@@"))

#4
def est_motdepasse_valide(chaine:str)->bool:
	espace = " "
	if len(chaine) >= 8 and contient_deux_types(chaine) == True and contient_trois_identiques(chaine) == False and  not espace in chaine   and contient_majuscule(chaine) == True and nb_chiffres(chaine) > 0 :
		return True
	else :
		return False
print("b4 ",est_motdepasse_valide("Lucas"))
print("b4 ",est_motdepasse_valide("Lucas Nortier"))
print("b4 ",est_motdepasse_valide("Lucas59@"))

#5
def conseil_motdepasse(chaine:str)->str:
	conseil =""
	espace = " "
	
	if est_motdepasse_valide(chaine) == False:
		if len(chaine) <= 8 : 
			conseil = conseil +"alonger à +8, "
		if contient_deux_types(chaine) == False:
			conseil = conseil + "utiliser 2 type de caractère dans votre mdp, "
		if contient_trois_identiques(chaine) == True :
			conseil = conseil + "n'utiliser pas + de 3 fois le même caractère d'affilée, "
		if espace in chaine : 
			conseil = conseil + " n'utiliser pas d'espace, "
		if contient_majuscule(chaine) == False:
			conseil = conseil + "utiliser des majuscules, "
		if nb_chiffres(chaine) == 0 :
			conseil = conseil + "utiliser des chiffres."
	return conseil
	
print("b5 ",conseil_motdepasse("Lucas"))
print("b5 ",conseil_motdepasse("Lucaaas"))
print("b5 ",conseil_motdepasse("Lucas59"))
print("b5 ",conseil_motdepasse("Lucas nortier"))
