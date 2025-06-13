# Dictionnaires

## Introduction

Les **dictionnaires** sont des structures de données qui associent des **clés** à des **valeurs**. Contrairement aux listes qui utilisent des indices numériques, les dictionnaires permettent d'utiliser n'importe quel type de données immutable comme clé.

**Principe :** Un dictionnaire est une collection de paires (clé, valeur) où chaque clé est unique.

## I. Concepts fondamentaux

### 1. Définition et propriétés

**Propriétés principales :**
- Association clé-valeur
- Clés uniques (pas de doublons)
- Accès direct par clé
- Taille variable
- Non ordonné (avant Python 3.7) / Ordonné par insertion (Python 3.7+)

### 2. Types de clés autorisées

Les clés doivent être de type **immutable** :
- Nombres (int, float)
- Chaînes de caractères (str)
- Tuples (si contiennent des éléments immutables)
- Booléens

**Non autorisés :** listes, dictionnaires, ensembles

```python
# Clés valides
dictionnaire_valide = {
    1: "un",
    "nom": "Alice",
    (1, 2): "coordonnées",
    True: "vrai"
}

# Clés invalides (erreur)
# dictionnaire_invalide = {
#     [1, 2]: "liste",      # Erreur : liste non immutable
#     {"a": 1}: "dict"      # Erreur : dictionnaire non immutable
# }
```

## II. Implémentation en Python

### 1. Dictionnaires Python natifs

#### Création et manipulation de base

```python
# Création d'un dictionnaire
contacts = {
    "Alice": "06.12.34.56.78",
    "Bob": "06.87.65.43.21",
    "Charlie": "06.11.22.33.44"
}

# Accès aux valeurs
print(contacts["Alice"])  # 06.12.34.56.78
print(contacts.get("David", "Non trouvé"))  # Non trouvé

# Modification et ajout
contacts["Alice"] = "06.99.88.77.66"  # Modification
contacts["David"] = "06.55.44.33.22"   # Ajout

# Suppression
del contacts["Bob"]                    # Suppression directe
tel_charlie = contacts.pop("Charlie")  # Suppression avec récupération

# Vérification d'existence
if "Alice" in contacts:
    print("Alice est dans les contacts")
```

#### Méthodes utiles

```python
contacts = {"Alice": "06.12.34.56.78", "Bob": "06.87.65.43.21"}

# Obtenir toutes les clés
print(list(contacts.keys()))    # ['Alice', 'Bob']

# Obtenir toutes les valeurs
print(list(contacts.values()))  # ['06.12.34.56.78', '06.87.65.43.21']

# Obtenir toutes les paires (clé, valeur)
print(list(contacts.items()))   # [('Alice', '06.12.34.56.78'), ('Bob', '06.87.65.43.21')]

# Parcours du dictionnaire
for nom, telephone in contacts.items():
    print(f"{nom}: {telephone}")

# Fusion de dictionnaires
autres_contacts = {"Eve": "06.11.11.11.11", "Frank": "06.22.22.22.22"}
contacts.update(autres_contacts)

# Copie
copie_contacts = contacts.copy()
```

### 2. Implémentation d'une classe Dictionnaire

```python
class Dictionnaire:
    def __init__(self):
        self.donnees = {}
    
    def ajouter(self, cle, valeur):
        """Ajoute ou modifie une paire clé-valeur"""
        self.donnees[cle] = valeur
    
    def obtenir(self, cle, defaut=None):
        """Retourne la valeur associée à la clé"""
        return self.donnees.get(cle, defaut)
    
    def supprimer(self, cle):
        """Supprime une paire clé-valeur"""
        if cle in self.donnees:
            return self.donnees.pop(cle)
        raise KeyError(f"Clé '{cle}' non trouvée")
    
    def contient(self, cle):
        """Vérifie si une clé existe"""
        return cle in self.donnees
    
    def cles(self):
        """Retourne toutes les clés"""
        return list(self.donnees.keys())
    
    def valeurs(self):
        """Retourne toutes les valeurs"""
        return list(self.donnees.values())
    
    def items(self):
        """Retourne toutes les paires (clé, valeur)"""
        return list(self.donnees.items())
    
    def taille(self):
        """Retourne le nombre d'éléments"""
        return len(self.donnees)
    
    def est_vide(self):
        """Vérifie si le dictionnaire est vide"""
        return len(self.donnees) == 0
    
    def vider(self):
        """Vide le dictionnaire"""
        self.donnees.clear()
    
    def __str__(self):
        return str(self.donnees)
```

## III. Tables de hachage (Hash Tables)

### 1. Principe du hachage

Les dictionnaires Python sont implémentés avec des **tables de hachage** qui utilisent une **fonction de hachage** pour convertir les clés en indices.

**Fonction de hachage :**
- Prend une clé en entrée
- Retourne un entier (hash)
- Même clé → même hash
- Distribution uniforme des hashs

```python
# Exemples de hachage en Python
print(hash("Alice"))    # Exemple : -2128831035
print(hash(42))         # Exemple : 42
print(hash((1, 2)))     # Exemple : 3713081631934410656

# Le hash d'une même valeur est constant dans une session
print(hash("Alice"))    # Même résultat que précédemment
```

### 2. Gestion des collisions

Quand deux clés différentes ont le même hash, on a une **collision**. Python utilise le **chaînage ouvert** et le **sondage linéaire**.

```python
class TableHachageSimple:
    def __init__(self, taille=10):
        self.taille = taille
        self.table = [[] for _ in range(taille)]  # Liste de listes
    
    def _hash(self, cle):
        """Fonction de hachage simple"""
        return hash(cle) % self.taille
    
    def ajouter(self, cle, valeur):
        """Ajoute une paire clé-valeur"""
        index = self._hash(cle)
        bucket = self.table[index]
        
        # Vérifier si la clé existe déjà
        for i, (k, v) in enumerate(bucket):
            if k == cle:
                bucket[i] = (cle, valeur)  # Mise à jour
                return
        
        # Nouvelle clé
        bucket.append((cle, valeur))
    
    def obtenir(self, cle):
        """Obtient la valeur associée à une clé"""
        index = self._hash(cle)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == cle:
                return v
        
        raise KeyError(f"Clé '{cle}' non trouvée")
    
    def supprimer(self, cle):
        """Supprime une paire clé-valeur"""
        index = self._hash(cle)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == cle:
                return bucket.pop(i)[1]
        
        raise KeyError(f"Clé '{cle}' non trouvée")
    
    def afficher(self):
        """Affiche le contenu de la table"""
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")

# Exemple d'utilisation
table = TableHachageSimple(5)
table.ajouter("nom", "Alice")
table.ajouter("age", 25)
table.ajouter("ville", "Paris")
table.afficher()
```

## IV. Applications pratiques

### 1. Comptage d'occurrences

```python
def compter_mots(texte):
    """Compte les occurrences de chaque mot dans un texte"""
    mots = texte.lower().split()
    compteur = {}
    
    for mot in mots:
        # Nettoyer le mot (enlever la ponctuation)
        mot_propre = ''.join(c for c in mot if c.isalnum())
        if mot_propre:
            compteur[mot_propre] = compteur.get(mot_propre, 0) + 1
    
    return compteur

# Exemple
texte = "Le chat mange. Le chat dort. Le chien mange."
resultat = compter_mots(texte)
print(resultat)  # {'le': 3, 'chat': 2, 'mange': 2, 'dort': 1, 'chien': 1}

# Afficher les mots les plus fréquents
mots_tries = sorted(resultat.items(), key=lambda x: x[1], reverse=True)
print("Mots les plus fréquents:")
for mot, freq in mots_tries[:3]:
    print(f"{mot}: {freq}")
```

### 2. Cache (mémoïsation)

```python
class Cache:
    def __init__(self):
        self.cache = {}
        self.hits = 0
        self.misses = 0
    
    def fibonacci_avec_cache(self, n):
        """Calcul de Fibonacci avec mémoïsation"""
        if n in self.cache:
            self.hits += 1
            return self.cache[n]
        
        self.misses += 1
        
        if n <= 1:
            resultat = n
        else:
            resultat = (self.fibonacci_avec_cache(n-1) + 
                       self.fibonacci_avec_cache(n-2))
        
        self.cache[n] = resultat
        return resultat
    
    def statistiques(self):
        """Affiche les statistiques du cache"""
        total = self.hits + self.misses
        if total > 0:
            taux_hit = (self.hits / total) * 100
            print(f"Cache hits: {self.hits}")
            print(f"Cache misses: {self.misses}")
            print(f"Taux de réussite: {taux_hit:.1f}%")

# Utilisation
cache = Cache()
print(f"Fibonacci(30) = {cache.fibonacci_avec_cache(30)}")
cache.statistiques()
```

### 3. Index inversé (moteur de recherche simple)

```python
class IndexInverse:
    def __init__(self):
        self.index = {}  # mot -> liste des documents
        self.documents = {}  # id_doc -> contenu
    
    def ajouter_document(self, id_doc, contenu):
        """Ajoute un document à l'index"""
        self.documents[id_doc] = contenu
        mots = contenu.lower().split()
        
        for mot in mots:
            mot_propre = ''.join(c for c in mot if c.isalnum())
            if mot_propre:
                if mot_propre not in self.index:
                    self.index[mot_propre] = set()
                self.index[mot_propre].add(id_doc)
    
    def rechercher(self, requete):
        """Recherche des documents contenant les mots de la requête"""
        mots_requete = requete.lower().split()
        resultats = None
        
        for mot in mots_requete:
            mot_propre = ''.join(c for c in mot if c.isalnum())
            if mot_propre in self.index:
                docs_mot = self.index[mot_propre]
                if resultats is None:
                    resultats = docs_mot.copy()
                else:
                    resultats = resultats.intersection(docs_mot)
            else:
                return set()  # Mot non trouvé
        
        return resultats if resultats else set()
    
    def afficher_resultats(self, ids_docs):
        """Affiche le contenu des documents trouvés"""
        for id_doc in ids_docs:
            print(f"Document {id_doc}: {self.documents[id_doc]}")

# Exemple d'utilisation
index = IndexInverse()
index.ajouter_document(1, "Le chat mange des croquettes")
index.ajouter_document(2, "Le chien mange des os")
index.ajouter_document(3, "Le chat dort sur le canapé")
index.ajouter_document(4, "Le chien court dans le jardin")

# Recherche
resultats = index.rechercher("chat mange")
print(f"Documents trouvés: {resultats}")
index.afficher_resultats(resultats)
```

## V. Complexité et performance

### 1. Complexités temporelles

| Opération | Complexité moyenne | Complexité pire cas |
|-----------|-------------------|--------------------|
| Accès (get) | O(1) | O(n) |
| Insertion | O(1) | O(n) |
| Suppression | O(1) | O(n) |
| Recherche de clé | O(1) | O(n) |

### 2. Facteur de charge

Le **facteur de charge** = nombre d'éléments / taille de la table

- Facteur faible (< 0.7) : peu de collisions, accès rapide
- Facteur élevé (> 0.8) : beaucoup de collisions, performance dégradée

Python redimensionne automatiquement les dictionnaires pour maintenir un bon facteur de charge.

### 3. Comparaison avec d'autres structures

```python
import time

# Comparaison liste vs dictionnaire pour la recherche
def comparer_recherche(taille):
    # Création des structures
    liste = list(range(taille))
    dictionnaire = {i: i for i in range(taille)}
    
    element_recherche = taille - 1  # Pire cas pour la liste
    
    # Recherche dans la liste
    start = time.time()
    resultat_liste = element_recherche in liste
    temps_liste = time.time() - start
    
    # Recherche dans le dictionnaire
    start = time.time()
    resultat_dict = element_recherche in dictionnaire
    temps_dict = time.time() - start
    
    print(f"Taille: {taille}")
    print(f"Liste: {temps_liste:.6f}s")
    print(f"Dictionnaire: {temps_dict:.6f}s")
    print(f"Ratio: {temps_liste/temps_dict:.1f}x plus rapide")
    print()

# Tests
for taille in [1000, 10000, 100000]:
    comparer_recherche(taille)
```

## VI. Exercices d'application

### Exercice 1 : Gestionnaire de notes

```python
class GestionnaireNotes:
    def __init__(self):
        self.notes = {}  # {nom_etudiant: [note1, note2, ...]}
    
    def ajouter_note(self, etudiant, note):
        """Ajoute une note pour un étudiant"""
        if etudiant not in self.notes:
            self.notes[etudiant] = []
        self.notes[etudiant].append(note)
    
    def moyenne_etudiant(self, etudiant):
        """Calcule la moyenne d'un étudiant"""
        if etudiant in self.notes and self.notes[etudiant]:
            return sum(self.notes[etudiant]) / len(self.notes[etudiant])
        return 0
    
    def moyenne_classe(self):
        """Calcule la moyenne de la classe"""
        toutes_notes = []
        for notes_etudiant in self.notes.values():
            toutes_notes.extend(notes_etudiant)
        
        if toutes_notes:
            return sum(toutes_notes) / len(toutes_notes)
        return 0
    
    def classement(self):
        """Retourne le classement des étudiants"""
        moyennes = [(etudiant, self.moyenne_etudiant(etudiant)) 
                   for etudiant in self.notes]
        return sorted(moyennes, key=lambda x: x[1], reverse=True)
```

### Exercice 2 : Analyseur de logs

```python
class AnalyseurLogs:
    def __init__(self):
        self.stats = {
            'ips': {},           # IP -> nombre de requêtes
            'pages': {},         # page -> nombre d'accès
            'codes_status': {},  # code -> nombre d'occurrences
            'heures': {}         # heure -> nombre de requêtes
        }
    
    def analyser_ligne(self, ligne_log):
        """Analyse une ligne de log Apache/Nginx"""
        # Format simplifié: IP - - [timestamp] "GET /page HTTP/1.1" status size
        parties = ligne_log.split()
        if len(parties) >= 7:
            ip = parties[0]
            timestamp = parties[3][1:]  # Enlever le '['
            page = parties[6]
            status = parties[8]
            
            # Extraire l'heure du timestamp
            heure = timestamp.split(':')[1] if ':' in timestamp else '00'
            
            # Mettre à jour les statistiques
            self.stats['ips'][ip] = self.stats['ips'].get(ip, 0) + 1
            self.stats['pages'][page] = self.stats['pages'].get(page, 0) + 1
            self.stats['codes_status'][status] = self.stats['codes_status'].get(status, 0) + 1
            self.stats['heures'][heure] = self.stats['heures'].get(heure, 0) + 1
    
    def top_ips(self, n=5):
        """Retourne les N IPs les plus actives"""
        return sorted(self.stats['ips'].items(), 
                     key=lambda x: x[1], reverse=True)[:n]
    
    def pages_populaires(self, n=5):
        """Retourne les N pages les plus visitées"""
        return sorted(self.stats['pages'].items(), 
                     key=lambda x: x[1], reverse=True)[:n]
```

## Conclusion

Les dictionnaires sont des structures de données extrêmement puissantes et efficaces :

**Avantages :**
- Accès très rapide (O(1) en moyenne)
- Flexibilité des clés
- Syntaxe simple et intuitive
- Nombreuses applications pratiques

**Inconvénients :**
- Consommation mémoire plus importante que les listes
- Ordre non garanti (avant Python 3.7)
- Clés doivent être immutables

Les dictionnaires sont essentiels pour de nombreux algorithmes et applications, notamment les caches, les index, les compteurs et les mappings en général.