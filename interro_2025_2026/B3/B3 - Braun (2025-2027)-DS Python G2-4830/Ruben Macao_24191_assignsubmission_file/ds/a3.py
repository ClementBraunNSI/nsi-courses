def contient_separateur(code: str) -> bool:
	seps = "-_"
	for c in code:
		if c == seps:
			return True
	return False
