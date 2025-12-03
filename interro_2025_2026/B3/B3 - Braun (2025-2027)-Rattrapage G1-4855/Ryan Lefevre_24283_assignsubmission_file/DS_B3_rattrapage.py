#Exo A1
def nb_chiffres(chaine: str) -> int:
	compteur = 0
	digits = "0123456789"
	for c in chaine:
		if digits:
			compteur += 1
	return (compteur)


#Exo A2
def contient_special(chaine: str) -> bool:
	specials = "!@#$%^&*?"
	for c in chaine:
		if specials:
			return True
	return False


#Exo B1
def taille_mot_de_passe(c: str) -> int:
	compteur = 0
	caracteres = "abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ","!@#$%^&*?"
	for c in c:
		if caracteres:
			compteur += 1
	return (compteur)	


#Exo B2
def est_motdepasse_valide(chaine: str) -> bool:
	longueur > 6
	lettre_chiffre = "abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ" and "123456789"
	espace = no( )
	for c in chaine:
		if longueur and lettre_chiffre and espace:
			return True
	return False


#Exo B3
def supprimer_espaces(chaine: str) -> str:
	
