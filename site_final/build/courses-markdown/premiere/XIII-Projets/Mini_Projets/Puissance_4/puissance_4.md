# Sujet de TP : Jeu du Puissance 4

## Présentation du problème

Le Puissance 4 est un jeu de stratégie à deux joueurs où l'objectif est d'aligner quatre jetons de sa couleur.

## Fonctions à implémenter

### 1. Gestion de la grille

**Écrire une fonction `grille_vide` qui ne prend pas de paramètres et renvoie une liste à deux dimensions de 6 lignes et 7 colonnes de chaînes de caractères.**

*Exemple d'utilisation et de résultat :*
```python
>>> grille = grille_vide()
>>> for ligne in grille:
...     print(ligne)
['.', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '.']
```

**Écrire une fonction `afficher_grille` qui prend en paramètre une grille et l'affiche de manière lisible.**

*Exemple d'utilisation :*
```python
>>> grille = grille_vide()
>>> afficher_grille(grille)
  1   2   3   4   5   6   7
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
```

### 2. Gestion des colonnes

**Écrire une fonction `colonne_valide` qui prend en paramètre une grille et une colonne et renvoie `True` si la colonne est bien comprise dans la grille.**
*Indication : La grille contient 7 colonnes allant d'indice 0 jusque 6.*

*Exemple d'utilisation :*
```python
>>> colonne_valide(grille, 3)
True
>>> colonne_valide(grille, 8)
False
```

#### 2.2 `colonne_pleine(grille, colonne)`
**Écrire une fonction `colonne_pleine` qui prend en paramètres une grille et un entier correspondant à une colonne et renvoie `True` si la colonne est pleine, `False` sinon.**

*Exemple d'utilisation :*
```python
>>> grille[0][2] = 'X'
>>> grille[1][2] = 'X'
>>> grille[2][2] = 'X'
>>> grille[3][2] = 'X'
>>> grille[4][2] = 'X'
>>> grille[5][2] = 'X'
>>> colonne_pleine(grille, 2)
True
>>> colonne_pleine(grille, 3)
False
```

### 3. Placement des jetons

**Écrire une fonction `ajouter_jeton` qui prend en paramètre une grille, un entier correspondant à une colonne et un caractère (X ou O) correspondant au joueur.**
*Indication : pour réaliser cette fonction, vous devrez traiter les lignes de bas en haut. Vous devrez utiliser une boucle `for` qui commence de la fin jusqu'au début avec un pas de -1.*

*Exemple d'utilisation :*
```python
>>> nouvelle_grille = ajouter_jeton(grille, 3, 'X')
>>> afficher_grille(nouvelle_grille)
  1   2   3   4   5   6   7
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . X . . .
```

### 4. Vérification de victoire

**Écrire une fonction `verifier_ligne` qui prend en paramètre une grille et une chaîne de caractère correspondant à un joueur qui vérifie s'il y a un alignement horizontal de 4 jetons.**
*Indication : Vous devrez vérifier si 4 symboles qui sont alignés horizontalement sont les mêmes. Pour se faire, vous pouvez réaliser une boucle for pour chaque ligne. Il sera plus pratique de réaliser un for par indice qui commencera à 0 et ira jusqu'au maximum la longueur de votre ligne - 3.*

**Écrire une fonction `verifier_colonne` qui prend en paramètre une grille et une chaîne de caractère correspondant à un joueur qui vérifie s'il y a un alignement vertical de 4 jetons.**

*Indication : Vous devrez vérifier si 4 symboles qui sont alignés verticalement sont les mêmes. Pour se faire, vous pouvez réaliser une boucle for pour chaque ligne puis une boucle imbriquée pour chaque colonne. Il sera plus pratique de réaliser ces for par indice qui commenceront à 0 et iront jusqu'à votre nombre de lignes -3 et traitera toutes les colonnes.*

**On dispose d'une fonction `verifier_diagonale`**

```python
def verifier_diagonale(grille:list[list[str]],joueur:str)->bool:
    for i in range(len(grille)-3):
        for j in range(len(grille[0])-3):
            if grille[i][j] == joueur and grille[i+1][j+1] == joueur and grille[i+2][j+2] == joueur and grille[i+3][j+3] == joueur:
                return True
    for i in range(3,len(grille)):
        for j in range(len(grille[0])-3):
            if grille[i][j] == joueur and grille[i-1][j+1] == joueur and grille[i-2][j+2] == joueur and grille[i-3][j+3] == joueur:
                return True
    return False
```


#### 4.4 `verifier_victoire(grille, joueur)`
**Écrire une fonction `verifier_victoire` qui combine les vérifications précédentes.**

*Exemple d'utilisation :*
```python
>>> verifier_victoire(grille, 'X')
False
```

### 5. Fonction principale

**Écrire la fonction `puissance4` qui gère le déroulement complet du jeu.**

#### Pseudo-code détaillé :
```
Fonction puissance4():
    Initialiser une grille vide
    joueur_actuel = 'X'
    
    Répéter :
        Afficher la grille
        Afficher "Tour du joueur", joueur_actuel
        
        Demander la colonne de jeu
        
        Tant que colonne invalide ou pleine:
            Afficher message d'erreur
            Redemander une colonne
        
        Ajouter le jeton du joueur
        
        Si victoire:
            Afficher "Victoire du joueur", joueur_actuel
            Arrêter
        
        Si match nul (grille pleine):
            Afficher "Match nul"
            Arrêter
        
        Changer de joueur
```
