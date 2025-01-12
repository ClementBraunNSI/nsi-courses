# Fiche d'exercices : Types en python

## Bases de la programmation, blocs conditionnels

!!! fox_exercice "Types en Python"
    **Donner les types des valeurs suivantes : `13`, `14.5`, `'Hello World!'`, `True`, `'15.5'`**

!!! fox_exercice "Table de vérité XOR"
    **À l'aide de python, écrire un programme qui affiche dans le terminal la table de vérité de la fonction booléenne `xor`.**  

??? fox_correction "Correction"
    ```python
    print('Table de vérité du XOR')
    print('a','b','s')
    print(0,0,0)
    print(0,1,1)
    print(1,0,1)
    print(1,1,0)
    ```

!!! fox_exercice "Somme de deux nombres"
    **Écrire un programme qui permet d'afficher la somme de deux nombres entiers de la forme 'La somme est x+y' avec x et y défini précédemment.**

??? fox_correction "Correction"
    ```python
    x = 4
    y = 3
    print('La somme est', x+y)
    ```

!!! fox_exercice "Affichage amélioré"
    **Améliorer le programme précédent pour qu'il affiche 'La somme de x et y est x+y'.**  

??? fox_correction "Correction"
    ```python
    x = 4
    y = 3
    print('La somme de',x, ' et ', y, ' est ', x+y)
    ```

!!! fox_exercice "Concaténation de chaînes"
    **Écrire un programme qui instancie deux chaînes de caractères, les concatène et affiche le résultat sous la forme `'La chaîne résultante est : [résultat]'`.**

??? fox_correction "Correction"
    ```python
    chaine_a = "Bonjour"
    chaine_b = "Au Revoir"
    print("La chaîne résultante est :", chaine_a+chaine_b)
    ```


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

!!! fox_exercice "Maximum entre trois nombres"
    **Écrire un programme qui permet de trouver la valeur maximale entre trois variables entières. Ce programme affichera dans la console : "Le nombre `x` est plus grand que `y` et `z`.**

??? fox_correction "Correction"
    ```python
    val_1 = int(input("Valeur 1"))
    val_2 = int(input("Valeur 2"))
    val_3 = int(input("Valeur 3"))
    if val_1 > val_2 and val_1 > val_3:
        print(val_1, " est la plus grande")
    elif val_2 > val_1 and val_2 > val_3:
        print(val_2, " est la plus grande")
    elif val_3 > val_1 and val_3 > val_2:
        print(val_3, " est la plus grande")
    ```

!!! fox_exercice "Calculatrice basique"
    **Écrire un programme qui est une calculatrice basique. Elle demandera à l'utilisateur 2 nombres entiers `a` et `b` et un opérateur (`+`,`-`,`*`,`/`). Ce programme affichera : L'opération `a` `operateur` `b` vaut ...**

??? fox_correction "Correction"
    ```python
    a = int(input("Entrez un premier nombre"))
    b = int(input("Entrez un second nombre"))
    operateur = input("Entrez un opérateur : + - / *")
    if operateur == "+":
        print(a+b)
    elif operateur == "-":
        print(a-b)
    elif operateur == "*":
        print(a*b)
    elif operateur == "/":
        # On ne peut pas diviser par zéro
        if b != 0:
            print(a/b)
    ```

!!! fox_exercice "Profit ou perte"
    **Écrire un programme qui étant donné deux valeurs cout_de_production et prix_de_vente, affiche dans le terminal `profit` si le cout est inférieur au prix de vente, `perte` sinon.**

??? fox_correction "Correction"
    ```python
    prix_de_vente = int(input("Entrez un prix de vente"))
    cout_de_production = int(input("Entrez un coût de production"))
    
    if prix_de_vente > cout_de_production:
        print("profit")
    elif prix_de_vente == cout_de_production:
        print("pas de marge")
    else:
        print("perte")
    ```

!!! fox_exercice "Mentions au baccalauréat"
    **Écrire un programme qui prend une note sur 20 et affiche dans le terminal si l'étudiant a obtenu une mention :**
    
    - `'Très bien'` pour une note supérieure ou égale à 16.
    - `'Bien'` pour une note entre 14 et 15.
    - `'Assez bien'` pour une note entre 12 et 13.
    - `'Passable'` pour une note entre 10 et 11.
    - `'Échec'` pour une note inférieure à 10.

??? fox_correction "Correction"
    ```python
    # Demander à l'utilisateur de saisir une note
    note = float(input("Entrez une note sur 20 : "))

    # Vérifier la mention correspondante et afficher le résultat
    if note >= 16:
        print("Mention : Très bien")
    elif 14 <= note <= 15:
        print("Mention : Bien")
    elif 12 <= note <= 13:
        print("Mention : Assez bien")
    elif 10 <= note <= 11:
        print("Mention : Passable")
    else:
        print("Mention : Échec")
    ```

!!! fox_exercice "Parité d'un nombre"
    **Écrire un programme qui affiche dans le terminal si un nombre est pair ou impair.**

??? fox_correction "Correction"
    ```python
    a = int(input("Entrez un nombre"))
    if a % 2 == 0:  # Si le reste de la division de a par 2 est 0 -> Si 2 divise a
        print("pair")
    else:
        print("impair")
    ```
