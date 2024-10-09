# Fiche d'exercices : Fonctions

## Exercices de niveau 1

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

**Écrire une fonction `moyenne` qui prend deux nombres en paramètre et renvoie la moyenne de ces deux nombres.**

??? fox_correction "Correction"

    ```python
    def moyenne(note_1 : float, note_2 : float)-> float:
        moy = (note_1 + note_2)/2
        return moy
    ```

**Écrire une fonction `somme` qui prend deux nombres en paramètres et renvoie leur somme.**  
*Exemple : somme(4,5) doit renvoyer 9.*  

**Écrire une fonction `parite` qui prend en paramètre un nombre et renvoie `True` s'il est pair, `False` sinon.**  
*Exemple : parite(7) doit renvoyer Faux.*  

**Écrire une fonction `maximum_deux_nombres` qui prend deux nombres en paramètres et renvoie le plus grand des deux.**  
*Exemple : maximum(10,15) doit renvoyer 15.*  

**Écrire une fonction `valeur_absolue` qui prend un nombre en paramètre et renvoie sa valeur absolue.**  
On rappelle que la valeur absolue d'un nombre correspond à celui-ci peu importe son signe, c'est à dire que la valeur absolue de -8 est 8 et que la valeur absolue de 56 est 56.  
*Exemple : valeur_absolue(-8) doit renvoyer 8.*

**Écrire une fonction `multiplication_par_addition` qui prend deux nombres en paramètres et renvoie le produit des deux nombres en utilisant une succession d'additions.**  
On sait que $4\times3 = 4 + 4 + 4 = 12~\texttt{ou}~4\times3 = 3 + 3 + 3 + 3 = 12$  
*Exemple : multiplication_par_addition(4,3) doit renvoyer 12.*

## Exercices de niveau 2

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



## Exercices de niveau 3

## Exercices de niveau 4

**Écrire une fonction `tetration` qui prend en paramètre un nombre `n` et son tétré `t` et renvoie la tétration du nombre par le tétré.**
La tétration est une opération mathématique se rapprochant des puissances.
On parle de tétration quand on réalise une "tour de puissance", on peut résumer cela ainsi :
Par exemple : 
$${^{3}3} = 3^{3{^3}} = 3^{3\times3} = 3^{27} = 7 625 597 484 987\newline
{^{5}4} = 4^{4^{4^{4^{4}}}} = 4 ^ {4^{4^{4\times4}}} = 4^{4^{4^{16}}} = 4^{4^{4294967296}}\cdots$$.