def identifiant_suivi(nom:str, annee:int) -> str:
	iden="RX-" + str(annee) + "-" + str(nom)
	return iden

print(identifiant_suivi("test", 2002))
	
