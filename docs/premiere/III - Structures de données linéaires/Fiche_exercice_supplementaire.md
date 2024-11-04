# Fiche d'exercices : Listes avancées

## Matrices

### Facile

1. On dispose de la matrice [[1,2,3],[4,5,6],[7,8,9]].
   1. Donner la position (indice de la ligne et de la colonne) de la valeur 2.
   2. Donner la valeur à la ligne 1 et colonne 2.
   3. Comment en python retrouver la valeur cherchée en question 2.

2. On dispose de la matrice [[1,2,3],[4,5,6],[7,8,9]]. 
   1. Écrire un programme qui permet de donner la somme de tous les nombres de cette matrice.
   2. Tester avec d'autres matrices plus grandes.

### Moyenne

1. Écrire une fonction `sous_matrice` qui prend en paramètre une matrice et deux indices (ligne et colonne), et renvoie une sous-matrice 2x2 commençant à cette position.  
   *Exemple :*  
   *`sous_matrice([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1)`, cela doit renvoyer `[[5, 6], [8, 9]]`.*

2. Écrire une fonction `valeurs_uniques_matrice` qui prend en paramètre une matrice et renvoie une liste des valeurs uniques présentes dans la matrice.  
   *Exemple :*  
   *`valeurs_uniques_matrice([[1, 2, 2], [3, 4, 4], [5, 1, 3]])`, cela doit renvoyer `[1, 2, 3, 4, 5]`.*

3. Écrire une fonction `somme_diagonales` qui prend une matrice carrée et renvoie la somme des éléments de ses deux diagonales.  
   *Exemple :*  
   *`somme_diagonales([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`, cela doit renvoyer `30` (1 + 5 + 9 + 3 + 7).*

### Difficile

1. Écrire une fonction `transpose_matrice` qui prend en paramètre une matrice et renvoie sa transposée.  
   *Exemple :*  
   *`transpose_matrice([[1, 2, 3], [4, 5, 6]])`, cela doit renvoyer `[[1, 4], [2, 5], [3, 6]]`.*

2. Écrire une fonction `produit_matrices` qui prend deux matrices et renvoie leur produit (en supposant qu'elles sont conformes).  
   *Exemple :*  
   *`produit_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])`, cela doit renvoyer `[[19, 22], [43, 50]]`.*

## Listes par compréhension

### Facile

1. On dispose de la compréhension suivante [i for i in range(10)].
   1. Quelle liste est créée par cette compréhension?
   2. Modifier cette compréhension pour donner le carré de chaque nombre.

2. On peut rajouter des conditions dans des compréhensions pour éviter certaines valeurs.
   1. Quelle liste est créée par la compréhension suivante : [i for i in range(20) if i %2 == 0] ?
   2. Modifier cette compréhension pour quelle fasse l'inverse.

### Moyenne

1. Écrire une fonction `double_liste` qui prend une liste d'entiers en paramètre et utilise une compréhension de liste pour renvoyer une nouvelle liste contenant le double de chaque élément.  
   *Exemple :*  
   *`double_liste([1, 2, 3, 4])`, cela doit renvoyer `[2, 4, 6, 8]`.*

2. Écrire une fonction `enlever_negatifs` qui prend une liste de nombres et renvoie une nouvelle liste sans les nombres négatifs, en utilisant une compréhension de liste.  
   *Exemple :*  
   *`enlever_negatifs([-3, 0, 5, -1, 7])`, cela doit renvoyer `[0, 5, 7]`.*

3. Écrire une fonction `longueur_liste` qui prend une liste de chaînes et renvoie une liste des longueurs de chaque chaîne, en utilisant une compréhension de liste.  
   *Exemple :*  
   *`longueur_liste(["chat", "chien", "poisson"])`, cela doit renvoyer `[4, 5, 7]`.*

4. Écrire une fonction `cubes_pairs` qui génère une liste des cubes des nombres pairs de 1 à 10 à l'aide d'une compréhension de liste.  
   *Exemple :*  
   *`cubes_pairs()`, cela doit renvoyer `[0, 8, 64]`.*

### Difficile

1. Écrire une fonction `nombres_multiples_3` qui crée une liste des nombres multiples de 3 de 0 à 30 à l'aide d'une compréhension de liste.  
   *Exemple :*  
   *`nombres_multiples_3()`, cela doit renvoyer `[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]`.*

2. Écrire une fonction `squares_pairs` qui crée une liste des carrés des nombres pairs de 1 à 20 en utilisant une compréhension de liste.  
   *Exemple :*  
   *`squares_pairs()`, cela doit renvoyer `[0, 4, 16, 36, 64, 100, 144, 196]`.*

3. Écrire une fonction `pairs_ou_impairs` qui prend une liste d'entiers et renvoie une liste de chaînes indiquant si chaque nombre est pair ou impair.  
   *Exemple :*  
   *`pairs_ou_impairs([1, 2, 3, 4])`, cela doit renvoyer `["impair", "pair", "impair", "pair"]`.*

4. Écrire une fonction `inverser_chaînes` qui prend une liste de chaînes de caractères et renvoie une nouvelle liste contenant ces chaînes inversées.  
   *Exemple :*  
   *`inverser_chaînes(["abc", "def", "ghi"])`, cela doit renvoyer `["cba", "fed", "ihg"]`.*

5. Écrire une fonction `fusionner_sans_doublons` qui prend en paramètres deux listes et renvoie une nouvelle liste contenant tous les éléments des deux listes sans doublons.  
   *Exemple :*  
   *`fusionner_sans_doublons([1, 2, 3], [3, 4, 5])`, cela doit renvoyer `[1, 2, 3, 4, 5]`.*

6. Écrire une fonction `prefixes` qui prend une liste de mots et renvoie une liste contenant tous les préfixes possibles pour chaque mot.  
   *Exemple :*  
   *`prefixes(["chat", "chien"])`, cela doit renvoyer `["", "c", "ch", "cha", "chat", "", "c", "ch", "chi", "chien"]`.*