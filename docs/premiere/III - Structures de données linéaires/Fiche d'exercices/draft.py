

def est_croissante(liste:list)->int:
      i = 0
      while i < len(liste)-1 and liste[i] <= liste[i+1] :
         i = i +1
      return i == len(liste)-1
print(est_croissante([1,2,3,4,5])) # True