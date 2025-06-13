import time

class Labyrinthe:
    ''' Permet de simuler les déplacemens vers la sortie dans un Labyrinthe'''
    
    def __init__(self,tab):
        self.tab=tab
        
    def nblignes(self):
        return len(self.tab)
    
    def nbcolonnes(self):
        return len(self.tab[0])
    
    def depart(self):
        for i in range(self.nblignes()):
            for j in range(self.nbcolonnes()):
                if self.tab[i][j]==2:
                    return i,j
    def arrivee(self):
        for i in range(self.nblignes()):
            for j in range(self.nbcolonnes()):
                if self.tab[i][j]==3:
                    return i,j
                
    def est_valide(self,i,j):
        return 0<=i<self.nblignes() and 0<=j<self.nbcolonnes()
    
    def nb_cases_vides(self):
        acc=0
        for i in range(self.nblignes()):
            for j in range(self.nbcolonnes()):
                if self.tab[i][j]==0 or self.tab[i][j]==2 or self.tab[i][j]==3:
                    acc+=1
        return acc
    
    def est_visitee(self,i,j):
        self.tab[i][j]=4
        
    def case_fausse(self,i,j):
        self.tab[i][j]=5
        
    def liste_voisines_libres(self,i,j):
        voisines=[]
        if self.est_valide(i-1,j) and self.tab[i-1][j]!=4 and self.tab[i-1][j]!=1 and self.tab[i-1][j]!=5:
            voisines.append((i-1,j))
        if self.est_valide(i+1,j) and self.tab[i+1][j]!=4 and self.tab[i+1][j]!=1 and self.tab[i+1][j]!=5:
            voisines.append((i+1,j))
        if self.est_valide(i,j-1) and self.tab[i][j-1]!=4 and self.tab[i][j-1]!=1 and self.tab[i][j-1]!=5:
            voisines.append((i,j-1))
        if self.est_valide(i,j+1) and self.tab[i][j+1]!=4 and self.tab[i][j+1]!=1 and self.tab[i][j+1]!=5:
            voisines.append((i,j+1))
        return voisines
    
    def affiche(self):
        chaine=''
        for i in range(self.nblignes()):
            nvligne=''
            for j in range(self.nbcolonnes()):
                nvligne+=str(self.tab[i][j])
               
            chaine+=nvligne+'\n'
        print(chaine)

    def solution(self):
        x,y=self.depart()
        pile=[(x,y)]
        chemin=[(x,y)]
        voisines=self.liste_voisines_libres(x,y)
        while pile!=[] and self.arrivee() not in voisines  :
            print(voisines)
            if voisines!=[]:
                x,y=voisines[0]
                self.est_visitee(x,y)
                pile.append((x,y))
                chemin.append((x,y))
            else:
                x,y=pile.pop()
                self.case_fausse(x,y)
            voisines=self.liste_voisines_libres(x,y)
            self.affiche()
            time.sleep(0.1)
            
        if self.arrivee() in voisines:
            chemin.append(self.arrivee())
        return chemin
    
tab1 = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[2, 0, 1, 0, 0, 0, 1, 0, 1, 0, 3],
[1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]]

tab2 = [[1, 1, 1, 1, 1, 1, 1],
[2, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 0, 0, 0, 1],
[1, 0, 1, 0, 1, 0, 1],
[1, 0, 0, 0, 1, 0, 1],
[1, 1, 1, 1, 1, 3, 1]]
lab2=Labyrinthe(tab2)
print(lab2.solution())