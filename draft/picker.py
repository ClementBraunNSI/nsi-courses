import random
import os
from time import sleep

premieres = ["a","b","c","d","e","f","g"]
alea = random.randint(0,3)
print(alea)
i = 0

print('Choisissons une victime')
if alea == 0 or i == 0 and alea > 0:
    print("La victime est ",random.choice(premieres))
else:
    while i != alea:
        s = "Voici la victime :"
        if i+1 >=1 :
                print("Petite feinte")
                sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(s, random.choice(premieres))
        i+=1
        
        