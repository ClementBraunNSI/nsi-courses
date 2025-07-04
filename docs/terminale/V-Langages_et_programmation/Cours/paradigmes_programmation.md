# Paradigmes de programmation

    💻 Paradigmes de programmation
    Approches et philosophies de développement logiciel

## I. Introduction aux paradigmes

🎯 Qu'est-ce qu'un paradigme de programmation ?

Un paradigme de programmation est une approche fondamentale pour concevoir et structurer des programmes. Il définit la manière de penser et d'organiser le code, influençant la résolution de problèmes et l'architecture logicielle.

### Classification des paradigmes

**Paradigmes principaux :**
- **Impératif** : Instructions séquentielles (comment faire)
- **Déclaratif** : Description du résultat souhaité (quoi faire)
- **Orienté objet** : Modélisation par objets et classes
- **Fonctionnel** : Calculs par fonctions mathématiques
- **Logique** : Raisonnement par règles et faits

Remarque importante :

La plupart des langages modernes sont **multi-paradigmes**, permettant de combiner plusieurs approches selon les besoins du projet.

## II. Programmation impérative

🔄 Paradigme impératif

**Principe :** Le programme est une séquence d'instructions qui modifient l'état du système.

**Caractéristiques :**
- Variables mutables
- Affectations successives
- Structures de contrôle (boucles, conditions)
- Procédures et fonctions

### Programmation procédurale

# Exemple en Python - Style procédural

def calculer_moyenne(notes):
    """Calcule la moyenne d'une liste de notes"""
    total = 0
    for note in notes:
        total += note
    return total / len(notes)

def afficher_resultats(etudiants):
    """Affiche les résultats des étudiants"""
    for nom, notes in etudiants.items():
        moyenne = calculer_moyenne(notes)
        print(f"{nom}: {moyenne:.2f}")

        if moyenne >= 10:
            print("  → Admis")
        else:
            print("  → Recalé")

# Utilisation
etudiants = {
    "Alice": [15, 12, 18, 14],
    "Bob": [8, 9, 7, 11],
    "Charlie": [16, 17, 15, 18]
}

afficher_resultats(etudiants)

### Avantages et inconvénients

✅ Avantages

Proche du fonctionnement machine
Contrôle précis de l'exécution
Performance optimisable
Facilité de débogage
Apprentissage intuitif

❌ Inconvénients

Code difficile à maintenir
Réutilisabilité limitée
Gestion complexe de l'état
Effets de bord nombreux
Difficulté de parallélisation

## III. Programmation orientée objet (POO)

🏗️ Paradigme orienté objet

**Principe :** Modélisation du monde réel par des objets qui encapsulent données et comportements.

**Concepts fondamentaux :**
- **Encapsulation** : Regroupement données/méthodes
- **Héritage** : Réutilisation et spécialisation
- **Polymorphisme** : Même interface, comportements différents
- **Abstraction** : Simplification de la complexité

### Exemple complet en Python

# Classe de base
class Vehicule:
    def __init__(self, marque, modele, annee):
        self._marque = marque      # Attribut protégé
        self._modele = modele
        self._annee = annee
        self._vitesse = 0

    @property
    def marque(self):
        return self._marque

    def accelerer(self, increment):
        self._vitesse += increment
        print(f"Vitesse: {self._vitesse} km/h")

    def freiner(self, decrement):
        self._vitesse = max(0, self._vitesse - decrement)
        print(f"Vitesse: {self._vitesse} km/h")

    def __str__(self):
        return f"{self._marque} {self._modele} ({self._annee})"

# Héritage
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, nb_portes):
        super().__init__(marque, modele, annee)
        self._nb_portes = nb_portes

    def klaxonner(self):
        print("Bip bip!")

    def __str__(self):
        return f"{super().__str__()} - {self._nb_portes} portes"

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, cylindree):
        super().__init__(marque, modele, annee)
        self._cylindree = cylindree

    def faire_wheeling(self):
        if self._vitesse > 30:
            print("Wheeling!")
        else:
            print("Trop lent pour un wheeling")

    def __str__(self):
        return f"{super().__str__()} - {self._cylindree}cc"

# Polymorphisme
def presenter_vehicule(vehicule):
    print(f"Véhicule: {vehicule}")
    vehicule.accelerer(50)

    # Comportement spécifique selon le type
    if isinstance(vehicule, Voiture):
        vehicule.klaxonner()
    elif isinstance(vehicule, Moto):
        vehicule.faire_wheeling()

# Utilisation
voiture = Voiture("Toyota", "Corolla", 2020, 4)
moto = Moto("Honda", "CBR", 2021, 600)

for vehicule in [voiture, moto]:
    presenter_vehicule(vehicule)
    print()

### Patterns de conception (Design Patterns)

#### 1. Singleton

class DatabaseConnection:
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self):
        if self._connection is None:
            self._connection = "Connected to database"
            print("Nouvelle connexion créée")
        return self._connection

    def disconnect(self):
        if self._connection:
            self._connection = None
            print("Connexion fermée")

# Test
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True - même instance

#### 2. Factory

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def faire_bruit(self):
        pass

class Chien(Animal):
    def faire_bruit(self):
        return "Woof!"

class Chat(Animal):
    def faire_bruit(self):
        return "Miaou!"

class Vache(Animal):
    def faire_bruit(self):
        return "Meuh!"

class AnimalFactory:
    @staticmethod
    def creer_animal(type_animal):
        animals = {
            "chien": Chien,
            "chat": Chat,
            "vache": Vache
        }

        animal_class = animals.get(type_animal.lower())
        if animal_class:
            return animal_class()
        else:
            raise ValueError(f"Animal '{type_animal}' non supporté")

# Utilisation
for animal_type in ["chien", "chat", "vache"]:
    animal = AnimalFactory.creer_animal(animal_type)
    print(f"{animal_type}: {animal.faire_bruit()}")

#### 3. Observer

class Observable:
    def __init__(self):
        self._observers = []

    def ajouter_observer(self, observer):
        self._observers.append(observer)

    def retirer_observer(self, observer):
        self._observers.remove(observer)

    def notifier_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)

class Thermometre(Observable):
    def __init__(self):
        super().__init__()
        self._temperature = 20

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notifier_observers(value)

class AffichageTemperature:
    def __init__(self, nom):
        self.nom = nom

    def update(self, observable, temperature):
        print(f"{self.nom}: Température = {temperature}°C")

class AlerteTemperature:
    def update(self, observable, temperature):
        if temperature > 30:
            print("🔥 ALERTE: Température élevée!")
        elif temperature

## IV. Programmation fonctionnelle

🔢 Paradigme fonctionnel

**Principe :** Les programmes sont des compositions de fonctions mathématiques pures, sans effets de bord.

**Caractéristiques :**
- Fonctions pures (même entrée → même sortie)
- Immutabilité des données
- Fonctions de première classe
- Récursion privilégiée
- Composition de fonctions

### Concepts fondamentaux

#### 1. Fonctions pures

# Fonction impure (avec effet de bord)
counter = 0

def increment_impure():
    global counter
    counter += 1
    return counter

# Fonction pure
def increment_pure(value):
    return value + 1

# Fonction pure pour calculer la factorielle
def factorielle(n):
    if n

#### 2. Fonctions d'ordre supérieur

# map() - Applique une fonction à chaque élément
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x**2, nombres))
print(f"Carrés: {carres}")  # [1, 4, 9, 16, 25]

# filter() - Filtre selon un prédicat
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(f"Pairs: {pairs}")  # [2, 4]

# reduce() - Réduit à une seule valeur
from functools import reduce
somme = reduce(lambda x, y: x + y, nombres)
print(f"Somme: {somme}")  # 15

# Composition de fonctions
def composer(f, g):
    return lambda x: f(g(x))

def doubler(x):
    return x * 2

def ajouter_un(x):
    return x + 1

# Compose: doubler puis ajouter un
composee = composer(ajouter_un, doubler)
print(composee(5))  # (5*2)+1 = 11

#### 3. Immutabilité

# Structures immutables avec namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def deplacer_point(point, dx, dy):
    """Retourne un nouveau point déplacé"""
    return Point(point.x + dx, point.y + dy)

def distance_origine(point):
    """Calcule la distance à l'origine"""
    return (point.x**2 + point.y**2)**0.5

# Utilisation
p1 = Point(3, 4)
p2 = deplacer_point(p1, 1, 1)

print(f"P1: {p1}, distance: {distance_origine(p1):.2f}")
print(f"P2: {p2}, distance: {distance_origine(p2):.2f}")

# Liste immutable avec tuple
def ajouter_element(liste, element):
    """Retourne une nouvelle liste avec l'élément ajouté"""
    return liste + (element,)

liste1 = (1, 2, 3)
liste2 = ajouter_element(liste1, 4)
print(f"Liste1: {liste1}")  # (1, 2, 3)
print(f"Liste2: {liste2}")  # (1, 2, 3, 4)

#### 4. Curryfication

# Curryfication manuelle
def multiplier_curry(x):
    def multiplier_par_x(y):
        return x * y
    return multiplier_par_x

# Utilisation
doubler = multiplier_curry(2)
tripler = multiplier_curry(3)

print(doubler(5))   # 10
print(tripler(4))   # 12

# Curryfication avec functools.partial
from functools import partial

def puissance(base, exposant):
    return base ** exposant

# Création de fonctions spécialisées
carre = partial(puissance, exposant=2)
cube = partial(puissance, exposant=3)

print(carre(5))   # 25
print(cube(3))    # 27

### Exemple pratique : Traitement de données

# Données d'exemple
etudiants = [
    {"nom": "Alice", "age": 20, "notes": [15, 12, 18, 14]},
    {"nom": "Bob", "age": 19, "notes": [8, 9, 7, 11]},
    {"nom": "Charlie", "age": 21, "notes": [16, 17, 15, 18]},
    {"nom": "Diana", "age": 20, "notes": [13, 14, 12, 15]}
]

# Style fonctionnel
def calculer_moyenne(notes):
    return sum(notes) / len(notes)

def ajouter_moyenne(etudiant):
    return {**etudiant, "moyenne": calculer_moyenne(etudiant["notes"])}

def est_admis(etudiant):
    return etudiant["moyenne"] >= 12

def formater_resultat(etudiant):
    statut = "Admis" if etudiant["moyenne"] >= 12 else "Recalé"
    return f"{etudiant['nom']} ({etudiant['age']} ans): {etudiant['moyenne']:.1f} - {statut}"

# Pipeline de traitement fonctionnel
resultats = list(map(
    formater_resultat,
    filter(
        est_admis,
        map(ajouter_moyenne, etudiants)
    )
))

print("Étudiants admis:")
for resultat in resultats:
    print(f"  {resultat}")

# Version avec compréhension de liste (plus pythonique)
resultats_pythonic = [
    formater_resultat(etudiant)
    for etudiant in [ajouter_moyenne(e) for e in etudiants]
    if est_admis(etudiant)
]

## V. Programmation logique

🧠 Paradigme logique

**Principe :** Programmation basée sur la logique formelle, utilisant des faits, règles et requêtes.

**Caractéristiques :**
- Déclaration de faits et règles
- Inférence automatique
- Backtracking
- Unification

### Exemple conceptuel en Python

# Simulation simple d'un système logique
class BaseFaits:
    def __init__(self):
        self.faits = set()
        self.regles = []

    def ajouter_fait(self, fait):
        self.faits.add(fait)

    def ajouter_regle(self, condition, conclusion):
        self.regles.append((condition, conclusion))

    def inferer(self):
        """Applique les règles pour inférer de nouveaux faits"""
        nouveaux_faits = True
        while nouveaux_faits:
            nouveaux_faits = False
            for condition, conclusion in self.regles:
                if condition(self.faits) and conclusion not in self.faits:
                    self.faits.add(conclusion)
                    nouveaux_faits = True
                    print(f"Inféré: {conclusion}")

    def interroger(self, fait):
        return fait in self.faits

# Exemple: Relations familiales
base = BaseFaits()

# Faits de base
base.ajouter_fait("parent(jean, marie)")
base.ajouter_fait("parent(marie, paul)")
base.ajouter_fait("parent(marie, sophie)")
base.ajouter_fait("parent(paul, lucas)")

# Règles
def regle_grand_parent(faits):
    # Si X est parent de Y et Y est parent de Z, alors X est grand-parent de Z
    for fait1 in faits:
        if fait1.startswith("parent("):
            x, y = fait1[7:-1].split(", ")
            for fait2 in faits:
                if fait2.startswith(f"parent({y},"):
                    z = fait2.split(", ")[1][:-1]
                    return True
    return False

# Application des règles (simplifiée)
print("Faits initiaux:")
for fait in sorted(base.faits):
    print(f"  {fait}")

# Dans un vrai système Prolog, l'inférence serait automatique
print("\nConclusions possibles:")
print("  jean est grand-parent de paul")
print("  jean est grand-parent de sophie")
print("  marie est grand-parent de lucas")

## VI. Programmation concurrente et parallèle

⚡ Paradigme concurrent

**Principe :** Exécution simultanée de plusieurs tâches pour améliorer les performances et la réactivité.

**Concepts :**
- **Concurrence** : Gestion de plusieurs tâches simultanément
- **Parallélisme** : Exécution réellement simultanée
- **Synchronisation** : Coordination entre tâches
- **Communication** : Échange de données

### Threading en Python

import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor

# Exemple 1: Thread simple
def tache_longue(nom, duree):
    print(f"Début de {nom}")
    time.sleep(duree)
    print(f"Fin de {nom}")
    return f"Résultat de {nom}"

# Exécution séquentielle
print("=== Exécution séquentielle ===")
start = time.time()
tache_longue("Tâche 1", 2)
tache_longue("Tâche 2", 2)
print(f"Temps total: {time.time() - start:.1f}s\n")

# Exécution avec threads
print("=== Exécution avec threads ===")
start = time.time()

thread1 = threading.Thread(target=tache_longue, args=("Tâche 1", 2))
thread2 = threading.Thread(target=tache_longue, args=("Tâche 2", 2))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Temps total: {time.time() - start:.1f}s\n")

### Synchronisation avec verrous

import threading
import time

# Problème de concurrence sans synchronisation
compteur = 0
verrou = threading.Lock()

def incrementer_sans_verrou():
    global compteur
    for _ in range(100000):
        compteur += 1

def incrementer_avec_verrou():
    global compteur
    for _ in range(100000):
        with verrou:
            compteur += 1

# Test sans synchronisation
compteur = 0
threads = []
for i in range(5):
    t = threading.Thread(target=incrementer_sans_verrou)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Sans verrou: {compteur} (attendu: 500000)")

# Test avec synchronisation
compteur = 0
threads = []
for i in range(5):
    t = threading.Thread(target=incrementer_avec_verrou)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Avec verrou: {compteur} (attendu: 500000)")

### Programmation asynchrone

import asyncio
import aiohttp
import time

# Fonction asynchrone
async def telecharger_url(session, url):
    print(f"Début téléchargement: {url}")
    async with session.get(url) as response:
        contenu = await response.text()
        print(f"Fin téléchargement: {url} ({len(contenu)} caractères)")
        return len(contenu)

async def telecharger_plusieurs_urls():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/1",
    ]

    start = time.time()

    async with aiohttp.ClientSession() as session:
        # Exécution concurrente
        taches = [telecharger_url(session, url) for url in urls]
        resultats = await asyncio.gather(*taches)

    print(f"Temps total: {time.time() - start:.1f}s")
    print(f"Tailles: {resultats}")

# Exécution
# asyncio.run(telecharger_plusieurs_urls())

## VII. Comparaison des paradigmes

    Paradigme
    Avantages
    Inconvénients
    Cas d'usage

    Impératif
    Simple, performant, contrôle précis
    Difficile à maintenir, effets de bord
    Systèmes embarqués, calcul intensif

    Orienté objet
    Modulaire, réutilisable, maintenable
    Complexité, overhead
    Applications complexes, interfaces

    Fonctionnel
    Pas d'effets de bord, parallélisable
    Courbe d'apprentissage, performance
    Traitement de données, calculs

    Logique
    Expressif, inférence automatique
    Performance, domaine spécialisé
    IA, systèmes experts

    Concurrent
    Performance, réactivité
    Complexité, bugs difficiles
    Serveurs, interfaces utilisateur

## VIII. Évolution des langages

1950s - Langages assembleur
Instructions machine, programmation de bas niveau

1960s - Langages structurés
FORTRAN, COBOL, ALGOL - Structures de contrôle

1970s - Programmation procédurale
C, Pascal - Fonctions et procédures

1980s - Orienté objet
C++, Smalltalk - Classes et objets

1990s - Langages interprétés
Python, JavaScript, Java - Portabilité

2000s - Langages fonctionnels
Haskell, Scala - Programmation fonctionnelle

2010s - Langages modernes
Rust, Go, Swift - Sécurité et performance

### Langages par paradigme

Impératif
C, Assembly, FORTRAN
Contrôle direct du matériel

Orienté objet
Java, C#, C++, Python
Modélisation par objets

Fonctionnel
Haskell, Lisp, Erlang, F#
Fonctions pures et immutabilité

Logique
Prolog, Mercury
Raisonnement et inférence

Multi-paradigme
Python, JavaScript, Scala
Flexibilité d'approche

Concurrent
Go, Erlang, Rust
Parallélisme natif

## IX. Choix du paradigme

🎯 Critères de sélection

Le choix d'un paradigme dépend de plusieurs facteurs :
- **Nature du problème** : Calcul, interface, système
- **Performance requise** : Temps réel, batch
- **Équipe de développement** : Expertise, taille
- **Maintenance** : Évolutivité, lisibilité
- **Écosystème** : Bibliothèques, outils

### Recommandations pratiques

Conseils pour le choix :

1. **Commencez simple** : Paradigme impératif/procédural
2. **Évoluez progressivement** : Ajoutez OOP si nécessaire
3. **Explorez le fonctionnel** : Pour le traitement de données
4. **Considérez la concurrence** : Pour les performances
5. **Restez pragmatique** : Mélangez les approches

## Exercices pratiques

TP 1 : Comparaison de paradigmes

1. Implémentez un système de gestion de bibliothèque en style procédural
2. Refactorisez en orienté objet
3. Créez une version fonctionnelle pour les requêtes
4. Comparez lisibilité, maintenabilité et performance

TP 2 : Patterns de conception

1. Implémentez le pattern Strategy pour différents algorithmes de tri
2. Utilisez Observer pour un système de notifications
3. Créez une Factory pour générer différents types de documents
4. Testez la flexibilité et l'extensibilité

TP 3 : Programmation concurrente

1. Créez un web scraper séquentiel
2. Parallélisez avec threading
3. Implémentez une version asynchrone
4. Mesurez et comparez les performances

---

    📝 Exercices
    🔬 TP Comparaison
    🏗️ TP Patterns