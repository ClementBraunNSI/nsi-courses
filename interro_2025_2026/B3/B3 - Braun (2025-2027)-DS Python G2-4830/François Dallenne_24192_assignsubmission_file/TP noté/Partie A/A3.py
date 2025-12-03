def contient_separateur(code: str) -> bool:
	seps = "-_"
	for c in code:
		if c == "-" or "_":
			return True
	return seps
