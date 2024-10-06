# Fiche d'exercices : Fonctions

**Écrire un programme qui prend deux variables `longueur` et `largeur` et qui calcule l'aire d'un rectangle en affichant le résultat sous la forme : `'L'aire du rectangle est : [aire]'`.**

??? fox_correction "Correction"

    ```python
    def aire_rectangle(longueur:float, largeur:float)-> None:
        print("L'aire du rectangle est ", longueur * largeur)
    ```

**Écrire une fonction python `aire_rectangle` qui prend en paramètres deux entiers correspondant à la largeur et la longueur d'un rectangle et renvoie l'aire de ce rectangle.**  

??? fox_correction "Correction"

    ```python
    def aire_rectangle(longueur:float, largeur:float)-> float:
        aire = longueur * largeur
        return aire
    ```

**Écrire une fonction python `factorielle` qui prend en paramètre un nombre entier n et renvoie la factorielle de ce nombre. On rappelle que la factorielle de 5 vaut $1\times2\times3\times4\times5$.**  

??? fox_correction "Correction"

    ```python
    def factorielle(n : int)-> int:
        i = 1
        facto = 1
        while i <= n:
            facto = facto * i
        return facto
    ```

**Tester cette fonction avec les valeurs 5, 6, 8 et 10.**  


**Écrire une fonction `moyenne` qui prend deux nombres en paramètre et renvoie la moyenne de ces deux nombres.**
??? fox_correction "Correction"

    ```python
    def moyenne(note_1 : float, note_2 : float)-> float:
        moy = (note_1 + note_2)/2
        return moy
    ```
