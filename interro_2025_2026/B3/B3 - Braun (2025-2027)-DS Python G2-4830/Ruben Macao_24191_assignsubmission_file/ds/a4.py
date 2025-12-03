def contient_deux_types(code: str) -> bool:
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	digits = "0123456789"
	a_lettre = False
	# au moins une lettre ?
	i = 0
	while i < len(alphabet):
		if nb_occurrences(code, alphabet[i]) > 1:
			a_lettre = True
		i = i + 1
	a_chiffre = False
	j = 0
	while j < len(digits):
		if nb_occurrences(code, digits[j]) > 1:
			a_chiffre = True
		j = j + 1
	a_sep = contient_separateur()
	if (a_lettre and a_chiffre) or (a_lettre and a_sep) or (a_chiffre and a_sep):
		return True
	return False
			
