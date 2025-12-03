
#B1

def repeter_hurlement(c: str , n: int) -> str:
	rep = 0 
	for rep in range(rep, n):
		print(c)
print(repeter_hurlement("Salut à tous",5))

'''B2'''
def compter_voyelles(nom: str) -> int:
	a = 0
	voyelles = "aeiouyAEIOUY"
	for c in nom:
		if c in voyelles:
			a = a + 1
	return a
	
print(compter_voyelles("Salut"))
		

'''B3'''
def categorie_age_renard(age: int) -> str:
	if age>6:
		return "Senior"
	elif age >= 2 and age <=6:
		return "Adulte"
	else:
		return "Jeune"

print(categorie_age_renard(3))
	
'''B4'''
def identifiant_suivi(nom: str , annee: int) -> str:
	a="RX"+"-"+str(annee)+"-"+nom
	return a

print(identifiant_suivi("IsaacBg", 2099))

'''
def inverser_chaine(chaine: str) -> str:
	for i in chaine:
		
'''
