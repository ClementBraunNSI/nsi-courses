# Fiche d'exercices : Fonctions

## Exercices de niveau 1

!!! fox_exercice "Calcul de l'aire d'un rectangle (affichage)"
    **Écrire un programme qui prend deux réels `longueur` et `largeur` et qui calcule l'aire d'un rectangle en affichant le résultat sous la forme : `'L'aire du rectangle est : [aire]'`.**

??? fox_correction "Correction"
    ```python
    def aire_rectangle(longueur: float, largeur: float) -> None:
        print("L'aire du rectangle est ", longueur * largeur)
    ```

---

!!! fox_exercice "Calcul de l'aire d'un rectangle (fonction)"
    **Écrire une fonction Python `aire_rectangle` qui prend en paramètres deux réels correspondant à la largeur et la longueur d'un rectangle et renvoie l'aire de ce rectangle.**

??? fox_correction "Correction"
    ```python
    def aire_rectangle(longueur: float, largeur: float) -> float:
        return longueur * largeur
    ```

---

!!! fox_exercice "Calcul de la moyenne"
    **Écrire une fonction `moyenne` qui prend deux réels en paramètres et renvoie la moyenne de ces deux nombres.**

??? fox_correction "Correction"
    ```python
    def moyenne(note_1: float, note_2: float) -> float:
        return (note_1 + note_2) / 2
    ```

---

!!! fox_exercice "Somme de deux entiers"
    **Écrire une fonction `somme` qui prend deux entiers en paramètres et renvoie leur somme.**  
    *Exemple : somme(4,5) doit renvoyer 9.*

??? fox_correction "Correction"
    ```python
    def somme(nombre_1: int, nombre_2: int) -> int:
        return nombre_1 + nombre_2
    ```

---

!!! fox_exercice "Test de parité"
    **Écrire une fonction `parite` qui prend en paramètre un entier et renvoie `True` s'il est pair, `False` sinon.**  
    *Exemple : parite(7) doit renvoyer False.*  

??? fox_correction "Correction"
    ```python
    def parite(nombre: int) -> bool:
        return nombre % 2 == 0
    ```

---

!!! fox_exercice "Maximum entre deux nombres"
    **Écrire une fonction `maximum_deux_nombres` qui prend deux entiers en paramètres et renvoie le plus grand des deux.**  
    *Exemple : maximum_deux_nombres(10, 15) doit renvoyer 15.*  

??? fox_correction "Correction"
    ```python
    def maximum_deux_nombres(nombre_1: int, nombre_2: int) -> int:
        return nombre_1 if nombre_1 > nombre_2 else nombre_2
    ```

---

!!! fox_exercice "Valeur absolue"
    **Écrire une fonction `valeur_absolue` qui prend un nombre en paramètre et renvoie sa valeur absolue.**  
    *Exemple : valeur_absolue(-8) doit renvoyer 8.*

??? fox_correction "Correction"
    ```python
    def valeur_absolue(nombre: int) -> int:
        return nombre if nombre >= 0 else -nombre
    ```

---

!!! fox_exercice "Multiplication par addition"
    **Écrire une fonction `multiplication_par_addition` qui prend deux entiers en paramètres et renvoie le produit des deux nombres en utilisant une succession d'additions.**  
    *Exemple : multiplication_par_addition(4, 3) doit renvoyer 12.*

??? fox_correction "Correction"
    ```python
    def multiplication_par_addition(nombre: int, multiple: int) -> int:
        resultat = 0
        for _ in range(multiple):
            resultat += nombre
        return resultat
    ```

---

## Exercices de niveau 2

!!! fox_exercice "Calcul de la factorielle"
    **Écrire une fonction `factorielle` qui prend en paramètre un entier n et renvoie la factorielle de ce nombre.**  

??? fox_correction "Correction"
    ```python
    def factorielle(n: int) -> int:
        resultat = 1
        for i in range(1, n + 1):
            resultat *= i
        return resultat
    ```

---

!!! fox_exercice "Somme des n premiers entiers"
    **Écrire une fonction `somme_n_entiers` qui prend en paramètre un entier `n` et renvoie la somme de tous les entiers de 1 à n.**  
    *Exemple : somme_n_entiers(100) doit renvoyer 5050.*

??? fox_correction "Correction"
    ```python
    def somme_n_entiers(n: int) -> int:
        return sum(range(1, n + 1))
    ```

---

!!! fox_exercice "Compter les voyelles"
    **Écrire une fonction `compter_voyelles` qui prend en paramètre une chaîne de caractères et renvoie le nombre de voyelles.**  
    *Exemple : compter_voyelles("bonjour") doit renvoyer 3.*

??? fox_correction "Correction"
    ```python
    def compter_voyelles(chaine: str) -> int:
        voyelles = "aeiouAEIOU"
        return sum(1 for lettre in chaine if lettre in voyelles)
    ```

---

!!! fox_exercice "Puissance sans opérateur **"
    **Écrire une fonction `puissance` qui prend en paramètres deux entiers a et b et renvoie a à la puissance b sans utiliser l'opérateur `**`.**  
    *Exemple : puissance(3, 2) doit renvoyer 9.*

??? fox_correction "Correction"
    ```python
    def puissance(base: int, exposant: int) -> int:
        resultat = 1
        for _ in range(exposant):
            resultat *= base
        return resultat
    ```

---

!!! fox_exercice "Nombre premier" 
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

!!! fox_exercice "Somme des chiffres d'un nombre"
    **Écrire une fonction `somme_chiffres` qui prend un entier en paramètre et renvoie la somme de ses chiffres.**  
    *Indication : Il peut être facile d'utiliser le changement de type en `str`*  
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

!!! fox_exercice "Nombre parfait"
    **Écrire une fonction `nombre_parfait` qui prend en paramètre un entier et renvoie True si la somme de ses diviseurs (sans lui-même) égale le nombre.**  
    Indication : Si un nombre divise le nombre demandé en paramètre, il peut être judicieux de le mettre dans une liste. Il faudra donc chercher tous ses diviseurs sauf lui-même pour réussir cet exercice.  
    *Exemple : nombre_parfait(6) doit renvoyer True (car 1 + 2 + 3 = 6).*  

??? fox_correction "Correction"
    ```python
    def nombre_parfait(nombre: int) -> bool:
        somme = 0
        for i in range(1, nombre):
            if nombre % i == 0:
                somme += i
        return somme == nombre
    ```

---

!!! fox_exercice "Suite de Fibonacci"
    **Écrire une fonction `fibonacci` qui prend en paramètre un entier et affiche les différents termes de la suite de Fibonacci.**  
    On rappelle que la suite de Fibonacci est calculée à partir des deux termes précédents.  
    $F(0) = 0$, $F(1) = 1$, $F(2) = 1 + 0 = 1$, $F(3) = F(2) + F(1) = 1 + 1 = 2$, $F(4) = F(3) + F(2) = 2 + 1 = 3$...  
    *Exemple : fibonacci(5) doit afficher 0, 1, 1, 2, 3, 5.*

??? fox_correction "Correction"
    ```python
    def fibonacci(n: int) -> None:
        a, b = 0, 1
        for _ in range(n + 1):
            print(a)
            a, b = b, a + b
    ```

---

!!! fox_exercice "Nombre d'Armstrong"
    **Écrire une fonction `nombre_armstrong` qui prend en paramètre un nombre entier et renvoie `True` s'il est un nombre d'Armstrong, `False` sinon.**  
    Un nombre est un nombre d'Armstrong si la somme des puissances de ses chiffres est égale au nombre lui-même.  
    *Exemple : nombre_armstrong(153) doit renvoyer True car $1^3 + 5^3 + 3^3 = 153$.*

??? fox_correction "Correction"
    ```python
    def nombre_armstrong(nombre: int) -> bool:
        somme = 0
        str_nombre = str(nombre)
        puissance = len(str_nombre)
        for chiffre in str_nombre:
            somme += int(chiffre) ** puissance
        return somme == nombre
    ```

---

!!! fox_exercice "Somme des nombres premiers"
    **Écrire une fonction `somme_premiers` qui prend en paramètre un entier n et renvoie la somme des nombres premiers jusque n (compris).**  
    *Exemple : somme_premiers(10) doit renvoyer 17 car les nombres premiers inférieurs à 10 sont 2, 3, 5, et 7 (2 + 3 + 5 + 7 = 17).*

??? fox_correction "Correction"
    ```python
    def somme_premiers(n:int)-> int:
        somme = 0
        for i in range(n+1):
            #On dispose d'une fonction qui renvoie True s'il est premier
            if est_premier(i):
                somme = somme +i
        return somme
    ```

---

!!! fox_exercice "Compter les occurrences"
    **Écrire une fonction `compter_occurences` qui prend en paramètres une chaîne de caractères et un caractère, et renvoie le nombre de fois que le caractère apparaît dans la chaîne.**  
    *Exemple : compter_occurences("programmation", "m") doit renvoyer 2.*

??? fox_correction "Correction"
    ```python
    def compter_occurences(chaine: str, caractere: str) -> int:
        occurences = 0
        for lettre in chaine:
            if lettre == caractere:
                occurences = occurences + 1
        return occurences
    ```

---

## Exercices de niveau 4

!!! fox_exercice "Tétration"
    **Écrire une fonction `tetration` qui prend en paramètre un nombre `n` et un tétré `t` et renvoie la tétration du nombre par le tétré.**  
    *Exemple : tetration(3, 3) doit renvoyer 7625597484987.*

??? fox_correction "Correction"
    ```python
    def tetration(n: int, t: int) -> int:
        if t == 0:
            return 1
        result = n
        for i in range(t - 1):
            result = n ** result
        return result
    ```