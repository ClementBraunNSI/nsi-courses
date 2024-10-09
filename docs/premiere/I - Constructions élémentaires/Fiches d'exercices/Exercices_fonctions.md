# Fiche d'exercices : Fonctions

## Exercices de niveau 1

**Écrire un programme qui prend deux réels `longueur` et `largeur` et qui calcule l'aire d'un rectangle en affichant le résultat sous la forme : `'L'aire du rectangle est : [aire]'`.**

??? fox_correction "Correction"

    ```python
    def aire_rectangle(longueur:float, largeur:float)-> None:
        print("L'aire du rectangle est ", longueur * largeur)
    ```

**Écrire une fonction python `aire_rectangle` qui prend en paramètres deux réels correspondant à la largeur et la longueur d'un rectangle et renvoie l'aire de ce rectangle.**  

??? fox_correction "Correction"

    ```python
    def aire_rectangle(longueur:float, largeur:float)-> float:
        aire = longueur * largeur
        return aire
    ```

**Écrire une fonction `moyenne` qui prend deux réels en paramètres et renvoie la moyenne de ces deux nombres.**

??? fox_correction "Correction"

    ```python
    def moyenne(note_1 : float, note_2 : float)-> float:
        moy = (note_1 + note_2)/2
        return moy
    ```

**Écrire une fonction `somme` qui prend deux entiers en paramètres et renvoie leur somme.**  
*Exemple : somme(4,5) doit renvoyer 9.*  

**Écrire une fonction `parite` qui prend en paramètre un entier et renvoie `True` s'il est pair, `False` sinon.**  
*Exemple : parite(7) doit renvoyer Faux.*  

**Écrire une fonction `maximum_deux_nombres` qui prend deux entiers en paramètres et renvoie le plus grand des deux.**  
*Exemple : maximum(10,15) doit renvoyer 15.*  

**Écrire une fonction `valeur_absolue` qui prend un nombre en paramètre et renvoie sa valeur absolue.**  
On rappelle que la valeur absolue d'un nombre correspond à celui-ci peu importe son signe, c'est à dire que la valeur absolue de -8 est 8 et que la valeur absolue de 56 est 56.  
*Exemple : valeur_absolue(-8) doit renvoyer 8.*

**Écrire une fonction `multiplication_par_addition` qui prend deux entiers en paramètres et renvoie le produit des deux nombres en utilisant une succession d'additions.**  
On sait que $4\times3 = 4 + 4 + 4 = 12~\texttt{ou}~4\times3 = 3 + 3 + 3 + 3 = 12$  
*Exemple : multiplication_par_addition(4,3) doit renvoyer 12.*

## Exercices de niveau 2

**Écrire une fonction `factorielle` qui prend en paramètre un entier n et renvoie la factorielle de ce nombre. On rappelle que la factorielle de 5 vaut $1\times2\times3\times4\times5$.**  

??? fox_correction "Correction"

    ```python
    def factorielle(n : int)-> int:
        i = 1
        facto = 1
        while i <= n:
            facto = facto * i
        return facto
    ```

**Écrire une fonction `somme_n_entiers` qui prend en paramètre un entier `n` et renvoie la somme de tous les entiers de 1 à n.**
*Exemple : somme_n_entiers(100) doit renvoyer 5050.*

**Écrire une fonction `compter_voyelles` qui prend en paramètre une chaîne de caractère et renvoie le nombre de voyelles.**
*Exemple : compteur_voyelles("bonjour") doit renvoyer 3.*

**Écrire une fonction `puissance` qui prend en paramètres deux entiers a et b et renvoie a à la puissance b. Cette fonction n'utilisera pas l'opérateur `**` mais plutôt une boucle.**
*Exemple : puissance(3,2) doit renvoyer 9.*

**Écrire une fonction `est_premier` qui prend en paramètre un entier et renvoie `True` s'il est premier, `False` sinon.**
Un nombre est premier uniquement s'il est divisible par 1 et par lui même.  
Indication : pour réussir cet exercice, vous utiliserez une boucle et vous compterez le nombre de diviseurs.
Rappel : un nombre en divise un autre si le reste de leur division est 0. En python, l'opérateur qui obtient le reste de la division est `%`.
*Exemple : est_premier(2) doit renvoyer Vrai, est_premier(6) doit renvoyer Faux.*

**Écrire une fonction `somme_chiffres` qui prend un entier en paramètre et renvoie la somme de ses chiffres.**
*Exemple : somme_chiffres(1234) doit renvoyer 10 (1+2+3+4)*

## Exercices de niveau 3

## Exercices de niveau 4

**Écrire une fonction `tetration` qui prend en paramètre un nombre `n` et son tétré `t` et renvoie la tétration du nombre par le tétré.**
La tétration est une opération mathématique se rapprochant des puissances.
On parle de tétration quand on réalise une "tour de puissance", on peut résumer cela ainsi :
Par exemple :  
$${^{3}3} = 3^{3{^3}} = 3^{3\times3} = 3^{27} = 7 625 597 484 987\newline
{^{5}4} = 4^{4^{4^{4^{4}}}} = 4 ^ {4^{4^{4\times4}}} = 4^{4^{4^{16}}} = 4^{4^{4294967296}}\cdots$$.
