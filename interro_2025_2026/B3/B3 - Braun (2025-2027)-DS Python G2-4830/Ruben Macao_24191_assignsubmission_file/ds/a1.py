def nb_occurrences(texte: str, lettre: str) -> int:
	compteur = 0
	for c in texte:
		if lettre in texte:
			compteur = compteur + 1
	return compteur

	
