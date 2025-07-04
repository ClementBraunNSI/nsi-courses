# Sujet BAC NSI - Écosystème et Conservation des Renards (3h30)
**Nom :** _________________ **Prénom :** _________________ **Classe :** _______

**Ce sujet comporte 5 exercices indépendants. La calculatrice est autorisée.**
**Barème indicatif : Ex1: 3pts, Ex2: 4pts, Ex3: 4pts, Ex4: 4pts, Ex5: 5pts**

---

## Exercice 1 : Bases de données - Suivi des populations (3 points)

Une réserve naturelle utilise une base de données pour suivre les populations de renards. Voici le schéma relationnel :

- **Renards** (id_renard, nom, espece, sexe, age_mois, poids_kg, id_territoire)
- **Territoires** (id_territoire, nom_territoire, superficie_ha, type_habitat)
- **Observations** (id_observation, id_renard, date_obs, comportement, heure)

**1.1** Écrire une requête SQL qui affiche le nom et l'âge en mois de tous les renards de l'espèce "Renard roux" pesant plus de 5 kg.

**1.2** Écrire une requête SQL qui affiche le nom du territoire et le nombre de renards présents dans chaque territoire, triés par nombre décroissant.

**1.3** Écrire une requête SQL qui affiche le nom des renards observés en comportement de "chasse" après 18h00 le 15 janvier 2025.

---

## Exercice 2 : Structures de données - Arbre généalogique (4 points)

Pour étudier la génétique des renards, les biologistes construisent des arbres généalogiques. Chaque nœud de l'arbre représente un renard avec ses informations.

```python
class Renard:
    def __init__(self, nom, sexe, couleur_pelage):
        self.nom = nom
        self.sexe = sexe
        self.couleur_pelage = couleur_pelage
        self.parent_gauche = None  # Premier parent
        self.parent_droit = None   # Deuxième parent
        self.descendants = []      # Liste des descendants directs
```

**2.1** Écrire une fonction récursive `compter_ancetres(renard)` qui renvoie le nombre total d'ancêtres d'un renard (parents, grands-parents, etc.).

**2.2** Écrire une fonction récursive `rechercher_couleur(renard, couleur)` qui renvoie `True` si au moins un ancêtre du renard a la couleur de pelage spécifiée, `False` sinon.

**2.3** Écrire une fonction `parcours_largeur_generation(racine, generation)` qui utilise un parcours en largeur pour renvoyer la liste des noms des renards à une génération donnée (0 = racine, 1 = enfants, 2 = petits-enfants, etc.).

**2.4** Quelle est la complexité temporelle de la fonction `compter_ancetres` dans le pire des cas ? Justifier.

---

## Exercice 3 : Algorithmes sur les graphes - Territoire et déplacements (4 points)

Les biologistes modélisent les déplacements des renards entre différentes zones de leur territoire sous forme de graphe. Chaque zone est un sommet, et les arêtes représentent les chemins possibles avec leur distance en mètres.

```python
# Représentation par dictionnaire d'adjacence
territoire = {
    'Taniere': [('Ruisseau', 150), ('Clairiere', 200)],
    'Ruisseau': [('Taniere', 150), ('Foret', 100), ('Prairie', 250)],
    'Clairiere': [('Taniere', 200), ('Foret', 180), ('Colline', 300)],
    'Foret': [('Ruisseau', 100), ('Clairiere', 180), ('Prairie', 120), ('Colline', 220)],
    'Prairie': [('Ruisseau', 250), ('Foret', 120)],
    'Colline': [('Clairiere', 300), ('Foret', 220)]
}
```

**3.1** Écrire une fonction `parcours_profondeur(graphe, sommet_depart, visites=None)` qui effectue un parcours en profondeur et renvoie la liste des sommets visités dans l'ordre.

**3.2** Écrire une fonction `chemin_existe(graphe, depart, arrivee)` qui détermine s'il existe un chemin entre deux zones en utilisant un parcours en profondeur.

**3.3** Implémenter l'algorithme de Dijkstra dans une fonction `plus_court_chemin(graphe, depart, arrivee)` qui renvoie la distance minimale et le chemin correspondant entre deux zones.

**3.4** Un renard se déplace de 'Taniere' vers 'Prairie'. Calculer à la main la distance minimale en appliquant l'algorithme de Dijkstra. Détailler les étapes.

---

## Exercice 4 : Programmation dynamique - Optimisation des ressources (4 points)

Un centre de réhabilitation doit planifier l'alimentation des renards en captivité. Chaque type d'aliment a un coût et une valeur nutritionnelle. Le centre a un budget limité et veut maximiser la valeur nutritionnelle.

```python
# aliments = [(nom, cout, valeur_nutritionnelle), ...]
aliments = [
    ('Souris', 2, 8),
    ('Lapin', 5, 15),
    ('Poisson', 3, 10),
    ('Insectes', 1, 4),
    ('Fruits', 1, 3)
]
budget_max = 10
```

**4.1** Modéliser ce problème comme un problème du sac à dos. Expliquer les variables et la fonction objectif.

**4.2** Écrire une fonction récursive `sac_a_dos_recursif(aliments, budget, index=0)` qui renvoie la valeur nutritionnelle maximale possible.

**4.3** Améliorer la solution avec la mémorisation. Écrire une fonction `sac_a_dos_memo(aliments, budget)` utilisant un dictionnaire pour éviter les calculs redondants.

**4.4** Implémenter la solution par programmation dynamique ascendante dans une fonction `sac_a_dos_dp(aliments, budget)` qui renvoie également la liste des aliments sélectionnés.

**4.5** Comparer les complexités temporelles des trois approches. Laquelle est la plus efficace et pourquoi ?

---

## Exercice 5 : Algorithmique avancée - Analyse de séquences ADN (5 points)

Les généticiens analysent l'ADN des renards pour étudier leur diversité génétique. Une séquence ADN est représentée par une chaîne de caractères contenant uniquement 'A', 'T', 'G', 'C'.

**5.1 Recherche de motifs (2 points)**

Écrire une fonction `recherche_motif_kmp(sequence, motif)` qui implémente l'algorithme de Knuth-Morris-Pratt pour trouver toutes les occurrences d'un motif dans une séquence ADN.

```python
# Exemple d'utilisation
>>> sequence = "ATCGATCGAATCG"
>>> motif = "ATCG"
>>> recherche_motif_kmp(sequence, motif)
[0, 3, 9]  # Positions des occurrences
```

**5.2 Plus longue sous-séquence commune (2 points)**

Deux renards sont apparentés si leurs séquences ADN partagent une longue sous-séquence commune. Écrire une fonction `lcs_longueur(seq1, seq2)` qui calcule la longueur de la plus longue sous-séquence commune entre deux séquences.

```python
# Exemple d'utilisation
>>> seq1 = "ATCGATCG"
>>> seq2 = "AGTCGTCG"
>>> lcs_longueur(seq1, seq2)
6  # "ATCGTCG" par exemple
```

**5.3 Analyse de complexité (1 point)**

Quelle est la complexité temporelle et spatiale de votre algorithme LCS ? Proposer une optimisation pour réduire la complexité spatiale.

**5.4 Application pratique (Bonus)**

Écrire une fonction `degre_parente(seq1, seq2)` qui renvoie un pourcentage de parenté basé sur le ratio entre la longueur de la LCS et la longueur moyenne des deux séquences.

```python
# Exemple d'utilisation
>>> degre_parente("ATCGATCG", "AGTCGTCG")
75.0  # (6 / ((8+8)/2)) * 100
```

---

## Annexe : Fonctions utiles

```python
# Pour l'exercice 3 - File de priorité simple
class FilePriorite:
    def __init__(self):
        self.elements = []
    
    def est_vide(self):
        return len(self.elements) == 0
    
    def ajouter(self, element, priorite):
        self.elements.append((priorite, element))
        self.elements.sort()
    
    def retirer(self):
        return self.elements.pop(0)[1]

# Pour l'exercice 5 - Fonction de préprocessing KMP
def construire_table_echec(motif):
    """Construit la table des échecs pour l'algorithme KMP"""
    m = len(motif)
    table = [0] * m
    j = 0
    
    for i in range(1, m):
        while j > 0 and motif[i] != motif[j]:
            j = table[j - 1]
        if motif[i] == motif[j]:
            j += 1
        table[i] = j
    
    return table
```

**Fin du sujet - Bonne chance !**