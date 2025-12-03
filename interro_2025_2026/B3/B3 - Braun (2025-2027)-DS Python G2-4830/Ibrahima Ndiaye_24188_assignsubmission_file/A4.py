def contient_deux_types(chaine:str) -> bool :
	a_lettre = false
	a_chiffres = false
	alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	digits = "0123456789"
	a_sep = false
	for lettre in chaine:
		if lettre in alphabet or digits:
			a_chiffres = true
		elif lettre in alphabet :
			a_chiffres = false
	    if (chaine):
			a_sep = true
		return (a_lettre and a_sep) or (a_lettre and a_chiffres)
		
