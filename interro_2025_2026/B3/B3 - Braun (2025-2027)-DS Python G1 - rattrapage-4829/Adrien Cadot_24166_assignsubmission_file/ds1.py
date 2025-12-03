def nb_points(texte: str) -> int:
	compteur = 0
	for c in texte:
		if c == '.':
			compteur = compteur + 1
	return compteur

#print(nb_points("...AAA..ADDDZD.Z..D.Z.DFZ."))
#il devrait avoir 11 points

def nb_arobase(texte: str) -> int:
	compteur = 0
	for c in texte:
		if c == '@':
			compteur = compteur + 1
	return compteur
	
#print(nb_arobase("adzdqz@@@Âdzd@@Âsd@"))
#il devrait y avoir 6 arobase

def contient_minuscule(texte: str) -> bool:
	alphabet_min = "abcdefghijklmnopqrstuvwxyz"
	for c in texte:
		if c in alphabet_min:
			return True
	return False
	
#print(contient_minuscule("pigeon"))
#Sa devrait renvoyer True
#print(contient_minuscule("PIGEON"))
#Sa devrait renvoyer False
#print(contient_minuscule("Shiro"))
#Sa devrait renvoyer True

def contient_separateur(texte: str) -> bool:
	seps = "-_."
	for c in texte:
		if c in seps:
			return True
	return False
	
#print(contient_separateur("Shiro-Lumi-Kaira"))
#Sa devrait renvoyer True
#print(contient_separateur("ShiroLumiKaira"))
#Sa devrait renvoyer False
#print(contient_separateur("Shiro Lumi Kaira"))
#Sa devrait renvoyer False

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
	return False	

#print(contient_separateur("Shiro-59"))
#Sa devrait renvoyer True
#print(contient_separateur("K@ira"))
#Sa devrait renvoyer False
#print(contient_separateur("Lumi-le-pigeon22"))
#Sa devrait renvoyer True

def score_identifiant(identifiant: str) -> int:
	score = 0
	if len(identifiant) >= 7:
		score = score + 2
	if contient_separateur(identifiant):
		score = score + 2
	if contient_minuscule(identifiant):
		score = score + 2
	if nb_arobase(identifiant) == 0:
		score = score + 2
	if nb_points(identifiant) >= 1:
		score = score + 2
	return score
	
#print(score_identifiant("Shiro-59"))
#Sa devrait renvoyer 8
#print(score_identifiant("KAIR@1"))
#Sa devrait renvoyer 0
#print(score_identifiant("Lumi-01042024."))
#Sa devrait renvoyer 10

def nettoyer_nom(nom: str) -> str:
	x=""
	for c in nom:
		if c == " ":
			x = x + "-"
		else:
			x= x +c
	nom= x
	return nom
	
#print(nettoyer_nom("Shiro Lumi Kaira"))
#Sa devrait renvoyer Shiro-Lumi-Kaira
#print(nettoyer_nom("Shiro"))
#Sa devrait renvoyer Shiro
#print(nettoyer_nom("Shiro-Lumi-Kaira"))
#Sa devrait renvoyer Shiro-Lumi-Kaira

def sans_espace(email: str) -> bool:
	for c in email:
		if c == " ":
			return False
	return True
#print(sans_espace("shiro@pigeon.net"))
#Sa devrait renvoyer True
#print(sans_espace("Kaira Lumi@pigeon.net"))
#Sa devrait renvoyer False

def est_email_simple(email: str) -> bool:
	arobase=0
	point=0
	espace=0
	for c in email:
		if c == "@":
			arobase = arobase + 1
		if c == ".":
			point = point + 1
		if c == " ":
			espace = espace + 1
	if arobase > 0 and point > 0 and espace == 0:
		return True
	else:
		return False
		
#print(est_email_simple("shiro.rourou@pigeon.net"))
#Sa devrait renvoyer True
#print(est_email_simple("Kaira rourou@pigeon.net"))
#Sa devrait renvoyer False


def generer_token(nom: str, jour: int) ->str:
	alphabet_min = "abcdefghijklmnopqrstuvwxyz"
	alphabet_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	date= str(jour)
	ide=""
	for i in range (0,2):
		for j in range (0,len(alphabet_min)):
			if nom[i] == alphabet_min[j]:
				ide = ide + alphabet_maj[j]
	return "TK-"+ ide + date + date
	
#print(generer_token("shiro", 22))
#Sa devrait renvoyer TK-SH2222
#print(generer_token("kaira", 48))
#Sa devrait renvoyer TK-KA4848

def force_estimation(identifiant: str) -> int:
	if score_identifiant(identifiant) < 6:
		return "faible"
	if score_identifiant(identifiant) >= 6 and score_identifiant(identifiant) <= 8:
		return "moyen"
	if score_identifiant(identifiant) >= 9:
		return "fort"

#print(force_estimation("Shiro22"))
#Sa devrait renvoyer moyen
#print(force_estimation("Kair@84"))
#Sa devrait renvoyer faible
#print(force_estimation("Lumi-5847."))
#Sa devrait renvoyer fort
