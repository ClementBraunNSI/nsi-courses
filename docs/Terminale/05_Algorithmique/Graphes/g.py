class Graphe_oriente:
    def __init__(self, ordre):
        '''
        Définit les listes des successeurs et prédécesseurs en fonction de l'ordre du graphe.
        
        @param_entree : ordre, entier
        '''
        self.ordre = ordre
        self.listes_successeurs = {i: [] for i in range(self.ordre)}
        self.listes_predecesseurs = {i: [] for i in range(self.ordre)}

    def ajouter_arc(self, noeud_i, noeud_j):
        '''
        Ajoute un arc du noeud i vers le noeud j.
        
        @param_entree : noeud_i, entier
        @param_entree : noeud_j, entier
        '''
        assert noeud_i < self.ordre and noeud_i >= 0, "Le noeud i n'appartient pas au graphe"
        assert noeud_j < self.ordre and noeud_j >= 0, "Le noeud j n'appartient pas au graphe"
        
        self.listes_successeurs[noeud_i].append(noeud_j)
        self.listes_predecesseurs[noeud_j].append(noeud_i)
   
    def supprimer_arc(self, noeud_i, noeud_j):
        '''
        Supprime un arc du noeud i vers le noeud j.
        
        @param_entree : noeud_i, entier
        @param_entree : noeud_j, entier
        '''
        assert noeud_i < self.ordre and noeud_i >= 0, "Le noeud i n'appartient pas au graphe"
        assert noeud_j < self.ordre and noeud_j >= 0, "Le noeud j n'appartient pas au graphe"
        assert noeud_j in self.listes_successeurs[noeud_i] and noeud_i in self.listes_predecesseurs[noeud_j], "L'arc n'existe pas"

#         position_noeud_j = self.listes_successeurs[noeud_i].index(noeud_j)
#         del self.listes_successeurs[noeud_i][position_noeud_j]
        
        self.listes_successeurs[noeud_i].remove(noeud_j)
        
        
#         position_noeud_i = self.listes_predecesseurs[noeud_j].index(noeud_i)
#         del self.listes_predecesseurs[noeud_j][position_noeud_i]
        
        self.listes_predecesseurs[noeud_j].remove(noeud_i)

    def sont_adjacents(self, noeud_i, noeud_j):
        '''
        Teste si le noeud i est relié au noeud j, de i vers j.
        
        @param_entree : noeud_i, entier
        @param_entree : noeud_j, entier
        @param_sortie : booléen
        '''
        assert noeud_i < self.ordre and noeud_i >= 0, "Le noeud i n'appartient pas au graphe"
        assert noeud_j < self.ordre and noeud_j >= 0, "Le noeud j n'appartient pas au graphe"
        
        return noeud_j in self.listes_successeurs[noeud_i] and noeud_i in self.listes_predecesseurs[noeud_j]

    def successeurs(self, noeud_i):
        '''
        Retourne la liste des successeurs du noeud i.
        
        @param_entree : noeud_i, entier
        @param_sortie : liste_successeurs, liste d'entiers
        '''
        
        assert noeud_i < self.ordre and noeud_i >= 0, "Le noeud i n'appartient pas au graphe"
        
        return self.listes_successeurs[noeud_i]

    def predecesseurs(self, noeud_j):
        '''
        Retourne la liste des prédécesseurs du noeud j.
        
        @param_entree : noeud_j, entier
        @param_sortie : liste_predecesseurs, liste d'entiers
        '''

        assert noeud_j < self.ordre and noeud_j >= 0, "Le noeud j n'appartient pas au graphe"
        
        return self.listes_predecesseurs[noeud_j]
    
    def detect_cycle(self, noeud, vus = None):

        if vus is None:
            vus = []
        voisins = self.successeurs(noeud)
        vus.append(noeud)

        for t in voisins:
            if t in vus:
                return True
            else:
                self.detect_cycle(t, vus)
        return False

#     def ajouter_sommet(noeud_i):
#         pass
#     
#     def supprimer_sommet(noeud_j):
#         pass

class Graphe_non_oriente:
    def __init__(self, ordre):
        '''
        Définit les listes des successeurs et prédécesseurs en fonction de l'ordre du graphe.
        
        @param_entree : ordre, entier
        '''
        self.ordre = ordre
        self.listes_adjacence = {i: [] for i in range(self.ordre)}

    def ajouter_arete(self, noeud_i, noeud_j):
        '''
        Ajoute une arête entre le noeud i et le noeud j.
        
        @param_entree : noeud_i, entier
        @param_entree : noeud_j, entier
        '''
        assert noeud_i < self.ordre and noeud_i >= 0, "Le noeud i n'appartient pas au graphe"
        assert noeud_j < self.ordre and noeud_j >= 0, "Le noeud j n'appartient pas au graphe"
        
        self.listes_adjacence[noeud_i].append(noeud_j)
        self.listes_adjacence[noeud_j].append(noeud_i)
   
    def supprimer_arete(self, noeud_i, noeud_j):
        '''
        Supprime une arete entre le noeud i et le noeud j.
        
        @param_entree : noeud_i, entier
        @param_entree : noeud_j, entier
        '''
        assert noeud_i < self.ordre and noeud_i >= 0, "Le noeud i n'appartient pas au graphe"
        assert noeud_j < self.ordre and noeud_j >= 0, "Le noeud j n'appartient pas au graphe"
        assert noeud_j in self.listes_adjacence[noeud_i] and noeud_i in self.listes_adjacence[noeud_j], "L'arete n'existe pas"

        self.listes_adjacence[noeud_i].remove(noeud_j)
        
        self.listes_adjacence[noeud_j].remove(noeud_i)

    def sont_adjacents(self, noeud_i, noeud_j):
        '''
        Teste si le noeud i est relié au noeud j.
        
        @param_entree : noeud_i, entier
        @param_entree : noeud_j, entier
        @param_sortie : booléen
        '''
        assert noeud_i < self.ordre and noeud_i >= 0, "Le noeud i n'appartient pas au graphe"
        assert noeud_j < self.ordre and noeud_j >= 0, "Le noeud j n'appartient pas au graphe"
        
        return noeud_j in self.listes_adjacence[noeud_i] and noeud_i in self.listes_adjacence[noeud_j]

    def adjacents(self, noeud_i):
        '''
        Retourne la liste des noeuds adjacents au noeud i.
        
        @param_entree : noeud_i, entier
        @param_sortie : liste_successeurs, liste d'entiers
        '''
        
        assert noeud_i < self.ordre and noeud_i >= 0, "Le noeud i n'appartient pas au graphe"
        
        return self.listes_adjacence[noeud_i]
    
    def parcours_largeur(self, noeud_depart):
        parcours = []
        file_deja_visites = [noeud_depart]

        while len(file_deja_visites) != 0:
            noeud_courant = file_deja_visites.pop(0)
            parcours.append(noeud_courant)
            for voisin in self.adjacents(noeud_courant):
                if voisin not in parcours and voisin not in file_deja_visites:
                    file_deja_visites.append(voisin)

        return parcours

    def parcours_profondeur(self, noeud_depart):
        parcours = []
        pile_deja_visites = [noeud_depart]

        while len(pile_deja_visites) != 0:
            noeud_courant = pile_deja_visites.pop()
            parcours.append(noeud_courant)
            for voisin in self.adjacents(noeud_courant):
                if voisin not in parcours and voisin not in pile_deja_visites:
                    pile_deja_visites.append(voisin)

        return parcours
    
    def cycles(self, noeud):
        visites = []
        pile = [noeud]

        while len(pile) != 0:
            sommet_courant = pile.pop()
            if sommet_courant in visites:
                return True
            visites.append(sommet_courant)
            for voisin in self.adjacents(sommet_courant):
                if voisin not in visites:
                    pile.append(voisin)
        return False

    def chemin(self, noeud):
        visites = {noeud: None}
        pile = [noeud]

        while len(pile) != 0:
            sommet_courant = pile.pop()
            for voisin in self.adjacents(sommet_courant):
                if voisin not in visites:
                    visites[voisin] = sommet_courant
                    pile.append(voisin)
        return visites
    
    def afficher_chemin(self, chemin):
        chaine = ""
        print(chemin)
        for e in chemin:
            if chaine == "":
                chaine += str(e)
            else:
                chaine += " -> " + str(e)
        print(chaine)
    
    def distance(self, noeud):
        distances = {noeud: 0}
        file = [noeud]

        while len(file) != 0:
            s = file.pop(0)
            for voisin in self.adjacents(s):
                if voisin not in distances:
                    distances[voisin] = distances[s] +1
                    file.append(voisin)

        return distances

    
    



#     def ajouter_sommet(noeud_i):
#         pass
#     
#     def supprimer_sommet(noeud_j):
#         pass


## Déclaration des fonctions


# Programme principal

""" graphe = Graphe_oriente(5)
print(graphe.listes_successeurs)
print(graphe.listes_predecesseurs)


graphe.ajouter_arc(0, 2)

graphe.ajouter_arc(1, 0)
graphe.ajouter_arc(1, 2)
graphe.ajouter_arc(1, 3)

#graphe.ajouter_arc(2, 1)

graphe.ajouter_arc(4, 0)
graphe.ajouter_arc(4, 3)

print(graphe.listes_successeurs)
print(graphe.listes_predecesseurs)

graphe.supprimer_arc(1, 3)

print(graphe.listes_successeurs)
print(graphe.listes_predecesseurs)

print(graphe.sont_adjacents(2, 1))

print(graphe.successeurs(4))
print(graphe.successeurs(1))

print(graphe.predecesseurs(1))
print(graphe.predecesseurs(2))

print(graphe.detect_cycle(0)) """

graphe = Graphe_non_oriente(5)

graphe.ajouter_arete(0, 2)

graphe.ajouter_arete(1, 0)

graphe.ajouter_arete(1, 2)
graphe.ajouter_arete(1, 3)

graphe.ajouter_arete(4, 0)
graphe.ajouter_arete(4, 3)

print(graphe.listes_adjacence)

print(graphe.parcours_profondeur(0))

print(graphe.cycles(1))
print(graphe.chemin(0))
graphe.afficher_chemin(graphe.chemin(0))
