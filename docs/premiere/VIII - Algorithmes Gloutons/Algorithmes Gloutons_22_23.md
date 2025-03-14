# Optimisation de problèmes : Algorithmes Gloutons

## Définitions et Concepts

Un algorithme glouton est un algorithme qui a pour principe de choisir à chaque étapes de résolution d'un problème la meilleure solution locale.

Ils peuvent répondre **au problème d'optimisation** en cherchant pour chaque itération un extremum qui **minimise ou maximise (suivant le problème) chacune des sous-étapes**.
En général, ces opérations de recherche d'extremum ne sont pas couteuses mais **l'ensemble de celles-ci n'est pas forcément la solution optimale globale**.

Cette méthode est en générale plus efficace que la méthode par **force brute**.  
La méthode **bruteforce** donnera (théoriquement) la solution optimale en testant toutes les combinaisons possibles si la machine a les ressources necessaires.

On peut illustrer cela par deux exemples simples.

!!! fox_exercice "Alpiniste"
    Prenons le cas d'un alpiniste qui gravit la chaîne de montagne *Kaisen*. Il cherche à monter par les plus grands sommets qui se trouvent à sa droite ou sa gauche.  
    Les conditions météorologiques ne sont pas les meilleures et il y a beaucoup de nuages par plateau qui l'empêchent de voir derrière chacun des pics qu'il rencontre.

!!! fox_exercice "Nombre le plus grand construit avec des chiffres"
    On dispose d'une liste de chiffres quelconques et on cherche à construire le nombre le plus grand sans trier la liste.  
    Une solution à ce problème est de trouver le chiffre le plus grand de la liste, le mettre la "colonne" la plus à gauche du nombre et le retirer de la liste.  
    On réalise cette opération jusqu'à ce que la liste soit vide.

## Le problème du rendu de monnaie

### Principe

!!! fox_exercice "Problème du rendu de monnaie"
    Le problème du rendu de monnaie consiste à rendre une certaine somme en limitant le nombre de pièces (ou billets) à rendre.  
    On a une somme qui nous est donnée et on doit rendre la monnaie.  
    On considère que (dans ce monde utopique), on dispose d'une infinité de billets/pièces de chaque coupure.

### Système monétaire de référence

||||||||||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1    | 2    | 5    | 10   | 20   | 50   | 100  | 200  | 500  |

### Exemple : Rendre 42€

|     Étapes     | Liste de monnaies rendues | Somme restante à vendre |
| :------------: | :-----------------------: | :---------------------: |
| Initialisation |    monnaie =  [      ]    |  Monnaie_restante = 42  |
|    Étape 1     |      monnaie = [20]       |  Monnaie_restante = 22  |
|    Étape 2     |    monnaie = [20, 20]     |  Monnaie_restante = 2   |
|    Étape 3     |   Monnaie = [20, 20, 2]   |  Monnaie_restante = 0   |

### Exercices de réflexion

!!! fox_exercice "Exercices rendu de monnaie"
    On souhaite rendre 49€ a un client.

    1. On dispose d'un système monaitaire tel que Système 1 = {1,2,5,10,20,50}.  
    **Quelle solution serait obtenue par l'algorithme glouton grâce au Système 1 ?  
    Est-elle optimale?  
    Si non, donner une solution optimale.**  
    <br/>
    2. On dispose d'un système monaitaire tel que Système 2 = {1,3,6,12,24,30}.  
    **Quelle solution serait obtenue par l'algorithme glouton grâce au Système 2 ?  
    Est-elle optimale?  
    Si non, donner une solution optimale.** 

### Système canonique

On appelle **système canonique**, un système qui permet à un algorithme glouton de donner la solution optimale.

### Idée de l'algorithme

L'algorithme de rendu de monnaie suit une approche gloutonne en sélectionnant à chaque étape la plus grande pièce ou billet possible ne dépassant pas le montant restant à rendre. Voici les étapes principales :

!!! fox_exercice_test "Idée de l'algorithme"
    **On initialise une liste vide pour stocker les pièces/billets à rendre triée.**  
   
    **Pour chaque valeur de pièce/billet, en commençant par la plus grande :**  

      - Tant que la valeur de la pièce/billet est inférieure ou égale au montant restant  
  
      - On ajoute cette pièce/billet à la solution  
  
      - On soustrait sa valeur du montant restant   
 
    **On continue jusqu'à ce que le montant restant soit nul et on renvoie la liste de billets / pièces à rendre.**

## Le problème du sac à dos

### Principe

!!! fox_exercice "Problème du sac à dos"
    Le problème du sac à dos consiste à remplir un sac avec une capacité maximale donnée en choisissant parmi différents objets ayant chacun une masse et une valeur.
    L'objectif est de maximiser la valeur totale des objets dans le sac tout en respectant la contrainte de capacité.
    On considère que chaque objet est unique et ne peut être fractionné.

### Exemple : Sac à dos de capacité 15kg

| Objet  | A    | B    | C    | D    |
| ------ | ---- | ---- | ---- | ---- |
| Masse  | 4    | 7    | 5    | 3    |
| Valeur | 10   | 15   | 8    | 5    |

|     Étapes     | Objets dans le sac | Masse totale | Valeur totale |
| :------------: | :----------------: | :----------: | :-----------: |
| Initialisation |         []         |      0       |       0       |
|    Étape 1     |        [B]         |      7       |      15       |
|    Étape 2     |      [B, A]        |     11       |      25       |
|    Étape 3     |    [B, A, D]       |     14       |      30       |

### Stratégies de remplissage

Il existe trois stratégies principales pour résoudre ce problème de manière gloutonne :

1. **Par masse** : Choisir d'abord les objets les plus légers
2. **Par valeur** : Choisir d'abord les objets de plus grande valeur
3. **Par rapport valeur/masse** : Choisir les objets ayant le meilleur rapport valeur/masse

### Idée de l'algorithme

!!! fox_exercice_test "Idée de l'algorithme"
    **On initialise un sac vide avec une masse totale et une valeur totale à 0.**

    **Pour chaque objet selon la stratégie choisie :**
    
    - Si l'ajout de l'objet ne dépasse pas la capacité du sac :
        - On ajoute l'objet au sac
        - On met à jour la masse totale
        - On met à jour la valeur totale
    
    **On continue jusqu'à ce qu'aucun objet ne puisse plus être ajouté.**

### Exercices de réflexion

!!! fox_exercice "Exercices sac à dos"
    Soit un sac à dos de capacité 20kg et les objets suivants :

    | Objet  | 1    | 2    | 3    | 4    | 5    |
    | ------ | ---- | ---- | ---- | ---- | ---- |
    | Masse  | 6    | 8    | 4    | 10   | 7    |
    | Valeur | 12   | 20   | 6    | 18   | 15   |

    1. Appliquer l'algorithme glouton en utilisant la stratégie par masse.
    **La solution est-elle optimale ? Si non, donner une meilleure solution.**

    2. Appliquer l'algorithme glouton en utilisant la stratégie par valeur.
    **La solution est-elle optimale ? Si non, donner une meilleure solution.**

    3. Appliquer l'algorithme glouton en utilisant la stratégie par rapport valeur/masse.
    **Quelle stratégie semble donner les meilleurs résultats ?**

## Travail Pratique : Implémentation des algorithmes gloutons

### Exercice 1 : Rendu de monnaie

Implémentez une fonction `rendu_monnaie(montant, systeme)` qui :

- Prend en paramètre un montant à rendre et un système monétaire
- Retourne la liste des pièces/billets à rendre
- Utilise le moins de pièces possible

**Exemple** :
```python
systeme = [1, 2, 5, 10, 20, 50]
print(rendu_monnaie(53, systeme))  # Devrait afficher [50, 2, 1]
```

### Exercice 2 : Sac à dos

!!! fox_exercice_important
    Cet exercice ressemble beaucoup à l'exercice réalisé au [**Jour 3**](../0%20-%20New%20Year%20Advent/Exercices%20J1%20-%20J9/Jour_3.md) et au [**Jour 4**](../0%20-%20New%20Year%20Advent/Exercices%20J1%20-%20J9/Jour_4.md) du calendrier de l'avant [**New Year Advent**](../0%20-%20New%20Year%20Advent/new_year_advent.md)

Implémentez les trois fonctions suivantes pour résoudre le problème du sac à dos selon différentes stratégies :

1. `sac_a_dos_masse(capacite, objets)` qui :
   - Prend en paramètres la capacité maximale du sac et une liste de tuples (masse, valeur)
   - Utilise la stratégie du choix par masse (objets les plus légers d'abord)
   - Retourne un tuple (objets_selectionnes, valeur_totale)

2. `sac_a_dos_valeur(capacite, objets)` qui :
   - Prend en paramètres la capacité maximale du sac et une liste de tuples (masse, valeur)
   - Utilise la stratégie du choix par valeur (objets les plus précieux d'abord)
   - Retourne un tuple (objets_selectionnes, valeur_totale)

3. `sac_a_dos_rapport(capacite, objets)` qui :
   - Prend en paramètres la capacité maximale du sac et une liste de tuples (masse, valeur)
   - Utilise la stratégie du choix par rapport valeur/masse
   - Retourne un tuple (objets_selectionnes, valeur_totale)

**Exemples** :
```python
objets = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (masse, valeur)

# Stratégie par masse (objets les plus légers)
print(sac_a_dos_masse(10, objets))  # Affiche les objets choisis et la valeur totale

# Stratégie par valeur (objets les plus précieux)
print(sac_a_dos_valeur(10, objets))  # Affiche les objets choisis et la valeur totale

# Stratégie par rapport valeur/masse
print(sac_a_dos_rapport(10, objets))  # Affiche les objets choisis et la valeur totale
```

### Exercice 3 : Compression de Huffman

Implémentez les fonctions suivantes pour la compression de Huffman :

1. `calculer_frequences(texte)` : Calcule la fréquence de chaque caractère
2. `construire_arbre(frequences)` : Construit l'arbre de Huffman
3. `generer_codes(arbre)` : Génère les codes binaires pour chaque caractère
4. `compresser(texte)` : Compresse le texte en utilisant l'algorithme de Huffman

**Exemple** :
```python
texte = "abracadabra"
print(compresser(texte))  # Affiche le texte compressé et le taux de compression
```