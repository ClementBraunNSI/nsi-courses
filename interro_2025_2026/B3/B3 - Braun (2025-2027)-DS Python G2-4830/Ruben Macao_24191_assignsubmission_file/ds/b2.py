def compter_voyelles(nom: str) -> int:
	a = 0
	voyelles = "aeiouyAEIOUY"
	for c in nom:
		if c in voyelles:
			a = a + 1
	return a


print(compter_voyelles("Aziz"))
			
