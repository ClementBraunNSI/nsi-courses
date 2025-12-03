def contient_majuscule(nom:str) -> bool:
	maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for c in nom:
		if "A"or"B"or"C"or"D"or"E"or"F"or"G"or"H"or"I"or"J"or"K"or"L"or"M"or"N"or"O"or"P"or"Q"or"R"or"S"or"T"or"U"or"V"or"W"or"X"or"Y"or"Z" in nom:
			return True
		
		return False
			
print(contient_majuscule("AB"))
