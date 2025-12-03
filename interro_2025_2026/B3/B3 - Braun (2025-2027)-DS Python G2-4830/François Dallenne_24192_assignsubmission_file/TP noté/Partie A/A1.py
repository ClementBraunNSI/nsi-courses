'''ne pas compter les points
def nb_occurrences(texte: str, lettre: str) -> int:
	compteur = 0
	for c in texte:
		if c == lettre :
			compteur = compteur + 1
	return compteur
'''
