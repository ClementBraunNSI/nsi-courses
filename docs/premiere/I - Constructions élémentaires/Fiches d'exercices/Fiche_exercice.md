# Fiche d'exercices : Types en python

1. Donner les types des valeurs suivantes : 13, 14.5, 'Hello World!', `True`, '15.5'

2. À l'aide de python, écrire un programme qui affiche dans le terminal la table de vérité de la fonction booléenne `xor`

3. Écrire un programme qui permet d'afficher la somme de deux nombres entiers de la forme 'La somme est x+y' avec x et y défini précédemment.

4. Améliorer le programme précédent pour qu'il affiche 'La somme de x et y est x+y'

5. Écrire un programme qui étant donné deux valeurs cout_de_production et prix_de_vente, affiche dans le terminal `profit` si le cout est inférieur au prix de vente, `perte` sinon.

6. Écrire un programme qui affiche le maximum entre 3 nombres mis dans des variables.

7. Écrire un programme qui affiche dans le terminal si un nombre est pair ou impair.

8. À l'aide de python, évaluer les résultats de ces comparaisons avec x = 5, x = 10 et x = -20  
   1. x < 20 and x > - 20
   2. x > 5 or x < 3
   3. `not (x == 10)`
   4. `x >= 0 and x <= 10`
   5. `x % 2 == 0 or x % 3 == 0`
   6. `x < 0 or (x > 0 and x % 2 != 0)`

9. Évaluer les valeurs de result à la fin de chaque programme

    ```python
    x = 8
    y = 6
    if x > y:
        result = x - y
    else:
        result = y - x
    ```

    ```python
    a = 4
    b = 9
    if a < b:
        result = a + b
    else:
        result = a * b
    ```

    ```python
    m = 7
    n = 3
    if m % 2 == 0:
        result = m * n
    else:
        result = m + n
    ```

10. Écrire une fonction python `factorielle` qui prend en paramètre un nombre entier n et renvoie la factorielle de ce nombre. On rappelle que la factorielle de 5 vaut $1\times2\times3\times4\times5$.
Tester cette fonction avec les valeurs 5, 6, 8 et 10.

11. Écrire une fonction python `aire_rectangle` qui prend en paramètres deux entiers correspondant à la largeur et la longueur d'un rectangle et renvoie l'aire de ce rectangle.

12. Écrire une fonction `moyenne` qui prend deux nombres en paramètre et renvoie la moyenne de ces deux nombres. 