# Fiche d'exercices : Fonctions

## Exercices de niveau 1

**Écrire un programme qui prend deux réels `longueur` et `largeur` et qui calcule l'aire d'un rectangle en affichant le résultat sous la forme : `'L'aire du rectangle est : [aire]'`.**

??? fox_correction "Correction"

    ```python
    def aire_rectangle(longueur:float, largeur:float)-> None:
        print("L'aire du rectangle est ", longueur * largeur)
    ```

---

**Écrire une fonction python `aire_rectangle` qui prend en paramètres deux réels correspondant à la largeur et la longueur d'un rectangle et renvoie l'aire de ce rectangle.**  

??? fox_correction "Correction"

    ```python
    def aire_rectangle(longueur:float, largeur:float)-> float:
        aire = longueur * largeur
        return aire
    ```

---

**Écrire une fonction `moyenne` qui prend deux réels en paramètres et renvoie la moyenne de ces deux nombres.**

??? fox_correction "Correction"

    ```python
    def moyenne(note_1 : float, note_2 : float)-> float:
        moy = (note_1 + note_2)/2
        return moy
    ```

**Écrire une fonction `somme` qui prend deux entiers en paramètres et renvoie leur somme.**  
*Exemple : somme(4,5) doit renvoyer 9.*  

??? fox_correction "Correction"

    ```python
    def somme(nombre_1 : int, nombre_2 : int)-> int:
        s = nombre_1 + nombre_2
        return s
    ```

---

**Écrire une fonction `parite` qui prend en paramètre un entier et renvoie `True` s'il est pair, `False` sinon.**  
*Exemple : parite(7) doit renvoyer Faux.* 

??? fox_correction "Correction"

    ```python
    def parite(nombre : int)-> bool:
        if nombre % 2 == 0:
            return True
        else:
            return False
    ```

---

**Écrire une fonction `maximum_deux_nombres` qui prend deux entiers en paramètres et renvoie le plus grand des deux.**  
*Exemple : maximum(10,15) doit renvoyer 15.*  

??? fox_correction "Correction"

    ```python
    def maximum_deux_nombres(nombre_1 : int, nombre_2 : int)-> int:
        if nombre_1 > nombre_2 : 
            return nombre_1
        else : 
            return nombre_2
    ```

---

**Écrire une fonction `valeur_absolue` qui prend un nombre en paramètre et renvoie sa valeur absolue.**  
On rappelle que la valeur absolue d'un nombre correspond à celui-ci peu importe son signe, c'est à dire que la valeur absolue de -8 est 8 et que la valeur absolue de 56 est 56.  
*Exemple : valeur_absolue(-8) doit renvoyer 8.*

??? fox_correction "Correction"

    ```python
    def valeur_absolue(nombre : int)-> int:
        if nombre >= 0:
            return nombre
        else:
            return -1*nombre
    ```

---

**Écrire une fonction `multiplication_par_addition` qui prend deux entiers en paramètres et renvoie le produit des deux nombres en utilisant une succession d'additions.**  
On sait que $4\times3 = 4 + 4 + 4 = 12~\texttt{ou}~4\times3 = 3 + 3 + 3 + 3 = 12$  
*Exemple : multiplication_par_addition(4,3) doit renvoyer 12.*

??? fox_correction "Correction"

    ```python
    def multiplication_par_addition(nombre : int, multiple : int)-> int:
        resultat = 0
        for i in range(multiple):
            resultat = resultat + nombre
        return resultat
    ```

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

---

**Écrire une fonction `somme_n_entiers` qui prend en paramètre un entier `n` et renvoie la somme de tous les entiers de 1 à n.**  
*Exemple : somme_n_entiers(100) doit renvoyer 5050.*??? fox_correction "Correction"

??? fox_correction "Correction"

    ```python
    def somme_n_entiers(borne : int)-> int:
        resultat = 0
        for i in range(borne):
            resultat = resultat + i
        return resultat
    ```
---

**Écrire une fonction `compter_voyelles` qui prend en paramètre une chaîne de caractère et renvoie le nombre de voyelles.**  
*Exemple : compteur_voyelles("bonjour") doit renvoyer 3.*

??? fox_correction "Correction"

    ```python
    def compter_voyelles(chaine : str)-> int:
        voyelles = 0
        for lettre in chaine:
            if lettre in 'aeiouAEIOU':
                voyelles = voyelles + 1
        return voyelles
    ```

---

**Écrire une fonction `puissance` qui prend en paramètres deux entiers a et b et renvoie a à la puissance b. Cette fonction n'utilisera pas l'opérateur `**` mais plutôt une boucle.**  
*Exemple : puissance(3,2) doit renvoyer 9.*

??? fox_correction "Correction"

    ```python
    def puissance(nombre_1 : int, nombre_2 : int)-> int:
        resultat = 1
        for i in range(nombre_2):
            resultat = resultat * nombre_1
        return resultat
    ```

---

**Écrire une fonction `est_premier` qui prend en paramètre un entier et renvoie `True` s'il est premier, `False` sinon.**  
Un nombre est premier uniquement s'il est divisible par 1 et par lui même.  
Indication : pour réussir cet exercice, vous utiliserez une boucle et vous compterez le nombre de diviseurs.  
Rappel : un nombre en divise un autre si le reste de leur division est 0. En python, l'opérateur qui obtient le reste de la division est `%`.  
*Exemple : est_premier(2) doit renvoyer Vrai, est_premier(6) doit renvoyer Faux.*  

??? fox_correction "Correction"

    ```python
    def est_premier(nombre : int)-> bool:
        diviseurs = 0
        for i in range(1,nombre+1):
            if nombre%i == 0:
                diviseurs = diviseurs + 1
        if diviseurs == 2 :
            return True
        else:
            return False
    ```
---

**Écrire une fonction `somme_chiffres` qui prend un entier en paramètre et renvoie la somme de ses chiffres.**  
*Exemple : somme_chiffres(1234) doit renvoyer 10 (1+2+3+4)* 

??? fox_correction "Correction"

    ```python
    def somme_chiffres(nombre : int)-> int:
        somme = 0
        str_nombre = str(nombre)
        for chiffre in str_nombre:
            somme = somme + int(chiffre)
        return somme
    ```

---

## Exercices de niveau 3

**Écrire un fonction `nombre_parfait` qui prend en paramètre un entier et renvoie True si la somme de ses diviseurs (sans lui même) égale le nombre.**  
Indication : Si un nombre divise le nombre demandé en paramètre, il peut être judicieux de le mettre dans une liste. Il faudra donc chercher tous ses diviseurs sauf lui-même pour réussir cet exercice.  
*Exemple : nombre_parfait(6) doit renvoyer True (car 1 + 2 + 3 = 6).* 

??? fox_correction "Correction"

    ```python
    def nombre_parfait(nombre : int)-> int:
        somme = 0
        for i in range(1,nombre):
            if nombre % i == 0:
                somme = somme + i
        if somme == nombre:
            return True
        else:
            return False
    ```

---

**Écrire une fonction `fibonacci` qui prend en paramètre un entier et affiche les différents termes de la suite de fibonacci.**  
On rappelle que la suite de fibonacci est calculée à partir des deux termes précédents.  
$F(0) = 0 \rightarrow F(1) = 1 \rightarrow F(2) = 1 + 0 = 1 \rightarrow F(3) = F(2) + F(1) = 1 + 1 = 2 \rightarrow F(4) = F(3) + F(2) = 2 + 1 = 3 \cdots$  
*Exemple : fibonacci(5) doit afficher 0, 1, 1, 2, 3, 5.*  

??? fox_correction "Correction"

    ```python
        def fibonacci(borne : int)-> None:
            x = 0
            y = 1
            for i in range(borne):
                print(x)
                y = x + y
                x = y - x
    ```

---

**Écrire une fonction `nombre_armstrong` qui prend en paramètre un nombre entier et renvoie `True` s'il est un nombre d'Amstrong, `False` sinon.**  
Un nombre est un nombre d'Armstrong si la somme des puissances de ses chiffres est égale au nombre lui-même.  
$153 = 1^3 + 5^3 + 3^3$  
$8208 = 8^4 + 2^4+ 0^4+8^4$  
*Exemple : nombre_armstrong(1634) doit renvoyer True.*

??? fox_correction "Correction"

    ```python
        def nombre_armstrong(nombre : int)-> bool:
            str_nombre = str(nombre)
            somme = 0
            taille = len(str_nombre)
            for chiffre in str_nombre:
                carre = int(chiffre)**taille
                somme = somme + carre
            if somme == nombre:
                return True
            else:
                return False
    ```

---

**Écrire une fonction `somme_premiers` qui prend en paramètre un entier n et renvoie la somme des nombres premiers jusque n (compris).**  
Vous pourrez utiliser la fonction `est_premier` dans la partie de niveau 2.  
*Exemple : somme_premiers(10) doit renvoyer 17 car les nombres premiers inférieurs à 10 sont 2,3,5,7 et $$2+3+5+7=17$$*  

??? fox_correction "Correction"

    ```python
        def somme_premiers(borne : int)-> int:
            somme = 0
            for i in range(borne+1):
                if est_premier(i):
                    somme = somme + i
            return somme
            
    ```
---

**Écrire une fonction `compter_occurences` qui prend en paramètres une chaîne de caractère et un caractère et renvoie le nombre de fois que le caractère apparaît dans la chaîne de caractère.**  
*Exemple : compter_occurences("programmation", "m") doit renvoyer 2.*

??? fox_correction "Correction"

    ```python
        def compter_occurences(chaine : str, caractere : str)-> int:
            compteur = 0
            for carac in chaine:
                if carac == caractere:
                    compteur = compteur + 1
            return compteur
            
    ```

## Exercices de niveau 4

**Écrire une fonction `tetration` qui prend en paramètre un nombre `n` et son tétré `t` et renvoie la tétration du nombre par le tétré.**  
La tétration est une opération mathématique se rapprochant des puissances.
On parle de tétration quand on réalise une "tour de puissance", on peut résumer cela ainsi :
Par exemple :  
${^{3}3} = 3^{3{^3}} = 3^{3\times3} = 3^{27} = 7 625 597 484 987$  
${^{5}4} = 4^{4^{4^{4^{4}}}} = 4 ^ {4^{4^{4\times4}}} = 4^{4^{4^{16}}} = 4^{4^{4294967296}}\cdots$.  
*Exemple : tetration(3,3) doit renvoyer 7 625 597 484 987.*

??? fox_correction "Correction"

    ```python
        def tetration(n:int,tetre:int)-> int:
            puissance = n
            if tetre == 0:
                return 1
            elif tetre == 1:
                return n
            else:
                for i in range(2,tetre):
                    puissance = puissance ** n
            return n**puissance
    ```
