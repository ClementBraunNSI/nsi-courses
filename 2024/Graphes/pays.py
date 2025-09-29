
import random


adjacence = {
            'Argentine': ['Bolivie', 'Brésil', 'Chili', 'Paraguay', 'Uruguay'],
            'Bolivie': ['Argentine', 'Brésil', 'Chili', 'Paraguay', 'Pérou'],
            'Brésil': ['Argentine', 'Bolivie', 'Colombie', 'Guyane', 'Paraguay', 'Pérou', 'Suriname', 'Uruguay', 'Venezuela'],
            'Chili': ['Argentine', 'Bolivie', 'Pérou'],
            'Colombie': ['Brésil', 'Équateur', 'Pérou', 'Venezuela'],
            'Équateur': ['Colombie', 'Pérou'],
            'Guyane': ['Brésil', 'Suriname'],
            'Paraguay': ['Argentine', 'Bolivie', 'Brésil'],
            'Pérou': ['Bolivie', 'Brésil', 'Chili', 'Colombie', 'Équateur'],
            'Suriname': ['Brésil', 'Guyane'],
            'Uruguay': ['Argentine', 'Brésil'],
            'Venezuela': ['Brésil', 'Colombie'],
        }

pile = []
voyage = []
pile.append('Pérou')
while len(pile) != 0:
    pays_courant = pile.pop(0)
    if pays_courant not in voyage:
        voyage.append(pays_courant)
        for voisin in adjacence[pays_courant]:
            if voisin not in pile:
                pile.append(voisin)
print(voyage)
