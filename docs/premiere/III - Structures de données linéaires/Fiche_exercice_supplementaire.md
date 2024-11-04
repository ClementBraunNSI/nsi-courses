## Fiche d'exercices : Listes avancées

## Matrices

On rappelle qu'une matrice est un tableau à deux dimensions. En python, pour les représenter, on réalise des listes de listes.

1. On dispose de la matrice [[1,2,3],[4,5,6],[7,8,9]].
   1. Donner la position (indice de la ligne et de la colonne) de la valeur 2.
   2. Donner la valeur à la ligne 1 et colonne 2.
   3. Comment en python retrouver la valeur cherchée en question 2.

2. On dispose de la matrice [[1,2,3],[4,5,6],[7,8,9]]. 
   1. Écrire un programme qui permet de donner la somme de tous les nombres de cette matrice.
   2. Tester avec d'autres matrices plus grandes.

3. Créer une matrice par compréhension qui contient tous les nombres de 0 à 11. Chacune des lignes de la matrice doivent avoir une taille de 4.

## Listes par compréhension

1. On dispose de la compréhension suivante [i for i in range(10)].
   1. Quelle liste est créée par cette compréhension?
   2. Modifier cette compréhension pour donner le carré de chaque nombre.

2. On peut rajouter des conditions dans des compréhensions pour éviter certaines valeurs.
   1. Quelle liste est créée par la compréhension suivante : [i for i in range(20) if i %2 == 0] ?
   2. Modifier cette compréhension pour quelle fasse l'inverse.

3. Créer une liste par compréhension qui contient les racines carrées des nombres allant de 1 jusque 20. On rappelle que le module `math` dispose de la fonction `sqrt` qui permet de calculer les racines carrées.