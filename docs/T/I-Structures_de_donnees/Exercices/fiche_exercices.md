# Fiche d'exercices - Structures de données

## Exercice 1 : Pile d'opérations

**Niveau :** ⭐⭐

Implémentez une calculatrice qui utilise une pile pour évaluer des expressions arithmétiques en notation postfixée (polonaise inverse).

### Questions :

1. **Implémentation de base**
   ```python
   def evaluer_postfixe(expression):
       """
       Évalue une expression en notation postfixée
       Exemple : "3 4 + 2 *" → 14
       """
       # À compléter
       pass
   ```

2. **Extension avec fonctions**
   Étendez votre calculatrice pour supporter les fonctions `sin`, `cos`, `sqrt`.

3. **Gestion d'erreurs**
   Ajoutez la gestion des erreurs (division par zéro, pile vide, etc.).

### Tests :
```python
# Tests à effectuer
assert evaluer_postfixe("3 4 +") == 7
assert evaluer_postfixe("15 7 1 1 + - / 3 * 2 1 1 + + -") == 5
assert evaluer_postfixe("5 1 2 + 4 * + 3 -") == 14
```

---

## Exercice 2 : File de priorité avec listes

**Niveau :** ⭐⭐⭐

Implémentez une file de priorité pour un système de gestion d'urgences médicales.

### Spécifications :
- Chaque patient a un nom, une priorité (1=critique, 2=urgent, 3=normal) et un temps d'arrivée
- Les patients sont traités par ordre de priorité, puis par ordre d'arrivée

```python
class Patient:
    def __init__(self, nom, priorite, temps_arrivee):
        self.nom = nom
        self.priorite = priorite
        self.temps_arrivee = temps_arrivee
    
    def __str__(self):
        return f"{self.nom} (P{self.priorite})"

class FileUrgences:
    def __init__(self):
        # À compléter
        pass
    
    def ajouter_patient(self, patient):
        """Ajoute un patient à la file"""
        # À compléter
        pass
    
    def traiter_patient(self):
        """Retire et retourne le patient prioritaire"""
        # À compléter
        pass
    
    def patients_en_attente(self):
        """Retourne la liste des patients en attente"""
        # À compléter
        pass
```

### Tests :
```python
file_urgences = FileUrgences()
file_urgences.ajouter_patient(Patient("Alice", 3, 10))
file_urgences.ajouter_patient(Patient("Bob", 1, 15))
file_urgences.ajouter_patient(Patient("Charlie", 2, 12))

# Bob doit être traité en premier (priorité 1)
patient = file_urgences.traiter_patient()
assert patient.nom == "Bob"
```

---

## Exercice 3 : Dictionnaire avec collision

**Niveau :** ⭐⭐⭐

Implémentez une table de hachage avec gestion des collisions par chaînage.

```python
class TableHachage:
    def __init__(self, taille=10):
        self.taille = taille
        self.table = [[] for _ in range(taille)]
        self.nb_elements = 0
    
    def _hash(self, cle):
        """Fonction de hachage simple"""
        # À compléter
        pass
    
    def ajouter(self, cle, valeur):
        """Ajoute ou met à jour une paire clé-valeur"""
        # À compléter
        pass
    
    def obtenir(self, cle):
        """Récupère la valeur associée à une clé"""
        # À compléter
        pass
    
    def supprimer(self, cle):
        """Supprime une paire clé-valeur"""
        # À compléter
        pass
    
    def facteur_charge(self):
        """Calcule le facteur de charge"""
        return self.nb_elements / self.taille
    
    def redimensionner(self):
        """Redimensionne la table si nécessaire"""
        # À compléter (optionnel)
        pass
```

### Questions :
1. Implémentez toutes les méthodes
2. Testez avec des clés qui génèrent des collisions
3. Mesurez les performances avec différentes tailles de table

---

## Exercice 4 : Arbre binaire de recherche équilibré

**Niveau :** ⭐⭐⭐⭐

Implémentez un arbre AVL (auto-équilibrant) avec rotations.

```python
class NoeudAVL:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None
        self.hauteur = 1

class ArbreAVL:
    def __init__(self):
        self.racine = None
    
    def hauteur(self, noeud):
        """Retourne la hauteur d'un nœud"""
        # À compléter
        pass
    
    def facteur_equilibre(self, noeud):
        """Calcule le facteur d'équilibre"""
        # À compléter
        pass
    
    def rotation_droite(self, y):
        """Rotation simple à droite"""
        # À compléter
        pass
    
    def rotation_gauche(self, x):
        """Rotation simple à gauche"""
        # À compléter
        pass
    
    def inserer(self, valeur):
        """Insère une valeur en maintenant l'équilibre"""
        self.racine = self._inserer_recursive(self.racine, valeur)
    
    def _inserer_recursive(self, noeud, valeur):
        """Insertion récursive avec rééquilibrage"""
        # À compléter
        pass
```

### Tests :
```python
avl = ArbreAVL()
valeurs = [10, 20, 30, 40, 50, 25]
for val in valeurs:
    avl.inserer(val)

# Vérifier que l'arbre reste équilibré
# La hauteur ne doit pas dépasser log₂(n) + 1
```

---

## Exercice 5 : Graphe de dépendances

**Niveau :** ⭐⭐⭐

Implémentez un système de gestion de dépendances pour un gestionnaire de paquets.

```python
class GestionnairePaquets:
    def __init__(self):
        self.dependances = {}  # paquet -> liste des dépendances
        self.installes = set()
    
    def ajouter_paquet(self, nom, dependances=[]):
        """Ajoute un paquet avec ses dépendances"""
        # À compléter
        pass
    
    def peut_installer(self, paquet):
        """Vérifie si un paquet peut être installé"""
        # À compléter
        pass
    
    def ordre_installation(self, paquet):
        """Retourne l'ordre d'installation des dépendances"""
        # À compléter
        pass
    
    def detecter_cycle(self):
        """Détecte les dépendances circulaires"""
        # À compléter
        pass
    
    def installer(self, paquet):
        """Installe un paquet et ses dépendances"""
        # À compléter
        pass
    
    def desinstaller(self, paquet):
        """Désinstalle un paquet si aucun autre ne dépend de lui"""
        # À compléter
        pass
```

### Scénario de test :
```python
gestionnaire = GestionnairePaquets()
gestionnaire.ajouter_paquet("A", [])
gestionnaire.ajouter_paquet("B", ["A"])
gestionnaire.ajouter_paquet("C", ["A", "B"])
gestionnaire.ajouter_paquet("D", ["B", "C"])

# Test d'installation
ordre = gestionnaire.ordre_installation("D")
print(f"Ordre d'installation pour D : {ordre}")  # ["A", "B", "C", "D"]

# Test de dépendance circulaire
gestionnaire.ajouter_paquet("E", ["F"])
gestionnaire.ajouter_paquet("F", ["E"])
assert gestionnaire.detecter_cycle() == True
```

---

## Exercice 6 : Réseau social - Analyse de graphe

**Niveau :** ⭐⭐⭐⭐

Analysez un réseau social avec différents algorithmes de graphes.

```python
class AnalyseurReseauSocial:
    def __init__(self):
        self.graphe = {}  # utilisateur -> liste d'amis
        self.posts = {}   # utilisateur -> liste de posts
    
    def ajouter_utilisateur(self, nom):
        """Ajoute un utilisateur"""
        # À compléter
        pass
    
    def ajouter_amitie(self, user1, user2):
        """Ajoute une relation d'amitié"""
        # À compléter
        pass
    
    def degres_separation(self, user1, user2):
        """Calcule les degrés de séparation entre deux utilisateurs"""
        # À compléter
        pass
    
    def amis_communs(self, user1, user2):
        """Trouve les amis communs"""
        # À compléter
        pass
    
    def suggestions_amis(self, utilisateur, nb_suggestions=5):
        """Suggère des amis basé sur les amis communs"""
        # À compléter
        pass
    
    def influenceurs(self, top_n=10):
        """Trouve les utilisateurs les plus influents (plus connectés)"""
        # À compléter
        pass
    
    def communautes(self):
        """Détecte les communautés (composantes connexes)"""
        # À compléter
        pass
    
    def coefficient_clustering(self, utilisateur):
        """Calcule le coefficient de clustering d'un utilisateur"""
        # À compléter
        pass
    
    def centralite_betweenness(self, utilisateur):
        """Calcule la centralité d'intermédiarité (optionnel)"""
        # À compléter (difficile)
        pass
```

### Données de test :
```python
analyseur = AnalyseurReseauSocial()

# Créer un petit réseau
utilisateurs = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
for user in utilisateurs:
    analyseur.ajouter_utilisateur(user)

# Ajouter des amitiés
amities = [
    ("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Diana"),
    ("Charlie", "Diana"), ("Diana", "Eve"), ("Eve", "Frank")
]
for user1, user2 in amities:
    analyseur.ajouter_amitie(user1, user2)

# Tests
print(f"Degrés de séparation Alice-Frank : {analyseur.degres_separation('Alice', 'Frank')}")
print(f"Amis communs Alice-Diana : {analyseur.amis_communs('Alice', 'Diana')}")
print(f"Suggestions pour Alice : {analyseur.suggestions_amis('Alice')}")
print(f"Influenceurs : {analyseur.influenceurs(3)}")
```

---

## Exercice 7 : Cache LRU avec structures combinées

**Niveau :** ⭐⭐⭐⭐

Implémentez un cache LRU (Least Recently Used) en combinant dictionnaire et liste doublement chaînée.

```python
class NoeudLRU:
    def __init__(self, cle=None, valeur=None):
        self.cle = cle
        self.valeur = valeur
        self.precedent = None
        self.suivant = None

class CacheLRU:
    def __init__(self, capacite):
        self.capacite = capacite
        self.cache = {}  # cle -> noeud
        
        # Sentinelles pour la liste doublement chaînée
        self.tete = NoeudLRU()
        self.queue = NoeudLRU()
        self.tete.suivant = self.queue
        self.queue.precedent = self.tete
    
    def _ajouter_en_tete(self, noeud):
        """Ajoute un nœud juste après la tête"""
        # À compléter
        pass
    
    def _supprimer_noeud(self, noeud):
        """Supprime un nœud de la liste"""
        # À compléter
        pass
    
    def _deplacer_en_tete(self, noeud):
        """Déplace un nœud en tête (récemment utilisé)"""
        # À compléter
        pass
    
    def _supprimer_queue(self):
        """Supprime le dernier nœud (LRU)"""
        # À compléter
        pass
    
    def get(self, cle):
        """Récupère une valeur du cache"""
        # À compléter
        pass
    
    def put(self, cle, valeur):
        """Ajoute/met à jour une valeur dans le cache"""
        # À compléter
        pass
    
    def afficher_etat(self):
        """Affiche l'état actuel du cache"""
        # À compléter
        pass
```

### Tests :
```python
cache = CacheLRU(3)

cache.put("A", 1)
cache.put("B", 2)
cache.put("C", 3)
print(cache.get("A"))  # 1, A devient le plus récent

cache.put("D", 4)      # B est évincé (LRU)
print(cache.get("B"))  # None (évincé)
print(cache.get("C"))  # 3
print(cache.get("D"))  # 4
print(cache.get("A"))  # 1
```

---

## Exercice 8 : Arbre de Huffman

**Niveau :** ⭐⭐⭐⭐⭐

Implémentez l'algorithme de compression de Huffman.

```python
import heapq
from collections import Counter

class NoeudHuffman:
    def __init__(self, caractere=None, frequence=0, gauche=None, droit=None):
        self.caractere = caractere
        self.frequence = frequence
        self.gauche = gauche
        self.droit = droit
    
    def __lt__(self, autre):
        return self.frequence < autre.frequence

class CompressionHuffman:
    def __init__(self):
        self.racine = None
        self.codes = {}  # caractère -> code binaire
    
    def construire_arbre(self, texte):
        """Construit l'arbre de Huffman à partir du texte"""
        # À compléter
        pass
    
    def generer_codes(self):
        """Génère les codes binaires pour chaque caractère"""
        # À compléter
        pass
    
    def _generer_codes_recursif(self, noeud, code_actuel):
        """Génère récursivement les codes"""
        # À compléter
        pass
    
    def encoder(self, texte):
        """Encode le texte en binaire"""
        # À compléter
        pass
    
    def decoder(self, code_binaire):
        """Décode le code binaire en texte"""
        # À compléter
        pass
    
    def taux_compression(self, texte_original, code_binaire):
        """Calcule le taux de compression"""
        # À compléter
        pass
```

### Test :
```python
compresseur = CompressionHuffman()
texte = "hello world"

compresseur.construire_arbre(texte)
compresseur.generer_codes()

code_binaire = compresseur.encoder(texte)
texte_decode = compresseur.decoder(code_binaire)

print(f"Texte original : {texte}")
print(f"Codes : {compresseur.codes}")
print(f"Code binaire : {code_binaire}")
print(f"Texte décodé : {texte_decode}")
print(f"Taux de compression : {compresseur.taux_compression(texte, code_binaire):.2f}%")

assert texte == texte_decode
```

---

## Exercice 9 : Système de recommandation

**Niveau :** ⭐⭐⭐⭐

Implémentez un système de recommandation basé sur les graphes.

```python
class SystemeRecommandation:
    def __init__(self):
        self.utilisateurs = set()
        self.items = set()
        self.evaluations = {}  # (utilisateur, item) -> note
        self.graphe_similarite = {}  # utilisateur -> {utilisateur: similarité}
    
    def ajouter_evaluation(self, utilisateur, item, note):
        """Ajoute une évaluation"""
        # À compléter
        pass
    
    def similarite_cosinus(self, user1, user2):
        """Calcule la similarité cosinus entre deux utilisateurs"""
        # À compléter
        pass
    
    def construire_graphe_similarite(self, seuil=0.5):
        """Construit le graphe de similarité"""
        # À compléter
        pass
    
    def utilisateurs_similaires(self, utilisateur, k=5):
        """Trouve les k utilisateurs les plus similaires"""
        # À compléter
        pass
    
    def recommander_items(self, utilisateur, nb_recommandations=5):
        """Recommande des items basé sur les utilisateurs similaires"""
        # À compléter
        pass
    
    def items_populaires(self, nb_items=10):
        """Retourne les items les plus populaires"""
        # À compléter
        pass
```

### Données de test :
```python
systeme = SystemeRecommandation()

# Ajouter des évaluations (utilisateur, film, note sur 5)
evaluations = [
    ("Alice", "Film1", 5), ("Alice", "Film2", 3), ("Alice", "Film3", 4),
    ("Bob", "Film1", 4), ("Bob", "Film2", 2), ("Bob", "Film4", 5),
    ("Charlie", "Film1", 5), ("Charlie", "Film3", 3), ("Charlie", "Film4", 4),
    ("Diana", "Film2", 4), ("Diana", "Film3", 5), ("Diana", "Film4", 3)
]

for user, item, note in evaluations:
    systeme.ajouter_evaluation(user, item, note)

systeme.construire_graphe_similarite()

# Tests
print(f"Utilisateurs similaires à Alice : {systeme.utilisateurs_similaires('Alice', 2)}")
print(f"Recommandations pour Alice : {systeme.recommander_items('Alice', 3)}")
print(f"Films populaires : {systeme.items_populaires(3)}")
```

---

## Exercice 10 : Défi - Labyrinthe et pathfinding

**Niveau :** ⭐⭐⭐⭐⭐

Implémentez différents algorithmes de recherche de chemin dans un labyrinthe.

```python
class Labyrinthe:
    def __init__(self, grille):
        self.grille = grille  # 0=libre, 1=mur
        self.hauteur = len(grille)
        self.largeur = len(grille[0])
    
    def voisins_valides(self, position):
        """Retourne les voisins valides d'une position"""
        # À compléter
        pass
    
    def bfs_chemin(self, depart, arrivee):
        """Trouve le plus court chemin avec BFS"""
        # À compléter
        pass
    
    def dfs_chemin(self, depart, arrivee):
        """Trouve un chemin avec DFS"""
        # À compléter
        pass
    
    def a_star(self, depart, arrivee):
        """Trouve le chemin optimal avec A*"""
        # À compléter
        pass
    
    def heuristique_manhattan(self, pos1, pos2):
        """Distance de Manhattan entre deux positions"""
        # À compléter
        pass
    
    def afficher_chemin(self, chemin):
        """Affiche le labyrinthe avec le chemin"""
        # À compléter
        pass
    
    def comparer_algorithmes(self, depart, arrivee):
        """Compare les performances des différents algorithmes"""
        # À compléter
        pass
```

### Test avec un labyrinthe :
```python
# 0 = libre, 1 = mur
grille = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0]
]

labyrinthe = Labyrinthe(grille)
depart = (0, 0)
arrivee = (5, 6)

# Comparer les algorithmes
labyrinthe.comparer_algorithmes(depart, arrivee)
```

---

## Barème et conseils

### Barème indicatif :
- **Exercices 1-3** : Niveau première/début terminale (⭐⭐)
- **Exercices 4-6** : Niveau terminale standard (⭐⭐⭐)
- **Exercices 7-8** : Niveau terminale avancé (⭐⭐⭐⭐)
- **Exercices 9-10** : Niveau projet/défi (⭐⭐⭐⭐⭐)

### Conseils de résolution :

1. **Commencez simple** : Implémentez d'abord les fonctionnalités de base
2. **Testez régulièrement** : Vérifiez chaque méthode avec des cas simples
3. **Optimisez ensuite** : Une fois que ça marche, améliorez les performances
4. **Documentez** : Ajoutez des commentaires et des docstrings
5. **Gérez les erreurs** : Pensez aux cas limites et aux erreurs possibles

### Ressources utiles :
- Documentation Python : `collections`, `heapq`, `itertools`
- Complexité algorithmique : analysez vos solutions
- Tests unitaires : utilisez `assert` ou `unittest`
- Visualisation : dessinez vos structures pour mieux comprendre

### Extensions possibles :
- Interface graphique pour visualiser les structures
- Benchmarks de performance
- Implémentations alternatives
- Applications réelles des algorithmes