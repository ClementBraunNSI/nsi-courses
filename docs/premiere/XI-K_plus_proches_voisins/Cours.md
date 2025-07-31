# 📚 Fiche de Cours : Algorithme des K Plus Proches Voisins (KNN)

## 📖 Définition

### 1. Qu'est-ce que l'algorithme des K Plus Proches Voisins (KNN) ?

L'algorithme des K Plus Proches Voisins (K-Nearest Neighbors ou KNN) est une méthode d'**apprentissage supervisé** simple et intuitive, utilisée principalement pour des problèmes de **classification** et de **régression**.

- **Apprentissage supervisé** : Cela signifie que l'algorithme apprend à partir d'un ensemble de données où les "bonnes réponses" (étiquettes ou valeurs) sont déjà connues.
- **Classification** : Prédire à quelle catégorie appartient un nouvel élément (par exemple, si un email est un spam ou non).
- **Régression** : Prédire une valeur continue pour un nouvel élément (par exemple, estimer le prix d'une maison).

L'idée centrale de KNN est que des choses similaires existent à proximité les unes des autres. Autrement dit, un nouvel élément sera probablement similaire à ses voisins les plus proches dans l'ensemble de données d'entraînement.

### 2. Comment fonctionne KNN ?

L'algorithme KNN fonctionne en plusieurs étapes :

1. **Choisir le nombre K** : On définit K, le nombre de voisins les plus proches à considérer. C'est un paramètre important à régler.
2. **Calculer les distances** : Pour un nouvel élément que l'on souhaite classifier (ou pour lequel on veut prédire une valeur), on calcule la distance entre cet élément et tous les autres éléments de l'ensemble de données d'entraînement. La mesure de distance la plus courante est la **distance euclidienne**.
3. **Identifier les K voisins** : On sélectionne les K éléments de l'ensemble d'entraînement qui sont les plus proches du nouvel élément (ceux ayant les plus petites distances).
4. **Prendre une décision** :
   - **Pour la classification** : On regarde la catégorie majoritaire parmi les K voisins. Le nouvel élément est assigné à cette catégorie.
   - **Pour la régression** : On calcule la moyenne (ou parfois la médiane) des valeurs des K voisins. Cette moyenne devient la valeur prédite pour le nouvel élément.

#### Exemple simple de classification :

Imaginons que nous ayons des points de données de deux catégories (A et B) et un nouveau point inconnu (X). Si nous choisissons K=3 :

1. On calcule la distance entre X et tous les autres points.
2. On trouve les 3 points les plus proches de X.
3. Si 2 de ces 3 voisins sont de la catégorie A et 1 est de la catégorie B, alors X sera classifié comme A.

### 3. La mesure de distance

La **distance euclidienne** est la plus utilisée. Pour deux points P(p1, p2, ..., pn) et Q(q1, q2, ..., qn) dans un espace à n dimensions, la distance euclidienne est :

```
d(P, Q) = √((p1-q1)² + (p2-q2)² + ... + (pn-qn)²)
```

D'autres mesures de distance existent, comme la distance de Manhattan ou la distance de Minkowski.

**Important : La normalisation des données**

Si les différentes caractéristiques (dimensions) de vos données n'ont pas la même échelle (par exemple, une caractéristique varie de 0 à 1 et une autre de 0 à 1000), celles avec des valeurs plus grandes domineront le calcul de la distance. Il est donc crucial de **normaliser** ou **standardiser** vos données avant d'appliquer KNN.

### 4. Choisir la valeur de K

Le choix de K est crucial :

- **K petit** (par exemple, K=1) : L'algorithme est très sensible au bruit et aux points aberrants. Le modèle peut être trop spécifique aux données d'entraînement (surapprentissage ou overfitting).
- **K grand** : L'algorithme est plus robuste au bruit, mais peut rendre les frontières de décision moins distinctes. Si K est trop grand (par exemple, K = nombre total d'échantillons), tous les nouveaux points seront classifiés dans la catégorie majoritaire de l'ensemble d'entraînement.

Il n'y a pas de règle d'or pour choisir K. On utilise souvent des techniques comme la validation croisée pour trouver une valeur optimale de K pour un problème donné. Une pratique courante est de choisir K comme un nombre impair pour éviter les égalités en classification binaire.

### 5. Avantages de KNN

- **Simple à comprendre et à implémenter**.
- **Non paramétrique** : Il ne fait aucune supposition sur la distribution sous-jacente des données.
- **Polyvalent** : Peut être utilisé pour la classification et la régression.
- **S'adapte facilement** : De nouvelles données peuvent être ajoutées sans avoir à ré-entraîner le modèle (on parle d'apprentissage "paresseux" ou "lazy learning" car la majorité du calcul se fait au moment de la prédiction).

### 6. Inconvénients de KNN

- **Coûteux en calcul** : Pour chaque nouvelle prédiction, il faut calculer la distance à tous les points de l'ensemble d'entraînement. Cela peut être très lent pour de grands ensembles de données.
- **Sensible aux dimensions non pertinentes** (le "fléau de la dimensionnalité") : Si l'ensemble de données a beaucoup de caractéristiques (dimensions) et que la plupart ne sont pas informatives, la performance de KNN peut se dégrader.
- **Nécessite une normalisation des données** : Comme mentionné, les échelles des caractéristiques influencent fortement les distances.
- **Nécessite beaucoup de mémoire** : Il faut stocker tout l'ensemble de données d'entraînement.
- **Le choix de K est critique**.

### 7. Quand utiliser KNN ?

KNN peut être un bon point de départ pour des problèmes de classification ou de régression, surtout si :

- L'ensemble de données n'est pas excessivement grand.
- Les relations entre les caractéristiques et la cible sont complexes et non linéaires.
- Vous avez besoin d'une méthode simple et interprétable.

Il est souvent utilisé comme baseline pour comparer avec des modèles plus complexes.