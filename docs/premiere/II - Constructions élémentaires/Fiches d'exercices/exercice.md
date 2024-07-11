# Exercices Boucles

1. Écrire une fonction qui écrit pour une valeur de **1** à **n** avec un pas de **1**, la phrase:

    "Tour n°..." 

    en remplaçant **...** par le numéro du tour en question

    _**indice:**_ Il est possible de concaténer deux chaines de caractère (str) en faisant:

    ```python
    chaine_complete = chaine_1 + chaine_2
    ```

2. Pour une valeur de **n** donnée, écrire une fonction qui fait la somme des entiers de **1** à **n**

3. Écrire une fonction qui additionne les éléments d'une liste de nombres entiers. La tester avec la liste [2,3,5,1,6,7]

**Exercice boucle while:**

1. Réaliser le même programme que pour la question 1 de l'exercice boucle for, en utilisant la boucle **while**, mais cette fois-ci en comptant le nombre de tours restants

2. écrire une fonction qui additionne tous les éléments d'une liste mis en paramètre en utilisant la boucle **while**. modifier cette fonction de sorte qu'elle renvoie un tuple (somme, moyenne).

3. Expliquer si les codes suivants affiche bel et bien quelque chose ou non:

```python
1.  while i < 10 :                      2.  i = 12
        print(i)                            while i < 10 :
        i = i + 1                               print(i)
                                                i = i + 1 


3.  while False :                       4.  i = 9
        print(i)                            while i != 0 and i < 10 :
                                                print(i)
                                                i = i - 1
```

4. Écrire une fonction qui prend en paramètre un entier **n**, tel que cette fonction affiche une pyramide de 'O' de taille **n**

    _**Exemple:**_ pour n = 4: 
    ```python
       O
      OOO
     OOOOO
    OOOOOOO
    ```

_**Pour aller plus loin:**_ en vous inspirant de la question 4, écrire une fonction qui prend un paramètre n, et qui crée une pyramide telle que:

```python
pour n = 4:                     pour n = 5:                     pour n = 6:
   1                                1                               1
  121                              121                             121
 12321                            12321                           12321
1234321                          1234321                         1234321
                                123454321                       123454321
                                                               12345654321
```
