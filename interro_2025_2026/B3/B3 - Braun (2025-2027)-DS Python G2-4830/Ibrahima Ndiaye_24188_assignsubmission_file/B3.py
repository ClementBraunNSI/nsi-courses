def categorie_age_renard(age:int) -> int:
	if age <= 1 :
		return "Jeune"
	if 2 <= age <=6:
		return "Adulte"
	else:
		return "senior"
print(categorie_age_renard(5))
