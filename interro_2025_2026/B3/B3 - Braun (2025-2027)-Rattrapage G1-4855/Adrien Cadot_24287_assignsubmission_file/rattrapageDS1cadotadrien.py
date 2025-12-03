def nb_chiffres(chaine: str) -> int:
	compteur = 0
	digits = "0123456789"
	for c in chaine:
		if c in digits:
			compteur = compteur + 1
	return compteur

#print(nb_chiffres("Pige0n22"))
#Sa devrait renvoyer 3
#print(nb_chiffres("01082006"))
#Sa devrait renvoyer 8

def nb_lettres(chaine: str) -> int:
	cpt=0
	lettres="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for c in chaine:
		if c in lettres:
			cpt += 1
	return cpt

#print(nb_lettres("Pigeon"))
#Sa devrait renvoyer 6
#print(nb_lettres("Shirolegrospigeon"))
#Sa devrait renvoyer 17

def espace(chaine: str) -> bool:
	esp=" "
	for c in chaine:
		if c == esp:
			return True
	return False

#print(espace("Pigeon"))
#Sa devrait renvoyer False
#print(espace("Shiro le gros pigeon"))
#Sa devrait renvoyer True

def contient_special(chaine: str) -> bool:
	specials = "!@#$%^&*?"
	for c in chaine:
		if c in specials:
			return True
	return False
	
#print(contient_special("pigeon!"))
#Sa devrait renvoyer True
#print(contient_special("Shiro"))
#Sa devrait envoyer False

def taille_mot_de_passe(c: str) -> int:
	cpt=0
	for i in c:
		if c is not None:
			cpt += 1
	return cpt

#print(taille_mot_de_passe("Pigeon221"))
#Sa devrait renvoyer 9
#print (taille_mot_de_passe(""))
#Sa devrait renvoyer 0

def est_motdepasse_valide(chaine: str) -> bool:
	if len(chaine) >= 6 and nb_lettres(chaine) > 1 and nb_chiffres(chaine) > 1 and espace(chaine) == False:
		return True
	return False
	
#print(est_motdepasse_valide("Pigeon11"))
#Sa devrait renvoyer True
#print(est_motdepasse_valide("Shiro 11"))
#Sa devrait renvoyer False
#print(est_motdepasse_valide("Shiro"))
#Sa devrait renvoyer False

def supprimer_espaces(chaine: str) -> str:
	esp=" "
	nouvchaine=""
	for c in chaine:
		if c == esp:
			None
		else:
			nouvchaine += c
	return nouvchaine

#print(supprimer_espaces("Les pigeons"))
#Sa devrait renvoyer Lespigeons
#print(supprimer_espaces("ShiroLumiKaira"))
#Sa devrait renvoyer ShiroLumiKaira
