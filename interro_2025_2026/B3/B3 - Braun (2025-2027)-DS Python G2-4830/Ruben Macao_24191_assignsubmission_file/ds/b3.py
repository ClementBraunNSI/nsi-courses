def categorie_age_renard(age: int) -> str:
	if age <= 1:
		return "Jeune"
	elif age <= 6:
		return "Adulte"
	else:
		return "Senior"
	 
		
print(categorie_age_renard(1))
