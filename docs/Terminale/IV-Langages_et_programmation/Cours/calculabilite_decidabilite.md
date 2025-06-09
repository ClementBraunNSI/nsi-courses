# Calculabilité et décidabilité

## Introduction

La calculabilité et la décidabilité sont des concepts fondamentaux de l'informatique théorique qui étudient les limites de ce qui peut être calculé par un ordinateur. Ces notions permettent de comprendre quels problèmes peuvent être résolus algorithmiquement et lesquels sont intrinsèquement impossibles à résoudre.

---

## Concepts fondamentaux

### Qu'est-ce que la calculabilité ?

**Définition :** La calculabilité étudie quelles fonctions peuvent être calculées par un algorithme.

**Fonction calculable :** Une fonction est calculable s'il existe un algorithme qui, pour toute entrée valide, produit la sortie correcte en un nombre fini d'étapes.

**Exemples de fonctions calculables :**
- Addition, multiplication
- Calcul du PGCD
- Tri d'une liste
- Recherche dans un graphe

### Qu'est-ce que la décidabilité ?

**Définition :** La décidabilité étudie quels problèmes de décision peuvent être résolus algorithmiquement.

**Problème décidable :** Un problème est décidable s'il existe un algorithme qui répond toujours "oui" ou "non" en un temps fini.

**Exemples de problèmes décidables :**
- "Ce nombre est-il premier ?"
- "Ce graphe est-il connexe ?"
- "Cette liste est-elle triée ?"

---

## Modèles de calcul

### Machine de Turing

#### Définition
Une machine de Turing est un modèle mathématique de calcul qui consiste en :
- Un **ruban** infini divisé en cases
- Une **tête de lecture/écriture** qui peut se déplacer
- Un **ensemble d'états** finis
- Une **fonction de transition** qui détermine les actions

#### Composants

```
... □ □ a b c □ □ ...
        ↑
    Tête de lecture
    
États : {q0, q1, q2, ..., qaccept, qreject}
Alphabet : {0, 1, □} (□ = case vide)
```

#### Fonctionnement
À chaque étape, selon l'état courant et le symbole lu :
1. Écrire un nouveau symbole
2. Déplacer la tête (gauche, droite, ou rester)
3. Changer d'état

#### Simulation d'une machine de Turing

```python
class MachineTuring:
    def __init__(self, etats, alphabet, transitions, etat_initial, etats_acceptants):
        self.etats = etats
        self.alphabet = alphabet
        self.transitions = transitions  # (etat, symbole) -> (nouvel_etat, nouveau_symbole, direction)
        self.etat_courant = etat_initial
        self.etats_acceptants = etats_acceptants
        self.ruban = ['□']  # Ruban initialement vide
        self.position_tete = 0
        self.etapes = 0
        self.max_etapes = 1000  # Limite pour éviter les boucles infinies
    
    def initialiser_ruban(self, entree):
        """Initialise le ruban avec l'entrée"""
        self.ruban = list(entree) + ['□']
        self.position_tete = 0
    
    def lire_symbole(self):
        """Lit le symbole sous la tête"""
        if self.position_tete < 0:
            return '□'
        if self.position_tete >= len(self.ruban):
            # Étendre le ruban si nécessaire
            self.ruban.extend(['□'] * (self.position_tete - len(self.ruban) + 1))
        return self.ruban[self.position_tete]
    
    def ecrire_symbole(self, symbole):
        """Écrit un symbole sous la tête"""
        if self.position_tete < 0:
            # Étendre le ruban à gauche
            self.ruban = ['□'] * (-self.position_tete) + self.ruban
            self.position_tete = 0
        if self.position_tete >= len(self.ruban):
            # Étendre le ruban à droite
            self.ruban.extend(['□'] * (self.position_tete - len(self.ruban) + 1))
        self.ruban[self.position_tete] = symbole
    
    def deplacer_tete(self, direction):
        """Déplace la tête (L=gauche, R=droite, S=stationnaire)"""
        if direction == 'L':
            self.position_tete -= 1
        elif direction == 'R':
            self.position_tete += 1
        # S = rester sur place
    
    def executer_etape(self):
        """Exécute une étape de la machine"""
        symbole_courant = self.lire_symbole()
        cle_transition = (self.etat_courant, symbole_courant)
        
        if cle_transition not in self.transitions:
            # Pas de transition définie -> arrêt
            return False
        
        nouvel_etat, nouveau_symbole, direction = self.transitions[cle_transition]
        
        # Appliquer la transition
        self.ecrire_symbole(nouveau_symbole)
        self.deplacer_tete(direction)
        self.etat_courant = nouvel_etat
        self.etapes += 1
        
        return True
    
    def executer(self, entree):
        """Exécute la machine sur une entrée"""
        self.initialiser_ruban(entree)
        self.etapes = 0
        
        print(f"Entrée: {''.join(entree)}")
        print(f"État initial: {self.etat_courant}")
        self.afficher_configuration()
        
        while self.etapes < self.max_etapes:
            if self.etat_courant in self.etats_acceptants:
                print(f"\nACCEPTÉ après {self.etapes} étapes")
                return True
            
            if self.etat_courant == 'qreject':
                print(f"\nREJETÉ après {self.etapes} étapes")
                return False
            
            if not self.executer_etape():
                print(f"\nARRÊT (pas de transition) après {self.etapes} étapes")
                return False
            
            self.afficher_configuration()
        
        print(f"\nTIMEOUT après {self.max_etapes} étapes")
        return None
    
    def afficher_configuration(self):
        """Affiche la configuration actuelle"""
        # Nettoyer le ruban (enlever les □ inutiles)
        debut = 0
        fin = len(self.ruban) - 1
        
        while debut < len(self.ruban) and self.ruban[debut] == '□':
            debut += 1
        while fin >= 0 and self.ruban[fin] == '□':
            fin -= 1
        
        if debut > fin:  # Ruban vide
            ruban_affiche = ['□']
            pos_affichee = 0
        else:
            ruban_affiche = self.ruban[debut:fin+1]
            pos_affichee = self.position_tete - debut
        
        # Afficher le ruban
        print(f"Étape {self.etapes}: État {self.etat_courant}")
        print(f"Ruban: {''.join(ruban_affiche)}")
        
        # Afficher la position de la tête
        if 0 <= pos_affichee < len(ruban_affiche):
            print(f"       {' ' * pos_affichee}^")
        print()

# Exemple : Machine qui reconnaît les mots de la forme a^n b^n
def creer_machine_anbn():
    """Crée une machine de Turing qui reconnaît L = {a^n b^n | n ≥ 1}"""
    etats = {'q0', 'q1', 'q2', 'q3', 'qaccept', 'qreject'}
    alphabet = {'a', 'b', 'X', 'Y', '□'}
    
    transitions = {
        # État q0 : chercher le premier 'a'
        ('q0', 'a'): ('q1', 'X', 'R'),  # Marquer le premier 'a' et aller à droite
        ('q0', 'Y'): ('q3', 'Y', 'R'),  # Si on voit un Y, aller vérifier la fin
        
        # État q1 : aller vers la droite jusqu'au premier 'b'
        ('q1', 'a'): ('q1', 'a', 'R'),  # Continuer à droite
        ('q1', 'Y'): ('q1', 'Y', 'R'),  # Passer les Y déjà marqués
        ('q1', 'b'): ('q2', 'Y', 'L'),  # Marquer le premier 'b' et revenir
        
        # État q2 : revenir au début
        ('q2', 'a'): ('q2', 'a', 'L'),  # Revenir à gauche
        ('q2', 'Y'): ('q2', 'Y', 'L'),  # Passer les Y
        ('q2', 'X'): ('q0', 'X', 'R'),  # Retourner à q0
        
        # État q3 : vérifier qu'il ne reste que des Y et □
        ('q3', 'Y'): ('q3', 'Y', 'R'),  # Continuer à droite
        ('q3', '□'): ('qaccept', '□', 'S'),  # Fin du ruban -> accepter
    }
    
    return MachineTuring(etats, alphabet, transitions, 'q0', {'qaccept'})

# Test de la machine
if __name__ == "__main__":
    machine = creer_machine_anbn()
    
    # Tests
    tests = [
        "ab",      # Devrait être accepté
        "aabb",    # Devrait être accepté
        "aaabbb",  # Devrait être accepté
        "aab",     # Devrait être rejeté
        "abb",     # Devrait être rejeté
        "abab",    # Devrait être rejeté
    ]
    
    for test in tests:
        print(f"\n{'='*50}")
        print(f"Test: {test}")
        print(f"{'='*50}")
        resultat = machine.executer(test)
        print(f"Résultat: {resultat}")
        
        # Réinitialiser la machine pour le test suivant
        machine.etat_courant = 'q0'
```

### Thèse de Church-Turing

**Énoncé :** Toute fonction calculable peut être calculée par une machine de Turing.

**Implications :**
- Les machines de Turing capturent la notion intuitive de calcul
- Tous les modèles de calcul "raisonnables" sont équivalents
- Les ordinateurs modernes ne sont pas plus puissants qu'une machine de Turing

**Modèles équivalents :**
- Fonctions récursives
- Lambda-calcul
- Machines à registres
- Langages de programmation complets

---

## Problèmes indécidables

### Le problème de l'arrêt

#### Énoncé
**Problème :** Étant donné un programme P et une entrée E, le programme P s'arrête-t-il sur l'entrée E ?

#### Preuve d'indécidabilité (par contradiction)

**Hypothèse :** Supposons qu'il existe un algorithme `ARRET(P, E)` qui :
- Retourne `True` si P s'arrête sur E
- Retourne `False` si P ne s'arrête pas sur E

**Construction d'une contradiction :**

```python
# Algorithme hypothétique ARRET
def ARRET(programme, entree):
    # Retourne True si le programme s'arrête sur l'entrée
    # Retourne False sinon
    pass  # Implémentation supposée exister

# Construction du paradoxe
def DIAGONALE(P):
    if ARRET(P, P):  # Si P s'arrête sur lui-même
        while True:   # Alors boucler infiniment
            pass
    else:            # Si P ne s'arrête pas sur lui-même
        return       # Alors s'arrêter

# Question paradoxale : DIAGONALE(DIAGONALE) s'arrête-t-il ?
# Si oui, alors ARRET(DIAGONALE, DIAGONALE) = True
# Donc DIAGONALE(DIAGONALE) boucle infiniment -> contradiction
# Si non, alors ARRET(DIAGONALE, DIAGONALE) = False
# Donc DIAGONALE(DIAGONALE) s'arrête -> contradiction
```

**Conclusion :** L'algorithme `ARRET` ne peut pas exister.

#### Simulation du problème de l'arrêt

```python
import sys
import signal
from contextlib import contextmanager

class TimeoutException(Exception):
    pass

@contextmanager
def timeout(seconds):
    """Context manager pour limiter le temps d'exécution"""
    def signal_handler(signum, frame):
        raise TimeoutException("Timeout")
    
    # Configurer le signal d'alarme
    old_handler = signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)

def detecteur_arret_approximatif(fonction, args, timeout_sec=5):
    """
    Tentative de détection d'arrêt avec timeout
    ATTENTION : Ceci n'est qu'une approximation !
    """
    try:
        with timeout(timeout_sec):
            resultat = fonction(*args)
            return True, resultat
    except TimeoutException:
        return False, None
    except Exception as e:
        return True, f"Erreur: {e}"

# Exemples de fonctions pour tester
def fonction_qui_sarrete(n):
    """Fonction qui s'arrête toujours"""
    return sum(range(n))

def fonction_qui_boucle():
    """Fonction qui boucle infiniment"""
    while True:
        pass

def fonction_collatz(n):
    """Conjecture de Collatz - on ne sait pas si elle s'arrête toujours"""
    etapes = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        etapes += 1
        if etapes > 1000000:  # Limite arbitraire
            break
    return etapes

def fonction_ackermann(m, n):
    """Fonction d'Ackermann - croissance très rapide"""
    if m == 0:
        return n + 1
    elif n == 0:
        return fonction_ackermann(m - 1, 1)
    else:
        return fonction_ackermann(m - 1, fonction_ackermann(m, n - 1))

# Tests
if __name__ == "__main__":
    print("Détection approximative d'arrêt (avec timeout)")
    print("ATTENTION : Ceci n'est qu'une heuristique !\n")
    
    tests = [
        (fonction_qui_sarrete, (1000,), "Fonction qui s'arrête"),
        (fonction_collatz, (27,), "Collatz(27)"),
        (fonction_collatz, (837799,), "Collatz(837799) - cas difficile"),
        (fonction_ackermann, (3, 3), "Ackermann(3,3)"),
        (fonction_ackermann, (4, 2), "Ackermann(4,2) - très lent"),
    ]
    
    for fonction, args, description in tests:
        print(f"Test: {description}")
        sarrete, resultat = detecteur_arret_approximatif(fonction, args, 2)
        
        if sarrete:
            print(f"  Résultat: S'arrête avec {resultat}")
        else:
            print(f"  Résultat: Timeout (probablement ne s'arrête pas)")
        print()
    
    print("Note: Un timeout ne prouve pas qu'une fonction ne s'arrête jamais,")
    print("elle pourrait juste prendre plus de temps que la limite fixée.")
```

### Autres problèmes indécidables

#### Problème de correspondance de Post

**Énoncé :** Étant donné deux listes de mots, existe-t-il une séquence d'indices qui produit le même mot en concaténant les mots correspondants des deux listes ?

```python
def probleme_correspondance_post(liste1, liste2, max_longueur=10):
    """
    Recherche exhaustive limitée pour le problème de Post
    ATTENTION : Le problème général est indécidable !
    """
    n = len(liste1)
    
    def recherche_recursive(sequence, mot1, mot2, profondeur):
        if profondeur > max_longueur:
            return None
        
        if mot1 == mot2 and len(mot1) > 0:
            return sequence
        
        # Si un mot est préfixe de l'autre, continuer
        if mot1.startswith(mot2) or mot2.startswith(mot1):
            for i in range(n):
                nouveau_mot1 = mot1 + liste1[i]
                nouveau_mot2 = mot2 + liste2[i]
                resultat = recherche_recursive(
                    sequence + [i], nouveau_mot1, nouveau_mot2, profondeur + 1
                )
                if resultat:
                    return resultat
        
        return None
    
    # Commencer avec chaque paire possible
    for i in range(n):
        resultat = recherche_recursive([i], liste1[i], liste2[i], 1)
        if resultat:
            return resultat
    
    return None

# Exemple
liste1 = ["a", "ab", "bba"]
liste2 = ["baa", "aa", "bb"]

resultat = probleme_correspondance_post(liste1, liste2)
if resultat:
    print(f"Solution trouvée: {resultat}")
    mot1 = "".join(liste1[i] for i in resultat)
    mot2 = "".join(liste2[i] for i in resultat)
    print(f"Mot 1: {mot1}")
    print(f"Mot 2: {mot2}")
else:
    print("Aucune solution trouvée (dans la limite fixée)")
```

#### Problème de l'équivalence de programmes

**Énoncé :** Étant donnés deux programmes, calculent-ils la même fonction ?

**Indécidabilité :** Conséquence directe du problème de l'arrêt.

---

## Hiérarchie de complexité

### Classes de complexité

#### Classe P
**Définition :** Problèmes décidables en temps polynomial par une machine de Turing déterministe.

**Exemples :**
- Tri d'une liste
- Recherche dans un graphe (BFS, DFS)
- Calcul du PGCD
- Test de primalité (AKS)

#### Classe NP
**Définition :** Problèmes décidables en temps polynomial par une machine de Turing non-déterministe, ou vérifiables en temps polynomial.

**Exemples :**
- Problème du voyageur de commerce (TSP)
- Satisfiabilité booléenne (SAT)
- Coloration de graphe
- Problème du sac à dos

#### Problèmes NP-complets
**Définition :** Problèmes les plus difficiles de NP. Si l'un d'eux est dans P, alors P = NP.

**Exemples :**
- SAT (premier problème prouvé NP-complet)
- 3-SAT
- Clique
- Couverture de sommets

### Simulation de problèmes NP

```python
import itertools
from typing import List, Tuple

class ProblemeNP:
    """Classe de base pour les problèmes NP"""
    
    def verifier_solution(self, instance, solution):
        """Vérifie si une solution est valide (en temps polynomial)"""
        raise NotImplementedError
    
    def resoudre_force_brute(self, instance, max_taille=None):
        """Résolution par force brute (exponentiel)"""
        raise NotImplementedError

class ProblemeColoration(ProblemeNP):
    """Problème de coloration de graphe"""
    
    def __init__(self, nb_couleurs):
        self.nb_couleurs = nb_couleurs
    
    def verifier_solution(self, graphe, coloration):
        """Vérifie si une coloration est valide"""
        # Vérifier que chaque sommet a une couleur
        sommets = set()
        for u, v in graphe:
            sommets.add(u)
            sommets.add(v)
        
        if set(coloration.keys()) != sommets:
            return False
        
        # Vérifier que les couleurs sont valides
        for couleur in coloration.values():
            if couleur < 0 or couleur >= self.nb_couleurs:
                return False
        
        # Vérifier qu'aucune arête ne relie deux sommets de même couleur
        for u, v in graphe:
            if coloration[u] == coloration[v]:
                return False
        
        return True
    
    def resoudre_force_brute(self, graphe, max_taille=10):
        """Résolution par énumération de toutes les colorations"""
        # Extraire les sommets
        sommets = set()
        for u, v in graphe:
            sommets.add(u)
            sommets.add(v)
        
        sommets = list(sommets)
        
        if len(sommets) > max_taille:
            print(f"Graphe trop grand ({len(sommets)} sommets > {max_taille})")
            return None
        
        # Énumérer toutes les colorations possibles
        for coloration_tuple in itertools.product(range(self.nb_couleurs), repeat=len(sommets)):
            coloration = dict(zip(sommets, coloration_tuple))
            
            if self.verifier_solution(graphe, coloration):
                return coloration
        
        return None

class ProblemeSAT(ProblemeNP):
    """Problème de satisfiabilité booléenne"""
    
    def verifier_solution(self, formule, assignation):
        """Vérifie si une assignation satisfait la formule"""
        # Formule = liste de clauses
        # Clause = liste de littéraux (entiers, négatifs pour la négation)
        # Assignation = dictionnaire variable -> booléen
        
        for clause in formule:
            clause_satisfaite = False
            
            for litteral in clause:
                variable = abs(litteral)
                valeur = assignation.get(variable, False)
                
                # Si le littéral est négatif, inverser la valeur
                if litteral < 0:
                    valeur = not valeur
                
                if valeur:
                    clause_satisfaite = True
                    break
            
            if not clause_satisfaite:
                return False
        
        return True
    
    def resoudre_force_brute(self, formule, max_variables=15):
        """Résolution par énumération de toutes les assignations"""
        # Extraire toutes les variables
        variables = set()
        for clause in formule:
            for litteral in clause:
                variables.add(abs(litteral))
        
        variables = list(variables)
        
        if len(variables) > max_variables:
            print(f"Trop de variables ({len(variables)} > {max_variables})")
            return None
        
        # Énumérer toutes les assignations possibles
        for assignation_tuple in itertools.product([False, True], repeat=len(variables)):
            assignation = dict(zip(variables, assignation_tuple))
            
            if self.verifier_solution(formule, assignation):
                return assignation
        
        return None

# Exemples d'utilisation
if __name__ == "__main__":
    print("=== Problème de coloration de graphe ===")
    
    # Graphe simple (triangle)
    graphe_triangle = [(1, 2), (2, 3), (3, 1)]
    
    # Essayer avec 2 couleurs (impossible)
    coloration_2 = ProblemeColoration(2)
    solution = coloration_2.resoudre_force_brute(graphe_triangle)
    print(f"Coloration avec 2 couleurs: {solution}")
    
    # Essayer avec 3 couleurs (possible)
    coloration_3 = ProblemeColoration(3)
    solution = coloration_3.resoudre_force_brute(graphe_triangle)
    print(f"Coloration avec 3 couleurs: {solution}")
    
    if solution:
        print(f"Vérification: {coloration_3.verifier_solution(graphe_triangle, solution)}")
    
    print("\n=== Problème SAT ===")
    
    # Formule SAT : (x1 ∨ ¬x2) ∧ (x2 ∨ x3) ∧ (¬x1 ∨ ¬x3)
    formule = [
        [1, -2],   # x1 ∨ ¬x2
        [2, 3],    # x2 ∨ x3
        [-1, -3]   # ¬x1 ∨ ¬x3
    ]
    
    sat = ProblemeSAT()
    solution = sat.resoudre_force_brute(formule)
    print(f"Solution SAT: {solution}")
    
    if solution:
        print(f"Vérification: {sat.verifier_solution(formule, solution)}")
    
    # Formule insatisfiable : (x1) ∧ (¬x1)
    formule_unsat = [
        [1],    # x1
        [-1]    # ¬x1
    ]
    
    solution = sat.resoudre_force_brute(formule_unsat)
    print(f"Solution formule insatisfiable: {solution}")
```

---

## Réduction et NP-complétude

### Concept de réduction

**Définition :** Une réduction de A vers B est un algorithme polynomial qui transforme toute instance de A en une instance de B, préservant la réponse.

**Notation :** A ≤_p B (A se réduit polynomialement à B)

**Propriétés :**
- Si A ≤_p B et B ∈ P, alors A ∈ P
- Si A ≤_p B et A est NP-difficile, alors B est NP-difficile

### Exemple de réduction : 3-SAT vers Clique

```python
def reduction_3sat_vers_clique(formule_3sat):
    """
    Réduit une instance de 3-SAT vers une instance de Clique
    """
    # Construire le graphe de conflit
    sommets = []  # (clause_id, litteral)
    aretes = []
    
    # Créer un sommet pour chaque littéral de chaque clause
    for i, clause in enumerate(formule_3sat):
        for litteral in clause:
            sommets.append((i, litteral))
    
    # Créer des arêtes entre sommets compatibles
    for j, (clause1, lit1) in enumerate(sommets):
        for k, (clause2, lit2) in enumerate(sommets):
            if j < k:  # Éviter les doublons
                # Arête si les sommets sont dans des clauses différentes
                # et ne sont pas contradictoires
                if clause1 != clause2 and lit1 != -lit2:
                    aretes.append((j, k))
    
    # La taille de la clique recherchée = nombre de clauses
    taille_clique = len(formule_3sat)
    
    return sommets, aretes, taille_clique

def verifier_clique(graphe, sommets_clique):
    """Vérifie si un ensemble de sommets forme une clique"""
    n = len(sommets_clique)
    
    # Vérifier que tous les sommets sont connectés entre eux
    for i in range(n):
        for j in range(i + 1, n):
            u, v = sommets_clique[i], sommets_clique[j]
            # Chercher l'arête (u,v) ou (v,u)
            if (u, v) not in graphe and (v, u) not in graphe:
                return False
    
    return True

# Exemple
if __name__ == "__main__":
    # Formule 3-SAT : (x1 ∨ x2 ∨ x3) ∧ (¬x1 ∨ x2 ∨ ¬x3)
    formule = [
        [1, 2, 3],
        [-1, 2, -3]
    ]
    
    sommets, aretes, k = reduction_3sat_vers_clique(formule)
    
    print(f"Formule 3-SAT: {formule}")
    print(f"Sommets du graphe: {sommets}")
    print(f"Arêtes: {aretes}")
    print(f"Taille de clique recherchée: {k}")
    
    # Vérifier qu'une clique de taille k existe
    # (ici on teste manuellement)
    clique_candidate = [0, 3]  # Sommets (0,1) et (1,2)
    
    if len(clique_candidate) == k and verifier_clique(aretes, clique_candidate):
        print(f"Clique trouvée: {clique_candidate}")
        print("La formule 3-SAT est satisfiable")
    else:
        print("Pas de clique de la bonne taille")
```

---

## Applications pratiques

### Optimisation avec contraintes

```python
import random
from typing import List, Callable

class AlgorithmeApproximation:
    """Algorithmes d'approximation pour problèmes NP-difficiles"""
    
    @staticmethod
    def couverture_sommets_glouton(graphe):
        """Approximation 2-optimale pour la couverture de sommets"""
        # Extraire tous les sommets
        sommets = set()
        for u, v in graphe:
            sommets.add(u)
            sommets.add(v)
        
        couverture = set()
        aretes_restantes = set(graphe)
        
        while aretes_restantes:
            # Prendre une arête arbitraire
            u, v = next(iter(aretes_restantes))
            
            # Ajouter les deux sommets à la couverture
            couverture.add(u)
            couverture.add(v)
            
            # Retirer toutes les arêtes couvertes
            aretes_a_retirer = set()
            for a, b in aretes_restantes:
                if a in couverture or b in couverture:
                    aretes_a_retirer.add((a, b))
            
            aretes_restantes -= aretes_a_retirer
        
        return couverture
    
    @staticmethod
    def tsp_plus_proche_voisin(distances):
        """Heuristique du plus proche voisin pour TSP"""
        n = len(distances)
        visite = [False] * n
        circuit = [0]  # Commencer par la ville 0
        visite[0] = True
        distance_totale = 0
        
        ville_courante = 0
        
        for _ in range(n - 1):
            distance_min = float('inf')
            prochaine_ville = -1
            
            # Trouver la ville non visitée la plus proche
            for ville in range(n):
                if not visite[ville] and distances[ville_courante][ville] < distance_min:
                    distance_min = distances[ville_courante][ville]
                    prochaine_ville = ville
            
            # Aller à la prochaine ville
            circuit.append(prochaine_ville)
            visite[prochaine_ville] = True
            distance_totale += distance_min
            ville_courante = prochaine_ville
        
        # Retourner au point de départ
        distance_totale += distances[ville_courante][0]
        circuit.append(0)
        
        return circuit, distance_totale
    
    @staticmethod
    def sac_a_dos_glouton(objets, capacite):
        """Heuristique gloutonne pour le sac à dos (ratio valeur/poids)"""
        # Trier par ratio valeur/poids décroissant
        objets_tries = sorted(objets, key=lambda x: x[1]/x[0], reverse=True)
        
        sac = []
        poids_total = 0
        valeur_totale = 0
        
        for poids, valeur, nom in objets_tries:
            if poids_total + poids <= capacite:
                sac.append((poids, valeur, nom))
                poids_total += poids
                valeur_totale += valeur
        
        return sac, valeur_totale, poids_total

class AlgorithmeGenetique:
    """Algorithme génétique pour l'optimisation"""
    
    def __init__(self, taille_population=50, taux_mutation=0.1, nb_generations=100):
        self.taille_population = taille_population
        self.taux_mutation = taux_mutation
        self.nb_generations = nb_generations
    
    def resoudre_tsp(self, distances):
        """Résout TSP avec un algorithme génétique"""
        n = len(distances)
        
        def fitness(circuit):
            """Calcule la fitness (inverse de la distance)"""
            distance = 0
            for i in range(len(circuit)):
                j = (i + 1) % len(circuit)
                distance += distances[circuit[i]][circuit[j]]
            return 1 / (1 + distance)
        
        def creer_individu():
            """Crée un circuit aléatoire"""
            circuit = list(range(1, n))  # Exclure la ville 0 (fixe)
            random.shuffle(circuit)
            return [0] + circuit  # Commencer par la ville 0
        
        def croiser(parent1, parent2):
            """Croisement par ordre (OX)"""
            # Sélectionner une sous-séquence du parent1
            start = random.randint(1, n - 2)
            end = random.randint(start + 1, n - 1)
            
            enfant = [None] * n
            enfant[0] = 0  # Ville de départ fixe
            
            # Copier la sous-séquence du parent1
            for i in range(start, end):
                enfant[i] = parent1[i]
            
            # Compléter avec les villes du parent2 dans l'ordre
            villes_utilisees = set(enfant[start:end])
            villes_utilisees.add(0)
            
            j = 1
            for ville in parent2[1:]:
                if ville not in villes_utilisees:
                    while enfant[j] is not None:
                        j += 1
                    enfant[j] = ville
            
            return enfant
        
        def muter(circuit):
            """Mutation par échange de deux villes"""
            if random.random() < self.taux_mutation:
                i = random.randint(1, n - 1)
                j = random.randint(1, n - 1)
                circuit[i], circuit[j] = circuit[j], circuit[i]
            return circuit
        
        # Initialiser la population
        population = [creer_individu() for _ in range(self.taille_population)]
        
        meilleur_circuit = None
        meilleure_fitness = 0
        
        for generation in range(self.nb_generations):
            # Évaluer la fitness
            fitness_population = [(individu, fitness(individu)) for individu in population]
            fitness_population.sort(key=lambda x: x[1], reverse=True)
            
            # Garder le meilleur
            if fitness_population[0][1] > meilleure_fitness:
                meilleure_fitness = fitness_population[0][1]
                meilleur_circuit = fitness_population[0][0][:]
            
            # Sélection et reproduction
            nouvelle_population = []
            
            # Élitisme : garder les 10% meilleurs
            elite_size = self.taille_population // 10
            for i in range(elite_size):
                nouvelle_population.append(fitness_population[i][0])
            
            # Reproduction
            while len(nouvelle_population) < self.taille_population:
                # Sélection par tournoi
                parent1 = self.selection_tournoi(fitness_population)
                parent2 = self.selection_tournoi(fitness_population)
                
                enfant = croiser(parent1, parent2)
                enfant = muter(enfant)
                nouvelle_population.append(enfant)
            
            population = nouvelle_population
            
            if generation % 20 == 0:
                distance = 1 / meilleure_fitness - 1
                print(f"Génération {generation}: Meilleure distance = {distance:.2f}")
        
        distance_finale = 1 / meilleure_fitness - 1
        return meilleur_circuit, distance_finale
    
    def selection_tournoi(self, fitness_population, taille_tournoi=3):
        """Sélection par tournoi"""
        participants = random.sample(fitness_population, taille_tournoi)
        return max(participants, key=lambda x: x[1])[0]

# Exemples d'utilisation
if __name__ == "__main__":
    print("=== Algorithmes d'approximation ===")
    
    # Test couverture de sommets
    graphe = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 5), (2, 4)]
    couverture = AlgorithmeApproximation.couverture_sommets_glouton(graphe)
    print(f"Couverture de sommets: {couverture}")
    
    # Test TSP plus proche voisin
    distances_tsp = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    circuit, distance = AlgorithmeApproximation.tsp_plus_proche_voisin(distances_tsp)
    print(f"TSP plus proche voisin: {circuit}, distance = {distance}")
    
    # Test sac à dos glouton
    objets = [
        (10, 60, "objet1"),  # (poids, valeur, nom)
        (20, 100, "objet2"),
        (30, 120, "objet3")
    ]
    
    sac, valeur, poids = AlgorithmeApproximation.sac_a_dos_glouton(objets, 50)
    print(f"Sac à dos glouton: {sac}, valeur = {valeur}, poids = {poids}")
    
    print("\n=== Algorithme génétique pour TSP ===")
    
    # Test avec un problème TSP plus grand
    n_villes = 6
    distances_grandes = [[0] * n_villes for _ in range(n_villes)]
    
    # Générer des distances aléatoires symétriques
    for i in range(n_villes):
        for j in range(i + 1, n_villes):
            distance = random.randint(10, 100)
            distances_grandes[i][j] = distance
            distances_grandes[j][i] = distance
    
    ag = AlgorithmeGenetique(taille_population=30, nb_generations=50)
    circuit_ag, distance_ag = ag.resoudre_tsp(distances_grandes)
    
    print(f"Meilleur circuit trouvé: {circuit_ag}")
    print(f"Distance: {distance_ag:.2f}")
```

---

## Exercices pratiques

### Exercice 1 : Machine de Turing
Concevez une machine de Turing qui reconnaît le langage L = {w#w | w ∈ {0,1}*}.

### Exercice 2 : Problème de l'arrêt
Implémentez un détecteur d'arrêt heuristique qui utilise plusieurs techniques (analyse statique, timeout, détection de cycles).

### Exercice 3 : Réduction
Implémentez la réduction du problème de la couverture de sommets vers le problème de l'ensemble indépendant.

### Exercice 4 : Algorithme d'approximation
Concevez un algorithme d'approximation pour le problème de la coloration de graphe et analysez son ratio d'approximation.

### Exercice 5 : Complexité expérimentale
Mesurez empiriquement la complexité de différents algorithmes et comparez avec la théorie.

---

## Conclusion

La calculabilité et la décidabilité nous enseignent les limites fondamentales de l'informatique :

**Limites théoriques :**
- Certains problèmes sont intrinsèquement impossibles à résoudre
- La complexité impose des contraintes pratiques
- Les approximations sont souvent nécessaires

**Implications pratiques :**
- Choix d'algorithmes appropriés
- Reconnaissance des problèmes difficiles
- Développement d'heuristiques efficaces

**Perspectives :**
- Informatique quantique
- Nouveaux modèles de calcul
- Algorithmes d'approximation avancés

Ces concepts fondamentaux guident la recherche en informatique et influencent la conception de systèmes informatiques efficaces.