# Fiche d'exercices : Types en python

## Bases de la programmation, blocs conditionnels

**Donner les types des valeurs suivantes : `13`, `14.5`, `'Hello World!'`, `True`, `'15.5'`**  

**À l'aide de python, écrire un programme qui affiche dans le terminal la table de vérité de la fonction booléenne `xor`.**  

??? Correction

    ```python
        print('Table de vérité du XOR')
        print('a','b','s')
        print(0,0,0)
        print(0,1,1)
        print(1,0,1)
        print(1,1,0)
    ```

**Écrire un programme qui permet d'afficher la somme de deux nombres entiers de la forme 'La somme est x+y' avec x et y défini précédemment.**  

**Améliorer le programme précédent pour qu'il affiche 'La somme de x et y est x+y'.**  

**Écrire un programme qui instancie deux chaînes de caractères, les concatène et affiche le résultat sous la forme `'La chaîne résultante est : [résultat]'`.**

## Étude de code

**Évaluer les valeurs de result à la fin de chaque programme.**  

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

**À l'aide de python, évaluer les résultats de ces comparaisons avec x = 5, x = 10 et x = -20**  

   1. x < 20 and x > - 20
   2. x > 5 or x < 3
   3. `not (x == 10)`
   4. `x >= 0 and x <= 10`
   5. `x % 2 == 0 or x % 3 == 0`
   6. `x < 0 or (x > 0 and x % 2 != 0)`

## Blocs conditionnels (if)

**Écrire un programme qui permet de trouver la valeur maximale entre trois variables entières. Ce programme affichera dans la console : "Le nombre `x` est plus grand que `y` et `z`.**

**Écrire un programme qui est une calculatrice basique. Elle demandera à l'utilisateur 2 nombres entiers `a` et `b` et un opérateur (`+`,`-`,`*`,`/`). Ce programme affichera : L'opération `a` `operateur` `b` vaut ...**

**Écrire un programme qui étant donné deux valeurs cout_de_production et prix_de_vente, affiche dans le terminal `profit` si le cout est inférieur au prix de vente, `perte` sinon.**  

**Écrire un programme qui prend une note sur 20 et affiche dans le terminal si l'étudiant a obtenu une mention :**

   - `'Très bien'` pour une note supérieure ou égale à 16.
   - `'Bien'` pour une note entre 14 et 15.
   - `'Assez bien'` pour une note entre 12 et 13.
   - `'Passable'` pour une note entre 10 et 11.
   - `'Échec'` pour une note inférieure à 10.

**Écrire un programme qui affiche dans le terminal si un nombre est pair ou impair.**  