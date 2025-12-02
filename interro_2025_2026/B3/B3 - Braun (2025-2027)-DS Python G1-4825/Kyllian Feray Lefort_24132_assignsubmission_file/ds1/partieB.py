from partieA import *
#exob1
def repeter_caractere(c:str , n:int ) -> str:


	return c * n

print(repeter_caractere('X', 5))

#exob2
def masquer_motdepasse(chaine:str ) -> str:
	chiffrer = chaine = f"{chaine[1]}****{chaine[5]}"
	
	if len(chaine) <= 2: 
		return chaine
	if len(chaine) >= 2:
		return chiffrer
	
	
	
print(masquer_motdepasse("opsggs"))

#exob3
def contient_trois_identiques(chaine:str ) -> bool:
	afile = 0
	for i in range (len(chaine)):
		if chaine[i] == chaine[i-1]:
			afile = afile + 1
		if afile == 3:
			return True
	return False
		 
print(contient_trois_identiques("yyy"))

#exo4
def est_motdepasse_valide(chaine:str) -> bool:
	espace = ""
	if len(chaine)>=8 and contient_deux_types(chaine) == True and contient_trois_identiques(chaine) == False and not espace in chaine and contient_majuscule(chaine) == True and nb_chiffres(chaine)>0:
		
		return True

print(est_motdepasse_valide("sggs"))
