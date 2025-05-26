# Travaux Pratiques : Algorithme des K Plus Proches Voisins (KNN)

## Objectif

L'objectif de ce TP est de mettre en pratique l'algorithme des K Plus Proches Voisins (KNN) sur un petit ensemble de données.

## Exercice 1 : Douceur d'un fruit

### Contexte

Imaginons que nous ayons des données sur des fruits, caractérisés par leur **douceur** (sur une échelle de 1 à 10) et leur **acidité** (sur une échelle de 1 à 10). Nous voulons prédire si un nouveau fruit est une "Pomme" ou une "Orange".

Nos données d'entraînement sont :

| Fruit   | Douceur | Acidité | Type   |
|---------|---------|---------|--------|
| Fruit 1 | 7       | 3       | Pomme  |
| Fruit 2 | 8       | 2       | Pomme  |
| Fruit 3 | 3       | 7       | Orange |
| Fruit 4 | 4       | 8       | Orange |
| Fruit 5 | 6       | 4       | Pomme  |
| Fruit 6 | 2       | 6       | Orange |

Nouveau fruit à classifier : **Fruit X (Douceur = 5, Acidité = 5)**

!!! fox_exercice "À réaliser"

    1.  **Représenter les données** :
        Créer une liste de dictionnaires pour stocker les données d'entraînement.

    2.  **Calculer la distance euclidienne** :
        Écrire une fonction `distance_euclidienne(point1, point2)` qui prend deux points (chacun étant un tuple ou une liste de coordonnées, par exemple `(douceur, acidite)` et retourne leur distance euclidienne).
        Rappel : `d = √((x2-x1)² + (y2-y1)²) `

    3.  **Trouver les K voisins** :
        Écrire une fonction `trouver_voisins(donnees_entrainement, point_test, k)` qui :
        *   Calcule la distance entre `point_test` et chaque point dans `donnees_entrainement`.
        *   Stocke ces distances avec les types de fruits correspondants.
        *   Trie les voisins par distance croissante.
        *   Retourne les `k` premiers voisins (les plus proches).

    4.  **Prédire la classe** :
        Écrire une fonction `predire_classe(voisins)` qui prend la liste des `k` voisins et retourne la classe majoritaire parmi eux.

    5.  **Mettre tout ensemble** :
        Utiliser les fonctions précédentes pour prédire la classe du **Fruit X** avec K=3.

## Exercice 2 : Classification de fleurs Iris (simplifié)

### Contexte

Nous allons appliquer l'algorithme KNN à un ensemble de données simplifié de fleurs Iris, caractérisées par la longueur de leurs sépales et de leurs pétales. Nous voulons distinguer deux types de fleurs : Setosa et Versicolor.

Nos données d'entraînement sont :

| Fleur      | Longueur Sépale | Longueur Pétale | Type       |
|------------|-----------------|-----------------|------------|
| Fleur A    | 5.1             | 1.4             | Setosa     |
| Fleur B    | 4.9             | 1.4             | Setosa     |
| Fleur C    | 6.0             | 5.1             | Versicolor |
| Fleur D    | 5.5             | 4.0             | Versicolor |
| Fleur E    | 5.2             | 1.5             | Setosa     |
| Fleur F    | 6.3             | 4.8             | Versicolor |

Nouvelle fleur à classifier : **Fleur Y (Longueur Sépale = 5.8, Longueur Pétale = 3.5)**

!!! fox_exercice "À réaliser"

    1.  **Représenter les données** :
        Créer une liste de dictionnaires pour stocker les données d'entraînement, incluant les mesures et le type de fleur.

    2.  **Calculer la distance euclidienne** :
        Écrire la fonction `distance_euclidienne` de l'Exercice 1 pour calculer la distance entre deux points (ici, `(longueur_sepale, longueur_petale)`).

    3.  **Trouver les K voisins** :
        Écrire la fonction `trouver_voisins` pour trouver les K voisins les plus proches de la **Fleur Y** dans les données d'entraînement.

    4.  **Prédire la classe** :
        Écrire la fonction `predire_classe` pour déterminer la classe majoritaire parmi les K voisins.

    5.  **Mettre tout ensemble** :
        Utiliser les fonctions précédentes pour prédire la classe de la **Fleur Y** avec K=5.

## Exercice 3 : Détection de spam (conceptuel)

### Contexte

Imaginons un système simplifié de détection de spam basé sur KNN. Nous caractérisons les emails par deux mesures : le **nombre de mots clés suspects** (comme "gratuit", "offre", "gagner") et la **longueur de l'email** (en nombre de caractères, normalisée sur une échelle de 1 à 10).

Nos données d'entraînement sont :

| Email     | Mots clés suspects | Longueur Email | Type     |
|-----------|--------------------|----------------|----------|
| Email 1   | 8                  | 9              | Spam     |
| Email 2   | 2                  | 3              | Non-Spam |
| Email 3   | 7                  | 8              | Spam     |
| Email 4   | 1                  | 2              | Non-Spam |
| Email 5   | 9                  | 7              | Spam     |
| Email 6   | 3                  | 4              | Non-Spam |

Nouvel email à classifier : **Email Z (Mots clés suspects = 6, Longueur Email = 6)**

!!! fox_exercice "À réaliser"

    1.  **Représenter les données** :
        Créer une liste de dictionnaires pour stocker les données d'entraînement, incluant les mesures et le type d'email.

    2.  **Calculer la distance euclidienne** :
        Écrire une fonction `distance_euclidienne` pour calculer la distance entre deux points (ici, `(mots_cles_suspects, longueur_email)`).

    3.  **Trouver les K voisins** :
        Écrire une fonction `trouver_voisins` pour trouver les K voisins les plus proches de l'**Email Z** dans les données d'entraînement.

    4.  **Prédire la classe** :
        Écrire une fonction `predire_classe` pour déterminer la classe majoritaire parmi les K voisins.

    5.  **Mettre tout ensemble** :
        Utiliser les fonctions précédentes pour prédire la classe de l'**Email Z** avec K=3.
