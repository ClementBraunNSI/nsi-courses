# Optimisation de problèmes : Algorithmes Gloutons

## Définitions et Concepts

Les algorithmes gloutons répondent au problème d'optimisation en cherchant à trouver la meilleure solution à un problème en utilisant un minimum de ressources.

### Méthodes de recherche de solutions optimales :

- **Bruteforce** : On cherche toutes les solutions possibles, ce qui requiert beaucoup de temps.
- **Algorithmes Gloutons** : On cherche à obtenir la meilleure solution à chaque étape du programme, c'est-à-dire des meilleures solutions locales.

### Caractéristiques principales
- Facilité de mise en place
- Choix optimal à chaque étape
- Décision irréversible
- Objectif : solution satisfaisante rapidement

## Le problème du rendu de monnaie

### Principe

Le problème du rendu de monnaie consiste à rendre une certaine somme en limitant le nombre de pièces (ou billets) à rendre.

### Système monétaire de référence

| 1    | 2    | 5    | 10   | 20   | 50   | 100  | 200  | 500  |
| ---- | ---- | ---- | ---- | ---- | ---- | :--: | ---- | ---- |

### Exemple : Rendre 42€

|     Étapes     | Liste de monnaies rendues | Somme restante à vendre |
| :------------: | :-----------------------: | :---------------------: |
| Initialisation |    monnaie =  [      ]    |  Monnaie_restante = 42  |
|    Étape 1     |      monnaie = [20]       |  Monnaie_restante = 22  |
|    Étape 2     |    monnaie = [20, 20]     |  Monnaie_restante = 2   |
|    Étape 3     |   Monnaie = [20, 20, 2]   |  Monnaie_restante = 0   |

### Exercices de réflexion

1. Système 1 = {1,2,5,10,20}, monnaie à rendre = 84
2. Système 2 = {1,3,6,12,24,30}, monnaie à rendre = 53
3. Ajouter une pièce de 3 euros dans le Système 1. Que peut-on déduire ?

### Système canonique

On appelle **système canonique**, un système dans lequel un algorithme glouton donne la solution globalement optimale.

## Le problème du sac à dos

### Définition

Le problème du sac à dos consiste à trouver la combinaison optimale d'objets à placer dans un sac à dos, en maximisant la valeur totale des objets tout en respectant la capacité maximale du sac.

### Stratégies de remplissage

Il existe différentes manières de remplir ce sac à dos : 
- Favoriser le poids : mettre le plus d'éléments de plus petit poids
- Favoriser la valeur : mettre le plus d'éléments de grande valeur
- Prendre le plus d'objets ayant les meilleurs rapports valeur / masse

### Pseudo-code de l'algorithme du sac à dos

```
Algorithme Sac_A_Dos(capacite, objets):
    # Trier les objets selon le critère choisi
    Trier objets par critère de sélection en ordre décroissant

    # Initialisation des variables
    sac = liste vide
    poids_total = 0
    valeur_totale = 0

    # Parcourir chaque objet trié
    Pour chaque objet dans objets:
        # Vérifier si l'objet peut être ajouté au sac
        Si (poids_total + poids_de_l_objet) <= capacite_maximale:
            # Ajouter l'objet au sac
            Ajouter objet à sac
            Mettre à jour poids_total
            Mettre à jour valeur_totale
        
        # Arrêter si le sac est plein
        Si poids_total == capacite_maximale:
            Arrêter

    # Retourner la solution
    Retourner sac, valeur_totale
```

### Exemples de problèmes de sac à dos

1. Sac à dos de 30kg :

| Objet  | 1    | 2    | 3    | 4    |
| ------ | ---- | ---- | ---- | ---- |
| Masse  | 5    | 13   | 6    | 10   |
| Valeur | 7    | 15   | 14   | 5    |

2. Sac à dos de 14kg :

| Objet  | 1    | 2    | 3    | 4    |
| ------ | ---- | ---- | ---- | ---- |
| Masse  | 4    | 11   | 5    | 9    |
| Valeur | 7    | 15   | 10   | 9    |

## Travail Pratique : Implémentation des problèmes

### Exercice 1 : Le problème du rendu de monnaie

Un distributeur automatique de snacks doit rendre la monnaie aux clients. 

**Objectifs** :
- Utiliser le moins de pièces et billets possible
- Privilégier les valeurs les plus élevées
- Disposer d'un nombre illimité de chaque type de pièce

### Exercice 2 : Le problème du sac à dos

Réaliser trois fonctions de résolution :
- `sac_a_dos_1` : Privilégier la masse des objets
  - Objets : `[(2, 5), (3, 8), (4, 10), (5, 7), (6, 3), (7, 6)]`

- `sac_a_dos_2` : Privilégier la valeur des objets
  - Objets : `[(2, 4), (3, 6), (4, 8), (5, 2), (6, 7), (7, 9)]`

- `sac_a_dos_3` : Privilégier le rapport valeur/masse
  - Objets : `[(3, 9), (5, 3), (6, 5), (7, 4), (8, 7), (9, 2)]`

### Exercice 3 : La planification d'activités

**Problématique** :
- Sélectionner un ensemble d'activités sans chevauchement
- Maximiser le nombre total d'activités
- Utiliser une stratégie gloutonne

**Méthode** :
- Trier les activités par ordre croissant d'horaire de fin
- Sélectionner les activités compatibles