# Récursivité

## Introduction

La récursivité est un concept fondamental en informatique où une fonction s'appelle elle-même pour résoudre un problème. Cette approche permet de décomposer des problèmes complexes en sous-problèmes plus simples de même nature.

---

## Concepts fondamentaux

### Définition

**Récursivité :** Une fonction est récursive si elle s'appelle elle-même directement ou indirectement.

**Éléments essentiels :**
1. **Cas de base** : Condition d'arrêt qui évite la récursion infinie
2. **Cas récursif** : Appel de la fonction sur un problème plus petit
3. **Convergence** : Garantie que les appels récursifs tendent vers le cas de base

### Structure générale

```python
def fonction_recursive(parametres):
    # Cas de base
    if condition_arret:
        return valeur_simple
    
    # Cas récursif
    else:
        # Traitement
        resultat_partiel = fonction_recursive(parametres_reduits)
        return combiner(resultat_partiel)
```

---

## Récursivité simple

### Factorielle

**Définition mathématique :**
- n! = 1 si n = 0
- n! = n × (n-1)! si n > 0

```python
def factorielle(n):
    """Calcule n! de manière récursive"""
    # Cas de base
    if n == 0 or n == 1:
        return 1
    
    # Cas récursif
    else:
        return n * factorielle(n - 1)

# Version avec vérification d'erreur
def factorielle_securisee(n):
    """Version sécurisée avec gestion d'erreurs"""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n doit être un entier positif")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorielle_securisee(n - 1)

# Test
for i in range(6):
    print(f"{i}! = {factorielle(i)}")
```

### Suite de Fibonacci

**Définition :**
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) pour n ≥ 2

```python
def fibonacci_naif(n):
    """Version naïve (inefficace) de Fibonacci"""
    if n <= 1:
        return n
    
    return fibonacci_naif(n - 1) + fibonacci_naif(n - 2)

def fibonacci_memo(n, memo={}):
    """Version avec mémoïsation"""
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

def fibonacci_iteratif(n):
    """Version itérative pour comparaison"""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Comparaison des performances
import time

def comparer_fibonacci(n):
    """Compare les différentes implémentations"""
    print(f"Calcul de F({n}):")
    
    # Version naïve (seulement pour petites valeurs)
    if n <= 35:
        start = time.time()
        result_naif = fibonacci_naif(n)
        time_naif = time.time() - start
        print(f"  Naïf: {result_naif} (temps: {time_naif:.4f}s)")
    
    # Version avec mémoïsation
    start = time.time()
    result_memo = fibonacci_memo(n, {})
    time_memo = time.time() - start
    print(f"  Mémoïsation: {result_memo} (temps: {time_memo:.6f}s)")
    
    # Version itérative
    start = time.time()
    result_iter = fibonacci_iteratif(n)
    time_iter = time.time() - start
    print(f"  Itératif: {result_iter} (temps: {time_iter:.6f}s)")

# Tests
for n in [10, 20, 30]:
    comparer_fibonacci(n)
    print()
```

### Puissance

```python
def puissance_naive(base, exposant):
    """Calcul naïf de base^exposant"""
    if exposant == 0:
        return 1
    
    return base * puissance_naive(base, exposant - 1)

def puissance_rapide(base, exposant):
    """Exponentiation rapide (diviser pour régner)"""
    if exposant == 0:
        return 1
    
    if exposant % 2 == 0:
        # Exposant pair : base^n = (base^(n/2))^2
        moitie = puissance_rapide(base, exposant // 2)
        return moitie * moitie
    else:
        # Exposant impair : base^n = base * base^(n-1)
        return base * puissance_rapide(base, exposant - 1)

# Comparaison
def comparer_puissance(base, exposant):
    """Compare les deux méthodes"""
    import time
    
    # Méthode naïve
    start = time.time()
    result_naive = puissance_naive(base, exposant)
    time_naive = time.time() - start
    
    # Méthode rapide
    start = time.time()
    result_rapide = puissance_rapide(base, exposant)
    time_rapide = time.time() - start
    
    print(f"{base}^{exposant}:")
    print(f"  Naïf: {result_naive} (temps: {time_naive:.6f}s)")
    print(f"  Rapide: {result_rapide} (temps: {time_rapide:.6f}s)")
    print(f"  Accélération: {time_naive/time_rapide:.2f}x")

# Test
comparer_puissance(2, 20)
```

---

## Récursivité sur les structures de données

### Listes

```python
def somme_liste(liste):
    """Calcule la somme des éléments d'une liste"""
    if not liste:  # Liste vide
        return 0
    
    return liste[0] + somme_liste(liste[1:])

def longueur_liste(liste):
    """Calcule la longueur d'une liste"""
    if not liste:
        return 0
    
    return 1 + longueur_liste(liste[1:])

def maximum_liste(liste):
    """Trouve le maximum d'une liste"""
    if len(liste) == 1:
        return liste[0]
    
    max_reste = maximum_liste(liste[1:])
    return liste[0] if liste[0] > max_reste else max_reste

def inverser_liste(liste):
    """Inverse une liste"""
    if len(liste) <= 1:
        return liste
    
    return [liste[-1]] + inverser_liste(liste[:-1])

def recherche_recursive(liste, element):
    """Recherche un élément dans une liste"""
    if not liste:
        return False
    
    if liste[0] == element:
        return True
    
    return recherche_recursive(liste[1:], element)

# Tests
liste_test = [1, 5, 3, 9, 2, 7]
print(f"Liste: {liste_test}")
print(f"Somme: {somme_liste(liste_test)}")
print(f"Longueur: {longueur_liste(liste_test)}")
print(f"Maximum: {maximum_liste(liste_test)}")
print(f"Inversée: {inverser_liste(liste_test)}")
print(f"Contient 5: {recherche_recursive(liste_test, 5)}")
print(f"Contient 10: {recherche_recursive(liste_test, 10)}")
```

### Chaînes de caractères

```python
def est_palindrome(chaine):
    """Vérifie si une chaîne est un palindrome"""
    # Nettoyer la chaîne (enlever espaces et ponctuation, mettre en minuscules)
    chaine_propre = ''.join(c.lower() for c in chaine if c.isalnum())
    
    def palindrome_recursif(s):
        if len(s) <= 1:
            return True
        
        if s[0] != s[-1]:
            return False
        
        return palindrome_recursif(s[1:-1])
    
    return palindrome_recursif(chaine_propre)

def compter_caractere(chaine, caractere):
    """Compte les occurrences d'un caractère"""
    if not chaine:
        return 0
    
    count = 1 if chaine[0] == caractere else 0
    return count + compter_caractere(chaine[1:], caractere)

def remplacer_caractere(chaine, ancien, nouveau):
    """Remplace toutes les occurrences d'un caractère"""
    if not chaine:
        return ""
    
    premier = nouveau if chaine[0] == ancien else chaine[0]
    return premier + remplacer_caractere(chaine[1:], ancien, nouveau)

# Tests
print(f"'radar' est palindrome: {est_palindrome('radar')}")
print(f"'A man a plan a canal Panama' est palindrome: {est_palindrome('A man a plan a canal Panama')}")
print(f"'hello' est palindrome: {est_palindrome('hello')}")
print(f"Nombre de 'l' dans 'hello': {compter_caractere('hello', 'l')}")
print(f"Remplacer 'l' par 'x' dans 'hello': {remplacer_caractere('hello', 'l', 'x')}")
```

---

## Récursivité sur les arbres

### Définition d'un arbre binaire

```python
class Noeud:
    """Représente un nœud d'arbre binaire"""
    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite
    
    def __str__(self):
        return str(self.valeur)

class ArbreBinaire:
    """Arbre binaire avec opérations récursives"""
    
    def __init__(self, racine=None):
        self.racine = racine
    
    def hauteur(self, noeud=None):
        """Calcule la hauteur de l'arbre"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return 0
        
        hauteur_gauche = self.hauteur(noeud.gauche)
        hauteur_droite = self.hauteur(noeud.droite)
        
        return 1 + max(hauteur_gauche, hauteur_droite)
    
    def taille(self, noeud=None):
        """Compte le nombre de nœuds"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return 0
        
        return 1 + self.taille(noeud.gauche) + self.taille(noeud.droite)
    
    def somme(self, noeud=None):
        """Calcule la somme des valeurs"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return 0
        
        return noeud.valeur + self.somme(noeud.gauche) + self.somme(noeud.droite)
    
    def rechercher(self, valeur, noeud=None):
        """Recherche une valeur dans l'arbre"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return False
        
        if noeud.valeur == valeur:
            return True
        
        return (self.rechercher(valeur, noeud.gauche) or 
                self.rechercher(valeur, noeud.droite))
    
    def parcours_prefixe(self, noeud=None, resultat=None):
        """Parcours préfixe (racine, gauche, droite)"""
        if resultat is None:
            resultat = []
        
        if noeud is None:
            noeud = self.racine
        
        if noeud is not None:
            resultat.append(noeud.valeur)
            self.parcours_prefixe(noeud.gauche, resultat)
            self.parcours_prefixe(noeud.droite, resultat)
        
        return resultat
    
    def parcours_infixe(self, noeud=None, resultat=None):
        """Parcours infixe (gauche, racine, droite)"""
        if resultat is None:
            resultat = []
        
        if noeud is None:
            noeud = self.racine
        
        if noeud is not None:
            self.parcours_infixe(noeud.gauche, resultat)
            resultat.append(noeud.valeur)
            self.parcours_infixe(noeud.droite, resultat)
        
        return resultat
    
    def parcours_postfixe(self, noeud=None, resultat=None):
        """Parcours postfixe (gauche, droite, racine)"""
        if resultat is None:
            resultat = []
        
        if noeud is None:
            noeud = self.racine
        
        if noeud is not None:
            self.parcours_postfixe(noeud.gauche, resultat)
            self.parcours_postfixe(noeud.droite, resultat)
            resultat.append(noeud.valeur)
        
        return resultat
    
    def est_equilibre(self, noeud=None):
        """Vérifie si l'arbre est équilibré"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return True
        
        hauteur_gauche = self.hauteur(noeud.gauche)
        hauteur_droite = self.hauteur(noeud.droite)
        
        return (abs(hauteur_gauche - hauteur_droite) <= 1 and
                self.est_equilibre(noeud.gauche) and
                self.est_equilibre(noeud.droite))
    
    def miroir(self, noeud=None):
        """Crée le miroir de l'arbre"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return None
        
        nouveau_noeud = Noeud(noeud.valeur)
        nouveau_noeud.gauche = self.miroir(noeud.droite)
        nouveau_noeud.droite = self.miroir(noeud.gauche)
        
        return nouveau_noeud
    
    def afficher_arbre(self, noeud=None, niveau=0, prefixe="Racine: "):
        """Affiche l'arbre de manière visuelle"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is not None:
            print(" " * (niveau * 4) + prefixe + str(noeud.valeur))
            if noeud.gauche is not None or noeud.droite is not None:
                if noeud.gauche is not None:
                    self.afficher_arbre(noeud.gauche, niveau + 1, "G--- ")
                else:
                    print(" " * ((niveau + 1) * 4) + "G--- None")
                
                if noeud.droite is not None:
                    self.afficher_arbre(noeud.droite, niveau + 1, "D--- ")
                else:
                    print(" " * ((niveau + 1) * 4) + "D--- None")

# Création d'un arbre exemple
#       1
#      / \
#     2   3
#    / \
#   4   5

racine = Noeud(1)
racine.gauche = Noeud(2)
racine.droite = Noeud(3)
racine.gauche.gauche = Noeud(4)
racine.gauche.droite = Noeud(5)

arbre = ArbreBinaire(racine)

# Tests
print("Arbre:")
arbre.afficher_arbre()
print(f"\nHauteur: {arbre.hauteur()}")
print(f"Taille: {arbre.taille()}")
print(f"Somme: {arbre.somme()}")
print(f"Recherche 3: {arbre.rechercher(3)}")
print(f"Recherche 6: {arbre.rechercher(6)}")
print(f"Parcours préfixe: {arbre.parcours_prefixe()}")
print(f"Parcours infixe: {arbre.parcours_infixe()}")
print(f"Parcours postfixe: {arbre.parcours_postfixe()}")
print(f"Est équilibré: {arbre.est_equilibre()}")
```

---

## Diviser pour régner

### Tri fusion (Merge Sort)

```python
def tri_fusion(liste):
    """Tri fusion récursif"""
    # Cas de base
    if len(liste) <= 1:
        return liste
    
    # Diviser
    milieu = len(liste) // 2
    gauche = liste[:milieu]
    droite = liste[milieu:]
    
    # Conquérir (appels récursifs)
    gauche_triee = tri_fusion(gauche)
    droite_triee = tri_fusion(droite)
    
    # Combiner
    return fusionner(gauche_triee, droite_triee)

def fusionner(gauche, droite):
    """Fusionne deux listes triées"""
    resultat = []
    i = j = 0
    
    # Fusionner les éléments en ordre
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    
    # Ajouter les éléments restants
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    
    return resultat

# Version avec visualisation
def tri_fusion_verbose(liste, niveau=0):
    """Tri fusion avec affichage des étapes"""
    indent = "  " * niveau
    print(f"{indent}Diviser: {liste}")
    
    if len(liste) <= 1:
        print(f"{indent}Cas de base: {liste}")
        return liste
    
    milieu = len(liste) // 2
    gauche = liste[:milieu]
    droite = liste[milieu:]
    
    print(f"{indent}Gauche: {gauche}, Droite: {droite}")
    
    gauche_triee = tri_fusion_verbose(gauche, niveau + 1)
    droite_triee = tri_fusion_verbose(droite, niveau + 1)
    
    resultat = fusionner(gauche_triee, droite_triee)
    print(f"{indent}Fusionner: {gauche_triee} + {droite_triee} = {resultat}")
    
    return resultat

# Test
liste_test = [64, 34, 25, 12, 22, 11, 90]
print(f"Liste originale: {liste_test}")
print("\nTri fusion avec visualisation:")
liste_triee = tri_fusion_verbose(liste_test.copy())
print(f"\nRésultat final: {liste_triee}")
```

### Recherche dichotomique

```python
def recherche_dichotomique(liste, element, debut=0, fin=None):
    """Recherche dichotomique récursive"""
    if fin is None:
        fin = len(liste) - 1
    
    # Cas de base : élément non trouvé
    if debut > fin:
        return -1
    
    milieu = (debut + fin) // 2
    
    # Élément trouvé
    if liste[milieu] == element:
        return milieu
    
    # Rechercher dans la moitié appropriée
    elif liste[milieu] > element:
        return recherche_dichotomique(liste, element, debut, milieu - 1)
    else:
        return recherche_dichotomique(liste, element, milieu + 1, fin)

# Version avec visualisation
def recherche_dichotomique_verbose(liste, element, debut=0, fin=None, niveau=0):
    """Recherche dichotomique avec affichage des étapes"""
    if fin is None:
        fin = len(liste) - 1
    
    indent = "  " * niveau
    print(f"{indent}Recherche de {element} dans {liste[debut:fin+1]} (indices {debut}-{fin})")
    
    if debut > fin:
        print(f"{indent}Élément non trouvé")
        return -1
    
    milieu = (debut + fin) // 2
    print(f"{indent}Milieu: index {milieu}, valeur {liste[milieu]}")
    
    if liste[milieu] == element:
        print(f"{indent}Élément trouvé à l'index {milieu}")
        return milieu
    elif liste[milieu] > element:
        print(f"{indent}{liste[milieu]} > {element}, recherche à gauche")
        return recherche_dichotomique_verbose(liste, element, debut, milieu - 1, niveau + 1)
    else:
        print(f"{indent}{liste[milieu]} < {element}, recherche à droite")
        return recherche_dichotomique_verbose(liste, element, milieu + 1, fin, niveau + 1)

# Test
liste_triee = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"Liste: {liste_triee}")
print("\nRecherche de 7:")
index = recherche_dichotomique_verbose(liste_triee, 7)
print(f"\nRecherche de 8:")
index = recherche_dichotomique_verbose(liste_triee, 8)
```

### Tours de Hanoï

```python
def tours_hanoi(n, source, destination, auxiliaire):
    """Résout le problème des Tours de Hanoï"""
    if n == 1:
        print(f"Déplacer disque 1 de {source} vers {destination}")
        return 1
    
    # Déplacer n-1 disques vers l'auxiliaire
    mouvements = tours_hanoi(n - 1, source, auxiliaire, destination)
    
    # Déplacer le plus grand disque vers la destination
    print(f"Déplacer disque {n} de {source} vers {destination}")
    mouvements += 1
    
    # Déplacer les n-1 disques de l'auxiliaire vers la destination
    mouvements += tours_hanoi(n - 1, auxiliaire, destination, source)
    
    return mouvements

# Version avec visualisation de l'état
class ToursHanoi:
    """Simulation complète des Tours de Hanoï"""
    
    def __init__(self, n):
        self.n = n
        self.tours = {
            'A': list(range(n, 0, -1)),  # Tour A avec tous les disques
            'B': [],                      # Tour B vide
            'C': []                       # Tour C vide
        }
        self.mouvements = 0
    
    def afficher_etat(self):
        """Affiche l'état actuel des tours"""
        print(f"\nÉtat après {self.mouvements} mouvements:")
        hauteur_max = max(len(tour) for tour in self.tours.values())
        
        for niveau in range(hauteur_max - 1, -1, -1):
            ligne = ""
            for nom_tour in ['A', 'B', 'C']:
                if niveau < len(self.tours[nom_tour]):
                    disque = self.tours[nom_tour][niveau]
                    ligne += f"  {disque}  "
                else:
                    ligne += f"  |  "
            print(ligne)
        
        print("  A    B    C  ")
        print("-" * 15)
    
    def deplacer_disque(self, source, destination):
        """Déplace un disque d'une tour à une autre"""
        if not self.tours[source]:
            raise ValueError(f"Tour {source} est vide")
        
        disque = self.tours[source].pop()
        
        if self.tours[destination] and self.tours[destination][-1] < disque:
            raise ValueError(f"Ne peut pas placer disque {disque} sur disque {self.tours[destination][-1]}")
        
        self.tours[destination].append(disque)
        self.mouvements += 1
        
        print(f"Mouvement {self.mouvements}: Déplacer disque {disque} de {source} vers {destination}")
        self.afficher_etat()
    
    def resoudre(self, n=None, source='A', destination='C', auxiliaire='B'):
        """Résout le problème avec visualisation"""
        if n is None:
            n = self.n
        
        if n == 1:
            self.deplacer_disque(source, destination)
            return
        
        # Déplacer n-1 disques vers l'auxiliaire
        self.resoudre(n - 1, source, auxiliaire, destination)
        
        # Déplacer le plus grand disque vers la destination
        self.deplacer_disque(source, destination)
        
        # Déplacer les n-1 disques de l'auxiliaire vers la destination
        self.resoudre(n - 1, auxiliaire, destination, source)

# Test
print("=== Tours de Hanoï (version simple) ===")
print(f"Solution pour 3 disques:")
mouvements = tours_hanoi(3, 'A', 'C', 'B')
print(f"\nNombre total de mouvements: {mouvements}")
print(f"Formule théorique: 2^n - 1 = {2**3 - 1}")

print("\n=== Tours de Hanoï (avec visualisation) ===")
jeu = ToursHanoi(3)
jeu.afficher_etat()
jeu.resoudre()
print(f"\nProblème résolu en {jeu.mouvements} mouvements!")
```

---

## Récursivité mutuelle

### Fonctions mutuellement récursives

```python
def est_pair(n):
    """Détermine si un nombre est pair (récursivité mutuelle)"""
    if n == 0:
        return True
    else:
        return est_impair(n - 1)

def est_impair(n):
    """Détermine si un nombre est impair (récursivité mutuelle)"""
    if n == 0:
        return False
    else:
        return est_pair(n - 1)

# Test
for i in range(10):
    print(f"{i} est {'pair' if est_pair(i) else 'impair'}")
```

### Automate à états finis

```python
class AutomateRecursif:
    """Automate à états finis implémenté avec récursivité mutuelle"""
    
    def __init__(self):
        self.position = 0
        self.chaine = ""
    
    def reconnaitre(self, chaine):
        """Reconnaît si une chaîne appartient au langage (a*b*)"""
        self.chaine = chaine
        self.position = 0
        return self.etat_initial()
    
    def etat_initial(self):
        """État initial : peut lire des 'a' ou passer aux 'b'"""
        if self.position >= len(self.chaine):
            return True  # Chaîne vide acceptée
        
        if self.chaine[self.position] == 'a':
            self.position += 1
            return self.etat_a()
        elif self.chaine[self.position] == 'b':
            self.position += 1
            return self.etat_b()
        else:
            return False  # Caractère non reconnu
    
    def etat_a(self):
        """État après avoir lu des 'a' : peut lire plus de 'a' ou des 'b'"""
        if self.position >= len(self.chaine):
            return True  # Fin de chaîne après des 'a'
        
        if self.chaine[self.position] == 'a':
            self.position += 1
            return self.etat_a()  # Rester dans l'état 'a'
        elif self.chaine[self.position] == 'b':
            self.position += 1
            return self.etat_b()  # Passer à l'état 'b'
        else:
            return False
    
    def etat_b(self):
        """État après avoir lu des 'b' : peut seulement lire plus de 'b'"""
        if self.position >= len(self.chaine):
            return True  # Fin de chaîne après des 'b'
        
        if self.chaine[self.position] == 'b':
            self.position += 1
            return self.etat_b()  # Rester dans l'état 'b'
        else:
            return False  # Pas de retour aux 'a' possible

# Test de l'automate
automate = AutomateRecursif()

chaines_test = [
    "",        # Acceptée
    "a",       # Acceptée
    "b",       # Acceptée
    "aa",      # Acceptée
    "bb",      # Acceptée
    "ab",      # Acceptée
    "aab",     # Acceptée
    "abb",     # Acceptée
    "aabb",    # Acceptée
    "ba",      # Rejetée
    "aba",     # Rejetée
    "abab",    # Rejetée
    "c",       # Rejetée
]

print("Test de l'automate (langage a*b*):")
for chaine in chaines_test:
    resultat = automate.reconnaitre(chaine)
    print(f"'{chaine}' : {'Acceptée' if resultat else 'Rejetée'}")
```

---

## Optimisation de la récursivité

### Mémoïsation

```python
from functools import lru_cache
import time

# Décorateur de mémoïsation personnalisé
def memoize(func):
    """Décorateur de mémoïsation"""
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        return result
    
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    return wrapper

# Comparaison des approches pour Fibonacci
@memoize
def fibonacci_memo_decorateur(n):
    """Fibonacci avec décorateur de mémoïsation"""
    if n <= 1:
        return n
    return fibonacci_memo_decorateur(n - 1) + fibonacci_memo_decorateur(n - 2)

@lru_cache(maxsize=None)
def fibonacci_lru_cache(n):
    """Fibonacci avec LRU cache de Python"""
    if n <= 1:
        return n
    return fibonacci_lru_cache(n - 1) + fibonacci_lru_cache(n - 2)

def fibonacci_dp(n):
    """Fibonacci avec programmation dynamique (bottom-up)"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# Comparaison des performances
def comparer_optimisations(n):
    """Compare les différentes optimisations"""
    print(f"Calcul de Fibonacci({n}):")
    
    # Mémoïsation avec décorateur
    fibonacci_memo_decorateur.cache_clear()
    start = time.time()
    result1 = fibonacci_memo_decorateur(n)
    time1 = time.time() - start
    print(f"  Mémoïsation (décorateur): {result1} (temps: {time1:.6f}s)")
    
    # LRU Cache
    fibonacci_lru_cache.cache_clear()
    start = time.time()
    result2 = fibonacci_lru_cache(n)
    time2 = time.time() - start
    print(f"  LRU Cache: {result2} (temps: {time2:.6f}s)")
    
    # Programmation dynamique
    start = time.time()
    result3 = fibonacci_dp(n)
    time3 = time.time() - start
    print(f"  Programmation dynamique: {result3} (temps: {time3:.6f}s)")
    
    print(f"  Taille du cache (décorateur): {len(fibonacci_memo_decorateur.cache)}")
    print(f"  Info LRU Cache: {fibonacci_lru_cache.cache_info()}")

# Tests
for n in [30, 50, 100]:
    comparer_optimisations(n)
    print()
```

### Récursivité terminale

```python
def factorielle_terminale(n, accumulateur=1):
    """Factorielle avec récursivité terminale"""
    if n <= 1:
        return accumulateur
    
    return factorielle_terminale(n - 1, n * accumulateur)

def fibonacci_terminale(n, a=0, b=1):
    """Fibonacci avec récursivité terminale"""
    if n == 0:
        return a
    
    return fibonacci_terminale(n - 1, b, a + b)

def somme_liste_terminale(liste, accumulateur=0):
    """Somme de liste avec récursivité terminale"""
    if not liste:
        return accumulateur
    
    return somme_liste_terminale(liste[1:], accumulateur + liste[0])

# Simulation de l'optimisation de récursivité terminale
class OptimisateurRecursiviteTerminale:
    """Simule l'optimisation de récursivité terminale"""
    
    @staticmethod
    def factorielle_optimisee(n):
        """Factorielle optimisée (simulation)"""
        accumulateur = 1
        
        while n > 1:
            accumulateur *= n
            n -= 1
        
        return accumulateur
    
    @staticmethod
    def fibonacci_optimise(n):
        """Fibonacci optimisé (simulation)"""
        a, b = 0, 1
        
        while n > 0:
            a, b = b, a + b
            n -= 1
        
        return a

# Tests
print("Récursivité terminale:")
print(f"Factorielle(10): {factorielle_terminale(10)}")
print(f"Fibonacci(10): {fibonacci_terminale(10)}")
print(f"Somme [1,2,3,4,5]: {somme_liste_terminale([1,2,3,4,5])}")

print("\nVersions optimisées:")
print(f"Factorielle(10): {OptimisateurRecursiviteTerminale.factorielle_optimisee(10)}")
print(f"Fibonacci(10): {OptimisateurRecursiviteTerminale.fibonacci_optimise(10)}")
```

---

## Analyse de complexité

### Complexité temporelle

```python
import matplotlib.pyplot as plt
import time
import sys

# Augmenter la limite de récursion pour les tests
sys.setrecursionlimit(10000)

class AnalyseurComplexite:
    """Analyse la complexité des algorithmes récursifs"""
    
    @staticmethod
    def mesurer_temps(fonction, *args):
        """Mesure le temps d'exécution d'une fonction"""
        start = time.time()
        try:
            resultat = fonction(*args)
            temps = time.time() - start
            return temps, resultat
        except RecursionError:
            return float('inf'), None
    
    @staticmethod
    def analyser_fibonacci():
        """Analyse la complexité de différentes versions de Fibonacci"""
        print("Analyse de complexité - Fibonacci:")
        print("n\tNaïf\t\tMémo\t\tItératif")
        print("-" * 50)
        
        for n in range(5, 36, 5):
            # Version naïve (limitée)
            if n <= 30:
                temps_naif, _ = AnalyseurComplexite.mesurer_temps(fibonacci_naif, n)
            else:
                temps_naif = float('inf')
            
            # Version avec mémoïsation
            temps_memo, _ = AnalyseurComplexite.mesurer_temps(fibonacci_memo, n, {})
            
            # Version itérative
            temps_iter, _ = AnalyseurComplexite.mesurer_temps(fibonacci_iteratif, n)
            
            print(f"{n}\t{temps_naif:.6f}\t{temps_memo:.6f}\t{temps_iter:.6f}")
    
    @staticmethod
    def analyser_tri_fusion():
        """Analyse la complexité du tri fusion"""
        import random
        
        print("\nAnalyse de complexité - Tri fusion:")
        print("Taille\tTemps (s)\tComparaisons théoriques")
        print("-" * 45)
        
        for taille in [100, 500, 1000, 2000, 5000]:
            # Générer une liste aléatoire
            liste = [random.randint(1, 1000) for _ in range(taille)]
            
            temps, _ = AnalyseurComplexite.mesurer_temps(tri_fusion, liste)
            comparaisons_theoriques = taille * (taille.bit_length() - 1)  # Approximation de n*log(n)
            
            print(f"{taille}\t{temps:.6f}\t{comparaisons_theoriques}")
    
    @staticmethod
    def compter_appels_recursifs(fonction_originale):
        """Décorateur pour compter les appels récursifs"""
        def decorateur(func):
            func.compteur = 0
            
            def wrapper(*args, **kwargs):
                func.compteur += 1
                return fonction_originale(*args, **kwargs)
            
            wrapper.compteur = 0
            wrapper.reset_compteur = lambda: setattr(wrapper, 'compteur', 0)
            return wrapper
        
        return decorateur

# Application du compteur d'appels
@AnalyseurComplexite.compter_appels_recursifs(fibonacci_naif)
def fibonacci_avec_compteur(n):
    if n <= 1:
        return n
    return fibonacci_avec_compteur(n - 1) + fibonacci_avec_compteur(n - 2)

# Tests d'analyse
if __name__ == "__main__":
    # Analyse de Fibonacci
    AnalyseurComplexite.analyser_fibonacci()
    
    # Analyse du tri fusion
    AnalyseurComplexite.analyser_tri_fusion()
    
    # Comptage des appels récursifs
    print("\nComptage des appels récursifs (Fibonacci naïf):")
    print("n\tAppels\tRésultat")
    print("-" * 25)
    
    for n in range(1, 11):
        fibonacci_avec_compteur.reset_compteur()
        resultat = fibonacci_avec_compteur(n)
        print(f"{n}\t{fibonacci_avec_compteur.compteur}\t{resultat}")
```

---

## Exercices pratiques

### Exercice 1 : Parcours de labyrinthe

```python
def resoudre_labyrinthe(labyrinthe, start, end, chemin=None, visite=None):
    """Résout un labyrinthe par backtracking récursif"""
    if chemin is None:
        chemin = []
    if visite is None:
        visite = set()
    
    x, y = start
    
    # Vérifications de base
    if (x < 0 or x >= len(labyrinthe) or 
        y < 0 or y >= len(labyrinthe[0]) or
        labyrinthe[x][y] == 1 or  # Mur
        (x, y) in visite):        # Déjà visité
        return False
    
    # Ajouter la position actuelle au chemin
    chemin.append((x, y))
    visite.add((x, y))
    
    # Vérifier si on a atteint la destination
    if (x, y) == end:
        return True
    
    # Explorer les 4 directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # droite, bas, gauche, haut
    
    for dx, dy in directions:
        nouvelle_pos = (x + dx, y + dy)
        if resoudre_labyrinthe(labyrinthe, nouvelle_pos, end, chemin, visite):
            return True
    
    # Backtrack : retirer la position actuelle
    chemin.pop()
    visite.remove((x, y))
    return False

# Test du labyrinthe
labyrinthe = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
end = (4, 4)
chemin = []

print("Labyrinthe (0=libre, 1=mur):")
for ligne in labyrinthe:
    print(ligne)

if resoudre_labyrinthe(labyrinthe, start, end, chemin):
    print(f"\nChemin trouvé: {chemin}")
else:
    print("\nAucun chemin trouvé")
```

### Exercice 2 : Génération de permutations

```python
def generer_permutations(elements):
    """Génère toutes les permutations d'une liste"""
    if len(elements) <= 1:
        return [elements]
    
    permutations = []
    
    for i in range(len(elements)):
        # Prendre l'élément à la position i
        element_courant = elements[i]
        # Créer une liste sans cet élément
        elements_restants = elements[:i] + elements[i+1:]
        
        # Générer les permutations des éléments restants
        for perm in generer_permutations(elements_restants):
            # Ajouter l'élément courant au début
            permutations.append([element_courant] + perm)
    
    return permutations

# Test
elements = ['A', 'B', 'C']
permutations = generer_permutations(elements)
print(f"Permutations de {elements}:")
for i, perm in enumerate(permutations, 1):
    print(f"{i}: {perm}")
print(f"\nNombre total: {len(permutations)}")
```

### Exercice 3 : Problème des N-reines

```python
def n_reines(n):
    """Résout le problème des N-reines"""
    def est_valide(positions, ligne, colonne):
        """Vérifie si placer une reine en (ligne, colonne) est valide"""
        for i in range(ligne):
            # Vérifier la colonne et les diagonales
            if (positions[i] == colonne or
                positions[i] - i == colonne - ligne or
                positions[i] + i == colonne + ligne):
                return False
        return True
    
    def placer_reines(positions, ligne):
        """Place les reines récursivement"""
        if ligne == n:
            return [positions[:]]
        
        solutions = []
        for colonne in range(n):
            if est_valide(positions, ligne, colonne):
                positions[ligne] = colonne
                solutions.extend(placer_reines(positions, ligne + 1))
        
        return solutions
    
    return placer_reines([-1] * n, 0)

def afficher_echiquier(solution, n):
    """Affiche une solution du problème des N-reines"""
    for ligne in range(n):
        for colonne in range(n):
            if solution[ligne] == colonne:
                print("♛ ", end="")
            else:
                print(". ", end="")
        print()
    print()

# Test
n = 4
solutions = n_reines(n)
print(f"Problème des {n}-reines:")
print(f"Nombre de solutions: {len(solutions)}")
print("\nPremière solution:")
if solutions:
    afficher_echiquier(solutions[0], n)
```

---

## Conclusion

La récursivité est un outil puissant qui permet :

**Avantages :**
- Code plus lisible et élégant
- Résolution naturelle de problèmes auto-similaires
- Implémentation directe d'algorithmes mathématiques

**Inconvénients :**
- Consommation mémoire (pile d'appels)
- Risque de débordement de pile
- Parfois moins efficace que les versions itératives

**Bonnes pratiques :**
- Toujours définir un cas de base clair
- S'assurer de la convergence vers le cas de base
- Utiliser la mémoïsation pour éviter les recalculs
- Considérer les versions itératives pour les cas critiques

**Applications importantes :**
- Structures de données (arbres, graphes)
- Algorithmes de tri et recherche
- Problèmes de backtracking
- Analyse syntaxique
- Fractales et géométrie

La maîtrise de la récursivité est essentielle pour comprendre de nombreux algorithmes avancés et structures de données complexes.