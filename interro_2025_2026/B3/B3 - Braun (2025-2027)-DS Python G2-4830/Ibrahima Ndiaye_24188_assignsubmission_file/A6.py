def score_renard(code: str) -> int:
	score = 0
	if len(code) >= 6:
		score = score + 2
	if contient_separateur(True):
		score = score + 2
	if contient_majuscule(True):
		score = score + 2
	if contient_deux_types(True):
		score = score + 2
	if nb_occurences(code, 'R') >= 1:
		score = score + 2
	return score
print(score_renard("babacar"))
